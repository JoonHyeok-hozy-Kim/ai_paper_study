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

#### 3.2.1.1. A function that register functions as methods in a class after the class has been created.
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
#### 3.2.1.2. A class that extend constructor call signatures implicitly without additional code.
- Implementation)
  - Define the ```HyperParameters``` class.
    ```python
    class HyperParameters:  #@save
        """The base class of hyperparameters."""
        def save_hyperparameters(self, ignore=[]):
            raise NotImplemented
    ```
    - The exact implementation will be covered in Section 23.7.
    - Currently, use the fully implemented HyperParameters class saved in ```d2l```package.
- Usage Example)
  - Define a class that inherits from ```HyperParameters``` and call```save_hyperparameters``` in the ```__init__``` method.
    ```python
    # Call the fully implemented HyperParameters class saved in d2l
    class B(d2l.HyperParameters):
        def __init__(self, a, b, c):
            self.save_hyperparameters(ignore=['c'])
            print('self.a =', self.a, 'self.b =', self.b)
            print('There is no self.c =', not hasattr(self, 'c'))
    
    b = B(a=1, b=2, c=3)
    ```
#### 3.2.1.3. A class that plot experiment progress interactively while it is going on.
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
    - Currently, use the fully implemented ProgressBoard class saved in ```d2l``package.
- Usage Example)
  - Draw $\sin{}$ and $\cos{}$ with a different smoothness.
    ```python
    board = d2l.ProgressBoard('x')
    for x in np.arange(0, 10, 0.1):
        board.draw(x, np.sin(x), 'sin', every_n=2)
        board.draw(x, np.cos(x), 'cos', every_n=10)
    ```

<br>

### 3.2.2 Models
The Module class is the base class of all models we will implement.   
At the very least we need three methods. 
1. ```__init__``` stores the learnable parameters. 
2. The ```training_step``` method accepts a data batch to return the loss value
3. ```configure_optimizers``` returns the optimization method, or a list of them, that is used to update the learnable parameters.   
4. (Optional) ```validation_step``` reports the evaluation measures. 
5. (Optional) ```forward``` : a reusable method that we can compute the output into

- Implementation)
  ```python
  class Module(nn.Module, d2l.HyperParameters):  #@save
      """The base class of models."""
      def __init__(self, plot_train_per_epoch=2, plot_valid_per_epoch=1):
          super().__init__()
          self.save_hyperparameters()
          self.board = ProgressBoard()
  
      def loss(self, y_hat, y):
          raise NotImplementedError
  
      def forward(self, X):
          assert hasattr(self, 'net'), 'Neural network is defined'
          return self.net(X)
  
      def plot(self, key, value, train):
          """Plot a point in animation."""
          assert hasattr(self, 'trainer'), 'Trainer is not inited'
          self.board.xlabel = 'epoch'
          if train:
              x = self.trainer.train_batch_idx / \
                  self.trainer.num_train_batches
              n = self.trainer.num_train_batches / \
                  self.plot_train_per_epoch
          else:
              x = self.trainer.epoch + 1
              n = self.trainer.num_val_batches / \
                  self.plot_valid_per_epoch
          self.board.draw(x, value.to(d2l.cpu()).detach().numpy(),
                          ('train_' if train else 'val_') + key,
                          every_n=int(n))
  
      def training_step(self, batch):
          l = self.loss(self(*batch[:-1]), batch[-1])
          self.plot('loss', l, train=True)
          return l
  
      def validation_step(self, batch):
          l = self.loss(self(*batch[:-1]), batch[-1])
          self.plot('loss', l, train=False)
  
      def configure_optimizers(self):
          raise NotImplementedError
  ```
  - ```Module``` is a subclass of ```nn.Module```, the base class of neural networks in PyTorch.
    - It provides convenient features for handling neural networks. 
      - e.g., if we define a ```forward``` method, such as ```forward(self, X)```, then for an instance a we can invoke this method by ```a(X)```. This works since it calls the forward method in the built-in ```__call__``` method. You can find more details and examples about ```nn.Module``` in Section 6.1.

<br>

### 3.2.3 Data
- Desc.)
  - The ```DataModule``` class is the base class for data.   
    - Quite frequently the ```__init__``` method is used to prepare the data. 
      - This includes downloading and preprocessing if needed. 
    - The ```train_dataloader``` returns *the data loader* for the training dataset. 
      - A *data loader* is a (Python) generator that yields a data batch each time it is used. 
    - This batch is then fed into the ```training_step``` method of ```Module``` to compute the loss. 
    - There is an optional ```val_dataloader``` to return the validation dataset loader.
      - It behaves in the same manner, except that it yields data batches for the ```validation_step``` method in ```Module```.
- Implementation)
  ```python
  class DataModule(d2l.HyperParameters):  #@save
      """The base class of data."""
      def __init__(self, root='../data', num_workers=4):
          self.save_hyperparameters()
  
      def get_dataloader(self, train):
          raise NotImplementedError
  
      def train_dataloader(self):
          return self.get_dataloader(train=True)
  
      def val_dataloader(self):
          return self.get_dataloader(train=False)
  ```

<br>

### 3.2.4 Training
- Desc.)
  - The ```Trainer``` class trains the learnable parameters in the Module class with data specified in DataModule. 
  - The key method is ```fit```.
    - ```fit``` accepts two arguments: 
      1. ```model``` : an instance of Module
      2. ```data``` : an instance of DataModule. 
    - It then iterates over the entire dataset ```max_epochs``` times to train the model. 
- Implementation)
  ```python
  class Trainer(d2l.HyperParameters):  #@save
      """The base class for training models with data."""
      def __init__(self, max_epochs, num_gpus=0, gradient_clip_val=0):
          self.save_hyperparameters()
          assert num_gpus == 0, 'No GPU support yet'
  
      def prepare_data(self, data):
          self.train_dataloader = data.train_dataloader()
          self.val_dataloader = data.val_dataloader()
          self.num_train_batches = len(self.train_dataloader)
          self.num_val_batches = (len(self.val_dataloader)
                                  if self.val_dataloader is not None else 0)
  
      def prepare_model(self, model):
          model.trainer = self
          model.board.xlim = [0, self.max_epochs]
          self.model = model
  
      def fit(self, model, data):
          self.prepare_data(data)
          self.prepare_model(model)
          self.optim = model.configure_optimizers()
          self.epoch = 0
          self.train_batch_idx = 0
          self.val_batch_idx = 0
          for self.epoch in range(self.max_epochs):
              self.fit_epoch()
  
      def fit_epoch(self):
          raise NotImplementedError
  ```








<br>

* [Back to Dive into Deep Learning](../../main.md)