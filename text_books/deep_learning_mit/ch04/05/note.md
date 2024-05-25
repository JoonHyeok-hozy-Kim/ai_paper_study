* [Back to Deep Learning MIT](../../main.md)

# 4.5 Example: Linear Least Squares
### Loss Function)
- $`f(x) = \frac{1}{2} ||Ax-b||^2_2`$

<br>

### Sol.) Gradient-Based Optimization
1. Obtain the following gradient.
   - $`\nabla_x f(x) = A^\top (Ax-b) = A^\top Ax - A^\top b`$
2. Use the following gradient downhill algorithm.   
   - Algorithm 4.1)
     1. Set the step size $`\epsilon`$ and tolerance $`\delta`$ to small positive numbers.
     2. `while` $`(||A^\top Ax - A^\top b||_2 \gt \delta)`$ `do`
        - $`x \leftarrow x - \epsilon(A^\top Ax - A^\top b)`$
   - Since the [target function](#loss-function) is quadratic, [Newton's method](../03/note.md#concept-the-newtons-method) will get to the global minimum in a single step.

<br>

### Constrained Optimization Problem
- Suppose we add additional constraint as follows.
  - $`x^\top x \le 1`$
- Then we should solve this problem using the [KKT](../04/note.md#concept-karush-kuhn-tucker-kkt).
  - Lagrangian) 
    - $`L(x,\lambda) = f(x) + \lambda \left( x^\top x - 1 \right)`$
  - Optimization Problem)
    - $`\displaystyle \min_x \max_{\lambda, \lambda \ge 0} L(x, \lambda) = \frac{1}{2} ||Ax-b||^2_2 + \lambda \left( x^\top x - 1 \right)`$
  - Sol.)
    - $`\displaystyle \frac{\partial L}{\partial x} = 0 \Leftrightarrow A^\top Ax - A^\top b + 2\lambda x = 0`$
      - Thus, $`x = (A^\top A-2\lambda I)^{-1}A^\top b`$
    - $`\displaystyle \frac{\partial L}{\partial \lambda} = x^\top x - 1`$
      - When the norm of $`x`$ exceeds $`1`$, $`\displaystyle \frac{\partial L}{\partial \lambda} \gt 0`$.
      - Thus, to follow the derivative uphill and increase the Lagrangian w.r.t. $`\lambda`$, we should increase $`\lambda`$.
      - Then, because the coefficient on the $`x^\top x \;(\lambda)`$ penalty has increased, solving the linear equation for $`x`$ will yield a solution with smaller norm. 




<br>

* [Back to Deep Learning MIT](../../main.md)