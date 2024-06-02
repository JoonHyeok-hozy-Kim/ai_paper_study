* [Back to Deep Learning MIT](../../main.md)

# 5.5 Maximum Likelihood Estimation

### Concept) Maximum Likelihood Principle
- Settings)
  - $`\mathbb{X} = \{x^{(1)}, \cdots, x^{(m)}\}`$ : a set of $`m`$ examples
    - where $`x^{(i)}`$ are iid from the true but unknown distribution $`p_{\textrm{data}}(\mathbf{x})`$
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
  - Optimizing $`\theta_{\textrm{ML}}`$ is identical to Minimizing the dissimilarity between $`\begin{cases}
        \hat{p}_{\textrm{data}} & \textrm{: the empirical distribution defined by the training set} \\
        p_{\textrm{model}} & \textrm{: the model distribution}
    \end{cases}`$
    - Why?)
      - Using the KL divergence we can denote the dissimilarity as below.
        - $`\displaystyle D_{\textrm{KL}}(\hat{p}_{\textrm{data}} || p_{\textrm{model}}) = \mathbb{E}_{\mathbf{x}\sim\hat{p}_{\textrm{data}}} \left[ \log{\hat{p}_{\textrm{data}}} - \log{p_{\textrm{model}}} \right]`$
      - Recall that we want to minimize $`D_{\textrm{KL}}(\hat{p}_{\textrm{data}} || p_{\textrm{model}})`$.
      - Also, $`\hat{p}_{\textrm{data}}`$ is a function only of the data generating process, not the model.
      - Thus, we only minimize $`- \mathbb{E}_{\mathbf{x}\sim\hat{p}_{\textrm{data}}} \left[  \log{p_{\textrm{model}}} \right]`$.
        - which is identical to the **Maximum Likelihood Estimator** optimization problem above. 














<br>

* [Back to Deep Learning MIT](../../main.md)