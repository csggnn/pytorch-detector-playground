from PIL import Image
from matplotlib import pyplot as plt
from sam3.visualization_utils import plot_results
from detector_playground.detectors.sam3 import Sam3Segmenter
import argparse



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("image_path", help="Path to the image file")
    parser.add_argument("prompt", help="Prompt for the segmentation task")
    args = parser.parse_args()


    if args.image_path and args.prompt:
        results =Sam3Segmenter().segment(path=args.image_path, prompt=args.prompt)
        img0 = Image.open(args.image_path)
        plot_results(img0, results)
        plt.show()
        plt.waitforbuttonpress()

