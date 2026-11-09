import detector_playground.detectors.sam3
from pathlib import Path

SAMPLES= Path(__file__).parents[2] / "data" / "samples"

SAMPLE_SCENES = {
    "mostly cardboard": SAMPLES / "conveyor_1.jpg",
}

class Sam3Driver:
    def look_for(self, item, on) -> list[str]:
        image_path = SAMPLE_SCENES.get(on)
        if image_path is None:
            raise ValueError(f"Unknown scene {on!r}, known: {list(SAMPLE_SCENES)}")

        segmentation_result = detector_playground.detectors.sam3.segment(path=image_path, prompt=item)
        print(f"Segmentation result for '{item}' on '{on}': {segmentation_result}")
        return len(segmentation_result["masks"]) * [item]
