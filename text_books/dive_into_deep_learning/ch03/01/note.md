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
2. Then our problem is to minimize the loss function of $||\mathbf{y}-\mathbf{Xw}||^2$
   - As long as $\mathbf{X}$ has full rank, then there will be just one critical point on the loss surface and it corresponds to the minimum of the loss over the entire domain.
   - Taking derivative of the loss function w.r.t. $\mathbf{w}$,
     - $\partial_\mathbf{w}||\mathbf{y}-\mathbf{Xw}||^2 = 2\mathbf{X}^\top(\mathbf{Xw-y})=0$
   - Thus, $\mathbf{X}^\top\mathbf{Xw} = \mathbf{X}^\top\mathbf{y}$
   - If $\mathbf{X}^\top\mathbf{X}$ is invertible, we can get the unique solution 
     - $\mathbf{w}^\star = \left(\mathbf{X}^\top\mathbf{X}\right)^{-1}\mathbf{X}^\top\mathbf{y}$


<br><br>

### 3.1.1.4 Minibatch Stochastic Gradient Descent
#### Concept) Gradient Descent
- Def.)
  - Iteratively reducing the error by updating the parameters in the direction that incrementally lowers the loss function

<br>

#### Concept) Naive Gradient Descent
- How?)
  - Taking the derivative of the loss function, which is an average of the losses computed on **every single example in the dataset**.
- Advantage)
  - Very powerful
- Drawback)
  - Extremely slow!
  - If there is a lot of redundancy in the training data, the benefit of a full update is limited.

<br>

#### Concept) Stochastic Gradient Descent (SGD)
- How?)
  - Consider only a single example at a time and to take update steps based on one observation at a time
- Advantage)
  - Effective even for large datasets
- Drawback)
  - Maybe slow because it can take a lot longer to process one sample at a time compared to a full batch.
     - why?)
       - CPUs are a lot faster **(1) multiplying and adding numbers** than they are at **(2) moving data from main memory to processor cache**. 
       - It is up to an order of magnitude more efficient to perform **(1) a matrix–vector multiplication** than **(2) a corresponding number of vector–vector operations**.
       - **(1) Full Batch** / **(2) SGD**
  - Some of the layers, such as batch normalization, only work well when we **have access to more than one observation at a time**.

<br>

#### Concept) Minibatch Stochastic Gradient Descent
- How?)
  - The intermediate strategy between Full Batch and SGD.
  - The size of the minibatch
    - depends on many factors, such as the amount of memory, the number of accelerators, the choice of layers, and the total dataset size
    - a number between 32 and 256, preferably a multiple of a large power of, is a good start.
- Model)
  1. Initialize the values of the model parameters, typically at random.
  2. In each iteration $t$,
     1. Randomly sample a minibatch $\mathcal{B}_t$
        - such that $|B|=|\mathcal{B}_t|, \forall t$, 
          - i.e.) Fix the size.
     2. Compute the derivative (gradient) of the **average** loss on the minibatch with respect to the model parameters $(\mathbf{w}, b)$.
        - $`\frac{1}{|\mathcal{B}|} \sum_{i \in \mathcal{B}_t} \partial_{(\mathbf{w},b)} l^{(i)}(\mathbf{w},b)`$
     3. Multiply the gradient by the learning rate $\eta$, and subtract the resulting term from the current parameter values.
        - i.e.) $`(\mathbf{w},b) \leftarrow (\mathbf{w},b) - \frac{\eta}{|\mathcal{B}|} \sum_{i \in \mathcal{B}_t} \partial_{(\mathbf{w},b)} l^{(i)}(\mathbf{w},b)`$
          - where $l^{(i)}(\mathbf{w}, b) = \frac{1}{2} \left(\hat{y}^{(i)} - y^{(i)}\right)^2$
- Solution)
  - For quadratic losses and affine transformations, this has a closed-form expansion:
    - $`\begin{aligned} \mathbf{w} & \leftarrow \mathbf{w} - \frac{\eta}{|\mathcal{B}|} \sum_{i \in \mathcal{B}_t} \partial_{\mathbf{w}} l^{(i)}(\mathbf{w}, b) && = \mathbf{w} - \frac{\eta}{|\mathcal{B}|} \sum_{i \in \mathcal{B}_t} \mathbf{x}^{(i)} \left(\mathbf{w}^\top \mathbf{x}^{(i)} + b - y^{(i)}\right)\\ b &\leftarrow b -  \frac{\eta}{|\mathcal{B}|} \sum_{i \in \mathcal{B}_t} \partial_b l^{(i)}(\mathbf{w}, b) &&  = b - \frac{\eta}{|\mathcal{B}|} \sum_{i \in \mathcal{B}_t} \left(\mathbf{w}^\top \mathbf{x}^{(i)} + b - y^{(i)}\right). \end{aligned}`$


<br>

* [Back to Dive into Deep Learning](../../main.md)