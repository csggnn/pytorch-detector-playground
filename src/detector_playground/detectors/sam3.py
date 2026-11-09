import torch
from PIL import Image
from sam3 import build_sam3_image_model
from sam3.model.sam3_image_processor import Sam3Processor


class Sam3Segmenter:
    def __init__(self):
        self._model = build_sam3_image_model()
        self._processor = Sam3Processor(self._model, confidence_threshold=0.5)
        self._loaded_image_path = None
        self._inference_state = None

    def load_image(self, path: str):
        if self._loaded_image_path == path:
            print(f"Image {path} is already loaded, skipping reload.")
            return
        self._loaded_image_path = path
        image = Image.open(path)
        with torch.autocast(device_type="cuda", dtype=torch.bfloat16):
            self._inference_state = self._processor.set_image(image)

    def segment(self, prompt: str, path: str):
        self.load_image(path)
        with torch.autocast(device_type="cuda", dtype=torch.bfloat16):
            self._processor.reset_all_prompts(self._inference_state)
            output = self._processor.set_text_prompt(state=self._inference_state, prompt=prompt)
        masks, boxes, scores = output["masks"], output["boxes"], output["scores"]
        return {"masks": masks, "boxes": boxes, "scores": scores}

