from diffusers import AutoPipelineForText2Image
from uuid import uuid1

# https://huggingface.co/docs/diffusers/main/en/tutorials/autopipeline?autopipeline=text-to-image
model = "dreamlike-art/dreamlike-photoreal-2.0"
pipeline = AutoPipelineForText2Image.from_pretrained(model)

prompt = "cinematic photo of Godzilla eating sushi with a cat in a izakaya, 35mm photograph, film, professional, 4k, highly detailed"
image = pipeline(prompt).images[0]

filename = f"text-to-image-{uuid1()}.png"
image.save(filename)
print(f"Output: {filename}")
