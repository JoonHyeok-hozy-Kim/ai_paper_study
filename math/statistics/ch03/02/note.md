* [Back to Statistics Main](../../main.md)

## 3.2 Special Distribution Functions
### 3.2.1 The Binomial Probability Distribution
#### Concept) Bernoulli Probability Distribution
- Def.)
  - $`p(x) = P(X=x) = \left \lbrace \begin{array}{cc} p^x(1-p)^{1-x}, & x=0,1 \\ 0, & otherwise \end{array} \right.`$
- Prop.)
  - Characterized by the single parameter $p$.
  - $E[X] = p$
  - $Var[X] = p(1-p)$
  - $M_X(t) = pe^t+(1-p)$

<br>

#### Def.) Binomial Experiment
A binomial experiment is one that has the following properties:
1. The experiment consists of $n$ identical trials.
2. Each trial results in one of the two outcomes, called success $S$ and failure $F$.
3. The probability of success on a single trial is equal to $p$ and remains the same from trial to trial. The probability of failure is $1-p=q$.
4. The outcomes of the trials are independent.
5. The random variable $X$ is the number of successes in $n$ trials.
   - cf.) $x$ successes in $n$ trials
     - $`{}_nC_x=\frac{n!}{x!(n-x)!}`$

<br>

#### Concept) Binomial Probability Distribution
- Def.)
  - A random variable $X$ is said to have binomial probability distribution with parameters $(n,p)$ if and only if
    - $`P(X=x)=p(x)={}_nC_xp^xq^{n-x}=\left\lbrace \begin{array}{cc} \frac{n!}{x!(n-x)!}p^xq^{n-x}, & x=0,1,2,\dots,n, \space 0 \le p \le 1, \space q=1-p \\ 0, & otherwise \end{array} \right.`$
- Notation)
  - The cumulative probability
    - $B(x,n,p) = \Sigma_{i=0}^x b(i,n,p)$
    - Consider that $n$ and $p$ are independent.
- Prop.)
  - $\Sigma_{i=0}^x \space {}_nC_x p^xq^{n-x}=1=1$
    - pf.)   
      - Consider that $(p+q)^n=\Sigma_{i=0}^x \space {}_nC_x p^xq^{n-x}$
      - Also, $p+q=1$.
  - $E(X)=\mu=np$
  - $Var(X)=\sigma^2=np(1-p)$
  - $M_X(t) = \left[ pe^t + (1-p) \right]^n$


<br><br>

### 3.2.2 Poisson Probability Distribution
- Def.)
  - A discrete random variable $X$ is said to follow the Poisson probability distribution with parameter $\lambda \gt 0$, denoted by $Poisson(\lambda)$, if
    - $P(X=x) = f(x, \lambda) = f(x) = \frac{e^{-\lambda} \lambda^x}{x!}, x=0,1,2, \cdots$
- Props.)
  - $E(X) = \lambda$
  - $Var(X) = \lambda$
  - $M_X(t) = e^{\lambda(e^t-1)}$
    - Refer to the Maclaurin's expansion, $e^\lambda = \Sigma_{i=0}^\infty (\lambda^i / i!)$
- When to use?)
  - In rare events!
  - Refer to the [Theorem 3.2.3](#theorem-323-poisson-approximation-to-the-binomial-probability-distribution) for this issue.

<br>

#### Theorem 3.2.3) Poisson Approximation to the Binomial Probability Distribution
If $X \sim B(n, p)$, a binomial random variable, then for each value $x=0,1,2, \cdots$ and as $p \rightarrow 0, n \rightarrow \infty$ with $np = \lambda$ constant,
- $\lim_{n \rightarrow \infty} {}_nC_x p^x(1-p)^{n-x}=\frac{e^{-\lambda} \lambda^x}{x!}$   

Thus, we use Poisson probability distribution in rare events.
- When $p$ is small and $n$ is large
  - More precisely...
    - $p \le 0.1$ and $n \ge 40$
    - $np \lt 5$

<br><br>

### 3.2.3 Uniform Probability Distribution
- Def.)
  - A random variable $X$ is said to have a uniform probability distribution on $(a, b)$, denoted by $U(a, b)$, if the density function of $X$ is given by
    - $`f(x)=\left\lbrace \begin{array}{cc} \frac{1}{b-a}, & a \le X \le b \\0, & otherwise. \end{array} \right.`$
- Props.)
  - $E(X) = \frac{a+b}{2}$
  - $Var(X) = \frac{(b-a)^2}{12}$
  - $M_X(t) = \left\lbrace \begin{array}{cc} \frac{e^{tb}-e^{ta}}{t(b-a)}, & t \ne 0 \\ 1, & t=0 \end{array} \right.$
- When to use?)
  - Useful as a “first guess” if no other information about a random variable $X$ is known, other than that it is between $a$ and $b$ ($a \le X \le b$).

![](images/002.png)

<br><br>

### 3.2.4 Normal Probability Distribution
- Def.)
  - A random variable $X$ is said to have a normal probability distribution with parameters $\mu$ and $\sigma^2$, if it has a probability density function given by
    - $f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$
      - where $-\infty \lt x, \mu \lt \infty$ and $\sigma \gt 0$.
    - $X \sim N(\mu, \sigma^2)$
  - Concept) Standard Normal Random Variable
    - $\frac{X-\mu}{\sigma} = Z \sim N(0, 1)$
- Prop.)
  - $E(X) = \mu$
  - $Var(X) = \sigma^2$
  - $M_X(t) = e^{t\mu + \frac{1}{2}t^2\sigma^2}$
- When to use?)
  - Simply...
    1. The data can be capped with a bell-shaped curve.
    2. If the stem-and-leaf diagram is fairly symmetrical with respect to its center.
  - In practice...
    - When a large number of small effects are present and acting additively.
      - Still, additional visualization is desirable.
        - e.g) histogram, box-plot, [QQ plot](#concept-qq-plot), etc.

<br>

#### Concept) QQ plot (A Quantile Quantile)
- Def.)
  - A scatterplot with the quantiles of the scores on the horizontal axis and the expected normal scores on the vertical axis. 
  -  The expected normal scores are calculated by taking the $z$-scores of $(r_i−0.5)/n$, where $r_i$ is the rank $i$-th observation in increasing order.
- How to construct)
  - First, we sort the data in an ascending order. 
    - If the plot of these scores against the expected normal scores is a straight line, then the data can be considered normal. 
  - Any curvature of the points indicates departures from normality.

<br>

#### Concept) Log-Normal Distribution
- A variable might be modeled as log-normal if it can be thought of as the **multiplicative** effect of many small independent factors.
  - Recall that **additive** was the normal distribution.

- Def.)   

![](images/003.png)

- When to use?)
  - When the domain of the variate, $X$, is greater than zero and its histogram is markedly skewed.
  - For $Y \sim N(\mu, \sigma^2)$, $\exp{(Y)}$ has a log-normal distribution.


<br><br>

### 3.2.5 Gamma Probability Distribution

<br><br>

### [Exercises](./exercises.md)

<br><br>

* [Back to Statistics Main](../../main.md)