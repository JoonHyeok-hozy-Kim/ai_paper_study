* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 9.3 An Illustrative Example

### Concept) GABIL, *DeJong et al. (1993)*
- Goal)
  - Learn boolean concepts represented by a disjunctive set of propositional rules.
- How?)
  - It used [the algorithm in the section 9.2](../02/note.md#algorithm-genetic-algorithm-ga).
    - Parameter Settings
      - ```r=0.6``` : the fraction of parent population replaced by crossover
      - ```m=0.001``` : the mutation rate
      - ```100 <= p <= 1000``` : the population size
  - Hypothesis Representation)
    - Each **hypothesis** corresponds to a disjunctive set of propositional rules.
      - [Bit String Representation](../02/note.md#tech-bit-string-representation)
    - The **hypothesis space** of rule preconditions consists of a **conjunction** of constraints on a fixed set of attributes, as described in that earlier section.
      - i.e.) concatenating the individual rules represented in bit strings.
      - e.g.)    
        |Hypothesis|Individual Rules|Representation|
        |-|-|-|
        |$\textrm{IF } a_1=\textrm{True} \vee a_2=\textrm{False THEN } c=\textrm{True}$|$a_1=\textrm{True}$ : $10$<br>$a_2=\textrm{False}$ : $01$<br>$c=\textrm{True}$ : $1$|$`\displaystyle \left.\begin{array}{ccc} a_1&a_2&c\\10&01&1 \end{array}\right. `$|
        |$\textrm{IF } a_2=\textrm{True THEN } c=\textrm{False}$|$a_1=\textrm{True} \wedge a_1=\textrm{False}$ : $11$<br>$a_2=\textrm{True}$ : $10$<br>$c=\textrm{False}$ : $0$|$`\displaystyle \left.\begin{array}{ccc} a_1&a_2&c\\11&10&0 \end{array}\right. `$|
  - Genetic Operators)
    - Mutation Operator
      - **A single bit** is chosen at random and replaced by its complement.
    - Crossover Operator
      - e.g.)
        - Let two parent hypotheses $h_1,h_2$ as follows.   
          $`\displaystyle \left.\begin{array}{ccccccccc} &&a_2&a_2&c&&a_1&a_2&c\\h_1&:&10&01&1&&11&10&0\\h_2&:&01&11&0&&10&01&0 \end{array}\right. `$
        - Choose two points randomly from $h_1$.
          - Suppose $`p_1=1,\;p_2=8`$ are chosen.   
            $`\displaystyle \left.\begin{array}{ccccccccc} &&a_2&a_2&c&&a_1&a_2&c\\h_1&:&10&01&1&&11&10&0\\&&\textrm{-}p_1&\textrm{-}\textrm{-}&\textrm{-}&&\textrm{-}\textrm{-}&\textrm{-}p_2&\textrm{-} \end{array}\right. `$
        - Let $d_1,d_2$ as...
          - $d_1$ : the distance from the **leftmost** of these two crossover points to the rule boundary immediately to its left.
          - $d_2$ : the distance from the **rightmost** of these two crossover points to the rule boundary immediately to its left.
            - Then we may get $d_1,d_2$ as follows.   
              $`\displaystyle \left.\begin{array}{ccccccccc} &&a_2&a_2&c&&a_1&a_2&c\\h_1&:&10&01&1&&11&10&0\\&&\ell_1p_1&**&*&&\ell_2*&*p_2&* \end{array}\right. `$
                - $d_1=1-0=1$
                  - The rule boundary immediately left to $p_1$ is $\ell_1$.
                - $d_2=8-5=3$
                  - The rule boundary immediately left to $p_2$ is $\ell_2$.
        - Choose two points randomly from $h_2$, subject to the constraint that they must have the same $d_1,d_2$ value.






<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)