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
### Concept) Rectified Linear Unit
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

### Concept) Generalizations for Rectified Linear Units
- Assumptions)
    - For a non-zero slope $`\alpha_i`$ when 
      - $`z_i \lt 0`$
      - $`h_i = g(z,\alpha)_i = \max(0, z_i) + \alpha_i \min(0,z_i)`$

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









<br>

* [Back to Deep Learning MIT](../../main.md)