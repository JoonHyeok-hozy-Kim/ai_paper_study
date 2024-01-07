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
   - e.g.)
     ```python
     class A:
         def __init__(self):
             self.b = 1
     
     a = A()
     ```
     












<br>

* [Back to Dive into Deep Learning](../../main.md)