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

<br>

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
  - $`\textrm{ReLU}(x) = \max(x, 0)`$
- Code Usage)
  ```python
  x = torch.arange(-8.0, 8.0, 0.1, requires_grad=True)
  y = torch.relu(x)
  d2l.plot(x.detach(), y.detach(), 'x', 'relu(x)', figsize=(5, 2.5))
  ```
- Prop.)
  - Not differentiable when $x=0$.
    - We may plot the derivative of ReLU as follows.
      ```python
      y.backward(torch.ones_like(x), retain_graph=True)
      d2l.plot(x.detach(), x.grad, 'x', 'grad of relu', figsize=(5, 2.5))
      ```
      - Advantage)
        - Its derivatives are particularly well behaved: either they vanish $(x\lt 0)$ or they just let the argument through $(x\gt 0)$.
        - This makes optimization better behaved and it mitigated the well-documented problem of vanishing gradients that plagued previous versions of neural networks (more on this later).
- cf.) Parametrized ReLU (pReLU) function
  - $`\textrm{pReLU}(x) = \max(0, x) + \alpha \min(0, x)`$
    - This variation adds a linear term to ReLU, so some information still gets through, even when the argument is negative.


<br><br>


### 5.1.2.2 Sigmoid Function
- Def.)
  - $`\textrm{sigmoid}(x) = \frac{1}{1 + \exp(-x)}`$
- Code Usage)
  ```python
  x = torch.arange(-8.0, 8.0, 0.1, requires_grad=True)
  y = torch.sigmoid(x)
  d2l.plot(x.detach(), y.detach(), 'x', 'sigmoid(x)', figsize=(5, 2.5))
  ```
- Prop.)
  - It is a smooth, **differentiable** approximation to a thresholding unit.
    - Appropriate for the Gradient-Based Learning.
  - Useful when we want to interpret the outputs as **probabilities** for binary classification problems.
    - $\textrm{sigmoid}(x) \in [0,1]$
    - You can think of the sigmoid as a special case of the [softmax](../../ch04/01/note.md#4112-softmax-model).
  - However, the sigmoid has largely been replaced by the simpler and more easily trainable ReLU for most use in hidden layers. 
    - why?)
      - Its gradient vanishes for large positive and negative arguments.
  - The derivative of the sigmoid function is given by the following equation.
    - $`\frac{d}{dx} \textrm{sigmoid}(x) = \frac{\exp(-x)}{(1 + \exp(-x))^2} = \textrm{sigmoid}(x)\left(1-\textrm{sigmoid}(x)\right)`$
      - The derivative of the sigmoid function is plotted below. 
        ```python
        x.grad.data.zero_() # Clear out previous gradients 
        y.backward(torch.ones_like(x),retain_graph=True)
        d2l.plot(x.detach(), x.grad, 'x', 'grad of sigmoid', figsize=(5, 2.5))
        ```
      - Note that when the input is 0, the derivative of the sigmoid function reaches a maximum of 0.25. 
      - As the input diverges from 0 in either direction, the derivative approaches 0.


<br><br>


### 5.1.2.3 Hyperbolic Tangent(tanh) Function
- Def.)
  - $`\textrm{tanh}(x) = \frac{1 - \exp(-2x)}{1 + \exp(-2x)}`$
- Code Usage)
  ```python
  x = torch.arange(-8.0, 8.0, 0.1, requires_grad=True)
  y = torch.tanh(x)
  d2l.plot(x.detach(), y.detach(), 'x', 'tanh(x)', figsize=(5, 2.5))
  ```
- Prop.)
  - $\textrm{tanh}(x) \in [-1,1]$
  - The derivative of the tanh function
    - $\frac{d}{dx} \textrm{tanh}(x) = 1 - \textrm{tanh}^2(x)$
      - As the input nears 0, the derivative of the tanh function approaches a maximum of 1. 
      - And as we saw with the sigmoid function, as input moves away from 0 in either direction, the derivative of the tanh function approaches 0.
      - Plotting
        ```python
        x.grad.data.zero_() # Clear out previous gradients
        y.backward(torch.ones_like(x),retain_graph=True)
        d2l.plot(x.detach(), x.grad, 'x', 'grad of tanh', figsize=(5, 2.5))
        ```


<br><br>




<br>

* [Back to Dive into Deep Learning](../../main.md)