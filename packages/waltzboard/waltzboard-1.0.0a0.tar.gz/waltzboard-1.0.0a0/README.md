# Waltzboard

This system is under-review

## Installation

```shell
pip install waltzboard
```

## Usage Example - Library Only

```python
from waltzboard import Waltzboard
gl = Waltzboard(df)
gl.train(["rect", "count", "Creative_Type"])
gl.infer().display()
```

## Usage Example - With Interface

```shell
pnpm run server
```

## Demo for Waltzboard Library

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/12_Wm74nT2_X9zJlV0PJ0SeEVhyOc0eUf)

## Demo for Web-based Interface

```
pip install .
python app.py
cd client
pnpm install
pnpm dev
```

## Development

TBA

## Reference

### Multi-Criteria Optimization for Automatic Dashboard Design

**_Jiwon Choi_** and Jaemin Jo

Presented in 2023 Eurographics Conference on Visualization (EuroVis), Leipzig, Germany

Invited to IEEE Pacific Visualization Symposium 2023, Seoul, Korea
