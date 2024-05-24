* [Back to Deep Learning MIT](../../main.md)

# 4.4 Constrained Optimization

### Concept) Constrained Optimization
- Def.)
  - Finding maximal/minimal value of a function $`f(x)`$ in some set $`\mathbb{S} \subseteq \mathbb{R}`$, not the entire domain.
    - Points $`x\in\mathbb{S}`$ are called the **feasible points**.
- Sols.) 
  - Modifying gradient descent taking the constraint into account.
    1. Using a small constant step size $`\epsilon`$.
       - After making gradient steps, project the result back into $`\mathbb{S}`$.
    2. Using the [line search](../03/note.md#concept-gradient-descent-method-of-steepest-descent) method.
       - Search over step sizes $`\epsilon`$ that yield new feasible points $`x`$
       - Or project each point on the line back into $`\mathbb{S}`$.
       - Or project the gradient into the tangent space of the feasible region before taking the step or beginning the line search (*Rosen, 1960*)
  - Design a different, unconstrained optimization problem whose solution can be converted into a solution to the original constrained optimization problem.
    - e.g.)
      - Minimize $`f(x)`$ where $`x \in \mathbb{R}^2`$ is constrained to have exactly unit $`L^2`$ norm.
        - i.e.) $`||x||_2 = 1, \forall x`$
        - Then, use $`g(\theta) = f([\cos\theta, \sin\theta]^\top)`$ and return $`[\cos\theta, \sin\theta]`$ as the solution.
  - Use [KKT](#concept-karush-kuhn-tucker-kkt).

<br><br>

### Concept) Karush-Kuhn-Tucker (KKT)
#### Concept) Generalized Lagrangian
- Why needed?)
  - We can solve a [constrained optimization](#concept-constrained-optimization) problem using unconstrained optimization of the generalized lagrangian.
- Def.)
  - Settings
    - $`\mathbb{S} = \left\lbrace x|\forall i, g^{(i)}(x) = 0 \textrm{ and } \forall j, h^{(j)}(x) \le 0 \right\rbrace`$
      - where
        - $`g^{(i)} (i=1,2,\cdots,m)`$ : $`m`$ equality constraints
        - $`h^{(j)} (j=1,2,\cdots,n)`$ : $`n`$ inequality constraints
  - The generalized Lagrangian is defined as
    - $`\displaystyle L(x, \lambda, \alpha) = f(x) + \sum_i\lambda_i g^{(i)}(x) + \sum_j\alpha_j h^{(j)}(x)`$
      - where
        - $`\lambda \in \mathbb{R}^m`$ : the vector of equality constraints KKT multipliers
        - $`\alpha \in \mathbb{R}^n`$ : the vector of inequality constraints KKT multipliers
- Props.)
  - Suppose a feasible point $`x`$ exists and $`f(x)`$ is not permitted to have value $`\infty`$.
    - Then, $`\displaystyle \min_x \max_\lambda \max_{\alpha, \alpha\ge 0} L(x, \lambda, \alpha)`$ has the same optimal objective function value and set of optimal points $`x`$ as $`\displaystyle\min_{x\in\mathbb{S}} f(x)`$
      - Why this works?)
        - When the constraints are satisfied, 
          - then $`\displaystyle\max_\lambda \max_{\alpha, \alpha\ge 0} L(x, \lambda, \alpha) = f(x)`$
        - When the constraints are violated, 
          - then $`\displaystyle\max_\lambda \max_{\alpha, \alpha\ge 0} L(x, \lambda, \alpha) = \infty`$
      - This property guarantees the followings.
        - No infeasible point can be optimal.
        - The optimum within the feasible points is unchanged.
      - Thus, we can use the generalized Lagrangian for the [constrained optimization](#concept-constrained-optimization) problem.
  - Karush-Kuhn-Tucker Conditions)
    - The following conditions are necessary conditions, but not always sufficient conditions, for a point to be optimal.
      1. The gradient of the generalized Lagrangian is zero.
      2. All constraints on both $`x`$ and the KKT multipliers are satisfied.
      3. The inequality constraints exhibit “complementary slackness”: $`\alpha \odot h(x) = 0`$
- Application)
  - Constrained Maximization Problem)
    - $`\displaystyle \max_x \min_\lambda \min_{\alpha, \alpha\ge 0} f(x) - \sum_i\lambda_i g^{(i)}(x) - \sum_j\alpha_j h^{(j)}(x)`$








<br>

* [Back to Deep Learning MIT](../../main.md)