* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 10.6 Induction as Inverted Deduction
- Ideation)
  - Induction is just the inverse of deduction!

- Notation) 
  - $X \vdash Y$
    - Meanings)
      - $Y$ follows deductively from $X$
      - $X$ entails $Y$

### Concept) Deductive Expression of Learning
- Def.)
  - Let
    - $`D = \{\langle x_i, f(x_i) \rangle : \exists i\}`$ : some data
      - where 
        - $x_i$ : the $i$th training instance
        - $f(x_i)$ : the target value of $x_i$
    - $B$ : some partial background knowledge
    - $h$ : the target hypothesis we want to learn
  - Then
    - $`(\forall \langle x_i, f(x_i) \rangle \in D) (B \wedge h \wedge x_i) \vdash f(x_i)`$
      - i.e.) Then **learning** is the problem of discovering a hypothesis $h$, such that the classification $f(x_i)$ of each training instance $x_i$ follows deductively from the hypothesis $h$, the description of $x_i$, and any other background knowledge $B$ known to the system.
- e.g.)
  - Settings)
    - Suppose we want to learn a target concept...
      - $Child(u,v)$ : pairs of people $\langle u, v \rangle$ such that the child of $u$ is $v$
    - A single positive example is given as follows.
      - $Child(Bob, Sharon)$
        - where the instances $Bob$ and $Sharon$ are described by the literals...
          - $Male(Bob)$
          - $Female(Sharon)$
          - $Father(Sharon, Bob)$
    - We have the general background knowledge
      - $Parent(u,v) \leftarrow Father(u,v)$
  - Then, we can denote the above situation in the following problem structure.
    - $`x_i : Male(Bob), Female(Sharon), Father(Sharon, Bob)`$
    - $`f(x_i) : Child(Bob, Sharon)`$
    - $`B : Parent(u,v) \leftarrow Father(u,v)`$

<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)