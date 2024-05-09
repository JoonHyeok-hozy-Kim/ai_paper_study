* [Back to Dive into Deep Learning](../../main.md)

# 2.2 Multiplying Matrices and Vectors

### Concept) Matrix Product
- Def.)
  - For $`A\in \mathbb{R}^{m\times n}, B\in \mathbb{R}^{n \times p}, C\in \mathbb{R}^{m \times p}`$
    - $`C = AB`$
      - where $\displaystyle C_{i,j} = \sum_k A_{i,k} B_{k,j}$

<br>

#### Cf.) Hadamard Product (Element-Wise Product)
- Def.)
  - For $`A,B,C\in \mathbb{R}^{m\times n}`$
    - $`C = A \odot B`$
      - where $\displaystyle C_{i,j} = A_{i,j} B_{i,j}$

#### Cf) Dot Product between Two Vectors of the Same Dimensionalities
- Def.)
  - For $x,y \in \mathbb{R}^n$
    - $`x^\top y`$

<br>

### Concept) Associative Property of Matrix Multiplication
- $`A(B+C) = AB+AC`$
- $`A(BC) = (AB)C`$
- cf.) Matrix multiplication is NOT commutative.
  - $`AB \ne BA`$

<br>

### Concept) Transpose of the Matrix Product
- $`(AB)^\top = B^\top A^\top`$


<br>

### Concept) System of Linear Equations
- Def.)
  - For $`A\in \mathbb{R}^{m\times n}, x \in \mathbb{R}^n, b\in \mathbb{R}^m`$
    - $`Ax = b`$
- Prop.)
  - $`\displaystyle A_{i,:} x = \sum_j A_{i,j}x_j = b_i`$


<br>

* [Back to Dive into Deep Learning](../../main.md)