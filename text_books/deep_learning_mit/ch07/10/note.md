* [Back to Deep Learning MIT](../../main.md)

# 7.10 Sparse Representations
### Concept) Sparsity
- Def.)
  - Many of the elements of the representation are zero (or close to zero).
- e.g.)
  - Model 1) Sparsely Parametrized Linear Regression Model   
    $`\begin{matrix}
      \begin{bmatrix} 18\\5\\15\\-9\\-3 \end{bmatrix}
     &= \begin{bmatrix} 
      4 &0 &0 &−2 &0 &0 \\
      0 &0 &−1& 0 & 3 & 0 \\
      0 &5 &0 & 0 & 0 & 0 \\
      1 &0 &0 &−1 & 0 &−4 \\
      1 &0 &0 & 0 &−5 & 0 \\
     \end{bmatrix} &
     \begin{bmatrix} 2 \\3 \\−2 \\−5 \\1 \\4 \end{bmatrix} \\
     y\in\mathbb{R}^m & A\in \mathbb{R}^{m\times n} & x\in\mathbb{R}^n
    \end{matrix}`$
  - Model 2) Linear Regression with a sparse representation $`h`$ of the data $`x`$   
    $`\begin{matrix}
      \begin{bmatrix} −14\\1\\19\\2\\23 \end{bmatrix}
     &= \begin{bmatrix} 
       3 &−1 & 2 &−5 & 4 & 1 \\
       4 & 2 &−3 &−1 & 1 & 3 \\ 
      −1 & 5 & 4 & 2 &−3 &−2 \\
       3 & 1 & 2 &−3 & 0 &−3 \\ 
      −5 & 4 &−2 & 2 &−5 &-1 \\
     \end{bmatrix} &
     \begin{bmatrix} 0\\2\\0\\0\\-3\\0 \end{bmatrix} \\
     y\in\mathbb{R}^m & B\in \mathbb{R}^{m\times n} & h\in\mathbb{R}^n
    \end{matrix}`$
    - i.e.) $`h`$ is a function of $`x`$ that represents the information present in $`x`$ but does so with sparse vector.

<br>

#### Concept) Sparse Representation
- Objective)
  - Place a penalty on the activations of the units in a neural network, encouraging their activations to be [sparse](#concept-sparsity).
  - Recall that [L1 penalization induces a sparse parametrization](../01/note.md#analysis-7123-comparison-with-l2-regularization).
- Methodologies)
  - Using [Parameter Norm Penalties](../01/note.md#concept-parameter-norm-penalty).
    - Notation)
      - $`\tilde{J}(\theta; X, y) = J(\theta; X, y) + \alpha\Omega(h)`$
        - where
          - $`J`$ : an unregularized loss function
          - $`\alpha \in [0, \infty]`$ : a weight determining the relative contribution of the norm penalty
          - $`\Omega(h)`$ : the penalty
    - e.g.)
      - [L1 Regularization](../01/note.md#712-l1-regularization) : $`\displaystyle \Omega(h) = ||h||_1 = \sum_i |h_i|`$
      - A Student-t prior on the representation by *Olshausen and Field, 1996; Bergstra, 2011*
      - KL divergence penalties by *Larochelle and Bengio, 2008*
  - Orthogonal Matching Pursuit (OMP-$`k`$)
    - *Pati et al., 1993*
    - Encoding an input $`x`$ with the representation $`h`$ that solves the constrained optimization problem
      - $`\displaystyle \arg\min_{h, ||h||_0\lt k} ||x-Wh||^2`$
        - where $`||h||_0`$ is the number of non-zero entries of $`h`$.
        - This problem can be solved efficiently when $`W`$ is constrained to be orthogonal.










<br>

* [Back to Deep Learning MIT](../../main.md)