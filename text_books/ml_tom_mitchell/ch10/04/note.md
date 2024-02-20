* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 10.4 Learning First-Order Rules

### Concept) Inductive Logic Program (ILP)
- A program that performs inductive learning of first-order rules or theories

<br>

## 10.4.1 First-Order Horn Clause
### E.g) Simple Target Concept Learning : Daughter
#### Settings)
- Person
  - Each person is described by attributes : $\langle Name, Mother, Father, Male, Female \rangle$
  - e.g.)
    - $`x = \langle Sharon,\;Louise,\;Bob,\;False,\;True \rangle`$
    - $`y = \langle Bob,\;Nora,\;Victor,\;True,\;False \rangle`$
- Target Concept : $`Daughter(x,y)=\left\{\begin{array}{ll}True & \textrm{if } x \textrm{ is the daughter of }y \\False & \textrm{otherwise}\end{array}\right.`$
  - where $x$ and $y$ are people
  - e.g.)
    - $`Daughter(x,y)=True`$
#### Training)
- Proposition Rule Learners)
  - e.g)
    - CN2, C4.5
  - Expected Result)
    - Collection of very specific Rules.
      - e.g) $`\textrm{IF } (Father_x=Bob)\wedge(Name_y=Bob)\wedge(Female_x=True)\textrm{ THEN }Daughter_{x,y}=True`$
    - Although it is correct, this rule is so specific that it will rarely, if ever, be useful in classifying future pairs of people.
  - Problem)
    - Propositional representations offer no general way to describe the essential relations among the values of the attributes.
- A Program Using First-Order Representations)
  - Expected Result)
    - General rules.
      - e.g.) 
        - $`\textrm{IF }Father(y, x) \wedge Female(y)\textrm{ THEN }Daughter(x,y), \forall x, y`$
    - Referring to variables in the preconditions that do not occur in the postconditions : $GrandDaughter()$
      - $`\textrm{IF }Father(y, z) \wedge Mother(z, x) \wedge Female(y)\textrm{ THEN }GrandDaughter(x,y), \forall x, y`$

<br><br>

## 10.4.2 Terminology
|Concept|e.g.|Desc.|
|-|-|-|
|Constants|$Bob, Louise$|- Capitalized symbols|
|Variable|$x, y$|- Lowercase|
|Predicate Symbols|$Married, Greater\_Than$|- Return boolean values<br>- Capitalized symbols|
|Function Symbols|$age$|- Return constants<br>- Lowercase|
|Term|$Bob, x, age(Bob)$|- Any constant, any variable, or any function applied to any term|
|Literal|$Married(Bob, Louise), \neg Greater\_Than(age(Sue),20)$|- Any predicate or its negation applied to any term<br>- A **ground literal** is a literal that does not contain any variables (e.g., $\neg Female(Joe)$ ).<br>- A **negative literal** is a literal containing a negated predicate (e.g., $\neg Female(Joe)$ ).<br>- A positive literal is a literal with no negation sign.|
|Clause||Any disjunction of literals, where all variables are assumed to be universally quantified.|
|Horn clause|$H\vee\neg{L_1}\vee\cdots\vee\neg{L_n}$|A clause containing at most one positive literal|

<br>

### Prop.) Horn Clause Representation
- Recall that a Horn clause can be represented as follows.
  - $H\vee\neg{L_1}\vee\cdots\vee\neg{L_n}$
- We can alternatively write the clause as follows.
  - $H\leftarrow({L_1}\wedge\cdots\wedge{L_n})$
    - why?)
      1. $\neg A \vee \neg B = \neg(A\wedge B)$
         - Then, $H\vee\neg{L_1}\vee\cdots\vee\neg{L_n} = H\vee\neg({L_1}\wedge\cdots\wedge{L_n})$
      2. $A\vee\neg B = A \leftarrow B$ ([why?](pf.md))
         - Then, $H\vee\neg({L_1}\wedge\cdots\wedge{L_n}) = H\leftarrow({L_1}\wedge\cdots\wedge{L_n})$
  - i.e.) $`\textrm{IF } {L_1}\wedge\cdots\wedge{L_n}\textrm{ THEN }H`$
- Term)
  - ${L_1}\wedge\cdots\wedge{L_n}$ : the clause body or the clause antecedents
  - $

### Props.) First-Order Logic
- Every well-formed expression is composed of constants, variables, predicates, and functions.
- A **substitution** is any function that replaces variables by terms.
  - e.g.) $`\{x/3, y/z\}`$
    - It replaces $x$ and $y$ by $3$ and $z$ respectively.
  - Notation) $L\theta$ : the result of substitution $\theta$ to $L$
    - where $\theta$ is a substitution and $L$ is a literal. 





<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)