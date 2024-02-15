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
#### e.g.) Child(u,v)
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
  - Among many possible hypotheses, following two satisfy the constraint $(B \wedge h \wedge x_i) \vdash f(x_i)$
    - $h_1 : Child(u,v)\leftarrow Father(v,u)$
    - $h_2 : Child(u,v)\leftarrow Parent(v,u)$
      - cf.) Refer to [Constructive Induction below](#concept-constructive-induction) for more description

<br>

### Concept) Constructive Induction
- Def.)
  - The process of augmenting the set of predicates, based on background knowledge
- E.g.)
  - Consider the case of learning $Child(u,v)$ [above](#eg-childuv).
    - $h_1 : Child(u,v)\leftarrow Father(v,u)$
      - cf.)
        - Entailed by $h_1\wedge x_i$.
        - $B$ not needed.
    - $h_2 : Child(u,v)\leftarrow Parent(v,u)$
      - cf.)
        - Entailed by $B\wedge h_2 \wedge x_i$.
        - Cannot be deducted solely from $h_2 \wedge x_i$.
        - This is how the background knowledge expands the set of acceptable hypotheses for a given set of training data.


<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)