* [Back to Deep Learning MIT](../../main.md)

# 8.2 Challenges in Neural Network Optimization
- Desc.)
  - Recall that **Machine Learning** technically ensures the **convexity** of the optimization problem by carefully choosing the objective function and constraints.
  - However, when training **Neural Networks**, we must confront the general **non-convex** case.
  - Followings are the problems related to this non-convexity.
    - [Ill-Conditioning](#821-ill-conditioning)
    - [Local Minima](#822-local-minima)
    - [Plateaus, Saddle Points and Other Flat Regions](#823-plateaus-saddle-points-and-other-flat-regions)
    - [Cliffs and Exploding Gradients](#824-cliffs-and-exploding-gradients)
    - [Long-Term Dependencies](#825-long-term-dependencies)
    - [Inexact Gradients](#826-inexact-gradients)
    - [Poor Correspondence between Local and Global Structure](#827-poor-correspondence-between-local-and-global-structure)
    - [Theoretical Limits of Optimization](#828-theoretical-limits-of-optimization)

<br>


## 8.2.1 Ill-Conditioning
### Concept) Ill-Conditioning of the Hessian Matrix
- Desc.)
  - Ill-conditioning can manifest by causing SGD to get “stuck” in the sense that even very small steps increase the cost function.
- e.g.)
  - Recall [the second-order Taylor approximation](../../ch04/03/note.md#concept-directional-second-derivative) predicting that a gradient descent step of $`-\epsilon g`$ would add $`\displaystyle\frac{1}{2}\epsilon^2 g^\top Hg - \epsilon g^\top g`$ to the cost.
  - Suppose $`\displaystyle\frac{1}{2}\epsilon^2 g^\top Hg \gt \epsilon g^\top g`$.
  - Then each optimization and updating process increases the cost, not minimizing it.
  - Thus, the learning becomes very slow despite the presence of the very strong gradient $`(g^\top g)`$.
    - Why?)
      - The learning rate must be shrunk to compensate for even stronger curvature.
- Test)
  - Monitor $`g^\top g`$ and $`g^\top H g`$.
  - If the $`g^\top g`$ does not shrink significantly throughout learning, but the $`g^\top H g`$ term grows by more than an order of magnitude, it may be the problem of the ill-conditioning.

## 8.2.2 Local Minima
## 8.2.3 Plateaus, Saddle Points and Other Flat Regions
## 8.2.4 Cliffs and Exploding Gradients
## 8.2.5 Long-Term Dependencies
## 8.2.6 Inexact Gradients
## 8.2.7 Poor Correspondence between Local and Global Structure
## 8.2.8 Theoretical Limits of Optimization















<br>

* [Back to Deep Learning MIT](../../main.md)