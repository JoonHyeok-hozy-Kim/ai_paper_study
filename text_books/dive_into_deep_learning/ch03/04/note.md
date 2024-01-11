* [Back to Dive into Deep Learning](../../main.md)

# 3.4. Linear Regression Implementation from Scratch

#### Index
1. Implementation
   1. [The Model](#341-defining-the-model)
   2. [The Loss Function](#342-defining-the-loss-function)
   3. [A Minibatch Stochastic Gradient Descent Optimizer]()
   4. [The Training Function]()
2. Test
   1. [Synthetic Data Generation]()
   2. [Application on the Model]()


### Import Packages
```python
import torch
from d2l import torch as d2l
```

<br><br>

## 3.4.1. Defining the Model
Implement the Model.
- In [the full script](scripts/LinearRegressionScratch.py#L5).
```python
class LinearRegressionScratch(d2l.Module):  #@save
    """The linear regression model implemented from scratch."""
    def __init__(self, num_inputs, lr, sigma=0.01):
        super().__init__()
        self.save_hyperparameters()
        self.w = torch.normal(0, sigma, (num_inputs, 1), requires_grad=True)
        self.b = torch.zeros(1, requires_grad=True)
```
- Set the parameters.
  - ```num_inputs``` : the number of inputs
  - ```lr``` : the learning rate
  - ```sigma``` : the standard deviation

<br>

Implement $\mathbf{y}= \mathbf{X} \mathbf{w} + b$ by adding the ```forward``` method to the ```LinearRegressionScratch``` class.
- In [the full script](scripts/LinearRegressionScratch.py#L15).
```python
@d2l.add_to_class(LinearRegressionScratch)  #@save
def forward(self, X):
    return torch.matmul(X, self.w) + self.b
```
- ```X``` : $n\times m$ matrix 
  - $n$ : the number of examples
  - $m$ : the number of features
- ```self.w``` : $m$ vector
- ```self.b``` : an integer, but [broadcasted](../../ch02/01/note.md#214-broadcasting) and can be added to the vector.

<br><br>

## 3.4.2 Defining the Loss Function
Implement the loss function by adding the ```loss``` method.
- In [the full script](scripts/LinearRegressionScratch.py#L20).
```python
@d2l.add_to_class(LinearRegressionScratch)  #@save
def loss(self, y_hat, y):
    l = (y_hat - y) ** 2 / 2
    return l.mean()
```

<br><br>

## 3.4.3 Defining the Optimization Algorithm
Implement the Stochastic Gradient Descent in the ```SGD``` class inheriting [the ```d2l.HyperParameters``` class](../02/note.md#3212-a-class-that-extend-constructor-call-signatures-implicitly-without-additional-code).
- In [the full script](scripts/LinearRegressionScratch.py#L26).
```python
class SGD(d2l.HyperParameters):  #@save
    """Minibatch stochastic gradient descent."""
    def __init__(self, params, lr):
        self.save_hyperparameters()

    def step(self):
        for param in self.params:
            param -= self.lr * param.grad

    def zero_grad(self):
        for param in self.params:
            if param.grad is not None:
                param.grad.zero_()
```


<br>

* [Back to Dive into Deep Learning](../../main.md)