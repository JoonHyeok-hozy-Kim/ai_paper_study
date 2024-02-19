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
  - Then there can be multiple clauses that satisfies the condition of $C_2$.
    - $C_2=A \vee \neg D$
    - $C_2=A \vee \neg D \vee B$
  - A heuristic for choosing among the alternatives...
    - Prefer shorter clauses over longer clauses
    - Assume $C_2$ shares no literals in common with $C_1$
      - Thus, $C_2=A \vee \neg D$


<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)