* [Back to Deep Learning MIT](../../main.md)

# 5.4 Estimators, Bias and Variance

## 5.4.1 Point Estimation
- Desc.)
  - Point estimation is the attempt to provide the **single “best” prediction** of some quantity of interest.
- Def.)
  - For
    - $`\{ x^{(1)}, \cdots, x^{(m)} \}`$ : a set of $`m`$ iid data points.
    - $`\theta`$ : a target parameter of the estimation
      - Assume that $`\theta`$ is fixed but unknown.
    - $`\hat{\theta}`$ : a point estimate of $`\theta`$
  - A **point estimator** or **statistic** is any function of the data:
    - $`\hat{\theta}_m = g(x^{(1)}, \cdots, x^{(m)})`$
      - where
        - $`g`$ does not have to return a value that is close to true $`\theta`$
          - which gives great flexibility to the designer of the model.
- Prop.)
  - $`\hat{\theta}`$ is a random variable.
    - why?)
      - The data $`\{ x^{(1)}, \cdots, x^{(m)} \}`$ is drawn from a random process, 
      - Thus, any function of the data is random.
  - Point estimation can also refer to [function estimation](#concept-function-estimation).

<br>

### Concept) Function Estimation
- Def.)
  - The estimation of the relationship between input and target variables.
- How?)
  - Suppose we are trying to predict a variable $`y`$ given an input vector $`x`$.
  - Assume that $`\exists f: X\rightarrow Y`$
    - where $`f(x)`$ describes the approximate relationship between $`y`$ and $`x`$.
  - Further assume $`y = f(x) + \epsilon`$
    - where $`\epsilon`$ stands for the part of $`y`$ that is not predictable from $`x`$.
  - We want to estimate a model $`\hat{f}`$ that approximates $`f`$.
    - where $`\hat{f}`$ is consisted with a parameter $`\theta`$.

<br><br>

## 5.4.2 Bias
### Concept) Bias
- Def.)
  - $`\textrm{bias}(\hat{\theta}_m) = \mathbb{E}(\hat{\theta}_m) - \theta`$
    - where
      - the expectation is over the data (i.e. samples from a random variable)
      - $`\theta`$ : the true underlying value of $`\theta`$
- Props.)
  - If $`\textrm{bias}(\hat{\theta}_m) = 0`$ then $`\hat{\theta}_m`$ is said to be **unbiased**.
    - Then $`\mathbb{E}(\hat{\theta}_m) = \theta`$.
  - If $`\displaystyle\lim_{m\rightarrow\infty}\textrm{bias}(\hat{\theta}_m) = 0`$ then $`\hat{\theta}_m`$ is said to be **asymptotically unbiased**.
    - Then $`\displaystyle\lim_{m\rightarrow\infty}\mathbb{E}(\hat{\theta}_m) = \theta`$.
- e.g.)
  - Bernoulli Distribution Estimator for the Mean
    - Settings)
      - $`\{ x^{(1)}, \cdots, x^{(m)} \}`$ : a set of $`m`$ iid data points according to a Bernoulli distribution with mean $`\theta`$:
        - $`P(x^{(i)};\theta) = \theta^{x^{(i)}} (1-\theta)^{(1-x^{(i)})}`$
    - Estimation)
      - Consider $`\hat{\theta}_m`$ which is an estimator for $`\theta`$ such that
        - $`\displaystyle \hat{\theta}_m = \frac{1}{m} \sum_{i=1}^m{x^{(i)}}`$.
      - We can calculate its bias as below.   
        $`\begin{aligned}
            \textrm{bias}(\hat{\theta}_m) &= \mathbb{E} \left[ \hat{\theta}_m \right] - \theta \\
            &= \mathbb{E} \left[\frac{1}{m} \sum_{i=1}^m{x^{(i)}}\right] - \theta \\
            &= \frac{1}{m}\sum_{i=1}^m \left(\mathbb{E} \left[ x^{(i)}\right]\right) - \theta \\
            &= \frac{1}{m}\sum_{i=1}^m  \left(\sum_{x^{(i)}=0}^1 {\theta^{x^{(i)}} (1-\theta)^{(1-x^{(i)})}}\right) - \theta \\
            &= \frac{1}{m}\sum_{i=1}^m\theta - \theta \\
            &= 0 \\
        \end{aligned}`$
      - Therefore $`\hat{\theta}_m`$ is an unbiased estimator.
  - Gaussian Distribution Estimator for the Mean
    - Settings)
      - $`\{ x^{(1)}, \cdots, x^{(m)} \}`$ : a set of $`m`$ iid data points according to a Gaussian distribution with mean $`\mu`$ and variance $`\sigma^2`$:
        - $`p(x^{(i)}) = \mathcal{N}(x^{(i)}; \mu,\sigma^2)`$
          - where $`i\in\{1,2,\cdots, m\}`$
          - i.e.) $`\displaystyle p(x^{(i)}; \mu,\sigma^2) = \frac{1}{\sqrt{2\pi\sigma^2}}\exp\left(-\frac{(x^{(i)}-\mu)^2}{2\sigma^2}\right)`$
    - Estimation)
      - Consider $`\hat{\mu}_m`$ which is an estimator for $`\mu`$ such that
        - $`\displaystyle \hat{\mu}_m = \frac{1}{m} \sum_{i=1}^m{x^{(i)}}`$.
      - We can calculate its bias as below.   
        $`\begin{aligned}
            \textrm{bias}(\hat{\mu}_m) &= \mathbb{E} \left[ \hat{\mu}_m \right] - \mu \\
            &= \mathbb{E}\left[ \frac{1}{m} \sum_{i=1}^m{x^{(i)}} \right] - \mu \\
            &= \frac{1}{m} \sum_{i=1}^m \mathbb{E}\left[ x^{(i)} \right] - \mu \\
            &= \frac{1}{m} \sum_{i=1}^m \int x p(x) dx - \mu \\
            &= \frac{1}{m} \sum_{i=1}^m \mu - \mu \\
            &= 0 \\
        \end{aligned}`$
      - Thus, we find that the sample mean is an unbiased estimator of Gaussian mean parameter.
  - Gaussian Distribution Estimator for the Variance
    - Settings)
      - Consider the following two estimators.
        1. $`\displaystyle\hat{\sigma}^2_m = \frac{1}{m}\sum_{i=1}^m \left( x^{(i)} - \mu \right)^2`$
        2. $`\displaystyle\tilde{\sigma}^2_m = \frac{1}{m-1}\sum_{i=1}^m \left( x^{(i)} - \mu \right)^2`$
    - Estimation)
      - $`\hat{\sigma}^2`$ is biased.
      - $`\tilde{\sigma}^2`$ is unbiased.

<br><br>

## 5.4.3 Variance and Standard Error
### Concept) Variance and Standard Error of Estimator
- Def.)
  - $`\textrm{Var}(\hat{\theta})`$
  - $`\textrm{SE}(\hat{\theta}) \equiv \sqrt{\textrm{Var}(\hat{\theta})}`$
- Meaning)
  - The **variance** or the **standard error** of an estimator provides a measure of how we would expect the estimate we compute from data to vary as we independently resample the dataset from the underlying data generating process.
- e.g.)
  - The standard error of the mean
    - Def.)
      - $`\displaystyle \textrm{SE}(\hat{\mu}_m) = \sqrt{\textrm{Var}\left[ \frac{1}{m} \sum_{i=1}^m x^{(i)} \right]} = \frac{\sigma}{\sqrt{m}}`$
        - where $`\sigma^2`$ is the true variance of the samples $`x^i`$
    - Props.)
      - Neither **the square root of the sample variance** nor **the square root of the unbiased estimator of the variance** provide an **unbiased estimate** of the standard deviation.
        - The square root of the unbiased estimator of the variance is less of an underestimate.
        - For large $`m`$, the approximation is quite reasonable.
    - Usage)
      - In ML, we often estimate the generalization error by computing the **sample mean** of the error on the test set.
        - The number of examples in the test set determines the accuracy of this estimate.
        - Taking advantage of the central limit theorem, we can use the standard error to compute the probability that the true expectation falls in any chosen interval.
          - e.g.) $`95\%`$ confidence interval centered on $`\hat{\mu}_m`$
            - $`(\hat{\mu}_m - 1.96 \textrm{SE}(\hat{\mu}_m), \hat{\mu}_m + 1.96 \textrm{SE}(\hat{\mu}_m))`$
        - In machine learning experiments, it is common to say that algorithm A is better than algorithm B 
          - if the upper bound of the 95% confidence interval for the error of algorithm A is less than the lower bound of the 95% confidence interval for the error of algorithm B.
- e.g.)
  - Bernoulli Distribution Estimator for the Mean
    - Settings)
      - $`\{ x^{(1)}, \cdots, x^{(m)} \}`$ : a set of $`m`$ iid data points according to a Bernoulli distribution with mean $`\theta`$:
        - $`P(x^{(i)};\theta) = \theta^{x^{(i)}} (1-\theta)^{(1-x^{(i)})}`$
    - Estimation)
      - Recall that we had the unbiased estimator $`\displaystyle \hat{\theta}_m = \frac{1}{m} \sum_{i=1}^m{x^{(i)}}`$.
      - Then the variance can be calculated as below.   
        $`\begin{aligned}
            \textrm{Var}(\hat{\theta}_m) &= \textrm{Var}\left( \frac{1}{m} \sum_{i=1}^m{x^{(i)}} \right) \\
            &= \frac{1}{m^2} \sum_{i=1}^m{\textrm{Var}\left(x^{(i)}\right)} \\
            &= \frac{1}{m^2} \sum_{i=1}^m{\theta(1-\theta)} \\
            &= \frac{1}{m^2} m \theta(1-\theta) \\
            &= \frac{1}{m} \theta(1-\theta) \\
        \end{aligned}`$

<br><br>

## 5.4.4. Trading off Bias and Variance to Minimize Mean Squared Error
#### Analysis) Bias vs Variance
- Comparison)
  - **Bias** measures the **expected deviation** from the true value of the function or parameter.
  - **Variance** provides a measure of the deviation from the **expected estimator value** that any particular sampling of the data is likely to cause.
- Problem)
  - There can be cases that we are only offered the choice between a model with **large bias** and one that suffers from **large variance**.
- How do we choose between them?)
  - Sol.1) The most common way to negotiate this trade-off is to use [cross-validation](../03/note.md#concept-cross-validation).
    - Empirically, cross-validation is highly successful on many real-world tasks.
  - Sol.2) Compare the mean squared error (MSE).
    - Def.)   
      $`\textrm{MSE} = \mathbb{E}\left[ (\hat{\theta}_m - \theta)^2 \right]`$
    - Prop.)
      - MSE incorporates both bias and the variance.
        - why?)   
          $`\begin{aligned}
              \textrm{MSE} &= \mathbb{E}\left[ (\hat{\theta}_m - \theta)^2 \right] \\
              &= \mathbb{E}\left[ (\hat{\theta}_m)^2 - 2\hat{\theta}_m \theta + \theta^2   \right] \\
              &= \mathbb{E}\left[ (\hat{\theta}_m)^2 \right] - 2\theta\mathbb{E}\left[ \hat  {\theta}_m\right]  + \theta^2 \\
              &= \mathbb{E}\left[ (\hat{\theta}_m)^2 \right] + \left( - \mathbb{E}\left[ (\hat  {\theta}_m) \right]^2 + \mathbb{E}\left[ (\hat{\theta}_m) \right]^2 \right)  -   2\theta\mathbb{E}\left[ \hat{\theta}_m\right] + \theta^2 \\
              &= \left( \mathbb{E}\left[ (\hat{\theta}_m)^2 \right] - \mathbb{E}\left[ (\hat  {\theta}_m) \right]^2 +   \right) + \left( \mathbb{E}\left[ (\hat{\theta}_m)   \right]^2 - 2\theta\mathbb{E}\left[ \hat{\theta}_m\right] + \theta^2 \right) \\
              &= \textrm{Var}(\hat{\theta}_m) + \left( \mathbb{E}\left[ (\hat{\theta}_m)   \right] - \theta \right)^2 \\
              &= \textrm{Var}(\hat{\theta}_m) + \left( \textrm{bias}(\hat{\theta}_m) \right)^2   \\
          \end{aligned}`$
      - In the case where generalization error is measured by the MSE, increasing **capacity** tends to increase **variance** and decrease **bias**.

<br><br>

## 5.4.5 Consistency
### Concept) Consistency
- Def.)
  - $`\displaystyle\plim_{m\rightarrow\infty} \hat{\theta}_m = \theta`$
    - i.e.) $`P(|\hat{\theta}_m - \theta| \gt \epsilon) \rightarrow 0 \textrm{ as } m\rightarrow\infty, \exists\epsilon`$
- Meaning)
  - A statistic that denotes whether our point estimates converge to the true value of the corresponding parameters as the number of data points $`m`$ in our dataset increases.
- Prop.)
  - Consistency ensures that the bias induced by the estimator diminishes as the number of data examples grows.
    - However, the reverse is not true.
      - i.e.) Asymptotic unbiasedness does not imply consistency.


<br>

* [Back to Deep Learning MIT](../../main.md)