* [Back to Deep Learning MIT](../../main.md)

# 8.6 Approximate Second-Order Methods
Application of second-order methods to the training of deep networks.

### Assumptions)
#### Objective Function)
- The empirical risk   
    $`\begin{aligned}
        J(\theta) &= \mathbb{E}_{\mathbf{x, y}\sim\hat{p}_{\textrm{data}}(x,y)} \left[ L(f(x;\theta), y) \right] \\
        &= \frac{1}{m}\sum_{i=1}^m L\left(f(x^{(i)};\theta), y^{(i)}\right)
    \end{aligned}`$

<br>

## 8.6.1 Newton's Method
- Desc.)
  - The most widely used second-order method.
- Algorithm)
  - Inputs)
    - $`\theta_0`$ : the initial parameters
    - $`m`$ examples from the training set $`\{x^{(1)}, \cdots, x^{(m)}\}`$ with corresponding targets $`y^{(i)}`$.
  - Procedure)\
    - `while` stopping criterion not met `do`
      - Compute gradient : $`\displaystyle g \leftarrow \frac{1}{m}\nabla_\theta \sum_i L\left(f(x^{(i)};\theta), y^{(i)}\right)`$
      - Compute Hessian : $`\displaystyle H \leftarrow \frac{1}{m}\nabla_\theta^2 \sum_i L\left(f(x^{(i)};\theta), y^{(i)}\right)`$
      - Compute Hessian inverse : $`H^{-1}`$
      - Compute update : $`\displaystyle \Delta\theta = -H^{-1}g`$
      - Apply update : $`\theta \leftarrow \theta + \Delta\theta`$
    - `end while`
- Ideation)
  - Consider the second-order Taylor series expansion to approximate $`J(\theta)`$ near som point $`\theta_0`$.
    - $`\displaystyle J(\theta) \approx J(\theta_0) + (\theta-\theta_0)^\top \nabla_\theta J(\theta_0) + \frac{1}{2} (\theta-\theta_0)^\top H(\theta-\theta_0)`$
      - where $`H`$ is the Hessian of $`J`$ w.r.t. $`\theta = \theta_0`$.
  - Solving for the critical point of this function, we obtain the Newton parameter update rule:
    - $`\theta^\ast = \theta_0 - H^{-1}\nabla_\theta J(\theta_0)`$
  - Thus, for a locally quadratic function (with [positive definite](../../ch02/07/note.md#concept-positivenegative-definite) $`H`$), by rescaling the gradient by $`H^{-1}`$, the Newton's method jumps directly to the minimum.
  - Two Cases of Results)
    - If the objective function is **convex but not quadratic** (there are higher-order terms), this update can be iterated, yielding the training algorithm associated with Newton’s method.
    - For surfaces that are **not quadratic**, as long as the Hessian remains [positive definite](../../ch02/07/note.md#concept-positivenegative-definite), Newton’s method can be applied iteratively.
      - Why the [positive definite](../../ch02/07/note.md#concept-positivenegative-definite) Hessian needed?
        - In deep learning, the surface of the objective function is typically **non-convex** with many features, such as saddle points.
        - In [section 8.2.3](../02/note.md#823-plateaus-saddle-points-and-other-flat-regions), we saw that Newton's methods is not capable of escaping saddle points.
      - Sol.) Regularize the Hessian
        - How?)
          - Add a constant $`\alpha`$ along the diagonal of the Hessian.
            - $`\theta^\ast = \theta_0 - \left[H(f(\theta_0)) + \alpha I \right]^{-1}\nabla_\theta J(\theta_0)`$
              - An approximations to Newton’s method, such as the Levenberg–Marquardt algorithm
              - It works fairly well as long as the negative eigenvalues of the Hessian are still relatively close to zero.







<br>

* [Back to Deep Learning MIT](../../main.md)