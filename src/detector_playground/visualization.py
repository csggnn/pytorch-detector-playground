from matplotlib import pyplot as plt
from PIL import Image
from sam3.visualization_utils import COLORS, plot_bbox, plot_mask


def plot_detections(img: Image.Image, results_by_label: dict[str, dict]) -> None:
    """Draw the masks and boxes of each label in one colour per label.

    The colour of a label is set by its position in results_by_label.
    """
    plt.figure(figsize=(12, 8))
    plt.imshow(img)
    width, height = img.size
    for label_index, (label, results) in enumerate(results_by_label.items()):
        color = COLORS[label_index % len(COLORS)]
        for mask, box, score in zip(results["masks"], results["boxes"], results["scores"]):
            plot_mask(mask.squeeze(0).cpu(), color=color)
            plot_bbox(
                height,
                width,
                box.cpu(),
                text=f"{label} {score.item():.2f}",
                box_format="XYXY",
                color=color,
                relative_coords=False,
            )
