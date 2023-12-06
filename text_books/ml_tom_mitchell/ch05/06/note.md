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
- Analysis)
  - Confidence interval for $\bar{\delta}$.
    - $\bar{\delta} \pm t_{N,k-1} \cdot s_{\bar{\delta}}$
      - where $t_{N,k-1}$ is the $t$-stat with the confidence level of $N$ and $k-1$ degrees of freedom.
      - and $s_{\bar{\delta}} \equiv \sqrt{\frac{1}{k(k-1)} \Sigma_{i=1}^k(\delta_i - \bar{\delta})^2}$
      - cf.) More precise explanation can be found on [Paired t Test](#561-paired-t-test) section below.
  - Comparison with the previous test
    - Recall that out [previous test compared two hypotheses evaluated using two independent test sets](../05/note.md#concept-estimating-the-difference-between-the-true-errors-of-two-hypotheses).
    - On the other hand, current testing method evaluate two hypotheses over identical samples.
      - We call this the **paired test**.
        - Prop.) Paired tests typically produce **tighter confidence intervals** because any differences in observed errors in a paired test are due to differences between the hypotheses.
          - cf.) If the sample data are heterogeneous, the difference in the two sample error may due to the difference in the samples, not the hypotheses.

<br><br>

## 5.6.1 Paired t Test
- Settings)
  - We are given the observed values of a set of independent, identically distributed random variables $Y_1, Y_2, \cdots, Y_k$.
    - Just like the [paired test](#sol-2-improved-sol) above, assume that each $Y_i$ is drawn from a sample with size of at least 30.
      - However, $Y_i$ is an idealistic case. In reality, $D_0$ from the [paired test](#sol-2-improved-sol) cannot be iid as $Y_i$. 
      - Refer to the [Practical Consideration](#562-practical-consideration) below.
    - Then, by the [Central Limit Theorem](../03/note.md#concept-the-central-limit-theorem), We may assume that each $Y_i$ follow an approximately Normal distribution.
  - We want to estimate the mean $\mu$ of the probability distribution governing these $Y_i$.
    - The estimator we will use is the sample mean $\bar{Y}$.
      - $\bar{Y} \equiv \frac{1}{k} \Sigma_{i=1}^k Y_i$
- Problem)
  - To evaluate the performance of the sample mean $\bar{Y}$, we may calculate the confidence interval of it.
  - If we want to estimate the confidence interval of $\bar{Y}$, we should know the standard deviation $\sigma_{\bar{Y}}$.
  - However, we do not know $\sigma_{\bar{Y}}$.
- Sol.) Use $t$ test.
  - According to the $t$ test, we may get the confidence interval as follows.
    - $\mu = \bar{Y} \pm t_{N,k-1} \cdot s_{\bar{Y}}$
      - where $s_{\bar{Y}}$ is the estimated standard deviation of the sample mean
        - $s_{\bar{Y}} \equiv \sqrt{\frac{1}{k(k-1)} \Sigma_{i=1}^k(Y_i - \bar{Y})^2}$
      - and $t_{N,k-1}$ is characterizes the area under a probability distribution known as the $t$-distribution.
        - cf.) Recall that $z_N$ characterized the Normal distribution.
- cf.) $t$-distribution
  - The $t$ distribution is a bell-shaped distribution similar to the Normal distribution, but wider and shorter to reflect the greater variance introduced by using $s_{\bar{Y}}$ to approximate the true standard deviation $\sigma_{\bar{Y}}$. 
  - The $t$ distribution approaches the Normal distribution $(t_{N,k-1} \rightarrow z_N)$ as k approaches infinity $(k \rightarrow \infty)$.
  - We expect $s_{\bar{Y}}$ to converge toward the true standard deviation $\sigma_{\bar{Y}}$ as the sample size k grows.


<br><br>

## 5.6.2 Practical Consideration
- Situation
  - Recall the [paired test](#56-comparing-learning-algorithms) above.
  - We sampled $D_0$ and divide them into a test set $T_i$ and a training set $S_i$.
  - In reality, the size of $D_0$ we can get is very limited so that we cannot get sufficient $k$ amount of $T_i$ and $S_i$ to generate $\delta_i$ which will be used to get $\bar{\delta}$.
  - Instead, we should resample $D_0$ several times to get $k$ amount of $T_i$ and $S_i$.
    - But, in this case, since each resampled $D_0$ will overlap with each other.
    - Thus, the $\delta_i$ over each $D_0$ are not independent of one another!
    - $\bar{\delta}$ we obtained from these $\delta_i$ cannot be regarded as drawn from the full distribution $D$.
- Solution)
  1. k-fold method
     - How?)
       - Each example from $D_0$ is used exactly once in a test set, and $k - 1$ times in a training set.
       - The method we used in our [paired test](#56-comparing-learning-algorithms).
     - Advantage)
       - The test sets generated by k-fold cross validation are independent because each instance is included in only one test set.
     - Drawback)
       - The k-fold method is limited by the total number of examples, by the use of each example only once in a test set, and by our desire to use samples of size at least 30.
  2. Randomly choose a test set of at least 30 examples from $D_0$ and use the remaining examples for training, then repeat this process as many times as desired.
     - Advantage)
       - Can be repeated an indefinite number of times, to shrink the confidence interval to the desired width.
     - Drawback)
       - The test sets no longer qualify as being independently drawn with respect to the underlying instance distribution $D$.


<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)