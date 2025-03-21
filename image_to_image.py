from random import randint
from sys import maxsize
import diffusers
import torch

if torch.cuda.is_available():
    device = "cuda"
# TODO: RuntimeError: MPS backend out of memory
# elif torch.backends.mps.is_available():
#     device = "mps"
else:
    device = "cpu"

# https://huggingface.co/docs/diffusers/main/en/tutorials/autopipeline?autopipeline=image-to-image
model = "dreamlike-art/dreamlike-photoreal-2.0"
pipeline = diffusers.AutoPipelineForImage2Image.from_pretrained(
    model,
    torch_dtype=None if device == "cpu" else torch.float16,
    use_safetensors=True
)
pipeline.to(device)

prompt = "cinematic photo of Godzilla eating burgers with a cat in a fast food restaurant, 35mm photograph, film, professional, 4k, highly detailed"
init_image = diffusers.utils.load_image("https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusers/autopipeline-text2img.png")
seed = randint(-maxsize, maxsize * 2)
generator = torch.Generator(device=device).manual_seed(seed)
image = pipeline(prompt, image=init_image, generator=generator).images[0]

filename = f"image-to-image{seed}.png"
image.save(filename)
print(f"Output: {filename}")
