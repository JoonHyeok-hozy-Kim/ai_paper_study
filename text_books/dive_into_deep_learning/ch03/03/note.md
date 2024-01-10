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
    - $`\mathbb{R}^{1000 \times 2}`$
      - 1000 rows for examples
      - 2 columns for attributes
  - We generate each label by applying a *ground truth* linear function, corrupting them via additive noise $`\boldsymbol{\epsilon}`$, drawn independently and identically for each example:
    - $\mathbf{y}= \mathbf{X} \mathbf{w} + b + \boldsymbol{\epsilon}$
      - For convenience we assume that $`\boldsymbol{\epsilon} \sim N(0, 0.1^2)`$.
- Implementation)
  ```python
  class SyntheticRegressionData(d2l.DataModule):  #@save
      """Synthetic data for linear regression."""
      def __init__(self, w, b, noise=0.01, num_train=1000, num_val=1000,
                   batch_size=32):
          super().__init__()
          self.save_hyperparameters()
          n = num_train + num_val
          self.X = torch.randn(n, len(w)) # 2000 X 2 matrix with values in N(0,1)
          noise = torch.randn(n, 1) * noise
          self.y = torch.matmul(self.X, w.reshape((-1, 1))) + b + noise
  ```
- Test
  - Set parameters as $`\mathbf{w} = [2, -3.4]^\top`$ and $`b = 4.2`$.
    ```
    data = SyntheticRegressionData(w=torch.tensor([2, -3.4]), b=4.2)
    print('features:', data.X[0],'\nlabel:', data.y[0])
    ```
    ![]











<br>

* [Back to Dive into Deep Learning](../../main.md)