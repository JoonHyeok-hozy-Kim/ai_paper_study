* [Back to Dive into Deep Learning](../../main.md)

# 2.1 Scalars, Vectors, Matrices, and Tensors

### Concept) Scalars
- Def.)
  - A scalar is just a single number.
- Notation)
  - $n\in \mathbb{R}$

<br>

### Concept) Vectors
- Def.)
  - A vector is an array of numbers.
- Notation)
  - $`\textbf{\textit{x}} = \left[\begin{array}{c}
    x_1 \\ x_2 \\ \vdots \\ x_n
  \end{array}\right] \in \mathbf{R}^n`$
  - cf.) A vector containing some elements of vector $`\textbf{\textit{x}}`$.
    - Suppose $`S=\left\lbrace 1,3,6 \right\rbrace`$
      - Then $`\textbf{\textit{x}}_S`$ is the vector containing $`x_1, x_3, x_6`$.
      - Then $`\textbf{\textit{x}}_{-S}`$ is the vector containing all of the elements of $`\textbf{\textit{x}}`$ except $`x_1, x_3, x_6`$.
    - $`\textbf{\textit{x}}_{-1}`$ : the vector containing all elements of $`\textbf{\textit{x}}`$ except for $`x_1`$

<br>

### Concept) Matrices
- Def.)
  - A matrix is a 2-D array of numbers.
- Notation)
  - $`\textbf{\textit{A}} = \left[\begin{array}{cccc}
    A_{1,1} & A_{1,2} & \cdots & A_{1,n} \\
    A_{2,1} & A_{2,2} & \cdots & A_{2,n} \\
    \vdots & \vdots & \ddots & \vdots \\
    A_{m,1} & A_{m,2} & \cdots & A_{m,n} \\
  \end{array}\right] \in \mathbb{R}^{m\times n}`$
  - cf.) $`i`$-th row of $`\textbf{\textit{A}}`$
    - $`A_{i,:} = \left[\begin{array}{cccc}
    A_{i,1} & A_{i,2} & \cdots & A_{i,n}
  \end{array}\right]`$
  - cf.) $`j`$-th column of $`\textbf{\textit{A}}`$
    - $`A_{:,j} = \left[\begin{array}{cccc}
    A_{1,j} \\ A_{2,j} \\ \vdots \\ A_{m,j}
  \end{array}\right]`$
  - cf.) $`f(\textbf{\textit{A}})_{i,j}`$ : $`(i,j)`$-th element of matrix $`\textbf{\textit{A}}`$ computed by applying the function of $f$

#### Operation) Transpose
- Def.)
  - An operation on matrices that mirrors image of the matrix across the main diagonal.
- Notation)
  - $`(\textbf{\textit{A}}^\top)_{i,j} = (\textbf{\textit{A}})_{j,i}`$

#### Operation) Broadcasting
- Def.)
  - Implicitly copying elements of an array to many locations
- e.g.)
  - Matrix-Vector Addition)
    - For $`C, A \in \mathbb{R}^{m\times n} \textrm{ and } b \in \mathbb{R}^{n}`$
      - $`C = A+b`$ denotes $`C_{i,j} = A_{i,j}+b_{j}`$
        - i.e.) The vector $`b`$ is added to each row of the matrix $`A`$.

<br>

### Concept) Tensors
- Def.)
  - An array of numbers arranged on a regular grid with a variable number of axes is known as a tensor.
- Notation)
  - $\mathsf{A}$

<br>










<br>

* [Back to Dive into Deep Learning](../../main.md)