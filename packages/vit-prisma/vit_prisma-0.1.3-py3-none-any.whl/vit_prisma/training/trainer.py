import wandb
import torch
import torch.optim as optim
import tqdm
from tqdm.auto import tqdm
from vit_prisma.training.training_utils import calculate_accuracy, calculate_loss, set_seed, PrismaCallback
from vit_prisma.utils.wandb_utils import dataclass_to_dict, update_dataclass_from_dict
from vit_prisma.training.training_dictionary import optimizer_dict, loss_function_dict
from vit_prisma.training.schedulers import WarmupThenStepLR
from vit_prisma.training.early_stopping import EarlyStopping
from vit_prisma.utils.saving_utils import save_config_to_file
import os
from torch.utils.data import Dataset, DataLoader
import dataclasses
from sklearn.model_selection import train_test_split

def train(
        model_function,
        config,
        train_dataset,
        val_dataset=None,
        checkpoint_path=None,
        callbacks: list[PrismaCallback] = None
):
    if val_dataset is None:
        train_dataset, val_dataset = train_test_split(train_dataset, test_size=0.2)
        print(f"Split train dataset into train and val with {len(train_dataset)} and {len(val_dataset)}.")

    if config.use_wandb:
        if config.wandb_team_name is None:
            wandb.init(project=config.wandb_project_name)
        else:
            wandb.init(entity=config.wandb_team_name, project=config.wandb_project_name)
        sweep_values = wandb.config._items # get sweep values
        update_dataclass_from_dict(config, sweep_values)
        wandb.config.update(dataclass_to_dict(config))
    
    print("Config is:", config)
    save_config_to_file(config, os.path.join(config.parent_dir, "config.json"))

    set_seed(config.seed if config.seed != None else 666)
    model = model_function(config)
    model.train()
    model.to(config.device)
    optimizer = optimizer_dict[config.optimizer_name](model.parameters(), lr = config.lr, weight_decay = config.weight_decay)
    loss_fn = loss_function_dict[config.loss_fn_name]()

    if config.batch_size == -1:
        batch_size_train, batch_size_test = len(train_dataset), len(val_dataset) # use full batch
    else:
        batch_size_train, batch_size_test = config.batch_size, config.batch_size

    train_loader = DataLoader(train_dataset, batch_size=batch_size_train, shuffle=True)
    test_loader = DataLoader(val_dataset, batch_size=batch_size_test, shuffle=False)

    print(f"Length of trainloader {len(train_loader)}.")
    print(f"Length of testloader {len(test_loader)}")
    steps = 0

    scheduler = WarmupThenStepLR(optimizer, warmup_steps=config.warmup_steps, step_size=config.scheduler_step, gamma=config.scheduler_gamma)

    if config.early_stopping:
        early_stopping = EarlyStopping(patience=config.early_stopping_patience, verbose=True)
    else: 
        early_stopping = None
    
    if checkpoint_path and os.path.exists(checkpoint_path):
        checkpoint = torch.load(checkpoint_path)
        model.load_state_dict(checkpoint['model_state_dict'])
        optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
        start_epoch = checkpoint['epoch'] + 1
        print(f"Loaded checkpoint from epoch {checkpoint['epoch']}")
                

    #create dir for checkoint if it doesn't exist
    if os.path.exists(config.parent_dir) and not os.path.exists(os.path.join(config.parent_dir, config.save_dir)):
        os.makedirs(os.path.join(config.parent_dir, config.save_dir))

    num_samples = 0

    for epoch in tqdm(range(1, config.num_epochs + 1)):
        for idx, items in enumerate(train_loader):
            if steps % config.log_frequency == 0:
                model.eval()
                logs = {}
                train_loss = calculate_loss(model, train_loader, loss_fn, config.device)
                test_loss = calculate_loss(model, test_loader, loss_fn, config.device)
                log_dict = {
                    "train_loss": train_loss,
                    "test_loss": test_loss,
                }
                if config.loss_fn_name == "MSE":
                    tqdm.write(f"Steps{steps} | Train loss: {train_loss:.6f} | Test loss: {test_loss:.6f}")
                else:
                    train_acc = calculate_accuracy(model, train_loader, config.device)
                    test_acc = calculate_accuracy(model, test_loader, config.device)
                    tqdm.write(f"Steps{steps} | Train loss: {train_loss:.6f} | Train acc: {train_acc:.5f} | Test loss: {test_loss:.6f} | Test acc: {test_acc:.5f}")
                    log_dict.update({
                                        "train_acc": train_acc, 
                                        "test_acc": test_acc
                                     })
                if config.use_wandb:
                    wandb.log(log_dict, step=num_samples) # Record number of samples
                model.train() # set model back to train mode

            images, labels, *metadata = items
            images, labels = images.to(config.device), labels.to(config.device)

            optimizer.zero_grad()

            y = model(images)
            
            loss = loss_fn(y, labels)
            loss.backward()
            
            torch.nn.utils.clip_grad_norm_(model.parameters(), config.max_grad_norm) if config.max_grad_norm is not None else None
            
            optimizer.step()
            scheduler.step() if config.warmup_steps > 0 else None
            
            tqdm.write(f"Epoch {epoch} | steps{steps} | Num Samples {num_samples} | Loss {loss.item()}") if config.print_every and steps % config.print_every == 0 else None
            
            if config.save_checkpoints and steps % config.save_cp_frequency == 0:
                torch.save({
                    'model_state_dict': model.state_dict(),
                    'optimizer_state_dict': optimizer.state_dict(),
                    'epoch': epoch
                }, os.path.join(os.path.join(config.parent_dir, config.save_dir), f"model_{num_samples}.pth"))
            
            if hasattr(config, 'max_steps') and config.max_steps and steps >= config.max_steps:
                break
            
            steps += 1
            num_samples += len(labels)
            for callback in callbacks:
                callback.on_step_end(steps, model, test_loader, wandb_logger=wandb)

        for callback in callbacks:
            callback.on_epoch_end(epoch, model, test_loader, wandb_logger=wandb)

        if config.early_stopping:
            early_stopping(train_acc)
            if early_stopping.early_stop:
                print("Stopping training due to early stopping!")
                break

    if config.use_wandb:
        wandb.finish()
    return model