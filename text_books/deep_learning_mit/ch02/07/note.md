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
  
#### e.g.) Calculating Eigenvector and Eigenvalue
- Consider $`A = \begin{bmatrix} 4 & 2 \\ 3 & 5 \end{bmatrix}`$.
- Put $`v = \begin{bmatrix} v_1 \\ v_2 \end{bmatrix}`$.
- Calculating eigenvalues.
  - Then by definition $`\begin{bmatrix} 4 & 2 \\ 3 & 5 \end{bmatrix}\begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \lambda\begin{bmatrix} v_1 \\ v_2 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 4-\lambda & 2 \\ 3 & 5-\lambda \end{bmatrix}\begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = 0`$.
  - We want to find $`\lambda \in \mathbb{R}`$ such that the above linear system has a solution.
  - Thus, $`\left|\begin{array}{cc} 4-\lambda & 2 \\ 3 & 5-\lambda \end{array}\right| = 0 \Rightarrow (4-\lambda)(5-\lambda)-2\cdot5 = 0`$.
  - Hence, the eigenvalues of $`A`$ are $`2 \textrm{ and } 7`$.
- Calculating eigenvectors
  1. $`\lambda = 2`$
     - By definition, $`\begin{bmatrix} 4-2 & 2 \\ 3 & 5-2 \end{bmatrix}\begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = 0 \Rightarrow \begin{bmatrix} 2 & 2 \\ 3 & 3 \end{bmatrix}\begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = 0`$
     - Thus, $`\begin{bmatrix} 2v_1+2v_2 \\ 3v_1+3v_2 \end{bmatrix} = (v_1+v_2)\begin{bmatrix} 2 \\ 3 \end{bmatrix} = 0 \Rightarrow v_1 = -v_2`$
     - Hence, $`\begin{bmatrix} v_1\\v_2 \end{bmatrix} = \begin{bmatrix} v_1\\-v_1 \end{bmatrix} = c_1\begin{bmatrix} 1\\-1 \end{bmatrix}, c_1\in\mathbb{R}`$
  2. $`\lambda = 7`$
     - By definition, $`\begin{bmatrix} 4-7 & 2 \\ 3 & 5-7 \end{bmatrix}\begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = 0 \Rightarrow \begin{bmatrix} -3 & 2 \\ 3 & -2 \end{bmatrix}\begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = 0`$
     - Thus, $`\begin{bmatrix} -3v_1+2v_2 \\ 3v_1-2v_2 \end{bmatrix} = 0 \Rightarrow v_1 = \frac{2}{3}v_2`$
     - Hence, $`\begin{bmatrix} v_1\\v_2 \end{bmatrix} = \begin{bmatrix} \frac{2}{3}v_2\\v_2 \end{bmatrix} = c_2\begin{bmatrix} 2\\3 \end{bmatrix}, c_2\in\mathbb{R}`$
- Therefore,
  - the eigenvalues are $`2 \textrm{ and } 7`$.
  - the eigenvectors are $`c_1\begin{bmatrix} 1\\-1 \end{bmatrix}, c_2\begin{bmatrix} 2\\3 \end{bmatrix} \textrm{ where } c_1, c_2\in\mathbb{R}`$.

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

#### E.g.) Eigendecomposition
- For $`A = \begin{bmatrix} 4 & 2 \\ 3 & 5 \end{bmatrix}`$, we [calculated eigenvalues and eigenvectors as below](#eg-calculating-eigenvector-and-eigenvalue).
  - the eigenvalues are $`2 \textrm{ and } 7`$.
  - the eigenvectors are $`c_1\begin{bmatrix} 1\\-1 \end{bmatrix}, c_2\begin{bmatrix} 2\\3 \end{bmatrix} \textrm{ where } c_1, c_2\in\mathbb{R}`$.
- Decompose $`A`$.
  - By definition, $`\begin{cases}
    \begin{bmatrix} 4 & 2 \\ 3 & 5 \end{bmatrix}\begin{bmatrix} 1\\-1 \end{bmatrix} = 2\begin{bmatrix} 1\\-1 \end{bmatrix} \\
    \begin{bmatrix} 4 & 2 \\ 3 & 5 \end{bmatrix}\begin{bmatrix} 2\\3 \end{bmatrix} = 7\begin{bmatrix} 2\\3 \end{bmatrix} \\
  \end{cases} \Rightarrow \begin{bmatrix} 4 & 2 \\ 3 & 5 \end{bmatrix}\begin{bmatrix} 1&2\\-1&3 \end{bmatrix} = \begin{bmatrix} 2 & 14\\-2 & 21 \end{bmatrix} = \begin{bmatrix} 1 & 2\\-1 & 3 \end{bmatrix}\begin{bmatrix} 2 & 0\\0 & 7 \end{bmatrix}`$
  - Thus, $`\begin{bmatrix} 4 & 2 \\ 3 & 5 \end{bmatrix} = \begin{bmatrix} 1 & 2\\-1 & 3 \end{bmatrix}\begin{bmatrix} 2 & 0\\0 & 7 \end{bmatrix}\begin{bmatrix} 1 & 2\\-1 & 3 \end{bmatrix}^{-1}`$
- Usage)
  - $`\begin{bmatrix} 4 & 2 \\ 3 & 5 \end{bmatrix}^n = \begin{bmatrix} 1 & 2\\-1 & 3 \end{bmatrix}\begin{bmatrix} 2^n & 0\\0 & 7^n \end{bmatrix}\begin{bmatrix} 1 & 2\\-1 & 3 \end{bmatrix}^{-1}`$



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