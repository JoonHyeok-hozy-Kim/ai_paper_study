* [Back to Dive into Deep Learning](../../main.md)

# 6.6 File I/O

#### Concept) Checkpointing
- Desc.)
  - Saving the intermediate results of the learning process
- Why needed?)
  - In practice, the learning process takes a long period of time.
    - Even days of training.
  - Thus, we should ensure that we do not lose the computation results due to sudden accident.
  - This chapter covers the method of storing and loading both individual **weights vectors** and **entire models**.

<br>

#### Import Packages
```python
import torch
from torch import nn
from torch.nn import functional as F
```

<br>

## 6.6.1 Loading and Saving Tensors
Call the ```save``` and ```load``` function of the tensor object.
```python
x = torch.arange(4)
torch.save(x, 'x-file')     # Save!

x2 = torch.load('x-file')   # Load!
x2
```

Data structures like ```list``` and ```dict``` can be used to save and load tensors.
```python
# Using list
y = torch.zeros(4)
torch.save([x, y],'x-files')    # Assign torch objects to a list and save.
x2, y2 = torch.load('x-files')  # Load the list!
(x2, y2)

# Using dict
mydict = {'x': x, 'y': y}       # Assign torch objects to a dict.
torch.save(mydict, 'mydict')    # Save.
mydict2 = torch.load('mydict')  # Load!
mydict2
```

<br>

## 6.6.2 Loading and Saving Model Parameters
- Deep learning frameworks provide built-in functionalities to load and save entire networks.
  - cf.) They save model **parameters**, not the entire model.

<br>

#### E.g.) 3-Layer MLP
Set up a MLP.
```python
class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.hidden = nn.LazyLinear(256)
        self.output = nn.LazyLinear(10)

    def forward(self, x):
        return self.output(F.relu(self.hidden(x)))

net = MLP()
X = torch.randn(size=(2, 20))
Y = net(X)
```

Store the parameters of the model as a file with the name “mlp.params” using the ```state_dict()``` method.
```python
torch.save(net.state_dict(), 'mlp.params')
```

How to recover the model.
1. Instantiate a clone MLP object.
2. Read parameters from the stored data and load them using the ```load_state_dict()``` method.
```python
clone = MLP()
clone.load_state_dict(torch.load('mlp.params'))

# # Check the parameter properties using the eval() method.
clone.eval()    

# Compare it with the original Y using the same input X.
Y_clone = clone(X)
Y_clone == Y
```





<br>

* [Back to Dive into Deep Learning](../../main.md)