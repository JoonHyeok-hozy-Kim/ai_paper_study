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
              $`\displaystyle \left.\begin{array}{ccccccccc} &&a_2&a_2&c&&a_1&a_2&c\\h_1&:&10&01&1&&11&10&0\\&&\ell_1p_1&\textrm{-}\textrm{-}&\textrm{-}&&\ell_2\textrm{-}&\textrm{-}p_2&\textrm{-} \end{array}\right. `$
                - $`\left\{\begin{array}{c}d_1=1-0=1\\d_2=8-5=3\end{array}\right.`$
                  - where $`\left\{\begin{array}{c}\ell_1\textrm{ : the rule boundary immediately left to }p_1\\\ell_2\textrm{ : the rule boundary immediately left to }p_2\end{array}\right.`$
        - Choose two points randomly from $h_2$, subject to the constraint that they must have the same $d_1,d_2$ value.
          - The available cases will be...   
            $`\displaystyle \begin{array}{ccccccccc} &&a_2&a_2&c&&a_1&a_2&c\\h_2&:&01&11&0&&10&01&0 \\ (p_1=1,\;p_2=3) &:&\ell_{12}p_1&\textrm{-}p_2&\textrm{-}&&\textrm{-}\textrm{-}&\textrm{-}\textrm{-}&\textrm{-} \\ (p_1=1,\;p_2=8) &:&\ell_1p_1&\textrm{-}\textrm{-}&\textrm{-}&&\ell_2\textrm{-}&\textrm{-}p_2&\textrm{-} \\ (p_1=6,\;p_2=8) &:&\textrm{-}\textrm{-}&\textrm{-}\textrm{-}&\textrm{-}&&\ell_{12}p_1&\textrm{-}p_2&\textrm{-} \end{array}`$
          - Suppose $`p_1=1,\;p_2=3`$ is randomly chosen.
        - Crossover the partitions of $h_1,h_2$.
          - Recall that the partitions of $h_1,h_2$ are
            - $h_1 \rightarrow [:1]+[1:8]+[8:]=[1],[0011111],[00]$
            - $h_2 \rightarrow [:1]+[1:3]+[3:]=[0],[11],[1010010]$
          - Cross over as...
            - $h_3 \leftarrow h_1[:1]+h_2[1:3]+h_1[8:]=[1],[11],[00]$
            - $h_4 \leftarrow h_2[:1]+h_1[1:8]+h_2[3:]=[0],[0011111],[1010010]$
          - Then the result goes...   
            $`\displaystyle \left.\begin{array}{cccccccccccc} &&a_2&a_2&c&&a_1&a_2&c&&a_2&a_2&c\\h_3&:&11&10&0&&&&&&\\h_4&:&00&01&1&&11&11&0&&10&01&0 \end{array}\right. `$
  - Fitness Function)
    - Fitness is the classification accuracy over the training data.
      - The measure of fitness : $\textrm{Fitness}(h) = (\textrm{correct}(h))^2$
        - where $\textrm{correct}(h)$  is the percent of all training examples correctly classified by hypothesis $h$.

<br><br>

## 9.3.1 Extensions
Newly added genetic operators

1. ```add_alternative()```
   - Desc.)
     - Generalizes the constraint on a specific attribute by changing a $0$ to a $1$ in the substring corresponding to the attribute.
     - This operator was applied with probability 0.01 to selected members of the population on each generation.
   - e.g.)
     - Suppose $`\displaystyle \left.\begin{array}{cccccccccccc} &&a_2&a_2&c\\h_3&:&11&00&0 \end{array}\right. `$.
     - Then the application of  ```add_alternative()``` on $a_2$ will be either
       - $`a_2 : 00 \rightarrow 01 \Rightarrow\displaystyle \left.\begin{array}{cccccccccccc} &&a_2&a_2&c\\h_3&:&11&01&0 \end{array}\right. `$
       - $`a_2 : 00 \rightarrow 10 \Rightarrow\displaystyle \left.\begin{array}{cccccccccccc} &&a_2&a_2&c\\h_3&:&11&10&0 \end{array}\right. `$
2. ```drop_condition()```
   - Desc.)
     - A more drastic generalization step, by replacing all bits for a particular attribute by a $1$.
     - This operator was applied on each generation with probability 0.60. 
   - e.g.)
     - Suppose $`\displaystyle \left.\begin{array}{cccccccccccc} &&a_2&a_2&c\\h_3&:&11&00&0 \end{array}\right. `$.
     - Then the application of  ```add_alternative()``` on $a_2$ will be...
       - $`a_2 : 00 \rightarrow 11 \Rightarrow\displaystyle \left.\begin{array}{cccccccccccc} &&a_2&a_2&c\\h_3&:&11&11&0 \end{array}\right. `$



<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)