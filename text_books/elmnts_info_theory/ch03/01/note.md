* [Back to Elements of Information Theory](../../main.md)

# 3.1 Asymptotic Equipartition Property Theorem

### Concept) Weak Law of Numbers
- Def.)
  - For i.i.d. random variables, $`\displaystyle\frac{1}{n}\sum_{i=1}^n X_i \rightarrow EX`$

<br><br>

### Def.) Convergence of Random Variable
Given a sequence of random variables $`X_1, X_2, \cdots`$   
the sequence $`X_1, X_2, \cdots`$ **converges** to a random variable $`X`$:
1. In probability 
   - if $`\forall\epsilon \gt 0, \textrm{Pr}\{|X_n-X| \gt \epsilon\} \rightarrow 0`$
2. In mean square 
   - if $`E(X_n-X)^2\rightarrow 0`$
3. With probability $`1`$ 
   - if $`\displaystyle\textrm{Pr}\left\{\lim_{n\rightarrow\infty} X_n = X\right\} = 1`$

<br>

### Theorem 3.1.1) Asymptotic Equipartition Property Theorem (AEP)
If $`X_1, X_2, \cdots, `$ are i.i.d. $`\sim p(x)`$,    
then $`\displaystyle -\frac{1}{n}\log{p(X_1, X_2, \cdots, X_n)} \rightarrow H(X)`$
- pf.)
  - If $`X_i`$ is i.i.d., then $`\log{p(X_i)}`$ is i.i.d.
    - why?)
      - Functions of independent random variables are also independent random variables.
  - Thus, by the [weak law of large numbers](#concept-weak-law-of-numbers),   
    $`\begin{aligned}
        -\frac{1}{n}\log{p(X_1, X_2, \cdots, X_n)}  &= -\frac{1}{n}\sum_i\log p(X_i) \\
        &\rightarrow -E\log{p(X)} \textrm{ in probability} \\
        &= H(X)
    \end{aligned}`$
    - Recall that $`\displaystyle H(X) \equiv \sum_i p(X_i)\log\frac{1}{p(X_i)} = E_{X\sim p(X)}\left[\log\frac{1}{p(X)}\right] = -E_{X\sim p(X)}\left[\log p(X)\right]`$


<br>

### Concept) Typical Set
- Def.)
  - The **typical set** $`A_\epsilon^{(n)}`$ w.r.t. $`p(x)`$ is the set of sequences $`(x_1, x_2, \cdots, x_n)\in\mathcal{X}^n`$ with property
    - $`2^{-n(H(X)+\epsilon)} \le p(x_1, x_2, \cdots, x_n) \le 2^{-n(H(X)-\epsilon)}`$
- Meaning)
  - A set which the sample entropy is close to the true entropy.
  - Any property that is proved for the typical sequences will then be **true with high probability** and will determine the average behavior of a large sample.

<br>

### Theorem 3.1.2) Properties of the Typical Set
#### 3.1.2.1)
If $`(x_1, x_2, \cdots, x_n)\in A_\epsilon^{(n)}`$   
then $`H(X)-\epsilon \le -\frac{1}{n}\log{p(x_1, x_2, \cdots, x_n)} \le H(X)+\epsilon`$
- pf.)
  - By definition, $`2^{-n(H(X)+\epsilon)} \le p(x_1, x_2, \cdots, x_n) \le 2^{-n(H(X)-\epsilon)}`$.
  - Thus, $`-n(H(X)+\epsilon) \le \log{p(x_1, x_2, \cdots, x_n)} \le -n(H(X)-\epsilon)`$.
  - $`\therefore H(X)-\epsilon \le -\frac{1}{n}\log{p(x_1, x_2, \cdots, x_n)} \le H(X)+\epsilon`$.

#### 3.1.2.2)
$`\textrm{Pr}\left\{ A_\epsilon^{(n)} \right\} \gt 1-\epsilon`$ for sufficiently large $`n`$.
- pf.)
  - Let $`\textrm{Pr}\left\{ A_\epsilon^{(n)} \right\}`$ be the probability of the event $`(X_1, \cdots, X_n) \in A_\epsilon^{(n)}`$.
  - By the definition of the [typical set](#concept-typical-set),
    - $`\textrm{Pr}\left\{ A_\epsilon^{(n)} \right\} = \textrm{Pr}\left\{ H(X)-\epsilon \le -\frac{1}{n}\log{p(x_1, x_2, \cdots, x_n)} \le H(X)+\epsilon \right\}`$
  - From [Theorem 3.1.2.1](#3121), we can derive
    - $`\left| -\frac{1}{n}\log{p(x_1, x_2, \cdots, x_n)} - H(X) \right| \le \epsilon`$
  - Thus, $`\textrm{Pr}\left\{ A_\epsilon^{(n)} \right\} = \textrm{Pr}\left\{ \left| -\frac{1}{n}\log{p(x_1, x_2, \cdots, x_n)} - H(X) \right| \le \epsilon \right\}`$
  - Recall that by [AEP](#theorem-311-asymptotic-equipartition-property-theorem-aep),   
    $`\begin{aligned}
      n\rightarrow\infty 
      &\Rightarrow -\frac{1}{n} \log{p(X_1,\cdots,X_n)} \rightarrow H(X) \\
      &\Rightarrow \textrm{Pr}\left\{ A_\epsilon^{(n)} \right\}\rightarrow 1\\
    \end{aligned}`$.
  - Thus, $`\forall\delta\gt 0, \; \exists n_0 \in \mathbb{R} \textrm{ s.t. } \textrm{Pr}\left\{\left| -\frac{1}{n} \log{p(X_1,\cdots,X_n)} - H(X) \right| \lt \epsilon \right\} \gt 1-\delta`$
    - where $`n \ge n_0`$
  - Setting $`\delta = \epsilon`$, we get   
    $`\begin{aligned}
      \textrm{Pr}\left\{ A_\epsilon^{(n)} \right\} &= \textrm{Pr}\left\{ \left| -\frac{1}{n}\log{p(x_1, x_2, \cdots, x_n)} - H(X) \right| \le \epsilon \right\} \\
      &\gt 1-\epsilon
    \end{aligned}`$.


#### 3.1.2.3)
$`|A_\epsilon^{(n)}| \le 2^{n(H(X)+\epsilon)}`$ where $`|A|`$ denotes the number of elements in the set $`A`$.
- pf.)   
  - Put $`p(\mathbf{x}) \equiv p(x_1, x_2, \cdots, x_n)`$
  - We can denote $`\displaystyle\textrm{Pr}\left\{ A_\epsilon^{(n)} \right\} = \sum_{\mathbf{x}\in A_\epsilon^{(n)}} p(\mathbf{x})`$.
  - Then   
    $`\begin{aligned}
      1 &= \sum_{\mathbf{x}\in\mathcal{X}^n} p(\mathbf{x}) \\
      &\ge \sum_{\mathbf{x}\in A_\epsilon^{(n)}} p(\mathbf{x}) & \because A_\epsilon^{(n)} \subset \mathcal{X}^n \\
      &\ge \sum_{\mathbf{x}\in A_\epsilon^{(n)}} 2^{-n(H(X)+\epsilon)} & \because AEP \\
      &= 2^{-n(H(X)+\epsilon)} |A_\epsilon^{(n)}|
    \end{aligned}`$
  - Thus,  
    $`|A_\epsilon^{(n)}| \le 2^{n(H(X)+\epsilon)}`$

#### 3.1.2.4)
$`|A_\epsilon^{(n)}| \le (1-\epsilon)2^{n(H(X)-\epsilon)}`$ for sufficiently large $`n`$.
- pf.)
  - By [Theorem 3.1.2.2](#3122), $`1-\epsilon \lt \textrm{Pr}\left\{ A_\epsilon^{(n)} \right\}`$ for sufficiently large $`n`$.
  - Recall that $`\displaystyle\textrm{Pr}\left\{ A_\epsilon^{(n)} \right\} = \sum_{\mathbf{x}\in A_\epsilon^{(n)}} p(\mathbf{x})`$ in [Theorem 3.1.2.3](#3123).
  - Considering the definition of [typical set](#concept-typical-set) that $`p(\mathbf{x}) \le 2^{-n(H(X)-\epsilon)}`$, we can get   
    $`\begin{aligned}
      1-\epsilon \lt \textrm{Pr}\left\{ A_\epsilon^{(n)} \right\} &= \sum_{\mathbf{x}\in A_\epsilon^{(n)}} p(\mathbf{x}) \\
      &\le \sum_{\mathbf{x}\in A_\epsilon^{(n)}} 2^{-n(H(X)-\epsilon)} \\
      &= 2^{-n(H(X)-\epsilon)} |A_\epsilon^{(n)}|
    \end{aligned}`$
  - $`\therefore |A_\epsilon^{(n)}| \ge (1-\epsilon) 2^{n(H(X)-\epsilon)}`$





<br>

* [Back to Elements of Information Theory](../../main.md)