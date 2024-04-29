* [Back to Dive into Deep Learning](../../main.md)

# 6.5 Custom Layers

Import Packages
```python
import torch
from torch import nn
from torch.nn import functional as F
from d2l import torch as d2l
```

<br>

## 6.5.1 Layers without Parameters
Simply inherit from the base layer and implement the forward propagation function.

#### E.g.) Centered Layer
- Objective)
  - Simply subtract mean from value and forward.
- Implementation)
    ```python
    class CenteredLayer(nn.Module):
        def __init__(self):
            super().__init__()

        def forward(self, X):
            return X - X.mean()     # Implementation
    ```
- Test)
  - Check whether the layer works as intended.
    ```python
    layer = CenteredLayer()
    layer(torch.tensor([1.0, 2, 3, 4, 5]))  # Centered around 3
    ```
- Application)
  - This layer can be incorporated into a network as others.
    ```python
    net = nn.Sequential(nn.LazyLinear(128), CenteredLayer())
    ```
    - Check whether the layer is working fine in the network.
      ```python
      Y = net(torch.rand(4, 8))
      Y.mean()
      ```
      - Result) a very small nonzero number due to quantization


<br>

## 6.5.2 Layers with Parameters
- How to)
  - Use built-in functions to create parameters.
    - They govern access, initialization, sharing, saving, and loading model parameters.
    - This way, among other benefits, we will not need to write custom serialization routines for every custom layer.
  - Implement the forward propagation function.

#### E.g.) Customized Linear Layer
- Objective)
  - Get input parameters that specify the number of input and output, respectively.
    - ```in_units``` : the number of input
    - ```units``` : the number of output
  - Create weight and bias as parameters and optimize them.
  - Activate with ReLU.
- Implementation)
  ```python
  class MyLinear(nn.Module):
      def __init__(self, in_units, units):
          super().__init__()
          self.weight = nn.Parameter(torch.randn(in_units, units))  # Create parameters with the built-in function
          self.bias = nn.Parameter(torch.randn(units,))             # Create parameters with the built-in function
  
      def forward(self, X):
          linear = torch.matmul(X, self.weight.data) + self.bias.data   # Implement linear operation.
          return F.relu(linear)                                         # Activate with ReLU.
  ```
- Test)
  - Simple test.
    ```python
    linear = MyLinear(5, 3)   # Instantiate the layer.
    linear.weight             # Check the weight initialization.

    linear(torch.rand(2, 5))  # Pass through the data.
    ```
    - Result) Two data with three output values respectively.
  - Incorporate the layer into a network.
    ```python
    net = nn.Sequential(MyLinear(64, 8), MyLinear(8, 1))
    net(torch.rand(2, 64))
    ```
    - Result) Two data with two output values respectively.



<br>

* [Back to Dive into Deep Learning](../../main.md)