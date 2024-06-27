* [Back to Deep Learning MIT](../../main.md)

# 7.3 Regularization and Under-Constrained Problems
## Props.) Regularization Guarantees Closed Form Solution
### Case 1) Linear Models
- e.g.)
  - Linear Regression
  - PCA
- Problem)
  - The learning process depends on inverting the matrix $`X^\top X`$
    - where $`X`$ is the design matrix.
  - However, $`X^\top X`$ can be singular (i.e. not invertible) in following situations.
    1. The data generating distribution truly has no variance in some direction.
    2. No variance is observed in some direction because there are fewer examples (rows of $`X`$) than input features (columns of $`X`$).
  - In this case, many forms of regularization correspond to inverting $`(X^\top X + \alpha I)`$ instead.
    - Refer to [Analysis 7.1.1.4](../01/note.md#analysis-7114-l2-regularization-in-linear-regression).

<br>

### Case 2) Problems with no Closed Form Solution
- Sol.)
  - Most forms of regularization are able to **guarantee the convergence** of iterative methods applied to underdetermined problems.
- e.g.)
  - [Logistics Regression](../../ch05/07/note.md#571-probabilistic-supervised-learning) applied to a problem where the classes are linearly separable.
    - e.g.)
      - If a weight vector $`w`$ is able to achieve perfect classification, then $`2w`$ will also achieve perfect classification and higher likelihood.
      - An iterative optimization procedure like [stochastic gradient descent](../../ch05/09/note.md#59-stochastic-gradient-descent) will continually increase the magnitude of $`w`$ and, in theory, will never halt.
      - In practice, a numerical implementation of gradient descent will eventually reach sufficiently large weights to cause numerical overflow.
        - Then, its behavior will depend on how the programmer has decided to handle values that are not real numbers.
      - [Weight decay](../01/note.md#711-l2-parameter-regularization-weight-decay) will cause gradient descent to quit increasing the magnitude of the weights when the slope of the likelihood is equal to the weight decay coefficient.
  - [Moore-Penrose pseudoinverse](../../ch02/09/note.md#concept-the-moore-penrose-pseudoinverse)
    - Recall that we solved underdetermined linear equations using the [Moore-Penrose pseudoinverse](../../ch02/09/note.md#concept-the-moore-penrose-pseudoinverse)
      - where $`\displaystyle X^+ = \lim_{\alpha\rightarrow0} \left( X^\top X + \alpha I \right)^{-1} X^\top`$
    - Here, $`(X^\top X + \alpha I)`$ is the term tha we covered in the [L2 Weight Decay](../01/note.md#analysis-7114-l2-regularization-in-linear-regression).






<br>

* [Back to Deep Learning MIT](../../main.md)