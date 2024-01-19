* [Back to Statistics Main](../../main.md)

# 4.2 Sampling Distributions Associated with Normal Populations

### Concepts)
|Concept|Def. & Desc.|
|:-|:-|
|Sample|- A set of observable random variables $X_1,\cdots,X_n$<br>- The number $n$ is called the **sample size**.|
|Identical Distribution|The random variables $X_1,\cdots,X_n$ are identically distributed if every $X_i$ has the same probability distribution.|
|Random Sample|a set of n **independent and identically distributed (iid)** observable random variables $X_1,\cdots,X_n$|
|Sample Statistic|- A function $T$ of observable random variables $X_1,\cdots,X_n$ that does not depend on any unknown parameters <br>- e.g.) $\bar{X}=\frac{1}{n}\Sigma_{i=1}^n X_i$ : the sample mean|
|Sampling Distribution|<br>- The probability distribution of a **sample statistic**<br>- It provides the link between probability theory and statistical inference.<br>- The sampling distribution of a statistic provides a theoretical model of the relative frequency histogram for the likely values of the statistic that one would observe through repeated sampling.|

<br><br>

### Theorem 4.1.1)
- Let $X_1,\cdots,X_n$ be a random sample of size $n$ from a population with mean $\mu$ and variance $\sigma^2$.
  - Then $E(\bar{X}) = \mu$ and $Var(\bar{X})=\frac{\sigma^2}{n}$
- $\sigma_{\bar{X}}=\frac{\sigma}{\sqrt{n}}$ : standard error of the mean

<br><Br>

### Theorem 4.1.2) Finite Population Case
- Let $\lbrace c_1, \cdots, c_N\rbrace$ be a finite population of size $N$
  - where $\mu = \frac{1}{N}\Sigma c_i$ and $\sigma^2 = \frac{1}{N}\Sigma (c_i-\mu)^2$
- If $X_1,\cdots,X_n$ is a sample of size $n$ from the population $\lbrace c_1, \cdots, c_N\rbrace$,
  - then $E(\bar{X}) = \mu$ and $Var(\bar{X})=\frac{\sigma^2}{n}\left(\frac{N-n}{N-1}\right)$
    - cd.) $\frac{N-n}{N-1}$ : the finite population correction factor
      - Close to 1 unless the sample amounts to a significant portion of the population
      - Not used in the derivation of sampling distribution, unless it is absolutely necessary

<br><br>

### Theorem 4.2.1)
- Let  
  - $X_i \sim N(\mu_i, \sigma_i^2) \textrm{ for } i=1,2,\cdots,n$
    - i.e.) $n$ independent random variables
  - $`Y=\Sigma_{i=1}^n{a_iX_i}, \exists a_1, \;\cdots, a_n \in \mathbb{R}`$
- Then $Y \sim N(\mu_Y, \sigma_Y^2)$
  - where $\mu_Y=\Sigma_{i=1}^n{a_i\mu_i}$ and $\sigma_Y^2=\Sigma_{i=1}^n{a_i^2\sigma_i^2}$



<br><br>

### [Exercises](./exercises.md)

<br><br>

* [Back to Statistics Main](../../main.md)