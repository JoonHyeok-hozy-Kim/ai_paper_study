import torch
from d2l import torch as d2l

a
a
a
a
a
a

a
a
a
a
a
a


# 3.4.1 Model
class LinearRegressionScratch(d2l.Module): #@save
    """The linear regression model implemented from scratch."""
    def __init__(self, num_inputs, lr, sigma=0.01):
        super().__init__()
        self.save_hyperparameters()
        self.w = torch.normal(0, sigma, (num_inputs, 1), requires_grad=True) # Refer to Gradient Buffer
        self.b = torch.zeros(1, requires_grad=True)

a
a
a
a
a
a
a
a
a
a
a
a
a
a
a



a
a
a
a
a
a
a
a