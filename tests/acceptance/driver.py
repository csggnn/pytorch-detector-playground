from detector_playground.detectors.sam3 import Sam3Segmenter
from pathlib import Path

SAMPLES= Path(__file__).parents[2] / "data" / "samples"

SAMPLE_SCENES = {
    "mostly cardboard": SAMPLES / "conveyor_1.jpg",
}

class Sam3Driver:
    def __init__(self):
        self._segmenter = Sam3Segmenter()
    def look_for(self, item, on) -> list[str]:
        image_path = SAMPLE_SCENES.get(on)
        if image_path is None:
            raise ValueError(f"Unknown scene {on!r}, known: {list(SAMPLE_SCENES)}")

        segmentation_result = self._segmenter.segment(path=image_path, prompt=item)
        print(f"Segmentation result for '{item}' on '{on}': {segmentation_result}")
        return len(segmentation_result["masks"]) * [item]
