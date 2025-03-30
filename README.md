# Hugging Face diffusers demo

[![text-to-image](https://github.com/ai-action/hugging-face-diffusers-demo/actions/workflows/text-to-image.yml/badge.svg)](https://github.com/ai-action/hugging-face-diffusers-demo/actions/workflows/text-to-image.yml)
[![image-to-image](https://github.com/ai-action/hugging-face-diffusers-demo/actions/workflows/image-to-image.yml/badge.svg)](https://github.com/ai-action/hugging-face-diffusers-demo/actions/workflows/image-to-image.yml)
[![inpainting](https://github.com/ai-action/hugging-face-diffusers-demo/actions/workflows/inpainting.yml/badge.svg)](https://github.com/ai-action/hugging-face-diffusers-demo/actions/workflows/inpainting.yml)

🤗 Hugging Face diffusers demo based on the [tutorial](https://huggingface.co/docs/diffusers/main/tutorials/autopipeline). Read the [blog post](https://remarkablemark.org/blog/2025/03/21/how-to-run-hugging-face-stable-diffusion-ai-model-on-mac/) or [Medium story](https://medium.com/@remarkablemark/how-to-run-hugging-face-stable-diffusion-on-mac-1076bf53083d).

## Prerequisites

[Python 3](https://www.python.org/):

```sh
brew install python
```

## Install

Clone the repository:

```sh
git clone https://github.com/ai-action/hugging-face-diffusers-demo.git
cd hugging-face-diffusers-demo
```

Create the [virtualenv](https://docs.python.org/library/venv.html):

```sh
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```sh
pip install -r requirements.txt
```

## Run

### Text-to-Image

[Text-to-image](https://huggingface.co/docs/diffusers/main/tutorials/autopipeline?autopipeline=text-to-image):

```sh
python text_to_image.py
```

### Image-to-Image

[Image-to-image](https://huggingface.co/docs/diffusers/main/tutorials/autopipeline?autopipeline=image-to-image):

```sh
python image_to_image.py
```

### Inpainting

[Inpainting](https://huggingface.co/docs/diffusers/main/tutorials/autopipeline?autopipeline=inpainting):

```sh
python inpainting.py
```

### Disable Telemetry

[Disable telemetry](https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables#donottrack):

```sh
DO_NOT_TRACK=1 python text_to_image.py
```

### Clear Cache

Clear cache:

```sh
rm -rf ~/.cache/huggingface/
```

## License

[MIT](LICENSE)
