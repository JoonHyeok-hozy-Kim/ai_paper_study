* [Back to Linear Algebra Main](../../main.md)

# 4.1 Subspaces

#### Def) Subspaces and Closure
![](images/001.png)
- Props.)
  - The set $\mathbb{R}^n$ is a subspace of itself.
    - why?)
      - $\mathbf{0} \in \mathbb{R}^n$
      - $\forall \mathbf{u}, \mathbf{v}\in \mathbb{R}^n, \mathbf{u}+\mathbf{v} \in \mathbb{R}^n$
      - $\forall c \in \mathbb{R}, \forall\mathbf{u}\in \mathbb{R}^n, c\mathbf{u} \in \mathbb{R}^n$

<br>

<img src="images/002.png" width="400px"><img>

#### Concept) Zero Subspace
- Def.)
  - A set consisting of only the zero vector in $\mathbb{R}^n$ is a subspace of $\mathbb{R}^n$ called the zero subspace.
- Prop.)
  - Zero subspace is a subspace of $\mathbb{R}^n$.

<br>

#### Concept) Nonzero Subspace
- Def.) $\mathbb{R}^n - \lbrace 0 \rbrace$
- Prop.)
  - Nonzero subspace is NOT a subspace of $\mathbb{R}^n$.
    - why?)
      - $\mathbf{0} \notin \mathbb{R}^n - \lbrace 0 \rbrace$

<br>

#### E.g.) No Subspace Cases
1. $`V = \left \{ \left[\begin{array}{c} v_1 \\ v_2 \end{array} \right] \in \mathbb{R}^2 : v_1, v_2 \ge 0 \right\}`$ : NOT a subspace of $\mathbb{R}^2$.
   - why?)
     - Counter ex.)
       - Let $\mathbf{u} \in V$.
       - Then $(-2)\cdot\mathbf{u} \notin V$
2. $`W = \left \{ \left[\begin{array}{c} w_1 \\ w_2 \end{array} \right] \in \mathbb{R}^2 : w_1^2 = w_2^2 \right\}`$ : NOT a subspace of $\mathbb{R}^2$.
   - why?)
     - Counter ex.)
       - Let $`\mathbf{u} = \left[\begin{array}{c} 1 \\ 1 \end{array} \right],\mathbf{v} = \left[\begin{array}{c} 1 \\ -1 \end{array} \right]`$.
       - Then $\mathbf{u}, \mathbf{v} \in W$.
       - But $`\mathbf{u}+\mathbf{v} = \left[\begin{array}{c} 2 \\ 0 \end{array} \right] \notin W`$.

<br>

### Theorem 4.1)
The span of a finite nonempty subset of $\mathbb{R}^n$ is a subspace of $\mathbb{R}^n$.
- pf.)
  - Let $V \in R^n$ and $`S=\{\mathbf{w}_1, \mathbf{w}_2, \cdots, \mathbf{w}_k\}`$ be the span of $V$.
  - Then by def., $`\displaystyle \sum_{i=1}^k 0\cdot\mathbf{w}_i = \mathbf{0} \in S`$.
  - Put $\mathbf{u}, \mathbf{v} \in S$ such that
    - $`\displaystyle\mathbf{u}=\sum_{i=1}^k{a_i\mathbf{w}_i}, \mathbf{v}=\sum_{i=1}^k{b_i\mathbf{w}_i}, \exists a_i, b_i \in \mathbb{R}`$
  - Then $\displaystyle\mathbf{u}+\mathbf{v}=\sum_{i=1}^k{(a_i+b_i)\mathbf{w}_i}\in S$.
  - Also, $`\displaystyle\forall c \in \mathbb{R}, c\mathbf{u}=c\sum_{i=1}^k{a_i\mathbf{w}_i}=\sum_{i=1}^k{ca_i\mathbf{w}_i} \in S`$

- e.g.) 
  - $`W = \left \{ \left[\begin{array}{c} 2a-3b \\ b \\ -a+4b \end{array} \right] \in \mathbb{R}^e : a,b\in \mathbb{R} \right\}`$ is a subspace of $\mathbb{R}^3$.
    - why?)
      - $`\left[\begin{array}{c} 2a-3b \\ b \\ -a+4b \end{array} \right] = a\left[\begin{array}{c} 2 \\ 0 \\ -1 \end{array} \right] + b\left[\begin{array}{c} -3 \\ 1 \\ 4 \end{array} \right]`$
      - Thus, $`W=Span\left(\left\{ \left[\begin{array}{c} 2 \\ 0 \\ -1 \end{array} \right], \left[\begin{array}{c} -3 \\ 1 \\ 4 \end{array} \right] \right\}\right)`$.
      - By [the Theorem 4.1](#theorem-41), $W$ is a subspace of $\mathbb{R}^3$.

<br><br>

## 4.1.1 Subspaces Associated with a Matrix
### Concept) Null Space
- Def.)
  - The null space of a matrix $A$ is the solution set of $A\mathbf{x} = \mathbf{0}$. It is denoted by $\textrm{Null}(A)$.
    - i.e.) $`\textrm{Null}(A)=\{\mathbf{v}\in \mathbb{R}^n : A\mathbf{v}=\mathbf{0}\}`$
- cf.)
  - [Already introduced for linear transformations.](../../ch02/08/note.md#def-null-space)

<br>

### Theorem 4.2)
If $A$ is a $m \times n$ matrix, then Null$`(A)`$ is a subspace of $\mathbb{R}^n$.

- pf.)   
  ![](images/003.png)

<br>

### Concept) Column Space
- Def.)
  - The column space of a matrix $A$ is the span of its columns. It is denoted by Col$`(A)`$.

<img src="images/004.png" width="400px"><img>

<br>

### Prop.) Column Space
$\textrm{Col}(A) = \lbrace A\mathbf{v} : \mathbf{v} \in \mathbb{R}^n\rbrace$
- pf)
  - Let $`A=\left[\begin{array}{ccc} \mathbf{c}_1 & \cdots & \mathbf{c}_n \end{array}\right]`$  and $`\mathbf{v}=\left[\begin{array}{c} v_1 \\ \vdots \\ v_n\end{array}\right]`$
    - where $`\mathbf{c}_k \in \mathbb{R}^m, v_k \in \mathbb{R}, k=1,2,\cdots,n`$
  - Then $`\displaystyle A\mathbf{v}=\sum_{i=1}^n v_i\mathbf{c}_i \in \textrm{Span}(A)`$

<br>

#### Example Question)
<img src="images/005.png" width="400px"><img>
- Sol.) No.   
  <img src="images/006.png" width="700px"><img>


<br>

### Concept) Row Space
- Def.)
  - The row space of a matrix $A$ is the span of its rows. It is denoted by Row$`(A)`$.

- e.g.)   

<img src="images/007.png" width="500px"><img>

<br>

### Prop.) Row Space and Column Space
$`\textrm{Row}(A)=\textrm{Col}(A)^{\top}`$

<br><br>

## 4.1.2 Subspaces Associated with a Linear Transformation
### Props.) The Range of a Linear Transformation
1. **The range of a linear transformation** is the same as the **column space** of its standard matrix.
   - Why?)
     - [Recall](../../ch02/08/note.md#concept-the-range-of-a-linear-transformation) that the range of a linear transformation is the span of the columns of its standard matrix.
     - Denoting the columns of its standard matrix with the Span of the matrix we can reformulate as above.
2. The range of a linear transformation $T:\mathbb{R}^n\rightarrow\mathbb{R}^m$ is a subspace of $\mathbb{R}^m$.
   - Why?)
     - Column space is a subspace of $\mathbb{R}^m$.
3. The null space of a linear transformation is the same as the null space of its standard matrix.
   - Why?)
     - [Recall](../../ch02/08/note.md#def-null-space) that the null space of a linear transformation is the solution set of $A\mathbf{x} = 0$, where $A$ is the standard matrix of $T$.
4. The null space of a linear transformation $T : R^n \rightarrow R^m$ is a subspace of $R^n$.





<br>

### [Exercises 4.1](./exercises.md)

* [Back to Linear Algebra Main](../../main.md)