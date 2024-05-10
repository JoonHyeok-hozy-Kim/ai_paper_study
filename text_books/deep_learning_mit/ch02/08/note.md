* [Back to Deep Learning MIT](../../main.md)

# 2.8 Singular Value Decomposition

### Concept) Singular Value Decomposition (SVD)
- Desc.)
  - Just like the [eigendecomposition](../07/note.md#concept-eigendecomposition), the singular value decomposition (SVD) The SVD allows us to discover some of the same kind of information about matrices.
  - **Every** real matrix has a SVD.
    - Recall that the [eigendecomposition](../07/note.md#concept-eigendecomposition) was limited to matrices that are not square matrices.
- Def.)
  - For $`A \in \mathbb{R}^{m\times n}`$
    - $`\exists U, D, V \textrm{ such that } A = UDV^\top`$
      - where
        - $`U \in \mathbb{R}^{m\times m}`$ : an orthogonal matrix
          - The columns of $`U`$ are the **left-singular vectors**.
        - $`D \in \mathbb{R}^{m\times n}`$ : a diagonal matrix, not necessarily square!
          - The diagonal of $`D`$ are the **singular values** of $`A`$
        - $`V \in \mathbb{R}^{n\times n}`$ : an orthogonal matrix
          - The columns of $`V`$ are the **right-singular vectors**.
- Prop.)
  - The left-singular vectors of $`A`$ are the eigenvectors of $`AA^\top`$.
  - The right-singular vectors of $`A`$ are the eigenvectors of $`A^\top A`$.
  - The non-zero singular values of $`A`$ are the square roots of the eigenvalues of $`AA^\top`$ and $`A^\top A`$.
  - SVD can be used to partially generalize matrix inversion to non-square matrices.
    - cf.) [The Moore-Penrose Pseudoinverse](../09/note.md#concept-the-moore-penrose-pseudoinverse)







<br>

* [Back to Deep Learning MIT](../../main.md)