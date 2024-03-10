import torch
import numpy as np
from PIL import Image
from typing import Tuple, List

# Custom imports from the MobileAgent and groundingdino packages
from .crop import (
    calculate_box_size,
    calculate_intersection_over_union as calculate_iou,
)
import groundingdino.datasets.transforms as GT
from groundingdino.models import construct_model
from groundingdino.util.slconfig import SLConfig
from groundingdino.util.utils import (
    sanitize_state_dict,
    extract_phrases_from_position_map,
)


def apply_transformations(image_pil: Image.Image) -> torch.Tensor:
    """
    Applies a series of transformations to an input image.

    Args:
      image_pil: A PIL Image object.

    Returns:
      A transformed image tensor.
    """
    transformations = GT.Compose(
        [
            GT.RandomResize([800], max_size=1333),
            GT.ToTensor(),
            GT.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
        ]
    )
    transformed_image, _ = transformations(image_pil, None)  # 3, h, w
    return transformed_image


def initialize_model(
    model_config_path: str, model_checkpoint_path: str, device: str
) -> torch.nn.Module:
    """
    Loads a model from a configuration file and checkpoint.

    Args:
      model_config_path: Path to the model configuration file.
      model_checkpoint_path: Path to the model checkpoint file.
      device: Device to load the model onto.

    Returns:
      A loaded model ready for inference.
    """
    config = SLConfig.fromfile(model_config_path)
    config.device = device
    model = construct_model(config)
    checkpoint = torch.load(model_checkpoint_path, map_location="cpu")
    load_result = model.load_state_dict(
        sanitize_state_dict(checkpoint["model"]), strict=False
    )
    print(load_result)
    _ = model.eval()
    return model


def generate_grounding_data(
    model: torch.nn.Module,
    image: torch.Tensor,
    caption: str,
    box_thresh: float,
    text_thresh: float,
    include_logits: bool = True,
) -> Tuple[List[List[int]], torch.Tensor, List[str]]:
    """
    Generates grounding output from an image and a caption.

    Args:
      model: The loaded model.
      image: The image tensor.
      caption: The caption as a string.
      box_thresh: Threshold for selecting boxes based on their scores.
      text_thresh: Threshold for selecting text based on its scores.
      include_logits: Whether to include logits in the output phrases.

    Returns:
      A tuple containing filtered boxes, scores, and predicted phrases.
    """
    caption = caption.lower().strip()
    caption += "." if not caption.endswith(".") else ""

    with torch.no_grad():
        outputs = model(image[None], captions=[caption])
    logits = outputs["pred_logits"].cpu().sigmoid()[0]  # (nq, 256)
    boxes = outputs["pred_boxes"].cpu()[0]  # (nq, 4)

    logits_filtered = logits.clone()
    boxes_filtered = boxes.clone()
    filter_mask = logits_filtered.max(dim=1)[0] > box_thresh
    logits_filtered = logits_filtered[filter_mask]  # num_filt, 256
    boxes_filtered = boxes_filtered[filter_mask]  # num_filt, 4

    tokenizer = model.tokenizer
    tokenized_caption = tokenizer(caption)

    predicted_phrases = []
    score_values = []
    for logit, box in zip(logits_filtered, boxes_filtered):
        phrase = extract_phrases_from_position_map(
            logit > text_thresh, tokenized_caption, tokenizer
        )
        if include_logits:
            predicted_phrases.append(f"{phrase}({str(logit.max().item())[:4]})")
        else:
            predicted_phrases.append(phrase)
        score_values.append(logit.max().item())

    return boxes_filtered, torch.Tensor(score_values), predicted_phrases


def filter_boxes(
    boxes_filtered: List[List[int]],
    image_size: Tuple[int, int],
    iou_thresh: float = 0.5,
) -> List[List[int]]:
    """
    Filters out overlapping and large boxes based on IOU and size thresholds.

    Args:
      boxes_filtered: A list of boxes to filter.
      image_size: A tuple representing the size of the image.
      iou_thresh: The IOU threshold for filtering overlapping boxes.

    Returns:
      A list of filtered boxes.
    """
    boxes_to_discard = set()

    for i in range(len(boxes_filtered)):
        if calculate_box_size(boxes_filtered[i]) > 0.05 * image_size[0] * image_size[1]:
            boxes_to_discard.add(i)
        for j in range(len(boxes_filtered)):
            if i == j or j in boxes_to_discard:
                continue
            iou = calculate_iou(boxes_filtered[i], boxes_filtered[j])
            if iou >= iou_thresh:
                boxes_to_discard.add(j)

    boxes_filtered = [
        box for idx, box in enumerate(boxes_filtered) if idx not in boxes_to_discard
    ]

    return boxes_filtered


def identify_bounding_boxes(
    input_image_path: str,
    text_query: str,
    grounding_model: torch.nn.Module,
    box_threshold: float = 0.05,
    text_threshold: float = 0.5,
) -> Tuple[List[List[int]], List[List[int]]]:
    """
    Detects bounding boxes in an image based on a text query.

    Args:
      input_image_path: Path to the input image.
      text_query: The text query for grounding.
      grounding_model: The loaded grounding model.
      box_threshold: Threshold for box scores.
      text_threshold: Threshold for text scores.

    Returns:
      A tuple containing image data (boxes) and their coordinates.
    """
    image = Image.open(input_image_path).convert("RGB")
    image_size = image.size

    transformed_image = apply_transformations(image)
    boxes_filtered, scores, predicted_phrases = generate_grounding_data(
        grounding_model, transformed_image, text_query, box_threshold, text_threshold
    )

    H, W = image_size[1], image_size[0]
    for i in range(boxes_filtered.size(0)):
        boxes_filtered[i] = boxes_filtered[i] * torch.Tensor([W, H, W, H])
        boxes_filtered[i][:2] -= boxes_filtered[i][2:] / 2
        boxes_filtered[i][2:] += boxes_filtered[i][:2]

    boxes_filtered = boxes_filtered.cpu().int().tolist()
    filtered_boxes = filter_boxes(boxes_filtered, image_size)
    box_data, box_coords = [], []
    for box in filtered_boxes:
        box_data.append(
            [
                max(0, box[0] - 10),
                max(0, box[1] - 10),
                min(box[2] + 10, image_size[0]),
                min(box[3] + 10, image_size[1]),
            ]
        )
        box_coords.append(
            [
                max(0, box[0] - 25),
                max(0, box[1] - 25),
                min(box[2] + 25, image_size[0]),
                min(box[3] + 25, image_size[1]),
            ]
        )

    return box_data, box_coords
