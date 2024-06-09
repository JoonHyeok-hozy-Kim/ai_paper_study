* [Back to Elements of Information Theory](../../main.md)

# 3.2 Consequences of the AEP : Data Compression

### Theorem 3.2.1) 
- Theorem)
  - Let 
    - $`X^n \stackrel{i.i.d}{\sim} p(x)`$ 
      - where $`p(x)`$ is a probability mass function 
    - $`\epsilon \gt 0`$.   
  - Then there exists 
    - a code that maps sequences $`x^n`$ of length $`n`$ into binary strings such that the mapping is one-to-one
    - $`\displaystyle E\left[ \frac{l(X^n)}{n} \right] \le H(X) + \epsilon`$ for sufficiently large $`n`$.
      - where $`l(X^n)`$ is the length of the codeword corresponding to $`X^n`$ 
  - Thus, we can represent sequences $`X^n`$ using $`nH(X)`$ bits on average.
- pf.)
  - Recall that we divided all sequences of $`\mathcal{X}^n`$ into two sets
    - $`A_\epsilon^{(n)}`$ : the typical set
    - $`{A_\epsilon^{(n)}}^c`$ : the complement of the typical set
  - Let $`x^n`$ denote a sequence $`x_1, x_2, \cdots, x_n`$.
  - Then, we can get the upper bound of the length of codewords as
    1. $`x^n \in A_\epsilon^{(n)}`$
       - [Recall](../01/note.md#3123) that there are $`\le 2^{n(H+\epsilon)}`$ sequences in $`A_\epsilon^{(n)}`$.
       - Thus, $`x^n \in A_\epsilon^{(n)}`$ can be indexed with $`n(H+\epsilon)`$ bits.
       - Since $`n(H+\epsilon)`$ may not be an integer, we may denote the length as
         - $`l(x^n) \le n(H+\epsilon)+1, x^n \in A_\epsilon^{(n)}`$
    2. $`x^n \in {A_\epsilon^{(n)}}^c`$
       - Since there are $`|\mathcal{X}|`$ number of values in $`\mathcal{X}`$, the sequence $`\mathcal{X}^n`$ can be index with $`n\log{|\mathcal{X}|}`$ bits.
       - Thus, it can be the upper bound for the length of the codewords $`x^n \in {A_\epsilon^{(n)}}^c`$.
       - Again, Since $`n\log{|\mathcal{X}|}`$ may not be an integer, we may denote the length as 
         - $`l(x^n) \le n\log{|\mathcal{X}|} + 1, x^n \in {A_\epsilon^{(n)}}^c`$.
  - Adding a prefix of $`1`$ bit that indexes whether a sequence $`x^n`$ is in $`A_\epsilon^{(n)}`$ or $`{A_\epsilon^{(n)}}^c`$   
    $`l(x^n) \le \begin{cases}
        n(H+\epsilon)+2 & x^n \in A_\epsilon^{(n)} \\
        n\log{|\mathcal{X}|} + 2 & x^n \in {A_\epsilon^{(n)}}^c
    \end{cases} \; \cdots (1)`$
  - [Recall](../01/note.md#3122) that $`\textrm{Pr}\left\{ A_\epsilon^{(n)} \right\} \ge 1-\epsilon`$.
    - Then,   
      $`\begin{aligned}
        \textrm{Pr}\left\{ {A_\epsilon^{(n)}}^c \right\} &= 1- \textrm{Pr}\left\{ A_\epsilon^{(n)} \right\} \\
        &\le 1 - (1-\epsilon) \\
        &= \epsilon
      \end{aligned} \; \cdots (2)`$.
  - We can get the expected length of the codeword as   
    $`\begin{aligned}
        E\left[ l(X^n) \right] &= \sum_{x^n} p(x^n)l(x^n) \\
        &= \sum_{x^n \in A_\epsilon^{(n)}} p(x^n)l(x^n) + \sum_{x^n \in {A_\epsilon^{(n)}}^c} p(x^n)l(x^n) \\
        &\le \sum_{x^n \in A_\epsilon^{(n)}} p(x^n) (n(H+\epsilon)+2) + \sum_{x^n \in {A_\epsilon^{(n)}}^c} p(x^n)(n\log{|\mathcal{X}|} + 2) & \because (1) \\
        &= \textrm{Pr}\left\{ A_\epsilon^{(n)} \right\} (n(H+\epsilon)+2) + \textrm{Pr}\left\{ {A_\epsilon^{(n)}}^c \right\}(n\log{|\mathcal{X}|} + 2) \\
        &\le (1-\epsilon) (n(H+\epsilon)+2) + \epsilon (n\log{|\mathcal{X}|} + 2) & \because (2)\\
        &= (1-\epsilon)n(H+\epsilon) + \epsilon n\log{|\mathcal{X}|} + 2 \\
        &\le n(H+\epsilon) + \epsilon n\log{|\mathcal{X}|} + 2 \\
        &\stackrel{\epsilon' \equiv \epsilon + \epsilon\log{|\mathcal{X}|}+\frac{2}{n}}{=} n(H+\epsilon')
    \end{aligned}`$







<br>

* [Back to Elements of Information Theory](../../main.md)