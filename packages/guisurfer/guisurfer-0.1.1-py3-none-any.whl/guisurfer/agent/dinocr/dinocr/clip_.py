from typing import List
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import clip
import torch


def clip_for_icon(clip_model, clip_preprocess, images, prompt):
    image_features = []
    for image_file in images:
        image = (
            clip_preprocess(Image.open(image_file))
            .unsqueeze(0)
            .to(next(clip_model.parameters()).device)
        )
        image_feature = clip_model.encode_image(image)
        image_features.append(image_feature)
    image_features = torch.cat(image_features)

    text = clip.tokenize([prompt]).to(next(clip_model.parameters()).device)
    text_features = clip_model.encode_text(text)

    image_features /= image_features.norm(dim=-1, keepdim=True)
    text_features /= text_features.norm(dim=-1, keepdim=True)
    similarity = (100.0 * image_features @ text_features.T).softmax(dim=0).squeeze(0)
    _, max_pos = torch.max(similarity, dim=0)
    pos = max_pos.item()

    return pos


def clip_for_top_icons(
    clip_model, clip_preprocess, images: List[str], prompt: str
) -> List[int]:
    """
    Returns the indices of the top images matching the prompt using CLIP, up to a maximum of 4.

    Args:
    - clip_model: The CLIP model.
    - clip_preprocess: The preprocessing function for images compatible with the CLIP model.
    - images (List[str]): List of paths to image files.
    - prompt (str): Text prompt for comparison.

    Returns:
    - List[int]: Indices of the top images ranked by similarity to the prompt, up to 4.
    """
    if not images:
        raise ValueError("Image list is empty.")

    print(f"finding the top icons from {len(images)} images")
    image_features = []
    for image_file in images:
        image = (
            clip_preprocess(Image.open(image_file))
            .unsqueeze(0)
            .to(next(clip_model.parameters()).device)
        )
        image_feature = clip_model.encode_image(image)
        image_features.append(image_feature)
    image_features = torch.cat(image_features)

    text = clip.tokenize([prompt]).to(next(clip_model.parameters()).device)
    text_features = clip_model.encode_text(text)

    image_features /= image_features.norm(dim=-1, keepdim=True)
    text_features /= text_features.norm(dim=-1, keepdim=True)
    similarity = (
        (100.0 * image_features @ text_features.T).softmax(dim=0).squeeze().flatten()
    )

    print(f"Similarity Tensor: {similarity}")
    print(f"Similarity Shape: {similarity.shape}")

    k = min(6, len(images))
    if similarity.numel() == 0:
        raise ValueError("Similarity tensor is empty.")

    top_indices = torch.topk(similarity, k).indices.tolist()
    print("top indices: ", top_indices)

    return top_indices


import torch
from PIL import Image


def clip_rank_all_icons(
    clip_model, clip_preprocess, images: List[str], prompt: str
) -> List[int]:
    """
    Returns the indices of all images sorted by their matching probability to the prompt using CLIP,
    from highest to lowest.

    Args:
        clip_model: The CLIP model.
        clip_preprocess: The preprocessing function for images compatible with the CLIP model.
        images (List[str]): List of paths to image files.
        prompt (str): Text prompt for comparison.

    Returns:
        List[int]: Indices of the images ranked by similarity to the prompt, from high to low.
    """
    if not images:
        raise ValueError("Image list is empty.")

    print(f"Ranking all icons from {len(images)} images")
    image_features = []
    for image_file in images:
        image = (
            clip_preprocess(Image.open(image_file))
            .unsqueeze(0)
            .to(next(clip_model.parameters()).device)
        )
        image_feature = clip_model.encode_image(image)
        image_features.append(image_feature)
    image_features = torch.cat(image_features)

    text = clip.tokenize([prompt]).to(next(clip_model.parameters()).device)
    text_features = clip_model.encode_text(text)

    image_features /= image_features.norm(dim=-1, keepdim=True)
    text_features /= text_features.norm(dim=-1, keepdim=True)
    similarity = (
        (100.0 * image_features @ text_features.T).softmax(dim=0).squeeze().flatten()
    )

    print(f"Similarity Tensor: {similarity}")
    print(f"Similarity Shape: {similarity.shape}")

    if similarity.numel() == 0:
        raise ValueError("Similarity tensor is empty.")

    sorted_indices = torch.argsort(similarity, descending=True).tolist()
    print("Sorted indices: ", sorted_indices)

    return sorted_indices
