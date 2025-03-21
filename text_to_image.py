from diffusers import AutoPipelineForText2Image
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

# https://huggingface.co/docs/diffusers/main/en/tutorials/autopipeline?autopipeline=text-to-image
model = "dreamlike-art/dreamlike-photoreal-2.0"
pipe = AutoPipelineForText2Image.from_pretrained(
    model,
    torch_dtype=None if device == "cpu" else torch.float16,
    use_safetensors=True
)
pipe.to(device)

seed = randint(-maxsize, maxsize * 2)
generator = torch.Generator(device=device).manual_seed(seed)
prompt = "cinematic photo of Godzilla eating sushi with a cat in a izakaya, 35mm photograph, film, professional, 4k, highly detailed"
image = pipe(prompt, generator=generator).images[0]

filename = f"text-to-image{seed}.png"
image.save(filename)
print(f"Output: {filename}")
