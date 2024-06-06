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
  - d


#### 3.1.2.3)
$`|A_\epsilon^{(n)}| \le 2^{n(H(X)+\epsilon)}`$ where $`A`$ denotes the number of elements in the set $`A`$.
- pf.)
  - d


#### 3.1.2.4)
$`|A_\epsilon^{(n)}| \le (1-\epsilon)2^{n(H(X)-\epsilon)}`$ for sufficiently large $`n`$.
- pf.)
  - d





<br>

* [Back to Elements of Information Theory](../../main.md)