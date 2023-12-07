* [Back to Linear Algebra Main](../../main.md)

# 2.3 Invertibility and Elementary Matrices

#### Def) Invertibility
An $n \times n$ matrix $A$ is called **invertible** if there exists an $n \times n$ matrix $B$ such that $AB = BA = I_n$. In this case, $B$ is called an **inverse** of $A$.
- Notation)
  - $A^{-1} = B$
- Props.)
  - If $A$ is invertible, $A^{-1}$ is unique.
    - pf.)
      - Suppose, $B=A^{-1}$ and $C=A^{-1}$.
      - Then, $B = BI_n = B(AC) = (BA)C = I_nC = C$
  - If $A^{-1} = B$, then $B^{-1} = A$
  - $\nexists O^{-1}$

<br>

#### Prop.)
If $A$ is an invertible $n \times n$ matrix, then for every $b$ in $\mathbb{R}^n$ , $Ax = b$ has the unique solution $A^{−1}b$.


### [Exercises 1.2](./exercises.md)





* [Back to Linear Algebra Main](../../main.md)