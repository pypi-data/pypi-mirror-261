import numpy as np
import plotly.graph_objects as go
import plotly.express as px

import torch

from vit_prisma.utils.data_utils.imagenet_emoji import IMAGENET_EMOJI

def display_grid_on_image_with_heatmap(image, patch_dictionary, patch_size=32,
                                       layer_idx=-1,
                                       imagenet_class_to_emoji=IMAGENET_EMOJI,
                                       emoji_font_size=30,
                                       heatmap_mode='logit_values',
                                       alpha_color=.6,
                                       return_graph=False):

    valid_heatmap_modes = ['logit_values', 'emoji_colors']
    if heatmap_mode not in valid_heatmap_modes:
        raise ValueError(f"Invalid heatmap_mode '{heatmap_mode}'. Valid options are {valid_heatmap_modes}.")

    if isinstance(image, np.ndarray) and image.shape[-1] == 3:
        # Image is in correct format.
        pass
    elif isinstance(image, torch.Tensor):
        # Convert torch.Tensor to numpy.ndarray if necessary.
        image = image.detach().cpu().numpy().transpose(1, 2, 0)
        if image.max() <= 1.0:
            image *= 255  # Convert from [0, 1] to [0, 255] if needed.
        image = image.astype(np.uint8)

    grid_size_x = image.shape[1] // patch_size
    grid_size_y = image.shape[0] // patch_size

    # Initialize matrices with NaNs for logit values or zeros for emoji colors
    if heatmap_mode == 'logit_values':
        heatmap_matrix = np.full((grid_size_y, grid_size_x), np.nan)
    else:  # 'emoji_colors'
        heatmap_matrix = np.zeros((grid_size_y, grid_size_x))

    if imagenet_class_to_emoji is not None and heatmap_mode == 'emoji_colors':
        # Map emojis to unique integers if in 'emoji_colors' mode
        unique_emojis = {emoji: idx for idx, emoji in enumerate(set(imagenet_class_to_emoji.values()))}
    else:
        unique_emojis = {}

    fig = px.imshow(image)
    fig.update_traces(hoverinfo='none', hovertemplate=None)

    annotations = []
    hover_texts = []
    x_centers = []
    y_centers = []
    for patch_index, patch_data in sorted(patch_dictionary.items()):
        if patch_index == 0:
            continue  # Skip the CLS token.
        logit_data = patch_data[layer_idx]
        length_of_patch_data = len(logit_data)
        if length_of_patch_data >= 3:
            logit_value, class_name, class_index = logit_data[:3]
        else:
            print("Error in length of patch data.")
            continue

        adjusted_index = patch_index - 1
        row, col = divmod(adjusted_index, grid_size_x)

        if heatmap_mode == 'logit_values':
            heatmap_matrix[row, col] = logit_value
        else:  # 'emoji_colors'
            emoji = imagenet_class_to_emoji.get(class_index, "❓")
            heatmap_matrix[row, col] = unique_emojis.get(emoji, 0)

        emoji = imagenet_class_to_emoji.get(class_index, "❓") if imagenet_class_to_emoji is not None else "❓"
        annotations.append(go.layout.Annotation(x=col * patch_size + patch_size / 2,
                                                y=row * patch_size + patch_size / 2,
                                                text=emoji,
                                                showarrow=False,
                                                font=dict(size=emoji_font_size)))
        hover_texts.append(f"Patch: {patch_index}<br>Class: {class_name}<br>Logit: {logit_value:.2f}")
        x_centers.append(col * patch_size + patch_size / 2)
        y_centers.append(row * patch_size + patch_size / 2)

    # Choose color scale based on heatmap_mode
    colorscale = 'Viridis' if heatmap_mode == 'logit_values' else px.colors.qualitative.Plotly
    heatmap = go.Heatmap(z=heatmap_matrix, x0=0.5 * patch_size, dx=patch_size, y0=0.5 * patch_size, dy=patch_size,
                         colorscale=colorscale, opacity=alpha_color, showscale=(heatmap_mode == 'logit_values'), hoverinfo="none")
    fig.add_trace(heatmap)

    fig.add_trace(go.Scatter(x=x_centers, y=y_centers, mode='markers', marker=dict(color='rgba(0,0,0,0)'),
                             hoverinfo='text', text=hover_texts, hoverlabel=dict(bgcolor="white", font_size=12, font_family="Arial")))
    fig.update_layout(annotations=annotations)
    fig.update_layout(showlegend=False, plot_bgcolor='rgba(0,0,0,0)')
    fig.update_xaxes(showticklabels=False).update_yaxes(showticklabels=False)


    if return_graph:
      return fig
    else:
      fig.show()


# Animal logit lens

def display_patch_logit_lens(patch_dictionary, width=1000, height=1200, emoji_size=26, return_graph=False, show_colorbar=True, labels=None):
    num_patches = len(patch_dictionary)

    # Assuming data_array_formatted is correctly shaped according to your data structure
    data_array_formatted = np.array([[item[0] for item in list(patch_dictionary.values())[i]] for i in range(num_patches)])

    # Modify hover text generation based on whether labels are provided
    if labels:
      hover_text = [
            [f"{labels[j]}: {item[1]}" for j, item in enumerate(list(patch_dictionary.values())[i])]
            for i in range(num_patches)
        ] 
    else:
        hover_text = [[str(item[1]) for item in list(patch_dictionary.values())[i]] for i in range(num_patches)]

    # Creating the interactive heatmap
    fig = go.Figure(data=go.Heatmap(
        z=data_array_formatted,
        x=list(patch_dictionary.keys())[:num_patches],
        y=[f'{i}' for i in range(data_array_formatted.shape[0])],  # Patch Number
        hoverongaps=False,
        colorbar=dict(title='Logit Value') if show_colorbar else None,
        text=hover_text,
        hoverinfo="text"
    ))

    # Initialize a list to hold annotations for emojis
    annotations = []

    # Calculate half the distance between cells in both x and y directions for annotation placement
    x_half_dist = 0.5
    y_half_dist = 0.2

    for i, patch in enumerate(patch_dictionary.values()):
        for j, items in enumerate(patch):  # Extract class index directly from the patch_dictionary
            class_index = items[2]
            emoji = IMAGENET_EMOJI.get(class_index, "")  # Use class index for emoji lookup, default to empty if not found
            if emoji:  # Add annotation if emoji is found
                annotations.append(go.layout.Annotation(x=j + x_half_dist, y=i + y_half_dist, text=emoji, showarrow=False, font=dict(color="white", size=emoji_size)))

    # Add annotations to the figure
    fig.update_layout(annotations=annotations)

    # Configure the layout of the figure
    fig.update_layout(
        title='Per-Patch Logit Lens',
        xaxis=dict(title='Layer Number'),
        yaxis=dict(title='Patch Number'),
        autosize=False,
        width=width,
        height=height
    )
    fig.show()

    if return_graph:
        return fig