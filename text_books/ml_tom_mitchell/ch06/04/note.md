* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 6.4 Maximum Likelihood and Least-Squared Error Hypothesis

#### Prop.) Bayesian Justification for Least-Squared Error Hypothesis
Under certain assumptions, any learning algorithm that minimizes the squared error between the output hypothesis predictions and the training data will output a maximum likelihood hypothesis.

- Problem Setting)
  - $`X`$ : the instance space, where each instance $`x \in X`$
  - $`f`$ : the unknown target function, where $`f : X \rightarrow \mathbb{R}`$
  - $`H`$ : the hypothesis space defined over $`X`$, where each hypothesis $`h \in H`$
    - $`h : X \rightarrow \mathbb{R}`$
  - $`L`$ : the learner that wants to learn $`f`$ drawn from $H$.
  - The set of $m$ training examples are provided in a paired form of $`\langle x_i, d_i \rangle`$.
    - $`x_i \in X`$
    - $`d_i = f(x_i) + e_i`$
      - Assume that $`e_i \sim N(0, \sigma^2)`$ : Normally distributed.
        - i.e.) We should assume that $`e_i`$ is independently and identically distributed.
      - Since $`e_i`$ is Normally distributed, it is **continuous**.
        - Thus, we should use the concept of **probability density**.
          - Def.) Probability Density Function
            - $`\displaystyle p(x_0) \equiv \lim_{\epsilon \rightarrow 0} \frac{1}{\epsilon} P(x_0 \le x \lt x_0 + \epsilon)`$
        - Since $`e_i \sim N(0, \sigma^2)`$, 
          - $`d_i = f(x_i) + e_i \sim N(f(x_i), \sigma^2)`$
- Maximum Likelihood Hypothesis)
  - Derivation)
    - Recall that $`h_{ML} = \arg\max_{h \in H} P(D|h)`$.
    - In our problem, 
      - $`d_i = f(x_i) + e_i`$ 
      - $`d_i \in D`$
      - $`e_i \sim N(0, \sigma^2)`$.
    - Thus,    
      $`\begin{array}{lll} h_{ML} & = \arg\max_{h \in H} p(D|h) & \\ 
      & = \displaystyle\arg\max_{h \in H} \prod_{i=1}^m p(d_i|h) & \\ 
      & = \displaystyle\arg\max_{h \in H} \prod_{i=1}^m \frac{1}{\sqrt 2 \pi \sigma^2} e^{-\frac{1}{2\sigma^2} (d_i-f(x_i))^2} & \because d_i \sim N(f(x_i), \sigma^2) \end{array}`$
    - Since the given $`\ln{p}`$ is monotonic function of $p$, let's optimize $`\ln{p}`$ instead.   
      $`\begin{array}{lll} h_{ML} & = \arg\max_{h \in H} \ln{p(D|h)} & \\ & = \displaystyle\arg\max_{h \in H} \sum_{i=1}^m \ln{\frac{1}{\sqrt 2 \pi \sigma^2} e^{-\frac{1}{2\sigma^2} (d_i-f(x_i))^2}} &  \end{array}`$
    - Discarding the constant,   
      $`\begin{array}{lll} h_{ML} & = \displaystyle\arg\max_{h \in H} \sum_{i=1}^m -\frac{1}{2\sigma^2} (d_i-f(x_i))^2 & \\ & = \displaystyle\arg\max_{h \in H} \sum_{i=1}^m -(d_i-f(x_i))^2  \end{array}`$
    - By switching the sign,   
      - $`\displaystyle h_{ML} = \arg\min_{h \in H} \sum_{i=1}^m (d_i-f(x_i))^2`$
  - Result)
    - The ML Hypothesis(LHS) we derived is the least squared method(RHS)!
      - $`\displaystyle h_{ML} = \arg\min_{h \in H} \sum_{i=1}^m (d_i-f(x_i))^2`$
  - Analysis)
    - Remind the followings.
      - This is the ML Hypothesis, not the MAP hypothesis.
        - Recall that MAP Hypothesis is identical to ML Hypothesis when [the uniform prior probability over the hypotheses is assumed](../03/note.md#desc).
      - This is true only if we assume that $e_i$ is iid and follows the Normal distribution.
        - Is it valid assumption?)
          - Maybe yes.
            - why?)
              - By the [Central Limit Theorem](../../ch05/03/note.md#concept-the-central-limit-theorem), the sum of a sufficiently large number of independent, identically distributed random variables itself obeys a Normal distribution, regardless of the distributions of the individual variables. 
    - Limit)
      - The above analysis considers noise only in the target value of the training example and does not consider noise in the attributes describing the instances themselves.
        - e.g.) Consider a problem that predicts the **weight** of someone based on that person's **age** and **height**.
          - Under the above analysis, we assume the noise in **weight**.
          - However, we do not assume the noise in **age** and **height**!











<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)