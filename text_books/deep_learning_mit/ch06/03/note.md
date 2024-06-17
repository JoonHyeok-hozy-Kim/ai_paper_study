* [Back to Deep Learning MIT](../../main.md)

# 6.3 Hidden Units
### Prop.) Differentiability of Hidden Units
- Desc.)
  - Some hidden units are not differentiable.
    - Why?)
      - Recall that the definition of the differentiability is that the left derivative and the right derivative are identical.
      - Functions such as $`g(z) = \max(0, z)`$ at point $`z=0`$ does not satisfy this condition.
  - Though not differentiable, it can be justified in learning algorithms thanks to following reasons.
    - Software implementations of neural network training usually return one of the one-sided derivatives
      - rather than reporting that the derivative is undefined or raising an error. 
    - Due to the nature of digital computer, values are approximated.
      - e.g.) When a function is asked to evaluate $`g(0)`$, it is very unlikely that the underlying value truly was $`0`$. 
        - Instead, it was likely to be some small value $`\epsilon`$ that was rounded to $`0`$
  - Most hidden units are distinguished by the choice of the form of the activation function
    - Why?) In most cases, when a vector of inputs $`x`$ is accepted
      - first compute the affine transformation $`z = W^\top x + B`$
      - then apply the element-wise non-linear function.

<br>

## 6.3.1 Rectified Linear Units and Their Generalizations
### Concept) Rectified Linear Unit (ReLU)
- Def.)
  - Units using activation function of $`g(z) = \max(0,z)`$.
  - $`h = g(W^\top x + b)`$
- Props.)
  - Rectified linear units are easy to optimize because they are so similar to linear units.
    - This makes the **derivatives** through a rectified linear unit... 
      - **remain large** whenever the unit is active
      - consistent
    - The **second derivative** of the rectifying operation is $`0`$ almost everywhere, and the derivative of the rectifying operation is $`1`$ everywhere that the unit is active.
      - Thus, **the gradient direction** is far more useful for learning than it would be with activation functions that introduce second-order effects.
  - Drawback)
    - They cannot learn via gradient-based methods on examples for which their activation is zero.

<br>

### Concept) Generalizations for Rectified Linear Units
- Assumptions)
    - For a non-zero slope $`\alpha_i`$ when 
      - $`z_i \lt 0`$
      - $`h_i = g(z,\alpha)_i = \max(0, z_i) + \alpha_i \min(0,z_i)`$
- Models)
  - [Absolute Value Rectification](#model-absolute-value-rectification)
  - [Leaky ReLU](#model-leaky-relu)
  - [Maxout Unit](#model-maxout-unit)

#### Model) Absolute Value Rectification
- Desc.)
  - Fix $`\alpha_i = 1`$ to obtain $`g(z) = |z|`$.
  - Used to seek features that are invariant under a polarity reversal of the input illumination.
    - e.g.) Image recognition in *Jarrett et al., 2009*

#### Model) Leaky ReLU
- Def.)
  - Fix $`\alpha_i`$ to small values like $`0.01`$.
  - cf.) Parametric ReLU, PReLU treats $`a_i`$ as a learnable parameter.


#### Model) Maxout Unit
*Goodfellow et al., 2013*
- Desc.)
  - Divide the result of the [affine transformation](#prop-differentiability-of-hidden-units) $`z`$ into groups of $`k`$ values.
  - Each $`i`$-th maxout unit outputs the maximum element of one of these groups
    - $`\displaystyle g(z)_i = \max_{j\in\mathbb{G}^{(i)}} z_j`$
      - where $`\mathbb{G}^{(i)}`$ is the set of indices into the inputs for group $`i = \underbrace{\{(i-1)k+1, (i-1)k+2, \cdots, ik\}}_{k \textrm{ values}}`$
- Prop.)
  - This provides a way of learning a **piecewise linear function** that responds to multiple  directions in the input $`x`$ space.
  - Maxout units can be seen as **learning the activation function itself** rather than just the relationship between units.
  - With large enough $`k`$, a maxout unit can learn to **approximate any convex function** with arbitrary fidelity.
  - Maxout units typically need more regularization than rectified linear units.
    - why?) Each maxout unit is now parametrized by $`k`$  weight vectors instead of just one.

<br><br>

## 6.3.2 Logistic Sigmoid and Hyperbolic Tangent
### Concept) Logistic Sigmoid
- Def.)
  - $`\displaystyle g(z) = \sigma(z) \equiv \frac{1}{1+\exp{(-x)}}`$
- Props.)
  - Refer to [3.10 for its principle properties](../../ch03/10/note.md#concept-logistic-sigmoid).
  - Not used as hidden units in feedforward networks these days.
    - Why?)
      - Sigmoidal units are strongly sensitive to their input only when $`z`$ is near zero.
        - i.e.) They saturate across most of their domain.
      - The widespread saturation of sigmoidal units can make gradient-based learning very difficult.
  - Still, can be used as output units in special cases where appropriate cost functions can undo the saturation of the sigmoid in the output layer.

### Concept) Hyperbolic Tangent
- Def.)
  - For logistic sigmoid activation function $`\sigma`$, the hyperbolic tangent activation function is given by
    - $`g(z) = \tanh(z) \equiv 2\sigma(2z)-1`$
- Props.)
  - When a [sigmoidal activation](#concept-logistic-sigmoid) function must be used, the hyperbolic tangent activation function typically performs better than the logistic sigmoid.
  - Training $`\tanh`$ activated neural network $`\hat{y} = w^\top\tanh(U^\top\tanh(V^\top x))`$ is similar to training a linear activated unit $`\hat{y} = w^\top U^\top V^\top x`$.
    - Why?) $`\tanh`$ is similar to identity function near $`0`$
      - i.e.) $`\tanh(0) = 0`$

<br><br>

## 6.3.3 Other Hidden Units
- Desc.)
  - During research and development of new techniques, it is common to test many different activation functions and find that several variations on standard practice perform comparably.

<br>

### Concept) Linear Hidden Unit
- Desc.)
  - Linear hidden units effectively reduces the number of parameters in a network.
- e.g.)
  - Consider 
    - a neural network layer with $`n`$ inputs and $`p`$ outputs.
      - $`h = g(W^\top x + b), \textrm{ where } x\in\mathbb{R}^n, \; h\in\mathbb{R}^p`$
    - another network with two layers using weight matrices $`U, V`$.
      - $`h = g(V^\top U^\top x + b)`$
  - Assuming $`U`$ produces $`q`$ outputs, the second network will have $`(n+p)q`$ parameters.
  - The first network has only $`np`$ parameters.
  - Thus, if $`q`$ is small, the first model can save a lot.

<br>

### Concept) Softmax Unit
- Desc.)
  - [Softmax](../../ch04/01/note.md#softmax-function) units represent a probability distribution over a discrete variable with $`k`$ possible values.

<br>

### Concept) Radial Basis Function (RBF) Unit
- Def.)
  - $`\displaystyle h_i = \exp\left( -\frac{1}{\sigma_i^2} ||W_{:i}-x||^2 \right)`$
- Prop.)
  - Recall the [RBF](../../ch05/07/note.md#eg-gaussian-kernel-radial-basis-function-rbf).
  - This function becomes more active as $`x`$ approaches a template $`W_{:i}`$.
  - Difficult to optimize.
    - Why?) It saturates to $`0`$ for most $`x`$

<br>

### Concept) Softplus Unit
- Def.)
  - $`g(a) = \varsigma(a) = \log(1+e^a)`$
- Props.)
  - Recall the [softplus](../../ch03/10/note.md#concept-softplus) function.
  - This is a smooth version of the [rectifier](#concept-rectified-linear-unit-relu).
  - Its usage is generally discouraged.

<br>

### Concept) Hard tanh
- Def.)
  - $`g(a) = \max(-1, \min(1,a))`$
- Props.)
  - This is shaped similarly to the $`\tanh`$ and the rectifier.
  - But unlike ReLU, it is bounded.



<br>

* [Back to Deep Learning MIT](../../main.md)