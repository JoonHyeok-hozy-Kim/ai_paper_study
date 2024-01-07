* [Back to Dive into Deep Learning](../../main.md)

# 3.2 Object-Oriented Design for Implementation

### Objective) Designing APIs
- Inspired by open-source libraries such as [PyTorch Lightning](https://lightning.ai/), at a high level we wish to have three classes: 
  1. Module contains models, losses, and optimization methods; 
  2. DataModule provides data loaders for training and validation; 
  3. Both classes are combined using the Trainer class, which allows us to train models on a variety of hardware platforms.
     - We will touch upon the Trainer class only when we discuss GPUs, CPUs, parallel training, and optimization algorithms.

---
## Implementation

### 3.2.0 Importing Modules
```python
import time
import numpy as np
import torch
from torch import nn
from d2l import torch as d2l
```

### 3.2.1 Utilities
Utilities to simplify object-oriented programming in Jupyter notebooks.

1. A function that register functions as methods in a class after the class has been created.
   - Implementation)
     - Define ```add_to_class()``` function as follows.
       ```python
       def add_to_class(Class):  #@save
           """Register functions as methods in created class."""
           def wrapper(obj):
               setattr(Class, obj.__name__, obj)
           
           return wrapper
       ```
     - Add ```do()``` method to a class that is instanciated by ```add_to_class()```.
       ```python
       @add_to_class(A)
       def do(self):
          print('Class attribute "b" is', self.b)
       ```
   - Usage Example)
     - Declare a class.
       ```python
       class A:
           def __init__(self):
               self.b = 1
       
       a = A()
       ```
     - Add a method to the class.
       ```python
       @add_to_class(A)
       def do(self):
           print('Class attribute "b" is', self.b)
       
       a.do()
       ```
2. A class that extend constructor call signatures implicitly without additional code.
   - Implementation)
     - Define the ```HyperParameters``` class.
       ```python
       class HyperParameters:  #@save
           """The base class of hyperparameters."""
           def save_hyperparameters(self, ignore=[]):
               raise NotImplemented
       ```
       - The exact implementation will be covered in Section 23.7.
       - Currently, use the fully implemented HyperParameters class saved in ```d2l``` package.
   - Usage Example)
     - Define a class that inherits from ```HyperParameters``` and calls ```save_hyperparameters``` in the ```__init__``` method.
       ```python
       # Call the fully implemented HyperParameters class saved in d2l
       class B(d2l.HyperParameters):
           def __init__(self, a, b, c):
               self.save_hyperparameters(ignore=['c'])
               print('self.a =', self.a, 'self.b =', self.b)
               print('There is no self.c =', not hasattr(self, 'c'))
       
       b = B(a=1, b=2, c=3)
       ```
3. A class that plot experiment progress interactively while it is going on.
   - Implementation)
     - Define the ```ProgressBoard``` class that inherits from ```HyperParameters```.
       ```python
       class ProgressBoard(d2l.HyperParameters):  #@save
           """The board that plots data points in animation."""
           def __init__(self, xlabel=None, ylabel=None, xlim=None,
                        ylim=None, xscale='linear', yscale='linear',
                        ls=['-', '--', '-.', ':'], colors=['C0', 'C1', 'C2', 'C3'],
                        fig=None, axes=None, figsize=(3.5, 2.5), display=True):
               self.save_hyperparameters()
       
           def draw(self, x, y, label, every_n=1):
               raise NotImplemented
       ```
       - The exact implementation will be covered in Section 23.7.
       - Currently, use the fully implemented ProgressBoard class saved in ```d2l``` package.
   - Usage Example)
     - Draw $\sin{}$ and $\cos{}$ with a different smoothness.
       ```python
       board = d2l.ProgressBoard('x')
       for x in np.arange(0, 10, 0.1):
           board.draw(x, np.sin(x), 'sin', every_n=2)
           board.draw(x, np.cos(x), 'cos', every_n=10)
       ```












<br>

* [Back to Dive into Deep Learning](../../main.md)