* [Back to Elements of Information Theory](../../main.md)

# 3.3 High-Probability Sets and the Typical Set
- Objective)
  - From the [definition of the typical set](../01/note.md#concept-typical-set), it is clear that $`A_\epsilon^{(n)}`$ is fairly small set that contains most of the probability.
  - But it is not clear whether it is the **smallest** such set.
  - To prove that *the typical set has essentially the same number of elements as the smallest set*, we
    1. Define the [High-Probability Set](#def-high-probability-set).
    2. Get the size of the smallest [High-Probability Set](#def-high-probability-set).
    3. Show that the size of the [typical set](../01/note.md#concept-typical-set) is almost the size of the smallest [High-Probability Set](#def-high-probability-set).

<br>

### Def.) High-Probability Set
For each $`n=1,2, \cdots`$, let $`B_\delta^{(n)} \subset \mathcal{X}^n`$ be the smallest set with $`\textrm{Pr}\left\{B_\delta^{(n)}\right\} \ge 1-\delta`$.


<br><br>

### Theorem 3.3.1) The Size of the Smallest High-Probability Set 
- Theorem)
  - Let 
    - $`X_1, X_2, \cdots, X_n \stackrel{i.i.d.}{\sim} p(x)`$
    - $`\displaystyle\delta\lt\frac{1}{2}`$ 
    - $`\delta'\gt 0`$,   
  - If $`\textrm{Pr}\left\{B_\delta^{(n)}\right\} \ge 1-\delta`$ 
  - then $`\displaystyle\frac{1}{n}\log|B_\delta^{(n)}| \gt H-\delta'`$ for sufficiently large $`n`$ 
- pf.)
  - Consider the following.
    - For 
      - $`0 \le a,b \le 1`$
      - $`P(A) \gt 1-a`$
      - $`P(B) \gt 1-b`$
    - $`P(A\cap B) \gt 1-a-b`$.
      - Why?)
        - Put $`P(A\cap B) = p \in [0,1]`$.
        - Then $`P(A\cup B) = P(A) + P(B) - P(A\cap B) \gt 1-a + 1-b - p = 2-a-b-p`$
        - Thus, $`P(A\cup B)^c = 1-P(A\cup B) = 1-(2-a-b-p) = a+b+p-1`$.
        - Consider that $`0 \lt P(A\cup B)^c \lt 1`$.
        - Therefore, $`0 \lt a+b+p-1 \lt 1 \Leftrightarrow 1-a-b \lt p = P(A\cap B) \lt 2-a-b`$.
  - Also, [recall](../01/note.md#3122) that $`\textrm{Pr}\left\{ A_\epsilon^{(n)}\right\} \ge 1-\epsilon`$.
  - Thus, $`\textrm{Pr}\left\{ A_\epsilon^{(n)} \cap B_\delta^{(n)} \right\} \ge 1-\epsilon-\delta`$.
  - Hence,   
    $`\begin{aligned}
        1-\epsilon-\delta &\le \textrm{Pr}\left\{ A_\epsilon^{(n)} \cap B_\delta^{(n)} \right\} \\
        &= \sum_{x^n \in \left\{ A_\epsilon^{(n)} \cap B_\delta^{(n)} \right\}} p(x^n) \\
        &\le \sum_{x^n \in \left\{ A_\epsilon^{(n)} \cap B_\delta^{(n)} \right\}} 2^{-n(H-\epsilon)} & \because \textrm{By def. of Typical Set and } A_\epsilon^{(n)} \cap B_\delta^{(n)} \subseteq A_\epsilon^{(n)} \\
        &= \left| A_\epsilon^{(n)} \cap B_\delta^{(n)} \right| \cdot 2^{-n(H-\epsilon)} & \because n, H, \epsilon \textrm{ are independent of } x^n \\
        &\le \left| B_\delta^{(n)} \right| \cdot 2^{-n(H-\epsilon)} & \because A_\epsilon^{(n)} \cap B_\delta^{(n)} \subseteq B_\delta^{(n)} \\
    \end{aligned}`$
  - Taking $`\log`$ on both sides, we get   
    $`\begin{aligned}
      \log(1-\epsilon-\delta) \le \log \left| B_\delta^{(n)} \right| - n(H-\epsilon) &\Rightarrow \log \left| B_\delta^{(n)} \right| \ge n(H-\epsilon) + \log(1-\epsilon-\delta) \\
      &\Rightarrow \frac{1}{n} \log \left| B_\delta^{(n)} \right| \ge H - \epsilon + \frac{\log(1-\epsilon-\delta)}{n}
    \end{aligned}`$.
  - Putting $`\displaystyle \delta' \equiv \epsilon - \frac{\log(1-\epsilon-\delta)}{n}`$, 
    - we get $`\displaystyle\frac{1}{n}\log|B_\delta^{(n)}| \gt H-\delta'`$.

<br>

### Def.) Equal to the First Order in the Exponent
$`a_n \doteq b_n \Leftrightarrow \displaystyle\lim_{n\rightarrow\infty}\frac{1}{n}\log\frac{a_n}{b_n} = 0`$

<br>

### Prop.) Size Comparison between the Typical Set and the Smallest High-Probability Set
- Recall that 
  - by [Theorem 3.1.2.3](../01/note.md#3123), $`\left|A_\epsilon^{(n)} \right| \le 2^{n(H(X)+\epsilon)}`$
  - by [Theorem 3.3.1](#theorem-331), $`\left| B_\delta^{(n)} \right| \ge 2^{n(H-\epsilon)} \cdot (1-\epsilon-\delta)`$
- The we may assume that the typical set $`A_\epsilon^{(n)}`$ is about the same size as the smallest high-probability set $`B_\delta^{(n)}`$.
- Using the $`\doteq`$ [above](#def-equal-to-the-first-order-in-the-exponent), we may denote as
  - $`\left| B_\delta^{(n)} \right| \doteq \left|A_\epsilon^{(n)} \right| \doteq 2^{nH}`$
    - e.g.)
      - Suppose $`X_1, X_2, \cdots, X_n \sim \textrm{Bernoulli}(0.9)`$.
      - Then, $`A_\epsilon^{(n)}`$ includes the sequences in which the proportion of $`1`$s is close to $`0.9`$.
        - $`A_\epsilon^{(n)}`$ does not include a sequence of all $`1`$s.
      - Meanwhile, $`B_\delta^{(n)}`$ includes all the most probable sequences.
        - Thus, it includes the sequence of all $`1`$s.
      - [Theorem 3.3.1](#theorem-331) implies that 
        - $`A_\epsilon^{(n)}`$ and $`B_\delta^{(n)}`$ both contains the sequences that have about $`90\% \; 1`$s
        - The two sets are almost equal in size.



<br>

* [Back to Elements of Information Theory](../../main.md)