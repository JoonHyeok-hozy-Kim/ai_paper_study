* [Back to Dive into Deep Learning](../../main.md)

# 2.5 Automatic Differentiation

### Concept) Automatic Differentiation and Backproagation
- All modern deep learning frameworks offer automatic differentiation (often shortened to [autograd](#hands-on-autograd-package)). 
- As we pass data through each successive function, the framework builds a computational graph that tracks how each value depends on others. 
- To calculate derivatives, automatic differentiation works backwards through this graph applying the chain rule. 
- The computational algorithm for applying the chain rule in this fashion is called **backpropagation**.

<br>

### Hands on) Autograd Package
- First, import ```torch```
  ```python
  import torch
  ```

<br>

1. Simple function differentiation
   - e.g.) For $\mathbf{y} = 2\mathbf{x}^{\top}\mathbf{x}$, get $\nabla_{\mathbf{x}} \mathbf{y}$.
     - Declare $\mathbf{x}$ as ```x``` and allocate memory for the derivative at ```x.grad```.
       ```python
       x = torch.arange(4.0)
       x.requires_grad_(True)    # Or, x = torch.arange(4.0, requires_grad=True)
       x.grad                    # Allocate memory for the differentiation.
       ```
      - Declare $\mathbf{y} = 2\mathbf{x}^{\top}\mathbf{x}$
        ```python
        y = 2 * torch.dot(x, x)
        y
        ```
      - Calculate the gradient of $\mathbf{y}$ w.r.t. $\mathbf{x}$ using ```y.backward()``` method.
        ```python
        y.backward()
        ```
      - Check the result, saved at ```x.grad```.
        ```python
        x.grad
        ```
        ![]








<br>

* [Back to Dive into Deep Learning](../../main.md)