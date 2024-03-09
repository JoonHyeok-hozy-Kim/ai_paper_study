* [Back to Dive into Deep Learning](../../main.md)

# 5.1 Multilayer Perceptrons

#### Import Packages
```python
import torch
from d2l import torch as d21
```

<br>

#### Ideation)
- Recall that our previous model utilized a simple [affine transformation](../../ch03/01/note.md#concept-affine-transformation-of-input-features).
  - i.e.) Preserving the linearity of the input features.
- However, linearity (in affine transformations) is a **strong** assumption.
  - Why?)
    - There are [limitations of linear models](#5111-limitations-of-linear-models).
      - e.g.) Linearity implies the weaker assumption of monotonicity.
        - Linear model preserves the monotonicity of the input features.
        - This simplicity will lower the accuracy of the prediction of the model.
- We can overcome the limitations of linear models by...
  1. Incorporating one or more [hidden layers](#511-hidden-layers).
  2. Using the [activation functions](#512-activation-functions)

<br><Br>

## 5.1.1 Hidden Layers
### Concept) Multilayer Perceptron (MLP)
- Desc.)
   - Stacking many fully connected layers on top of one another.   
     - e.g.)   
       ![](images/001.png)
       - Four inputs, three outputs, and its hidden layer contains five hidden units
       - The number of layers in this MLP is two.
         - why?)
           - The input layer does not involve any calculations, producing outputs with this network requires implementing the computations for both the hidden and output layers.
- Notation) One-Hidden-Layer MLP
  - Suppose
    - $`\mathbf{X} \in \mathbb{R}^{n \times d}`$ : a minibatch of $`n`$ examples
      - where each example has $`d`$ inputs (features)
    - $`\mathbf{H} \in \mathbb{R}^{n \times h}`$ : the outputs of the hidden layer, which are *hidden representations*.
    - $`\mathbf{O} \in \mathbb{R}^{n \times q}`$ : the outputs of the One-Hidden-Layer MLP
  - Then   
    $`\begin{aligned}
        \mathbf{H} & = \mathbf{X} \mathbf{W}^{(1)} + \mathbf{b}^{(1)} \\
        \mathbf{O} & = \mathbf{H}\mathbf{W}^{(2)} + \mathbf{b}^{(2)}
    \end{aligned}, 
    \;\; \exists \left\{ \begin{array}{ll} \mathbf{W}^{(1)} \in \mathbb{R}^{d \times  h} & \textrm{ : the hidden-layer weights} \\ \mathbf{b}^{(1)} \in \mathbb{R}^{1 \times h} &  \textrm{ : the hidden-layer biases} \\ \mathbf{W}^{(2)} \in \mathbb{R}^{h \times q} & \textrm { : the output-layer weights} \\ \mathbf{b}^{(2)} \in \mathbb{R}^{1 \times q} & \textrm{ :  the output-layer biases} \end{array} \right.`$
- Prop.)
  - Applying solely the MLP cannot alleviate the linearity problem.
    - why?)
      - Recall that $`\mathbf{O} = \mathbf{H}\mathbf{W}^{(2)} + \mathbf{b}^{(2)}`$
      - Since, $`\mathbf{H} = \mathbf{X} \mathbf{W}^{(1)} + \mathbf{b}^{(1)}`$,   
        $`\begin{array}{ll}
          \mathbf{O} &= \left(\mathbf{X} \mathbf{W}^{(1)} + \mathbf{b}^{(1)}\right)\mathbf{W}^{(2)} + \mathbf{b}^{(2)} \\
          &= \mathbf{X} \mathbf{W}^{(1)}\mathbf{W}^{(2)} + \mathbf{b}^{(1)}\mathbf{W}^{(2)} + \mathbf{b}^{(2)} \\
          &= \mathbf{X} \mathbf{W} + \mathbf{b}
        \end{array}`$
    - Thus, we should add nonlinear [activation function](#512-activation-functions) $\sigma$ to each hidden unit as follows.   
       $`\begin{aligned}
        \mathbf{H} & = \sigma\left(\mathbf{X} \mathbf{W}^{(1)} + \mathbf{b}^{(1)}\right) \\
        \mathbf{O} & = \mathbf{H}\mathbf{W}^{(2)} + \mathbf{b}^{(2)}
       \end{aligned}`$

<br><Br>

## 5.1.2 Activation Functions
### 5.1.2.1 ReLu Function
- Def.)
  - $`\operatorname{ReLU}(x) = \max(x, 0)`$

<br><br>


### 5.1.2.2 Sigmoid Function


<br><br>


### 5.1.2.3 Hyperbolic Tangent(tanh) Function


<br><br>




<br>

* [Back to Dive into Deep Learning](../../main.md)