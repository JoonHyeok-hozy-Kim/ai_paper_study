* [Back to Statistics Main](../../main.md)

## 2.6 Moments and Moment-Generating Functions
#### Def. 2.6.1) Expected Value
Let $X$ be a discrete random variable with pf $p(x)$. Then the expected value of $X$, denoted by $E(X)$, is defined by
* $\mu = E(X) = \Sigma_x{xp(x)}$
  * provided $\Sigma_x{|x|p(x)} \lt \infty$

<br>

#### Def. 2.6.2) Expected Value for a Continuous Random Variable
The expected value of a continuous random variable $X$ with pdf $f(x)$ is defined by
* $\mu = E(X) = \int_{-\infty}^\infty xf(x)dx$
  * provided $\int_{-\infty}^\infty |x|f(x)dx \lt \infty$

<br>

#### Def. 2.6.3) Variance and Standard Deviation
The variance of a random variable $X$ is defined by 
* $\sigma^2 = Var(X) = E(X-\mu)^2$   

The squared root of variance, denoted by $\sigma$, is called the standard deviation. 

<br>

#### Theorem 2.6.1) Expectation of Function of a Random Variable
Let $g(X)$ be a function of $X$, then the expected value of $g(X)$ is
* $`E[g(X)] = \left \lbrace \begin{array}{ll} {\Sigma_xg(x)p(x)} & {if \space X \space is \space discrete} \\ {\int_{-\infty}^\infty{g(x)f(x)dx}} & {if \space X \space is \space continuous} \end{array} \right.`$ 





<br><br>

### [Exercises](./exercises.md)

<br><br>

* [Back to Statistics Main](../../main.md)