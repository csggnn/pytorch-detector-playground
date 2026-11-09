import torch
from PIL import Image
from sam3 import build_sam3_image_model
from sam3.model.sam3_image_processor import Sam3Processor

def segment(path: str, prompt: str):
    model = build_sam3_image_model()
    image = Image.open(path)
    print(f"Segmenting image {path} with prompt '{prompt}'")

    processor = Sam3Processor(model, confidence_threshold=0.5)
    with torch.autocast(device_type="cuda", dtype=torch.bfloat16):
        inference_state = processor.set_image(image)
        processor.reset_all_prompts(inference_state)
        output = processor.set_text_prompt(state=inference_state, prompt=prompt)
    masks, boxes, scores = output["masks"], output["boxes"], output["scores"]
    return {"masks": masks, "boxes": boxes, "scores": scores}
