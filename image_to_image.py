from diffusers import AutoPipelineForImage2Image
from diffusers.utils import load_image
from random import randint
from sys import maxsize
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
pipe = AutoPipelineForImage2Image.from_pretrained(
    model,
    torch_dtype=None if device == "cpu" else torch.float16,
    use_safetensors=True
)
pipe.to(device)

seed = randint(-maxsize, maxsize * 2)
generator = torch.Generator(device=device).manual_seed(seed)
prompt = "cinematic photo of Godzilla eating burgers with a cat in a fast food restaurant, 35mm photograph, film, professional, 4k, highly detailed"
image = load_image("https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusers/autopipeline-text2img.png")
image = pipe(prompt, image=image, generator=generator).images[0]

filename = f"image-to-image{seed}.png"
image.save(filename)
print(f"Output: {filename}")
