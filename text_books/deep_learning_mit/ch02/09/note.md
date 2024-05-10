* [Back to Deep Learning MIT](../../main.md)

# 2.9 The Moore-Penrose Pseudoinverse
Why needed?)
- Recall that deriving inverse matrix could be an efficient solution for the system of linear equation $`Ax = b`$.
- However, only the square matrices can have the inverse.
- Meanwhile, there are cases that $`A`$ is a rectangular matrix.
- [The Moore-Penrose Pseudoinverse](#concept-the-moore-penrose-pseudoinverse) can be useful for solving such systems.


<br>

### Concept) The Moore-Penrose Pseudoinverse
- Def.)
  - For $`A \in \mathbb{R}^{m\times n}`$
    - The pseudoinverse of $`A`$ is defined as a matrix
      - $`\displaystyle A^{+} \equiv \lim_{\alpha\rightarrow 0} \left(A^\top A + \alpha I \right)^{-1} A^\top`$
- Prop.)
  - Practical way to get $`A^{+}`$ is to use [the SVD](../08/note.md#concept-singular-value-decomposition-svd).
    - $`A^{+} = V D^{+} U^\top`$
      - where
        - $`U, V, D`$ are the [the singular value decomposition](../08/note.md#concept-singular-value-decomposition-svd) of $`A`$
        - $`D^{+}`$ is the pseudoinverse of a diagonal matrix $`D`$, obtained by taking reciprocal of its non-zero an taking transpose of the resulting matrix.
          - i.e.) $`D^{+}_{i,j} = \frac{1}{D{j,i}}`$
  - Cases by the shape of $`A`$
    1. $A$ has more columns that rows $`(m \gt n)`$
       - Solving a linear equation using the pseudoinverse provides **one of the many possible solutions**.
       - It provides the solution $`x=A^{+}y`$ with minimal Euclidean norm $`||x||_2`$ among all possible solutions.
    2. $A$ has more rows that columns $`(m \lt n)`$
       - It is possible for there to be no solution.
       - Using the pseudoinverse gives us the $`x`$ for which $`Ax`$ is as close as possible to $`y`$ in terms of Euclidean norm $`||Ax-y||_2`$.






<br>

* [Back to Deep Learning MIT](../../main.md)