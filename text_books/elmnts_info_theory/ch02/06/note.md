* [Back to Elements of Information Theory](../../main.md)

# 2.6 Jensen's Inequality and Its Consequences

### Concept) Convexity
- Def.)
  - For
    - $`f(x)`$ : a function
    - $`(a,b)`$ : an interval 
  - $`f(x)`$ is convex over $`(a,b)`$
    - if $`f(\lambda x_1 + (1-\lambda)x_2) \le \lambda f(x_1) + (1-\lambda)f(x_2)`$
      - where
        - $`\forall x_1, x_2 \in (a,b) \textrm`$
        - $` 0 \le \lambda \le 1`$
  - Moreover, $`f`$ is **strictly convex** if the equality holds only if $`\lambda = 0 \vee \lambda = 1`$.
- e.g.)
  - $`x^2, |x|, e^x, x\log{x} (x\ge 0)`$
  - Linear functions are both convex and [concave](#concept-concavity).

<br>

### Concept) Concavity
- Def.)
  - A function $`f`$ is concave if $`-f`$ is [convex](#concept-convexity).
- e.g.)
  - $`\log{x} \; (x\ge 0), \sqrt{x} \; (x\ge 0)`$
  - Linear functions are both [convex](#concept-convexity) and concave.

<br>

### Theorem 2.6.1)
If the function $`f`$ has a second derivative that is non-negative (positive) over an interval, the function is [convex (strictly convex)](#concept-convexity) over that interval.
- pf.)
  - Consider the Taylor series approximation around $`x_0`$ as below.
    - $`f(x) \approx f(x_0) + f'(x_0)(x-x_0) + \frac{f''(x_0)}{2}(x-x_0)^2`$
  - Assuming $`f''(x) \ge 0, \forall x`$,
    - $`f(x) \approx f(x_0) + f'(x_0)(x-x_0) + \frac{f''(x_0)}{2}(x-x_0)^2 \ge f(x_0) + f'(x_0)(x-x_0)`$
  - Put $`x_0 = \lambda x_1 + (1-\lambda)x_2`$
    - Then, $`f(x) \ge f(x_0) + f'(x_0)(x-\lambda x_1 - (1-\lambda)x_2)`$
  - When $`x=x_1`$,
    - $`f(x_1) \ge f(x_0) + f'(x_0)((1-\lambda)(x_1-x_2)) \cdots (1)`$
  - When $`x=x_2`$,
    - $`f(x_2) \ge f(x_0) + f'(x_0)(\lambda(x_2-x_1)) \cdots (2)`$
  - By multiplying $`\lambda`$ and $`(1-\lambda)`$ on (1) and (2) respectively and adding them we get   
    $`\begin{aligned}
        \lambda f(x_1) + (1-\lambda)f(x_2) &\ge \lambda f(x_0) + f'(x_0)(\lambda(1-\lambda)(x_1-x_2))  + (1-\lambda)f(x_0) + f'(x_0)(\lambda(1-\lambda)(x_2-x_1)) \\
        &= f(x_0) \\
        &= f(\lambda x_1 + (1-\lambda)x_2)
    \end{aligned}`$

<br>

### Theorem 2.6.2) Jensen's Inequality
1. If $`f`$ is a convex function and $`X`$ is a random variable, $`Ef(X) \ge f(EX)`$.
   - pf.)
     - Consider the discrete distribution case
       - where 
         - $`p_i`$ denotes the probability of $`x=x_i`$.
         - $`i=1,2,\cdots, k`$
     - Put $`\displaystyle p_i' = \frac{p_i}{1-p_k}`$.
     - Then   
       $`\begin{aligned}
        Ef(X) = \sum_{i=1}^k p_i f(x_i) & = p_k f(x_k) + (1-p_k)\sum_{i=1}^{k-1}p_i'f(x_i) \\
        &\ge p_k f(x_k) + (1-p_k)\left(\sum_{i=1}^{k-1}p_i'x_i\right) & \because f\textrm{ is convex.} \\
        &\ge f\left( p_k x_k + (1-p_k)\sum_{i=1}^{k-1}p_i'x_i \right) & \because f\textrm{ is convex.} \\
        &= f\left( \sum_{i=1}^{k} p_i x_i \right) = f(EX)
       \end{aligned}`$
2. Moreover, if $`f`$ is strictly convex, $`X = EX`$ with probability $`1`$.
   - i.e.) $`X`$ is a constant.


<br>

* [Back to Elements of Information Theory](../../main.md)