* [Back to Dive into Deep Learning](../../main.md)

# 5.2 Implementation of Multilayer Perceptrons

#### Import packages
```python
import torch
from torch import nn
from d2l import torch as d2l
```

## 5.2.1 Implementation from Scratch
### 5.2.1.1 Initializing Model Parameters
- Assumptions)
  - A classification data set with $784$ input features and $10$ classes.
    - Just like [the MNIST problem](../../ch04/02/note.md#tech-mnist--lecun-et-al-1998) that we previously covered.
      - $28\times 28=784$ grid of grayscale pixel image
      - $10$ classification output categories
  - One hidden layer and $256$ hidden units (i.e. the width).
    - The number of hidden layer and the hidden units are adjustable with the hyperparameters.
      - cf.) Choose the layer widths to be divisible by larger powers of $2$, which is computationally efficient due to the way memory is allocated and addressed in hardware.
      - cf.) For every layer, we must keep track of **one weight matrix** and **one bias vector**.

#### Implementation
```python
class MLPScratch(d2l.Classifier):
    def __init__(self, num_inputs, num_outputs, num_hiddens, lr, sigma=0.01):
        super().__init__()
        self.save_hyperparameters()
        self.W1 = nn.Parameter(torch.randn(num_inputs, num_hiddens) * sigma)
        self.b1 = nn.Parameter(torch.zeros(num_hiddens))
        self.W2 = nn.Parameter(torch.randn(num_hiddens, num_outputs) * sigma)
        self.b2 = nn.Parameter(torch.zeros(num_outputs))
```
- Recall $`\begin{aligned}
        \mathbf{H} & = \mathbf{X} \mathbf{W}^{(1)} + \mathbf{b}^{(1)} \\
        \mathbf{O} & = \mathbf{H}\mathbf{W}^{(2)} + \mathbf{b}^{(2)}
    \end{aligned}, 
    \;\; \exists \left\{ \begin{array}{ll} \mathbf{W}^{(1)} \in \mathbb{R}^{d \times  h} & \textrm{ : the hidden-layer weights} \\ \mathbf{b}^{(1)} \in \mathbb{R}^{1 \times h} &  \textrm{ : the hidden-layer biases} \\ \mathbf{W}^{(2)} \in \mathbb{R}^{h \times q} & \textrm { : the output-layer weights} \\ \mathbf{b}^{(2)} \in \mathbb{R}^{1 \times q} & \textrm{ :  the output-layer biases} \end{array} \right.`$












<br>

* [Back to Dive into Deep Learning](../../main.md)