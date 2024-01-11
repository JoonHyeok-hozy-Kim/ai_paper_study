* [Back to Dive into Deep Learning](../../main.md)

# 3.4. Linear Regression Implementation from Scratch

#### Index
1. Implementation
   1. [The Model](#341-defining-the-model)
   2. [The Loss Function]()
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

<br>

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
  - ```lr``` : 
  - ```sigma``` : the standard deviation

<br>

Implement $\mathbf{y}= \mathbf{X} \mathbf{w} + b$ by adding the ```forward``` method to the ```LinearRegressionScratch``` class.
- In [the full script](scripts/LinearRegressionScratch.py#L15).
```python
@d2l.add_to_class(LinearRegressionScratch)  #@save
def forward(self, X):
    return torch.matmul(X, self.w) + self.b
```




<br>

* [Back to Dive into Deep Learning](../../main.md)