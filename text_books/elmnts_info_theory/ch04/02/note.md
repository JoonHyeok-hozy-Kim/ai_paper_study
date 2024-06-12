* [Back to Elements of Information Theory](../../main.md)

# 4.2 Entropy Rate

### Concept) Entropy Rate (per Symbol)
- Def.)
  - The entropy of a stochastic process $`\{X_i\}`$ is defined by
    - $`\displaystyle H(\mathcal{X}) = \lim_{n\rightarrow\infty} \frac{H(X_1, X_2,\cdots, X_n)}{n}`$
      - when limit exists.
- e.g.)
  - Typewriter
    - Consider a typewriter that has $`m`$ equally likely output letters.
    - Then the typewriter can produce $`m^n`$ sequences of length $`n`$.
      - All of which are equally likely.
    - Hence, $`H(X_1, X_2, \cdots, X_n) = \log{m^n}`$
    - Therefore, the **entropy rate** is $`H(\mathcal{X}) = \log{m}`$ bits per symbol.
  - I.I.D.
    - Suppose $`X_1, X_2, \cdots \stackrel{i.i.d.}{\sim} p(x)`$.
    - Then, $`\displaystyle H(\mathcal{X}) = \lim_{n\rightarrow\infty}\frac{H(X_1, X_2, \cdots, X_n)}{n} = \lim_{n\rightarrow\infty}\frac{nH(X_1)}{n} = H(X_1)`$
  - Independent but Not Identically Distributed
    - $`\displaystyle H(X_1, X_2, \cdots, X_n) = \sum_{i=1}^n H(X_i)`$
      - cf.) Non-existing-limit case
        - A random binary sequence where
          - $`p_i = P(X_i=1) = \begin{cases}
            0.5 & \textrm{if } 2k \lt \log\log{i} \le 2k+1 \\
            0 & \textrm{if } 2k+1 \lt \log\log{i} \le 2k+2 \\
          \end{cases}`$
            - for $`k=0,1,2,\cdots`$
        - In this case, the average of $`H(X_i)`$ oscillates between 0 and 1.
        - Thus, $`H(\mathcal{X})`$ is not defined for this process.

<br>

### Concept) Conditional Entropy
- Def.)
  - $`\displaystyle H'(\mathcal{X}) = \lim_{n\rightarrow\infty} H(X_n|X_1, X_2,\cdots, X_{n-1})`$
    - when limit exists.

<br>

### Theorem 4.2.1) 
- Theorem)
  - For a [stationary](../01/note.md#concept-stationary) stochastic process, 
    1. the [entropy rate](#concept-entropy-rate-per-symbol) $`H(\mathcal{X})`$ and the [conditional entropy](#concept-conditional-entropy) $`H'(\mathcal{X})`$ exists.
    2. $`H(\mathcal{X}) = H'(\mathcal{X})`$
- pf.)
  - [Theorem 4.2.2](#theorem-422) shows that $`H'(\mathcal{X})`$ exists.
  - By the [chain rule of entropy](../../ch02/05/note.md#theorem-251-chain-rule-for-entropy),   
    $`\displaystyle\frac{H(X_1, X_2, \cdots, X_n)}{n} = \frac{1}{n} \sum_{i=1}^n H(X_i|X_1, \cdots, X_{{i-1}})`$
    - i.e.) The entropy rate is the time average of the conditional entropies.
  - Thus,   
    $`\begin{aligned}
        H(\mathcal{X}) &= \lim_{n\rightarrow\infty} \frac{H(X_1, X_2, \cdots, X_n)}{n} \\
        &= \lim_{n\rightarrow\infty} \frac{1}{n} \sum_{i=1}^n H(X_i|X_1, \cdots, X_{{i-1}}) \\
        &= \lim_{n\rightarrow\infty} H(X_n|X_1, \cdots, X_{n-1}) & \because \textrm{Theorem 4.2.3} \\
        &= H'(\mathcal{X})
    \end{aligned}`$

<br>

### Theorem 4.2.2) 
- Theorem)
  - For a [stationary](../01/note.md#concept-stationary) stochastic process, 
    1. $`H(X_n|X_1, X_2,\cdots, X_{n-1})`$ is non-increasing
    2. $`H(X_n|X_1, X_2,\cdots, X_{n-1})`$ has a limit $`H'(\mathcal{X})`$.
- pf.)
  - Consider that   
    $`\begin{aligned}
        H(X_{n+1}|X_1, X_2,\cdots, X_{n}) &\le H(X_{n+1}|X_2,\cdots, X_{n}) & \because \textrm{Conditioning reduces entropy.} \\
        &= H(X_{n}|X_1,\cdots, X_{n-1}) & \because \textrm{The process is stationary.}
    \end{aligned}`$
  - Thus,    
    $`H(X_{n}|X_1,\cdots, X_{n-1}) \le H(X_{n-1}|X_1,\cdots, X_{n-2}) \le \cdots \le H(X_2|X_1) \le H(X_1) `$.
  - Since $`H(X_{n}|X_1,\cdots, X_{n-1})`$ is a decreasing sequence of **nonnegative numbers**, it has a limit, $`H'(\mathcal{X})`$.


<br>

### Theorem 4.2.3) Cesaro mean
If $`\begin{cases} a_n\rightarrow a \\ b_n = \frac{1}{n}\sum_{i=1}^n a_i \end{cases}`$, then $`b_n \rightarrow a`$
- pf.)
  - Let $`\epsilon \gt 0`$.
  - Since $`a_n \rightarrow a`$,
    - $`\exists N(\epsilon) \le n \textrm{ such that } |a_n-a| \le \epsilon`$.
  - Hence, for all $`n \le N(\epsilon)`$,   
    $`\begin{aligned}
        |b_n - a| &= \left| \frac{1}{n}\sum_{i=1}^n a_i-a \right| = \left| \frac{1}{n}\sum_{i=1}^n (a_i-a) \right| \\
        &\le \frac{1}{n}\sum_{i=1}^n |a_i-a| \\
        &\le \frac{1}{n} \left( \sum_{i=1}^{N(\epsilon)} |a_i-a| + (n-N(\epsilon))\epsilon \right) \\
        &\le \frac{1}{n} \sum_{i=1}^{N(\epsilon)} |a_i-a| + \epsilon
    \end{aligned}`$
  - Since $`\displaystyle\lim_{n\rightarrow\infty} \sum_{i=1}^{N(\epsilon)} |a_i-a| + \epsilon = 0`$
    - $`b_n\rightarrow a`$ as $`n\rightarrow \infty`$

<br><br>

### Theorem 4.2.4) Entropy Rate of the Stationary Markov Chain
- Theorem)
  - Let 
    - $`\{X_i\}`$ be a **stationary Markov chain** with [stationary distribution](../01/note.md#concept-stationary-distribution) $`\mu`$ and [transition matrix](../01/note.md#concept-probability-transition-matrix) $`P`$.
    - $`X_1\sim\mu`$
  - Then the **entropy rate** is
    - $`\displaystyle H(\mathcal{X}) = -\sum_{ij}\mu_i P_{ij} \log P_{ij}`$
- pf.)
  - For a [stationary Markov chain](../01/note.md#concept-stationary-distribution), the **entropy rate** is given by    
    $`\begin{aligned}
      H(\mathcal{X}) = H'(\mathcal{X}) &= \lim H(X_n|X_1, \cdots, X_{n-1}) \\
      &=\lim H(X_n|X_{n-1}) \\ 
      &= H(X_2|X_1)
    \end{aligned}`$
    - where the **conditional entropy** is calculated using the given [stationary distribution](../01/note.md#concept-stationary-distribution).
  - Recall that the stationary distributioni $`\mu`$ is the solution of
    - $`\displaystyle \mu P = \mu \Leftrightarrow \mu_j = \sum_i\mu_i P_{ij}`$
  - Thus,   
    $`\begin{aligned}
        H(\mathcal{X}) = H(X_2|X_1) &= \sum_i \mu_i \left( \sum_j -P_{ij}\log{P_{ij}} \right) \\
        &= -\sum_{ij}\mu_i P_{ij} \log P_{ij} \\
    \end{aligned}`$

#### E.g.) Two-State Markov Chain
- Recall the previous [Two-State Markov Chain](../01/note.md#example-411) problem.
- Its entropy rate can be calculated as
  - $`\displaystyle H(\mathcal{X}) = H(X_2|X_1) = \frac{\beta}{\alpha+\beta}H(\alpha) + \frac{\alpha}{\alpha+\beta}H(\beta)`$


<br>

* [Back to Elements of Information Theory](../../main.md)