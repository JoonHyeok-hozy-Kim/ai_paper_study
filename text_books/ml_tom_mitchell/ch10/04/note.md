* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 10.4 Learning First-Order Rules

### Concept) Inductive Logic Program (ILP)
- A program that performs inductive learning of first-order rules or theories

<br>

## 10.4.1 First-Order Horn Clause
#### E.g) Simple Target Concept Learning : Daughter
- Settings)
  - Target Concept : $`Daughter(x,y)=\left\{\begin{array}{ll}True & \textrm{if } x \textrm{ is the daughter of }y \\False & \textrm{otherwise}\end{array}\right.`$
    - where $x$ and $y$ are people
      - Each person is described by attributes : $Name, Mother, Father, Male, Female$
        - e.g.)
          - $`\langle Name_1=Sharon,\;Mother_1=Louise,\;Father_1=Bob,\;Male_1=False,\;Female_1=True \rangle`$
          - $`\langle Name_2=Bob,\;Mother_2=Nora,\;Father_2=Victor,\;Male_2=True,\;Female_2=False \rangle`$



<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)