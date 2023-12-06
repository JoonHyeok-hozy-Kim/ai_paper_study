* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 5.6 Comparing Learning Algorithms

### Concept) Comparing Learning Algorithms
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

#### Sol. 1) 
Divide the limited sample data $D_0$ into a training set $S_0$ and a disjoint test set $T_0$.
- Train $L_A$ and $L_B$ using $S_0$.
  - i.e.) Measure the following.
    - $error_{T_0}(L_A(S_0)) - error_{T_0}(L_B(S_0))$
      - why?)
        - $error_{T_0}(h) \approx error_{D}(h)$

#### Sol. 2) Improved Sol.
Repeatedly partition the data $D_0$ into disjoint training and test sets and to take the mean of the test set errors for these different experiments.
- How?)
  1. Partition the available data $D_0$ into $k$ disjoint subsets $T_1, T_2, \cdots, T_k$ of equal size, where this size is at least 30.
  2. For $i$ from $1$ to $k$, use $T_i$ for the test set and the remaining data for training set $S_i$
      - $S_i \leftarrow \lbrace D_0 - T_i \rbrace$
      - $h_A \leftarrow L_A(S_i)$
      - $h_B \leftarrow L_B(S_i)$
      - $\delta_i \leftarrow error_{T_i}(h_A) - error_{T_i}(h_B)$
  3. Return the value $\bar{\delta}$ where
     - $\bar{\delta} \equiv \frac{1}{k} \Sigma_{i=1}^k \delta_i$
- Result)
  - The learning algorithms $L_A$ and $L_B$ are tested on $k$ independent test sets
  - The mean difference in errors $\bar{\delta}$ is returned as an estimate of the difference between the two learning algorithms.
    - We can view $\bar{\delta}$ as the following.
      - $E_{S \subset D_0} [error_D(L_A(S)) -error_D(L_B(S))]$
        - where $S$ is the random sample of size $\frac{k-1}{k}|D_0| drawn uniformly from $D_0$.













<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)