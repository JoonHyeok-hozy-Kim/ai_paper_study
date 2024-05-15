* [Back to Deep Learning MIT](../../main.md)

# 3.9 Common Probability Distributions

## 3.9.1 Bernoulli Distribution
- Def.)
  - The distribution over a single binary random variable.
- Notation)
  - $`\begin{cases}
    P(\mathbf{x} = 1) = \phi \\
    P(\mathbf{x} = 0) = 1-\phi \\
  \end{cases}`$
    - Thus, $`P(\mathbf{x} = x) = \phi^x (1-\phi)^{1-x}`$
- Props.)
  - Mean : $`\mathbb{E}_\mathbf{x}\left[\mathbf{x}\right] = \phi`$
  - Variance : $`\textrm{Var}_\mathbf{x}\left[\mathbf{x}\right] = \phi(1-\phi)`$


## 3.9.2 Multinoulli Distribution (Cartegorical Distribution)
- Def.)
  - The distribution over a single discrete variable with $`k`$ different states, where $`k`$ is finite.
- Notation)
  - $`p = \left[\begin{array}{c}
    p_1 \\ p_2 \\ \vdots \\ p_{k-1}
  \end{array}\right] \in [0,1]^{k-1}`$
    - where $`p_i \in [0,1]`$ gives the probability of the $`i`$-th state.
  - $`p_k = 1- 1^\top p`$ : the probability of the $`k`$-th state.
    - where $`1^\top p \le 1`$
  


## 3.9.3 Gaussian Distribution (Normal Distribution)
- Def.)
  - $`\displaystyle \mathcal{N}(x;\mu,\sigma^2) = \sqrt{\frac{1}{2\pi\sigma^2}} \exp\left(-\frac{1}{2\sigma^2} (x-\mu)^2\right)`$
    - where
      - $`\mu\in\mathbb{R}`$
      - $`\sigma\in (0, \infty)`$
- Prop.)
  - $`\mu = \mathbb{E}[\mathbf{x}]`$
  - $`\sigma^2 = \textrm{Var}[\mathbf{x}]`$
  - $`\displaystyle \beta = \frac{1}{\sigma^2}`$ : the precision
    - Usage)
      - $`\displaystyle \mathcal{N}(x;\mu,\beta^{-1}) = \sqrt{\frac{\beta}{2\pi}} \exp\left(-\frac{1}{2} \beta(x-\mu)^2\right)`$
  - Good Properties)
    - [The central limit theorem](../../../../math/statistics/ch03/05/note.md#theorem-central-limit-theorem-clt) shows that the sum of many independent random variables is approximately normally distributed.
    - The normal distribution encodes the maximum amount of uncertainty over the real numbers.

<br>

#### Concept) Multivariate Normal Distribution
- Def.)
  - $`\displaystyle \mathcal{N}(x;\mu,\Sigma) = \sqrt{\frac{1}{(2\pi)^n \; \textrm{det}(\Sigma)}} \exp\left(-\frac{1}{2} (x-\mu)^\top \Sigma^{-1} (x-\mu) \right)`$
    - where
      - $`x \in \mathbb{R}^n`$
      - $`\mu \in \mathbb{R}^n`$ : the means of the distributions of $`x`$
      - $`\Sigma \in \mathbb{R}^{n\times n}`$ : the covariance matrix of the distribution
- Prop.)
  - $`\displaystyle \beta = \Sigma^{-1}`$ : the precision matrix
    - Usage)
      - $`\displaystyle \mathcal{N}(x;\mu,\beta^{-1}) = \sqrt{\frac{\textrm{det}(\beta)}{(2\pi)^n}} \exp\left(-\frac{1}{2} (x-\mu)^\top \beta (x-\mu) \right)`$

<br>

## 3.9.4 Exponential and Laplace Distributions
- Objective)
  - Get a probability distribution with a sharp point at $`x=0`$.

### Concept) Exponential Distribution
- Def.)
  - $`p(x;\lambda) = \lambda 1_{x\ge 0} \; \exp(-\lambda x) = \begin{cases}
    1 & x \gt 0 \\
    0 & \textrm{otherwise}
  \end{cases}`$
    - where
      - $`1_{x\ge 0}`$ : the indicator function that assign probability zero to all negative values of $`x`$.

### Concept) Laplace Distribution
- Def.)
  - $`\displaystyle\textrm{Laplace}(x;\mu, \gamma) = \frac{1}{2\gamma} \exp\left(-\frac{|x-\mu|}{\gamma}\right)`$
- Prop.)
  - A sharp peak of probability mass at an arbitrary point $`\mu`$

<br>


## 3.9.5 The Dirac Distribution and Empirical Distribution
- Objective)
  - Get a probability distribution that all of its mass clusters around a single point.

### Concept) Dirac Distribution
- Def.)
  - $`p(x) = \delta(x-\mu)`$
    - where
      - $`\delta(x)`$ is the Dirac delta function
        - The Dirac delta function is defined such that it is zero-valued everywhere except 0, yet integrates to 1. 
          - i.e.)
            - $`\delta(x) = \begin{cases}
                1 & x=0 \\
                0 & \textrm{otherwise}
            \end{cases}`$
            - $`\displaystyle\int_{-\infty}^\infty\delta(x) = 1`$
- e.g.)
  - Empirical Distribution
    - Def.)
      - $`\displaystyle\hat{p}(x) = \frac{1}{m}\sum_{i=1}^m \delta(x-x^{(i)})`$
        - where
          - $`x^{(1)}, x^{(2)}, \cdots, x^{(m)}`$ : $`m`$ points forming a given dataset or collection of samples.
          - The probability mass of $`\displaystyle\frac{1}{m}`$ is given for each point $`x^{(i)}`$.
- Prop.)
  - We can view the empirical distribution formed from a dataset of training examples as specifying the distribution that we sample from when we train a model on this dataset. 
  - It is the probability density that **maximizes the likelihood** of the training data.
  

<br>

## 3.9.6 Mixtures of Distributions
- Objective)
  - Combining multiple probability distributions
- How?)
  - A mixture distribution is made up of several **component distributions**. 
  - On each trial, the choice of **which component distribution generates the sample** is determined by sampling a component identity from a [multinoulli distribution](#392-multinoulli-distribution-cartegorical-distribution):
    - $`\displaystyle P(\mathbf{x}) = \sum_i P(c=i) P(\mathbf{x} | c=i)`$
      - where
        - $`c`$ : the component identity variable
        - $`P(c)`$ : the multinoulli distribution over component identities

<br>

#### Concept) Latent Variable
- Def.)
  - A latent variable is a **random variable** that we cannot observe directly.
- e.g.)
  - The component identity variable $`c`$ of the [mixture model](#396-mixtures-of-distributions).
    - Latent variables may be related to $`\mathbf{x}`$ through the joint distribution.
      - i.e.) $`P(\mathbf{x}, c) = P(\mathbf{x}|c) P(c)`$ 
    - The distribution $`P(c)`$ over the latent variable and the distribution $`P(\mathbf{x}|c)`$ relating the latent variables to the visible variables determines the shape of the distribution $`P(\mathbf{x})`$ without reference to latent variables.

<br>

#### Concept) Gaussian Mixture
- Def.)
  - $`p(\mathbf{x}|c=i)`$
    - where each component $`i`$ has a separately parametrized mean $`\mu^{(i)}`$ and covariance $`\Sigma^{(i)}`$.
    - cf.)
      - Here, $`\alpha_i = P(c=i)`$ is the prior probability given to each component $`i`$.
      - $`P(c|\mathbf{x})`$ is a posterior probability which is computed after the observation of $`\mathbf{x}`$


<br>

* [Back to Deep Learning MIT](../../main.md)