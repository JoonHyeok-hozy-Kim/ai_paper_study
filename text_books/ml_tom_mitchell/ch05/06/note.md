* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 5.6 Comparing Learning Algorithms

#### Concept) Comparing Learning Algorithms
- Settings)
  - $f$ : the target function
  - $L_A, L_B$ : methods that learn $f$
- Objective)
  - Determine which of $L_A$ and $L_B$ is better on average for learning $f$?
    - i.e.) relative performance of the two algorithms averaged over the training sets of size $n$ drawn from the underlying instance distribution $D$.
    - Notation)
      - $E_{S \subset D} [error_D(L_A(S)) - error_D(L_B(S))]$
        - where $L(S)$ is the hypothesis output by learning method $L$ when given the sample $S$ of training data 
        - $S \subset D$ indicates that the expected value is taken over samples $S$ drawn according to the underlying instance distribution $D$.
- Sol.)
  - Divide the limited sample data $D_0$ into a training set $S_0$ and a disjoint test set $T_0$.
  - Train $L_A$ and $L_B$ using $S_0$.
    - i.e.) Measure the following.
      - $error_{T_0}(L_A(S_0)) - error_{T_0}(L_B(S_0))$
        - why?)
          - $error_{T_0}(h) \approx error_{D}(h)$














<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)