* [Back to Dive into Deep Learning](../../main.md)

# 5.4. Numerical Stability and Initialization
- Ideation)
  - Recall that we initialized parameters.
    - This choice of initialization scheme plays a significant role in neural network learning.
      - why?)
        - It can be crucial for maintaining **numerical stability**.
    - The choice of initialization can be tied up with the choice of the **nonlinear activation function**.
      - why?)
        - Choosing appropriate initial parameters can determine how **quickly** our optimization algorithm converges.
        - Poor choices can cause [exploding or vanishing gradients](#541-vanishing-and-exploding-gradients) while training.

#### Import Packages
```python
import torch
from d2l import torch as d2l
```

<br>

## 5.4.1 Vanishing and Exploding gradients
- Setting)
  - Consider a deep network with...
    - $L$ : the set of layers in the network
      - $l\in L$ : a layer in the network
    - $\mathbf{x}$ : the input to the network
    - $\mathbf{o}$ : the output of the network
    - $f_l$ : a transformation of the layer $l$
      - where $f_l$ is parametrized by weights $\mathbf{W}^{(l)}$
    - $\mathbf{h}^{(l)} = f_l(\mathbf{h}^{(l-1)})$ : the output of the layer $l$
- Derivation)
    - Then, $\mathbf{o}$ can be denoted as $\mathbf{o} = f_L \circ\cdots\circ f_1(\mathbf{x})$
    - Thus, the gradient of $\mathbf{o}$ is $`\begin{array}{lll}
        \partial_{\mathbf{W}^{(l)}} \mathbf{o} 
        &= \underbrace{\partial_{\mathbf{h}^{(L-1)}} \mathbf{h}^{(L)}}_{ \mathbf{M}^{(L)} \stackrel{\textrm{def}}{=}} \; \cdots \; \underbrace{\partial_{\mathbf{h}^{(l)}} \mathbf{h}^{(l+1)}}_{ \mathbf{M}^{(l+1)} \stackrel{\textrm{def}}{=}} \; \underbrace{\partial_{\mathbf{W}^{(l)}} \mathbf{h}^{(l)}}_{ \mathbf{v}^{(l)} \stackrel{\textrm{def}}{=}} \\
        &= \mathbf{M}^{(L)} \; \cdots \; \mathbf{M}^{(l+1)} \; \mathbf{v}^{(l)}
    \end{array}`$













<br>

* [Back to Dive into Deep Learning](../../main.md)