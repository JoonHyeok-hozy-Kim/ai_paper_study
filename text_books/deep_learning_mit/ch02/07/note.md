* [Back to Deep Learning MIT](../../main.md)

# 2.7 Eigendecomposition

Why needed?)
- By decomposing **integers** into prime factors, we can conclude useful properties.
  - e.g.) $12 = 2^2\times 3$
    - Then
      - $12$ is not divisible by $5$
      - Any integer multiple of $12$ will be divisible by $3$.
- Likewise, decomposing **matrices** can show us information about their functional properties that is not obvious from the representation of the matrix as an array of elements.
- [Eigendecomposition](#concept-eigendecomposition) is one of those decomposing techniques.

<br>

### Concept) Eigenvector and Eigenvalue
- Def.)
  - An **eigenvector** of a square matrix $`A`$ is a non-zero vector $`v`$ such that multiplication by $`A`$ alters only the scale of $`v`$ :
    - $`Av = \lambda v`$
  - The scalar $`\lambda`$ is known as the **eigenvalue** corresponding to this **eigenvector**.

#### cf.) Left Eigenvector
- Def.)
  - $v$ such that $v^\top A = \lambda v^\top$
- Not much used...

<br><br>

### Concept) Eigendecomposition
- Desc.)
  - A matrix decomposition that decompose a matrix into a set of [eigenvectors and eigenvalues](#concept-eigenvector-and-eigenvalue).
- Def.)
  - Let
    - $`A \in \mathbb{R}^{n\times n}`$
      - that has $n$ linearly independent eigenvectors $`\left\lbrace v^{(1)}, \cdots, v^{(n)} \right\rbrace`$
      - with corresponding eigenvalues $`\left\lbrace \lambda_1, \cdots, \lambda_n \right\rbrace`$
    - $`V \equiv \left[\begin{array}{ccc}
        v^{(1)} & \cdots & v^{(n)}
    \end{array}\right] \in \mathbb{R}^{n\times n}`$
    - $`\lambda \equiv \left[\begin{array}{ccc}
        \lambda_1 & \cdots & \lambda_n
    \end{array}\right] \in \mathbb{R}^n`$
  - Then the **eigendecomposition** of $`A`$ is then given by
    - $`A = V \textrm{diag}(\lambda) V^{-1}`$
- Prop.)
  - Not every matrix can be decomposed into eigenvalues and eigenvectors.
    - But we will focus on real symmetric matrices.

<br>

### Tech.) Eigendecomposition for Real Symmetric Matrices
- Def.)
  - Let 
    - $`A \in \mathbb{R}^{n\times n}`$ be a real symmetric matrix.
  - Then there exists $`Q, \Lambda\in \mathbb{R}^{n\times n}`$ such that
    - $`Q`$ is an orthogonal matrix composed of eigenvectors of $`A`$
    - $`\Lambda`$ is an diagonal matrix
      - where 
        - $`\Lambda_{i,j} = \begin{cases}
            \textrm{the eigenvalue associated with } Q_{:,j} & i=j \\
            0 & i\ne j
        \end{cases}`$ 
- Prop.)
  - If (1) $`\Lambda`$ is sorted in descending order and (2) eigenvalues are unique
    - then the **eigendecomposition is unique**.
  - The matrix is [singular](../04/note.md#concept-singularity) iff. the every eigenvalue is nonzero.
- Application)
  - Quadratic Expression Optimization
    - Consider a quadratic expressions of the form $`f(x) = x^\top A x`$ subject to $`||x||_2 = 1`$.
    - If $`x`$ is equal to an eigenvector of $`A`$
      - then $`f`$ takes on the value of the corresponding **eigenvalue**.
    - Thus,
      - the maximum value of $`f`$ within the constraint region is the maximum **eigenvalue**
      - the minimum value within the constraint region is the minimum **eigenvalue**.

<br><br>

### Concept) Positive/Negative Definite
- Def.)
  - A matrix whose eigenvalues are all positive(negative) is called **positive(negative) definite**.
  - A matrix whose eigenvalues are all positive(negative) or zero-valued is called **positive(negative) semidefinite**.
- Prop.)
  - If $`A`$ is positively semidefinite,
    - $`\forall x, \; x^\top A x \ge 0`$
  - If $`A`$ is positively definite,
    - $`\forall x, \; x^\top A x = 0 \Rightarrow x = 0`$



<br>

* [Back to Deep Learning MIT](../../main.md)