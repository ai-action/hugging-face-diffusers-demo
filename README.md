# Hugging Face diffusers demo

[![text-to-image](https://github.com/ai-action/hugging-face-diffusers-demo/actions/workflows/text-to-image.yml/badge.svg)](https://github.com/ai-action/hugging-face-diffusers-demo/actions/workflows/text-to-image.yml)
[![image-to-image](https://github.com/ai-action/hugging-face-diffusers-demo/actions/workflows/image-to-image.yml/badge.svg)](https://github.com/ai-action/hugging-face-diffusers-demo/actions/workflows/image-to-image.yml)
[![inpainting](https://github.com/ai-action/hugging-face-diffusers-demo/actions/workflows/inpainting.yml/badge.svg)](https://github.com/ai-action/hugging-face-diffusers-demo/actions/workflows/inpainting.yml)

🤗 Hugging Face diffusers demo based on the [tutorial](https://huggingface.co/docs/diffusers/main/tutorials/autopipeline).

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

Create the [virtualenv](https://docs.python.org/3/library/venv.html):

```sh
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```sh
pip3 install -r requirements.txt
```

## Run

### Text-to-Image

[Text-to-image](https://huggingface.co/docs/diffusers/main/tutorials/autopipeline?autopipeline=text-to-image):

```sh
python3 text_to_image.py
```

### Image-to-Image

[Image-to-image](https://huggingface.co/docs/diffusers/main/tutorials/autopipeline?autopipeline=image-to-image):

```sh
python3 image_to_image.py
```

### Inpainting

[Inpainting](https://huggingface.co/docs/diffusers/main/tutorials/autopipeline?autopipeline=inpainting):

```sh
python3 inpainting.py
```

### Disable Telemetry

[Disable telemetry](https://huggingface.co/docs/diffusers/main/installation#telemetry-logging):

```sh
DISABLE_TELEMETRY=YES python3 text_to_image.py
```

### Clear Cache

Clear cache:

```sh
rm -rf ~/.cache/huggingface/
```

## License

[MIT](LICENSE)
