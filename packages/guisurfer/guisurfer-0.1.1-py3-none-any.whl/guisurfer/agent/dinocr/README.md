# DinOCR

A desktop agent that uses Grounding Dino and OCR

GPT-4V is bad at positional reasoning, so this agent has been augmented with Grounding Dino and an OCR model to help.
We take inspiration and libraries from [MobileAgent](https://github.com/X-PLUG/MobileAgent), adding to them with a
novel _Jeffries Composite_ technique to help with icon recognition.

## Installation

For arm64

```sh
pip install -r requirements_m1.txt
```

For amd64

```sh
pip install -r requirements.txt
```

## Usage

For a simple overview of the internals see [note.ipynb](./note.ipynb)

To try the agent run

```
python -m dinocr.main --task "Search for types of French ducks" --max_steps 10
```
