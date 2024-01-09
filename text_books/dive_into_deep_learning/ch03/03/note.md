* [Back to Dive into Deep Learning](../../main.md)

# 3.3 Synthetic Regression Data

#### Import Libraries
```python
import random
import torch
from d2l import torch as d2l
```

<br>

## 3.3.1 Generating Dataset
- Goal)
  - Generate 1000 examples with 2-dimensional features drawn from a standard normal distribution
- Settings)
  - The resulting design matrix $`\mathbf{X}`$ belongs to $`\mathbb{R}^{1000 \times 2}`$.
    - We generate each label by applying a *ground truth* linear function, corrupting them via additive noise $`\boldsymbol{\epsilon}`$, drawn independently and identically for each example:
      - $\mathbf{y}= \mathbf{X} \mathbf{w} + b + \boldsymbol{\epsilon}$













<br>

* [Back to Dive into Deep Learning](../../main.md)