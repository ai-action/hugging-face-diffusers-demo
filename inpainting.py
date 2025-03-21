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

# https://huggingface.co/docs/diffusers/main/tutorials/autopipeline?autopipeline=inpainting
model = "stabilityai/stable-diffusion-xl-base-1.0"
pipeline = diffusers.AutoPipelineForInpainting.from_pretrained(
    model,
    torch_dtype=None if device == "cpu" else torch.float16,
    use_safetensors=True
)
pipeline.to(device)

prompt = "cinematic photo of Godzilla eating burgers with a cat in a fast food restaurant, 35mm photograph, film, professional, 4k, highly detailed"
init_image = diffusers.utils.load_image("https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusers/autopipeline-img2img.png")
mask_image = diffusers.utils.load_image("https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusers/autopipeline-mask.png")
seed = randint(-maxsize, maxsize * 2)
generator = torch.Generator(device=device).manual_seed(seed)
strength = 0.4
num_inference_steps = 50

image = pipeline(
    prompt,
    image=init_image,
    mask_image=mask_image,
    generator=generator,
    strength=strength,
    num_inference_steps=num_inference_steps
).images[0]

filename = f"image-to-image{seed}.png"
image.save(filename)
print(f"Output: {filename}")
