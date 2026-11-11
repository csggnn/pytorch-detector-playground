import argparse

from matplotlib import pyplot as plt
from PIL import Image

from detector_playground.detectors.sam3 import Sam3Segmenter
from detector_playground.visualization import plot_detections


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("image_path", help="Path to the image file")
    parser.add_argument(
        "prompts",
        nargs="+",
        help='Object types to segment, separated by spaces. Quote multi-word prompts, e.g. "office paper".',
    )
    args = parser.parse_args()

    results = Sam3Segmenter().segment(path=args.image_path, prompts=args.prompts)
    print(", ".join(f"{label}: {len(result['scores'])}" for label, result in results.items()))
    plot_detections(Image.open(args.image_path), results)
    plt.show()
