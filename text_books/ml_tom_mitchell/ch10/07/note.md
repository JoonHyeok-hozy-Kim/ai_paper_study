* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 10.7 Inverting Resolution

### Concept) Resolution Rule
*Robinson, 1965*
- Def.) In propositional form...
  - Let 
    - $L$ : an arbitrary propositional literal
    - $P, R$ : arbitrary propositional clauses
  - Then, the **resolution rule** is $`\begin{array}{ccc} P & \vee & L \\ \neg L & \vee & R \\ \hline P & \vee & R \end{array}`$
    - where the dividing line stands for "entails".
- Interpretation)
  - Given the two clauses above the line, conclude the clause below the line.
- Intuitive Proof)
  - Suppose $(P \vee L) \wedge (\neg L \vee R)$ is true.
    - Then, $L$ would be either true or false.
      - Case 1) $L$ is true.
        - Then, $R$ should be true.
        - Thus, $P \vee R$ is true.
      - Case 2) $L$ is false.
        - Then, $P$ should be true.
        - Thus, $P \vee R$ is true.
    - Hence, $P \vee R$ is true

<br>

### Concept) Resolution Operator
- Def.)
  - Let 
    - $C_1, C_2$ : given clauses
    - $L$ : a literal such that $L$ occurs in $C_1$ and $\neg L$ occurs in $C_2$
  - The **resolution operator** constructs a clause such that
    - $`C = (C_1-\{L\}) \cup (C_2 - \{\neg L \})`$ 
      - i.e.) The resolvent $C$ includes all literals from $C_1$ and $C_2$, except for $L$ and $\neg L$ respectively.
- e.g.)
  - Suppose
    - $C_1 = A\vee B\vee C\vee \neg D$
    - $C_2 = \neg B\vee E\vee F$.
  - Then the result of applying the resolution rule to $C_1$ and $C_2$ is the clause $A\vee C\vee \neg D\vee E\vee F$.
    - In this case, $L=B$.

<br>

### Tech) Inverting Resolution Operator to Form Inverse Entailment Operator
- Review
  - [Inverse Entailment Operator](../06/note.md#concept-inverse-entailment-operator) : $O(C_1, C)$
- Prop.)
  - In general, the inverse entailment operator must derive one of the initial clauses, $C_2$, given the resolvent $C$ and the other initial clause $C_1$.
- How?)
  - Let $C_1$ and $C$ be initial clauses.
  - We should find a literal $L$ that occurs in $C_1$, but not in $C$.
  - Form the second clause $C_2$ by including the following literals
    - $`C_2 = (C-(C_1-\{L\})) \cup \{\neg L\}`$
- e.g.)
  - Suppose
    - $C = A\vee B$
    - $C_1 = B \vee D$
  - Then, we should get $C_2$ such that $C_1 \wedge C_2 \vdash C$.
  - By the definition of the resolution operator,
    1. Any literal occurred in $C$ but not in $C_1$ must be present in $C_2$.
    2. The **negation** of any literal occurred in $C_1$ but not in $C$ must be present in $C_2$.
  - Then there can be multiple clauses that satisfy the condition of $C_2$.
    - $C_2=A \vee \neg D$
    - $C_2=A \vee \neg D \vee B$
  - A heuristic for choosing among the alternatives...
    - Prefer shorter clauses over longer clauses
    - Assume $C_2$ shares no literals in common with $C_1$
      - Thus, $C_2=A \vee \neg D$

<br><br>

## 10.7.1 First-Order Resolution
- Objective)
  - Extending the [resolution rule](#concept-resolution-rule) to [first-order expressions](../02/note.md#concept-first-order-rule).

<br>

#### Concept) Substitution
- Def.)
  - Mapping of variables to terms
- e.g.)
  - $`\theta = \left\{ x/Bob, y/z \right\}`$
    - The variable $x$ is to be replaced with $Bob$. 
    - The variable $y$ is to be replaced by the term $z$.
- Notation)
  - Let $W$ be an expression.
  - Then, $W\theta$ denotes the result of applying the substitution $\theta$ to $W$.
    - e.g.)
      - Let $L$ is the literal $Father(x, Bill)$ and $`\theta = \left\{ x/Bob, y/z \right\}`$.
      - Then, $L\theta = Father(Bob, Bill)$.

<br>

#### Concept) Unifying Substitution
- Def.)
  - $\theta$ is a **unifying substitution** for two literals $L_1$ and $L_2$, provided $L_1\theta = L_2\theta$.
    - where $\theta$ is a [substitution](#concept-substitution).
- e.g.)
  - Let
    - $L_1=Father(x,y)$
    - $L_2=Father(Bill,z)$
    - $`\theta=\{x/Bill,z/y\}`$
  - Then $L_1\theta = Father(Bill, y) =L_2\theta$.
  - Thus, $\theta$ is an unifying substitution.

<br>

### Tech) Resolution Rule with Unifying Substitution
- Idea)
  - Recall that we derived a resolvent $C$ from the clauses $C_1, C_2$ using the [resolution rule](#concept-resolution-rule).
  - In first-order resolution, the [unifying substitution](#concept-unifying-substitution) generalizes to finding one literal $L_1$ from clause $C_1$ and one literal $L_2$ from $C_2$ for some unifying substitution $\theta$ such that $L_1\theta = \neg L_2\theta$.
- How?)
  - Let
    - $C_1, C_2$ : clauses
    - $L_1, L_2$ : literals from $C_1, C_2$
    - $\theta$ : a substitution such that $L_1\theta = \neg L_2 \theta$
  - Then, $`C=(C_1-\{L_1\})\theta \cup (C_2-\{L_2\})\theta`$
- e.g.)
  - Suppose
    - $C_1=White(x)\leftarrow Swan(x)$
    - $C_2=Swan(Fred)$
  - Consider that $C_1=White(x)\leftarrow Swan(x)$ is [equivalent](../04/pf.md) to $C_1=White(x) \vee \neg Swan(x)$.


<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)