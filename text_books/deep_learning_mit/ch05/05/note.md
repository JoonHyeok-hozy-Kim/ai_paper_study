* [Back to Deep Learning MIT](../../main.md)

# 5.5 Maximum Likelihood Estimation

### Concept) Maximum Likelihood Principle
- Settings)
  - $`\mathbb{X} = \{x^{(1)}, \cdots, x^{(m)}\}`$ : a set of $`m`$ examples
    - where $`x^{(i)}`$ are iid on the true but unknown distribution $`p_{\textrm{data}}(\mathbf{x})`$
  - $`p_{\textrm{model}}(\mathbf{x};\theta)`$ : a parametric family of probability distributions over the same space indexed by $`\theta`$
    - i.e.) $`p_{\textrm{model}}(\mathbf{x};\theta)`$ maps any configuration $`x`$ to a real number estimating the true probability $`p_{\textrm{data}}(x)`$.
- Def.) Maximum Likelihood Estimator
  - The maximum likelihood estimator for $`\theta`$ is defined as   
    $`\begin{aligned}
        \theta_{\textrm{ML}} &\equiv \arg\max_\theta p_{\textrm{model}}(\mathbb{X};\theta) \\
        &= \arg\max_\theta \prod_{i=1}^m p_{\textrm{model}}(x^{(i)};\theta) & \because x^{(i)} \textrm{ is iid.} \\
    \end{aligned}`$
  - For convenience, we may take logarithm as follows.   
    $`\displaystyle \theta_{\textrm{ML}} = \arg\max_\theta \sum_{i=1}^m \log p_{\textrm{model}}(x^{(i)};\theta)`$
  - Without affecting the $`\arg\max`$, we may divide both sides by $`m`$ to obtain a version of the criterion expressed as an expectation w.r.t. the empirical distribution $`\hat{p}_{\textrm{data}}`$ defined by the training data:   
    $`\begin{aligned}
        \theta_{\textrm{ML}} &= \arg\max_\theta \frac{1}{m} \sum_{i=1}^m \log p_{\textrm{model}}(x^{(i)};\theta)\\
        &= \arg\max_\theta \mathbb{E}_{\mathbf{x}\sim\hat{p}_{\textrm{data}}} \log p_{\textrm{model}}(x;\theta)
    \end{aligned}`$
- Interpretation)
  - Optimizing $`\theta_{\textrm{ML}}`$ is identical to minimizing the dissimilarity between $`\begin{cases}
        \hat{p}_{\textrm{data}} & \textrm{: the empirical distribution defined by the training set} \\
        p_{\textrm{model}} & \textrm{: the model distribution}
    \end{cases}`$
    - Why?)
      - Using the [KL divergence](../../../elmnts_info_theory/ch02/03/note.md#concept-relative-entropy-kullbackleibler-distance) we can denote the dissimilarity as below.
        - $`\displaystyle D_{\textrm{KL}}(\hat{p}_{\textrm{data}} || p_{\textrm{model}}) = \mathbb{E}_{\mathbf{x}\sim\hat{p}_{\textrm{data}}} \left[ \log{\hat{p}_{\textrm{data}}} - \log{p_{\textrm{model}}} \right]`$
      - Recall that we want to minimize $`D_{\textrm{KL}}(\hat{p}_{\textrm{data}} || p_{\textrm{model}})`$.
      - Also, $`\hat{p}_{\textrm{data}}`$ is a function only of the data generating process, not the model.
      - Thus, we only minimize $`- \mathbb{E}_{\mathbf{x}\sim\hat{p}_{\textrm{data}}} \left[  \log{p_{\textrm{model}}} \right]`$.
        - which is identical to the **Maximum Likelihood Estimator** optimization problem above. 
- Props.)
  - Under the following conditions, the ML estimator is [consistent](../04/note.md#concept-consistency).
    - i.e.)
      - As the **number of training examples** approaches infinity, the **maximum likelihood estimate** of a parameter **converges to the true value** of the parameter.
    - Conditions)
      1. The true distribution $`p_{\textrm{data}}`$ lies within the model family $`p_{\textrm{model}}(\bullet; \theta)`$.
      2. The true distribution $`p_{\textrm{data}}`$ corresponds to exactly one value of $`\theta`$.


<br><br>

## 5.5.1 Conditional Log-Likelihood and Mean Squared Error
### Concept) Supervised Learning and Maximum Likelihood Estimation
- Desc.)
  - In the supervised learning problem, our goal is to estimate the conditional probability $`P(\mathbf{y}|\mathbf{x};\theta)`$ to predict $`\mathbf{y}`$ given $`\mathbf{x}`$.
  - Suppose
    - $`\mathbf{X}`$ represents all our inputs
    - $`\mathbf{Y}`$ represents all our observed targets.
  - Then the conditional likelihood estimator goes
    - $`\displaystyle \theta_{ML} = \arg\max_\theta P(\mathbf{Y}|\mathbf{X};\theta)`$.
  - Further assuming that $`x \in \mathbf{X}`$ are iid,
    - $`\displaystyle \theta_{ML} = \arg\max_\theta \sum_{i=1}^m\log P(y^{(i)}|x^{(i)};\theta)`$

#### E.g.) Linear Regression as Maximum Likelihood
- Linear Regression problem using MSE
  - Recall that the Linear Regression problem was 
    - taking an input $`x`$
    - producing an output value $`\hat{y}`$
  - We used MSE to optimize the problem.
- Maximum Likelihood Approach
  - Consider a model producing a conditional distribution $`p(y|x)`$.
  - In a training set, there may be several examples with the same input $`x`$ but different values of $`y`$.
  - The goal of our algorithm is to fit the distribution $`p(y|x)`$ to all of those different $`y`$ values that are all compatible with $`x`$.
  - Using the Gaussian, define $`p(y|x)`$ as follows.
    - $`p(y|x) = \mathcal{N}(y; \; \hat{y}(x;w), \sigma^2)`$
      - where
        - $`\hat{y}(x;w)`$ : the prediction of the mean of the Gaussian
        - $`\sigma^2`$ : a hyperparameter as the variance of the model chosen by the user
  - Further assuming that each example are iid, the conditional log-likelihood is given by   
    $`\begin{aligned}
       \sum_{i=1}^m \log p(y^{(i)}|x^{(i)};\theta) &= \sum_{i=1}^m \log \left( \sqrt{\frac{1}{2\pi\sigma^2}} \exp\left(-\frac{1}{2\sigma^2} (  y^{(i)} - \hat{y}(x;w)  )^2\right) \right) \\
       &= m\log\sqrt{\frac{1}{2\pi\sigma^2}} - \sum_{i=1}^m \frac{(  y^{(i)} - \hat{y}(x;w)  )^2}{2\sigma^2} \\
       &= m\log\sqrt{\frac{1}{2\pi\sigma^2}} - \sum_{i=1}^m \frac{||\hat{y}^{(i)} - y^{(i)}||^2}{2\sigma^2} \\
    \end{aligned}`$
  - Thus, the maximizing the above conditional log-likelihood is identical to the MSE minimizing problem which of
    - $`\displaystyle \textrm{MSE}_{\textrm{train}} = \frac{1}{m}\sum_{i=1}^m ||\hat{y}^{(i)} - y^{(i)}||^2`$








<br>

* [Back to Deep Learning MIT](../../main.md)