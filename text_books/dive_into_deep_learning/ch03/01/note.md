* [Back to Dive into Deep Learning](../../main.md)

# 3.1 Linear Regression
Predicting numerical values.

#### Terms)
- The dataset is called a training dataset.
- Each row (containing the data corresponding to one sale) is called an example (or data point, instance, sample).
- The thing we are trying to predict (price) is called a label (or target). 
- The variables (age and area) upon which the predictions are based are called features (or covariates).

<br>

#### Importing Packages
```python
import math
import time
import numpy as np
import torch
from d2l import torch as d2l
```

<br>

### 3.1.1.1 Model
- Assumptions)
  - $d$ features and $n$ examples
  - Prediction $\hat{y}=w_1x_1 + \cdots + w_dx_d + b = \mathbf{w}^{\top}\mathbf{x}+b$
  - Putting 






<br>

* [Back to Dive into Deep Learning](../../main.md)