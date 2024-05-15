* [Back to Deep Learning MIT](../../main.md)

# 3.8 Expectation, Variance, and Covariance

### Concept) Expectation (Expected Value)
- Def.)
  - The **Expectation (Expected Value)** of some function $`f(x)`$ w.r.t. a probability distribution $`P(x)`$ is the average or mean value that $`f`$ takes on when $`x`$ is drawn from $`P`$.
- Notation)
  - Discrete Case
    - $`\displaystyle \mathbb{E}_{\mathbf{x}\sim P} \left[ f(x) \right] = \sum_x P(x)f(x)`$
  - Continuous Case
    - $`\displaystyle \mathbb{E}_{\mathbf{x}\sim P} \left[ f(x) \right] = \int p(x)f(x) dx`$
  - Simply
    - $`\mathbb{E}\left[ f(x) \right]`$
- Prop.)
  - Linearity
    - For $`\alpha, \beta \in \mathbb{R}`$
      - $`\mathbb{E}\left[\alpha f(x) + \beta g(x) \right] = \alpha\mathbb{E}\left[ f(x)\right] + \beta \mathbb{E}\left[g(x)\right]`$
        - i.e.) $`\alpha, \beta`$ are not dependent on $`x`$.

<br>

### Concept) Variance
- Def.)
  - The variance gives a measure of how much the values of a function of a random variable $`\mathbf{x}`$ vary as we sample different values of $`x`$ from its probability distribution.
- Notation)
  - $`\displaystyle \textrm{Var}\left(f(x)\right) = \mathbb{E} \left[ \left( f(x) - \mathbb{E}\left[f(x)\right]\right)^2 \right]`$

<br>

### Concept) Covariance
- Def.)
  - The covariance gives some sense of how much two values are linearly related to each other, as well as the scale of these variables:
- Notation)
  - $`\displaystyle\textrm{Cov}\left(f(x),g(y)\right) = \mathbb{E}\left[ \left( f(x) - \mathbb{E}\left[ f(x) \right] \right) \left( g(y) - \mathbb{E}\left[ g(y) \right] \right) \right]`$
- Props.)
  - Absolute value of Covariance : $`|\textrm{Cov}\left(f(x),g(y)\right)|`$
    - High **absolute** values of the covariance mean that the values change very much and are both far from their respective means at the same time.
  - Sign of the Covariance
    - Positive)
      - Both variables tend to take on relatively high values simultaneously.
    - Negative)
      - One variable tends to take on a relatively high value at the times that the other takes on a relatively low value and vice versa.
  - Covariance and dependence are **related**, but are **distinct** concepts.
    - For two variables to have **zero covariance**, there must be **no linear dependence** between them.
    - **Independence** is a stronger requirement than zero covariance, because independence also **excludes nonlinear relationships**.
      - i.e.) It is possible for two variables to be **dependent** but have **zero covariance**.
        - e.g.)
          - Consider $`x\sim U(-1,1) \textrm{ and } s=\begin{cases}
            1 & \textrm{with } p = \frac{1}{2} \\
            -1 & \textrm{with } p = \frac{1}{2} \\
          \end{cases}`$
          - Put $`y = sx = \begin{cases}
                x & \textrm{with } p = \frac{1}{2} \\
                -x & \textrm{with } p = \frac{1}{2} \\
                \end{cases}`$
          - Then $`\textrm{Cov}(x,y) = 0`$
          - However, $`x`$ determines the magnitude of $`y`$.
          - Hence, $`x,y`$ are dependent.

<br>

### Concept) Covariance Matrix
- Def.)
  - The covariance matrix of a random vector $`\mathbf{x} \in \mathbb{R}^n`$ is an $`\times n\times n`$ matrix, such that
    - $`\textrm{Cov}(\mathbf{x})_{i,j} = \textrm{Cov}(\mathbf{x}_i, \mathbf{x}_j)`$
- Prop.)
  - The diagonal elements of the covariance give the variance.
    - i.e.) $`\textrm{Cov}(\mathbf{x}_i, \mathbf{x}_j) = \textrm{Var}(\mathbf{x}_i)`$



<br>

* [Back to Deep Learning MIT](../../main.md)