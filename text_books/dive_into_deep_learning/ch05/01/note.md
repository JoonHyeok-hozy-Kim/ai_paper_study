* [Back to Dive into Deep Learning](../../main.md)

# 5.1 Multilayer Perceptrons

#### Import Packages
```python
import torch
from d2l import torch as d21
```

## 5.1.1 Hidden Layers
- Recall that our previous model utilized a simple [affine transformation](../../ch03/01/note.md#concept-affine-transformation-of-input-features).
  - i.e.) Preserving the linearity of the input features.
- However, linearity (in affine transformations) is a **strong** assumption.
  - Why?)
    - There are [limitations of linear models](#5111-limitations-of-linear-models).

<br>

### 5.1.1.1 Limitations of Linear Models
- e.g.) Linearity implies the weaker assumption of monotonicity.
  - Linear model preserves the monotonicity of the input features.
  - This simplicity will lower the accuracy of the prediction of the model.












<br>

* [Back to Dive into Deep Learning](../../main.md)