* [Back to Dive into Deep Learning](../../main.md)

# 6.4 Lazy Initialization

### Concept) Lazy Initialization
- Desc.)
  - An initialization technique that the model does not specify dimensionality of the input.
  - When the first data is passed through the model, it recognizes the shape of the data initialize the size and the weight values.
  - The framework automatically proceeds to the following layers through the computational graph until all shapes are known.

#### Test)
Import packages.
```python
import torch
from torch import nn
from d2l import torch as d2l
```

Instantiate a MLP.
```python
net = nn.Sequential(
    nn.LazyLinear(256), nn.ReLU(), 
    nn.LazyLinear(10)
)
```

Check whether the weights are initialized. 
```python
net[0].weight
```
- Desc.)
  - ```<UninitializedParameter>``` denotes that the weight is not initialized yet.

Create a data and pass it through the model.
```python
X = torch.rand(2, 20)   # 2 X 20 Matrix
net(X)                  # Pass the data.

net[0].weight.shape     # Check whether the weights are initialized. 
```
- Desc.)
  - ```torch.Size([256, 20])``` denotes that the framework automatically recognized the size of the input data.


<br>

#### Tech.) Passing Dummy Input to Infer all Parameter Shapes
```python
@d2l.add_to_class(d2l.Module)  #@save
def apply_init(self, inputs, init=None):
    self.forward(*inputs)   # Pass the input data
    if init is not None:
        self.net.apply(init)
```



<br>

* [Back to Dive into Deep Learning](../../main.md)