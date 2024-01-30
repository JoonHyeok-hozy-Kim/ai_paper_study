* [Back to Dive into Deep Learning](../../main.md)

# 4.4. Softmax Regression Implementation from Scratch

#### Import packages
```python
import torch
from d2l import torch as d2l
```

## 4.4.1 The Softmax
- Recall the sum operation along specific dimensions in a tensor.
  - Sum over elements in each column.
    ```python
    X = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    X.sum(0, keepdims=True)
    ```
  - Sum over elements in each row.
    ```python
    X = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    X.sum(1, keepdims=True)
    ```
- We can use this for calculating the softmax function.
  - Recall that $`\displaystyle\textrm{softmax}(\mathbf{X})_{ij} = \frac{\exp{(\mathbf{X}_{ij})}}{\sum_k \exp{(X_{ik})}}`$
  - Thus calculate by
    1. Exponentiation of each term. 
    2. A sum over each row to compute the normalization constant for each example.
    3. Division of each row by its normalization constant, ensuring that the result sums to 1.  
    ```python
    def softmax(X):
        X_exp = torch.exp(X)
        partition = X_exp.sum(1, keepdims=True)
        return X_exp / partition  # The broadcasting mechanism is applied here
    ```
       - cf.)
         - Caution: the code above is not robust against very large or very small arguments.
         - Thus, we may use the built-in ```softmax()``` instead.
  - Built-in ```softmax()``` example.
    ```python
    X = torch.rand((2, 5))
    X_prob = softmax(X)
    X_prob, X_prob.sum(1)
    ```





<br>

* [Back to Dive into Deep Learning](../../main.md)