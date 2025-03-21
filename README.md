# Hugging Face diffusers demo

[![text-to-image](https://github.com/ai-action/hugging-face-diffusers-demo/actions/workflows/text-to-image.yml/badge.svg)](https://github.com/ai-action/hugging-face-diffusers-demo/actions/workflows/text-to-image.yml)
[![image-to-image](https://github.com/ai-action/hugging-face-diffusers-demo/actions/workflows/image-to-image.yml/badge.svg)](https://github.com/ai-action/hugging-face-diffusers-demo/actions/workflows/image-to-image.yml)

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

Create the [virtualenv](https://docs.python-guide.org/dev/virtualenvs/):

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

### Disable Telemetry

[Disable telemetry](https://huggingface.co/docs/diffusers/main/installation#telemetry-logging):

```sh
DISABLE_TELEMETRY=YES python3 text_to_image.py
```

## License

[MIT](LICENSE)
