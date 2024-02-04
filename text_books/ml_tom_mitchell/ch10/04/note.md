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


<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)