* [Back to Dive into Deep Learning](../../main.md)

# 2.4 Calculus

#### Import Packages
```python
%matplotlib inline
import numpy as np
from matplotlib_inline import backend_inline
from d2l import torch as d2l
```

<br>

## 2.4.1 Derivatives and Differentiation
- e.g.) $f(x) = 3x^2 -4x$
  ```python
  def f(x):
      return 3*x**2 - 4*x
  ```
  - Implementing $f'(x) = \lim_{h \rightarrow 0}\frac{f(x+h)-f(x)}{h}$
    ```python
    for h in 10.0**np.arange(-1, -6, -1):
        print(f'h={h:.5f}, numerical limit={(f(1+h)-f(1))/h:.5f}')
    ```













<br>

* [Back to Dive into Deep Learning](../../main.md)