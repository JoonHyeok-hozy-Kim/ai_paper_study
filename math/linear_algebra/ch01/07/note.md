* [Back to Linear Algebra Main](../../main.md)

# 1.7 Linear Dependence and Linear Independence

#### Def) Linear Dependence
A set of $k$ vectors $\lbrace u_1, u_2, \dots, u_k \rbrace \sub \mathbb{R}^n$ is called linearly dependent if there exists scalars $c_1, c_2, \dots, c_k$, not all 0, such that $\Sigma_{i=1}^k c_iu_i = 0$.

Also, the vectors $u_1, u_2, \dots, u_k$ are linearly dependent.

<br>

#### Def) Linear Independence
A set of $k$ vectors $\lbrace u_1, u_2, \dots, u_k \rbrace \sub \mathbb{R}^n$ is called linearly independent if the only scalars $c_1, c_2, \dots, c_k$ such that $\Sigma_{i=1}^k c_iu_i = 0$ are $c_1 = c_2 = \dots = c_k = 0$.

Also, the vectors $u_1, u_2, \dots, u_k$ are linearly independent.

<br>

#### Prop.) A Set with the Zero Vector
Any finite subset $S \sub \mathbb{R}^n$ that contains the zero vector is linearly dependent.
- why?)
  - $\forall u_i \in \mathbb{R^n}, 1\cdot \overrightarrow{0} + \Sigma_{i=1}^k 0 \cdot u_i = 0$
    - where $\overrightarrow{0}$ is the zero vector.

<br>

#### Notation) Matrix Vector Product
$\Sigma c_iu_i = 0$ can be denoted as follows.
- $`\left[ \begin{array}{cccc} u_1 & u_2 & \cdots & u_k \end{array} \right] \left[ \begin{array}{c} c_1 \\ c_2 \\ \vdots \\ c_k \end{array} \right] = 0`$



<br>

### [Exercises 1.2](./exercises.md)





* [Back to Linear Algebra Main](../../main.md)