# Hugging Face diffusers demo

[![build](https://github.com/ai-action/hugging-face-diffusers-demo/actions/workflows/build.yml/badge.svg)](https://github.com/ai-action/hugging-face-diffusers-demo/actions/workflows/build.yml)

🤗 Hugging Face diffusers demo based on the [tutorial](https://huggingface.co/docs/diffusers/main/en/tutorials/autopipeline).

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

[Text to image](https://huggingface.co/docs/diffusers/main/en/tutorials/autopipeline?autopipeline=text-to-image):

```sh
python3 text_to_image.py
```

[Disable telemetry](https://huggingface.co/docs/diffusers/v0.21.0/en/installation#notice-on-telemetry-logging):

```sh
DISABLE_TELEMETRY=YES python3 text_to_image.py
```

## License

[MIT](LICENSE)
