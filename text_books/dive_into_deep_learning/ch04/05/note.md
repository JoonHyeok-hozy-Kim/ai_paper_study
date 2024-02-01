* [Back to Dive into Deep Learning](../../main.md)

# 4.5. Concise Implementation of Softmax Regression

#### Import Libraries
```python
import torch
from torch import nn
from torch.nn import functional as F
from d2l import torch as d2l
```

## 4.5.1 Defining the Model
As in [previous Linear Regression Implementation](../../ch03/05/note.md#351-defining-the-model), we construct our fully connected layer using the built-in layer. The built-in``` __call__``` method then invokes forward whenever we need to apply the network to some input.

Use a ```torch.nn.Flatten``` layer to convert the fourth-order tensor ```X``` to second order by keeping the dimensionality along the first axis unchanged.

```python
class SoftmaxRegression(d2l.Classifier):  #@save
    """The softmax regression model."""
    def __init__(self, num_outputs, lr):
        super().__init__()
        self.save_hyperparameters()
        self.net = nn.Sequential(nn.Flatten(),
                                 nn.LazyLinear(num_outputs))

    def forward(self, X):
        return self.net(X)
```

<br><br>

## 4.5.2 Softmax Revisited
### Concept) Overflow/Underflow Problem
- Desc.)
  - [Recall](../01/note.md) that our previous softmax function computes probabilities via $`\displaystyle\hat{y}_i = \frac{\exp(o_i)}{\sum_j \exp(o_j)}`$.
  - In the program, $\exp(o_j)$ may cause overflow/underflow issue.
    - If $\exp(o_j) \gt 10^{38}$, it may overflow.
    - If $\exp(o_j) \lt -10^{38}$, it may underflow.
- Sol.)
  - Use $\bar{o} \equiv \max_k{o_k}$ as follows.
    - $`\displaystyle\hat{y}_i = \frac{\exp(o_i)}{\sum_j \exp(o_j)}=\frac{\exp(o_i-\bar{o})\exp{\bar{o}}}{\sum_j \exp(o_j-\bar{o})\exp{\bar{o}}}=\frac{\exp(o_i-\bar{o})}{\sum_j \exp(o_j-\bar{o})}`$
  - Desc.)
    - Consider that $o_i-\bar{o} \le 0, \forall i$
    - Then, the denominator $\exp(o_i-\bar{o})$ is contained in the interval $[1,q]$ for the $q$-class classification problem.
      - Why?)
        - $o_j = x_1w_{j1}+x_2w_{j2}+\cdots+x_kw_{jk}+b_k$
          - where $x_i \in \lbrace 0,1 \rbrace$, $0 \le w_{ji} \le 1$, $b_i \approx 0$, $i=1,2,\cdots,k$
        - Thus, 
    - Also, the nominator $\sum_j \exp(o_j-\bar{o})$ never exceeds $1$.





<br>

* [Back to Dive into Deep Learning](../../main.md)