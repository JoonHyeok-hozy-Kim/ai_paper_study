* [Back to Dive into Deep Learning](../../main.md)

# 6.3. Parameter Initialization
How to call the built-in parameter initializations and customize it.

#### Import packages.
```python
import torch
from torch import nn
```

#### Create a simple network.
```python
# A network with a 8-unit hidden layer and one output layer.
net = nn.Sequential(
    nn.LazyLinear(8),
    nn.ReLU(),
    nn.LazyLinear(1),
)

X = torch.rand(size=(2,4))
net(X).shape
```

<br>

## 6.3.1 Built-in Initialization
Call Gaussian random variables and zero initialization.
```python
def init_normal(module):
    if type(module) == nn.Linear:
        nn.init.normal_(module.weight, mean=0, std=0.01)    # Gaussian initialization
        nn.init.zeros_(module.bias)                         # Zero initialization.

net.apply(init_normal)  # Apply the initialization setting.
net[0].weight.data[0], net[0].bias.data[0]
```
- Desc.)
  - ```nn.init.normal_()``` : Gaussian
  - ```nn.init.zeros_()``` : Zero

<br>

Initializing to a constant value.
```python
def init_constant(module):
    if type(module) == nn.Linear:
        nn.init.constant_(module.weight, 1)     # Constant initialization
        nn.init.zeros_(module.bias)

net.apply(init_constant)
net[0].weight.data[0], net[0].bias.data[0]
```
- Desc.)
  - ```nn.init.constant_()``` : Constant

<br>

Initializing with xavier initializer : ```nn.init.xavier_uniform_()```
```python
def init_xavier(module):
    if type(module) == nn.Linear:
        nn.init.xavier_uniform_(module.weight)

def init_42(module):
    if type(module) == nn.Linear:
        nn.init.constant_(module.weight, 42)

net[0].apply(init_xavier)
net[2].apply(init_42)
print(net[0].weight.data[0])
print(net[2].weight.data)
```

<br><br>

## 6.3.2 Customized Initialization
#### E.g.) Customized Uniform Distribution
- Distribution)
  - $`\begin{aligned}
    w \sim
    \begin{cases}
        U(5,10) & \textrm{with probability } \frac{1}{4} \\
        0 & \textrm{with probability } \frac{1}{2} \\
        U(-10, -5) & \textrm{with probability } \frac{1}{4} \\
    \end{cases}
  \end{aligned}`$
- Implementation)
    ```python
    def my_init(module):
        if type(module) == nn.Linear:
            print("Init", *[(name, param.shape)
                            for name, param in module.named_parameters()][0])
            nn.init.uniform_(module.weight, -10, 10)
            module.weight.data *= module.weight.data.abs() >= 5

    net.apply(my_init)
    net[0].weight[:2]
    ```

<br>

#### E.g.) Direct Setting
```python
net[0].weight.data[:] += 1
net[0].weight.data[0, 0] = 42
net[0].weight.data[0]
```


<br>

* [Back to Dive into Deep Learning](../../main.md)