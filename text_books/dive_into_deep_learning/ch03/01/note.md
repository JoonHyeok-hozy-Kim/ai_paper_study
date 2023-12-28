* [Back to Dive into Deep Learning](../../main.md)

# 3.1 Linear Regression
Predicting numerical values.

#### Terms)
- The dataset is called a training dataset.
- Each row (containing the data corresponding to one sale) is called an example (or data point, instance, sample).
- The thing we are trying to predict (price) is called a label (or target). 
- The variables (age and area) upon which the predictions are based are called features (or covariates).

<br>

#### Importing Packages
```python
import math
import time
import numpy as np
import torch
from d2l import torch as d2l
```

<br>

### 3.1.1.1 Model
- Assumptions)
  - $d$ features and $n$ examples
- Model)
  - Representation)
    - $\hat{y}=w_1x_1 + \cdots + w_dx_d + b$
      - Or, $\hat{y}=\mathbf{w}^{\top}\mathbf{x}+b$
        - where $\mathbf{w}, \mathbf{x} \in \mathbb{R}^d$
    - Referring to the entire dataset of $n$ examples using a design matrix $\mathbf{X} \in \mathbb{R}^{n \times d}$
      - $\hat{\mathbf{y}} = \mathbf{X} \mathbf{w} + b$
  - Goal)
    - Find the weight vector $\mathbf{w}$ and the bias term $b$ such that the new example’s label will (in expectation) be predicted with the smallest error, given features of a new data example sampled from the same distribution as $\mathbf{X}$.
- Prop.)
  - Even when we are confident that the underlying relationship is linear, we will incorporate a noise term to account for errors.


<br>

### 3.1.1.2 Loss Function
#### Concept) Squared Error
- For the $i$-th example, the squared error is given by
  - $l^{(i)}(\mathbf{w}, b) = \frac{1}{2} \left(\hat{y}^{(i)} - y^{(i)}\right)^2$
- Prop.)
  - Large differences between estimates $\hat{y}^{(i)}$ and targets $y^{(i)}$  lead to even larger contributions to the loss, due to its quadratic form.
  - To measure the quality of a model on the entire dataset of examples, we simply average (or equivalently, sum) the losses on the training set:
    - $L(\mathbf{w}, b) =\frac{1}{n}\sum_{i=1}^n l^{(i)}(\mathbf{w}, b) =\frac{1}{n} \sum_{i=1}^n \frac{1}{2}\left(\mathbf{w}^\top \mathbf{x}^{(i)} + b - y^{(i)}\right)^2$
  - Training a model
    - Find $(\mathbf{w}^*, b^*)$ such that
      - $\mathbf{w}^*, b^* = \operatorname*{argmin}_{\mathbf{w}, b}\  L(\mathbf{w}, b)$


<br>

### 3.1.1.3 Analytic Solution
1. Subsume the bias $b$ into the parameter $\mathbf{w}$ by appending a column to the design matrix consisting of all 1s.
   - $`\mathbf{X} = \left[ \begin{array}{c} 1 & x_{11} & \cdots & x_{1d} \\ 1 & x_{21} & \cdots & x_{2d} \\ \vdots & \vdots & \ddots & \vdots \\ 1 & x_{n1} & \cdots & x_{nd} \end{array} \right]`$, $`\mathbf{w} = \left[ \begin{array}{c} b \\ w_1 \\ w_2 \\ \vdots \\ w_d \end{array} \right]`$
2. Then our problem is to minimize $||\mathbf{y}-\mathbf{Xw}||^2$




<br>

* [Back to Dive into Deep Learning](../../main.md)