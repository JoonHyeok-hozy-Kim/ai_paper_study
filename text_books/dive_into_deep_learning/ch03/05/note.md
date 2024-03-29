* [Back to Dive into Deep Learning](../../main.md)

# 3.5. Concise Implementation of Linear Regression
Implementing [the same linear regression model](../04/note.md#34-linear-regression-implementation-from-scratch) concisely by using high-level APIs of deep learning frameworks.   

### Import Packages
```python
import numpy as np
import torch
from torch import nn
from d2l import torch as d2l
```


<br><br>

## 3.5.1 Defining the Model
For standard operations, we can use a framework’s predefined **layers**, which allow us to focus on the layers used to construct the model rather than worrying about their implementation.   

![](images/001.svg)

The layer is called fully connected, since each of its inputs is connected to each of its outputs by means of a matrix–vector multiplication.   

In PyTorch, the fully connected layer is defined in ```Linear``` and ```LazyLinear``` classes (available since version 1.8.0).
- ```Linear``` asks for how many inputs go into this layer.
  - Specifying input shapes is inconvenient and may require nontrivial calculations (such as in convolutional layers).
- ```LazyLinear``` allows users to specify *merely* the output dimension.

```python
class LinearRegression(d2l.Module):  #@save
    """The linear regression model implemented with high-level APIs."""
    def __init__(self, lr):
        super().__init__()
        self.save_hyperparameters()
        self.net = nn.LazyLinear(1)
        self.net.weight.data.normal_(0, 0.01)
        self.net.bias.data.fill_(0)
```

In the forward method we just invoke the built-in ```__call__``` method of the predefined layers to compute the outputs.
```python
@d2l.add_to_class(LinearRegression)  #@save
def forward(self, X):
    return self.net(X)
```



<br><br>

## 3.5.2 Defining the Loss Function
The ```MSELoss``` class computes the mean squared error. 
- By default, ```MSELoss``` returns the average loss over examples. 
- It is faster (and easier to use) than implementing our own.
```python
@d2l.add_to_class(LinearRegression)  #@save
def loss(self, y_hat, y):
    fn = nn.MSELoss()
    return fn(y_hat, y)
```



<br><br>

## 3.5.3 Defining the Optimization Algorithm
PyTorch supports it alongside a number of [Minibatch SGD](../../ch03/01/note.md#3114-minibatch-stochastic-gradient-descent) variations on this algorithm in the ``optim`` module. When we instantiate an ```SGD``` instance, we specify the parameters to optimize over, obtainable from our model via ```self.parameters()```, and the learning rate (```self.lr```) required by our optimization algorithm.
```python
@d2l.add_to_class(LinearRegression)  #@save
def configure_optimizers(self):
    return torch.optim.SGD(self.parameters(), self.lr)
```


<br><br>

## 3.5.4 Training
```python
model = LinearRegression(lr=0.03)
data = d2l.SyntheticRegressionData(w=torch.tensor([2, -3.4]), b=4.2)
trainer = d2l.Trainer(max_epochs=3)
trainer.fit(model, data)


# Compare the model parameters learned by training on finite data and the actual parameters that generated our dataset.
@d2l.add_to_class(LinearRegression)  #@save
def get_w_b(self):
    return (self.net.weight.data, self.net.bias.data)
w, b = model.get_w_b()

print(f'error in estimating w: {data.w - w.reshape(data.w.shape)}')
print(f'error in estimating b: {data.b - b}')
```










<br>

* [Back to Dive into Deep Learning](../../main.md)