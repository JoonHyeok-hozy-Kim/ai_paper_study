* [Back to Dive into Deep Learning](../../main.md)

# 3.7 Weight Decay

### Concept) Limits of the Previously Covered Regularization Techniques
1. Collecting more training data
   - Costly, time consuming, or entirely out of our control, making it impossible in the short run.
2. Tweaking the degree of the fitted polynomial
   - Simply tossing aside features can be too blunt an instrument
   - The number of terms with degree $d$ blows up rapidly as $d$ grows larger.
     - e.g.)
       - Suppose $k$ variable are given.
       - Then the number of monomials of degree $d$ is $`{}_{k-1++d} C_{k-1}`$
         - where monomials are the natural extensions of polynomials to multivariate data.
           - e.g.) monomials of degree 3 : $`x_1x_2^2, \;x_4^3, \;x_5x_6x_7`$

<br><br>

## 3.7.1 Norms and Weight Decay
### Concept) Weight Decay
- Intuition)
  - We want to restrict the values that the parameters can take.
  - Before that we want to define the value of the parameters.
  - The value of the parameters may be defined as the distance of the from zero.
  - Among all functions $\mathcal{f}$, the function $\mathcal{f}=0$ is the simplest form.
  - Thus, we may measure the distance of its parameters from zero.
  - There is no single right answer. 
    - In fact, entire branches of mathematics, including parts of functional analysis and the theory of Banach spaces, are devoted to addressing such issues.
- Simpler Approach)
  - Consider the $`\ell_2`$ norm of the weight vector : $`\|\mathbf{w}\|^2`$
    - cf.) [Why l_2, not l_1?](#analysis-l1-vs-l2)
    - cf.) Should we include a penalty to the bias $b$?
      - i.e.) $b^2$ in $\mathbf{w}$?
      - The answer may vary across layers of a neural network.
      - Often, we do not regularize the bias term.
  - Add the weight vector's norm as a penalty term to the problem of minimizing the loss.
    - $`L(\mathbf{w}, b) + \frac{\lambda}{2} \|\mathbf{w}\|^2`$
      - where 
        - $`L(\mathbf{w}, b) = \frac{1}{n}\sum_{i=1}^n \frac{1}{2}\left(\mathbf{w}^\top \mathbf{x}^{(i)} + b - y^{(i)}\right)^2`$ is the loss function
        - $\lambda \gt 0$ is the regularization constant which restrict the size of $`\|\mathbf{w}\|^2`$.
  - Update $\mathbf{w}$ using minibatch stochastic gradient descent.
    - $`\mathbf{w} \leftarrow \left(1- \eta\lambda \right) \mathbf{w} - \frac{\eta}{|\mathcal{B}|} \sum_{i \in \mathcal{B}} \mathbf{x}^{(i)} \left(\mathbf{w}^\top \mathbf{x}^{(i)} + b - y^{(i)}\right)`$
      - where $\eta$ is the learning rate
    - cf.) The term *Weight Decay*
      - We shrink the size of $\mathbf{w}$ towards zero.
      - That is why the method is sometimes called “weight decay”: given the penalty term alone, our optimization algorithm decays the weight at each step of training.

<br>

#### Analysis) Why l_2, not l_1?
- $`\ell_2`$-regularized linear models constitute the classic ridge regression algorithm
  - It places an outsize penalty on large components of the weight vector.
  - This biases our learning algorithm towards models that distribute weight evenly across a larger number of features.
  - In practice, this might make them more **robust to measurement error in a single variable**.
- $`\ell_1`$-regularized linear regression is a similarly fundamental method in statistics, popularly known as lasso regression.
  - $`\ell_1`$ penalties lead to models that concentrate weights on a small set of features by clearing the other weights to zero.
  - This gives us an effective method for feature selection, which may be desirable for other reasons.
    - e.g.) If our model only relies on a few features, then we may not need to collect, store, or transmit data for the other (dropped) features.

<br>

## Implementation)

- Import modules.
  ```python
  import torch
  from torch import nn
  from d2l import torch as d2l
  ```



<br>

* [Back to Dive into Deep Learning](../../main.md)