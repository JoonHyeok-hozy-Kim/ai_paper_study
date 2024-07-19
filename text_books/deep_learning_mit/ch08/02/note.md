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

<br>

## 8.2.2 Local Minima
### Concept) Model Identifiability
- Def.)
  - A model is said to be **identifiable** if a sufficiently large training set can rule out all but one setting of the model’s parameters.
- Prop.)
  - Models with [latent variables](../../ch03/09/note.md#concept-latent-variable) are often **not identifiable** because we can obtain equivalent models by exchanging latent variables with each other.
    - e.g.) Weight Space Symmetry
      - Consider a neural network with $m$ layers each with $`n`$ units.
      - Then each layer can be rearranged in $`n!`$ ways.
      - Thus, there are $`n! \times m`$ ways of rearranging hidden units.
        - i.e.) There are too many equivalent models!
      - This kind of non-identifiability is known as **weight space symmetry**.
    - e.g.) [ReLU](../../ch06/03/note.md#concept-rectified-linear-unit-relu) / [Maxout](../../ch06/03/note.md#model-maxout-unit) Network Case
      - Consider the case that the model does not include the [weight decay](../../ch07/01/note.md#711-l2-parameter-regularization-weight-decay) terms.
      - Then we can scale all of the incoming weights and biases of a unit by $`\alpha`$ if we scale all of its outgoing weights by $`\frac{1}{\alpha}`$.
      - Thus, every local minium lies on an $`m\times n`$ - dimensional hyperbola of equivalent local minima.

### Concept) Convex vs Non-Convex
- Desc.)
  - Convex optimization problem)
    - Any local minimum is guaranteed to be a global minium.
    - Some convex functions have a flat region at the bottom, but any point within that region is an acceptable solution.
  - Non-Convex optimization problem)
    - It is possible that there are multiple local minima.
      - why?)
        - Non-[identifiable](#concept-model-identifiability) models tend to have multiple local minima.
        - Moreover, there can be an extremely large or even uncountably infinite amount of local minima in a neural network cost function.
    - Local minima can be problematic if they have high cost in comparison to the global minimum.
      - If local minima with high cost are common, this could pose a serious problem for gradient-based optimization algorithms.
    - Recent studies say...
      - For sufficiently large neural networks, most local minima have a low cost function value
      - It is more important to find a point in parameter space that has low but not minimal cost than to find a true global minimum.
- In practice)
  - Conduct a test that can rule out local minima.
    - How?) Negative Test for Local Minima 
      - While optimizing the target problem, plot the norm of the gradient over time.
      - If the norm of the gradient does not shrink to insignificant size, the problem is neither a local minima nor any kind of critical point.
      - Rule out such problems.

<br>

## 8.2.3 Plateaus, Saddle Points and Other Flat Regions


<br>

## 8.2.4 Cliffs and Exploding Gradients


<br>

## 8.2.5 Long-Term Dependencies


<br>

## 8.2.6 Inexact Gradients


<br>

## 8.2.7 Poor Correspondence between Local and Global Structure


<br>

## 8.2.8 Theoretical Limits of Optimization


<br>
















<br>

* [Back to Deep Learning MIT](../../main.md)