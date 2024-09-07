# cs_manim_animations

Manim-powered animations for various Computer Science lessons

## Sections
- `web_app_evolution/` - simplified overview of web app evolution from static page to scallable and high-reachable web applications

## Requirements
- Python 3.12+
- manim 0.18.1+

## Getting Started

1. Clone repository to your local machine
2. Crete new `venv` and install dependencies:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
3. Render & play selected animation in low quality:
```bash
manim -pql project/web_app_evolution/__init__.py WebAppBuildingBlocks
```

## Development

### Makefile

- `make clean` - remove all media files & Manim cache

### Manim commands

- `-pql` - play after render in low quality
- `-pqk` - play after render in 4K quality

> [!TIP]
> Use `-pql` to quickly check the animation and then use `-pqk` to render in 4K quality for the final touches.