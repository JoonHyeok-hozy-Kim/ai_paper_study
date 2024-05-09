* [Back to Dive into Deep Learning](../../main.md)

# 2.4 Linear Dependence and Span

### Concept) Linear Combination
- Def.)
  - For some set of vectors $`\lbrace v^{(1)}, \cdots, v^{(n)}\rbrace`$ and some set of scalars $`\lbrace c_1, \cdots, c_n \rbrace`$
    - $`\displaystyle\sum_i c_i v^{(i)}`$

<br>

### Concept) Span
- Def.)
  - The span of a set of vectors is the set of all points obtainable by [linear combination](#concept-linear-combination) of the original vectors.

<br>

### Concept) Column Space
- Def.)
  - For the [system of linear equations](../02/note.md#concept-system-of-linear-equations) $`Ax = b`$,
    - the span of $A$ is called the **column space** or the **range** of $`A`$.
- Prop.)
  - If $`b`$ is in the column space of $`A`$, the system has at least one solution.

<br>

### Concept) Linear Independence
- Def.)
  - A set of vectors is **linearly independent** if no vector in the set is a linear combination of the other vectors.
- Prop.)
  - Necessary and sufficient for $`Ax = b`$ to have a solution for every value of $`b`$.
    - For the column space of the matrix to encompass all of $`\mathbb{R}^m`$, the matrix must contain at least one set of $`m`$ linearly independent columns.

<br>

### Concept) Singularity
- Def.)
  - A matrix is singular if all of its columns are [linearly independent](#concept-linear-independence).







<br>

* [Back to Dive into Deep Learning](../../main.md)