* [Back to Deep Learning MIT](../../main.md)

# 5.6 Bayesian Statistics
### Concept) Bayesian Statistics
- Desc.)
  - The Bayesian uses **probability** to reflect degrees of certainty of states of knowledge.
  - The dataset is directly observed and so is not random.
  - The true parameter $`\theta`$ 
    - Assumed to be unknown or uncertain
    - Represented as a random variable using the **prior probability distribution** $`p(\theta)`$.
      - cf.) **Frequentist Statistics**
        - $`\theta`$ is fixed but unknown.
        - $`\hat{\theta}`$ is a random variable 
          - i.e.) $`\hat{\theta}`$ is a function of the dataset.
  - The prior probability distribution $`p(\theta)`$ 
    - Generally, the machine learning practitioner selects a **prior distribution** that is quite broad.
      - i.e.) the distribution with high entropy.
      - Why?)
        - To reflect a high degree of uncertainty in the value of $`\theta`$ before observing the data.
      - e.g.)
        - One might assume a priori that $`\theta`$ lies in some finite range or volume with a uniform distribution.
  - Estimating $`p(\theta)`$ 
    - How?)
      - Suppose a set of data samples $`\{x^{(1)}, x^{(2)}, \cdots, x^{(m)}\}`$ are observed.
      - Then we can recover the effect of data on our belief about $`\theta`$ by combining the data likelihood $`p(\theta | x^{(1)}, x^{(2)}, \cdots, x^{(m)})`$ via Bayes' rule.
        - $`\displaystyle p(\theta | x^{(1)}, x^{(2)}, \cdots, x^{(m)}) = \frac{p(x^{(1)}, x^{(2)}, \cdots, x^{(m)} | \theta ) p(\theta)}{p(x^{(1)}, x^{(2)}, \cdots, x^{(m)})}`$
          - In general
            - The prior begins as a relatively uniform or Gaussian distribution with high entropy.
            - The observation of the data usually causes the posterior to lose entropy and concentrate around a few highly likely values of the parameters.
    - Prop.)
      - [Maximum Likelihood Estimation](../05/note.md#concept-maximum-likelihood-principle) vs Bayesian Estimation
        1. Difference in the way of making prediction
           - The **ML approach** makes predictions using a [point estimate](../04/note.md#541-point-estimation) of $`\theta`$.
             - By evaluating $`\theta`$'s variance
           - The **Bayesian approach** is to make predictions using a full distribution over $`\theta`$.
             - e.g.) 
               - Suppose we observed $`m`$ examples.
               - Then we can predict the distribution over the next data sample $`x^{(m+1)}`$ as
                 - $`\displaystyle p(x^{(m+1)}|x^{(1)},\cdots, x^{(m)}) = \int p(x^{(m+1)}|\theta) p(\theta | x^{(1)},\cdots, x^{(m)}) d\theta`$
               - Here each value of $`\theta`$ with positive probability density contributes to the prediction of the next example, with the contribution weighted by the posterior density itself.
             - Prop.)
               - Tends to protect well against overfitting.
        2. Using the prior distribution
           - In the Bayesian approach, the prior has an influence by shifting probability mass density towards regions of the parameter space that are preferred a priori.
             - It can be seen as subjective human judgment impacting the predictions

#### E.g.) Bayesian Linear Regression
- Settings)
  - $`x\in\mathbb{R}^n`$ : an input vector
  - $`y\in\mathbb{R}`$ : the output value we want to predict
  - $`\hat{y} = w^\top x`$ : the prediction
    - where $`w\in\mathbb{R}^n`$ is the parameters vector.
  - **Prior Distribution** : $`p(y|Xw)`$
    - Given set of $`m`$ training samples $`(X^{(\textrm{train})}, y^{(\textrm{train})})`$,
      - the prediction of $`y`$ over the entire training set can be expressed as
        - $`\hat{y}^{(\textrm{train})} = X^{(\textrm{train})} w`$
          - where
            - $`y^{(\textrm{train})}, \hat{y}^{(\textrm{train})} \in \mathbb{R}^{m}`$
            - $`X^{(\textrm{train})} \in \mathbb{R}^{m\times n}`$
    - Expressed as a Gaussian conditional distribution on $`y^{(\textrm{train})}`$,   
      $`\begin{aligned}
          p(y^{(\textrm{train})} | X^{(\textrm{train})}, w) &= \mathcal{N}(y^{(\textrm{train})}; X^{(\textrm{train})} w, I) \\
          &\propto \exp\left( -\frac{1}{2} \left(y^{(\textrm{train})} - X^{(\textrm{train})} w \right)^\top  \left(y^{(\textrm{train})} - X^{(\textrm{train})} w \right) \right) 
      \end{aligned}`$
      - where
        - $`I \in \mathbb{R}^{m\times m}`$ : an identity matrix
          - i.e.) the Gaussian variance on $`y`$ is $`1`$.
    - For the simplicity of the notation, put $`(X^{(\textrm{train})}, y^{(\textrm{train})})`$ as $`(X, y)`$.
      - Then $`p(y|X,w) \propto \exp\left( -\frac{1}{2} \left(y - Xw \right)^\top  \left(y - Xw \right) \right)`$
  - **Prior Distribution over** $`w`$) : $`p(w)`$
    - Recall that the prior should reflect our naive belief about the value of these parameters.
    - In practice, we typically assume a fairly broad distribution expressing a high degree of uncertainty about $`\theta`$.
    - Using a Gaussian as a prior distribution,   
      $`\begin{aligned}
        p(w) &= \mathcal{N}(w;\mu_0, \Lambda_0) \\
        &\propto \exp \left( -\frac{1}{2} \left(w - \mu_0 \right)^\top \Lambda_0^{-1} \left(w - \mu_0 \right) \right)
      \end{aligned}`$
      - where
        - $`\mu_0 \in \mathbb{R}^n`$ : the prior distribution mean vector
        - $`\Lambda_0 \in \mathbb{R}^{n\times n}`$ : the prior distribution covariance matrix
- Estimation)
  - Since we determined the prior distributions $`p(y|Xw)`$ and $`p(w)`$, we can determine the **posterior distribution over the model parameters** as   
    $`\begin{aligned}
        p(w|X,y) &\propto p(y|Xw)p(w) \\
        &\propto \exp\left( -\frac{1}{2} \left(y - Xw \right)^\top  \left(y - Xw \right) \right) \left( -\frac{1}{2} \left(w - \mu_0 \right)^\top \Lambda_0^{-1} \left(w - \mu_0 \right) \right) \\
        &\propto \exp\left( -\frac{1}{2} \left( \left(y - Xw \right)^\top  \left(y - Xw \right) + \left(w - \mu_0 \right)^\top \Lambda_0^{-1} \left(w - \mu_0 \right) \right) \right) \\
        &\propto \exp\left( -\frac{1}{2} \left( -2y^\top Xw + w^\top X^\top Xw + w^\top \Lambda_0^{-1}w -2\mu_0 \right) \right) \\
    \end{aligned}`$
  - Put
    - $`\Lambda_m = (X^\top X + \Lambda_0^{-1})^{-1}`$
    - $`\mu_m = \Lambda_m(X^\top y + \Lambda_0^{-1}\mu_0)`$
  - Then   
    $`\begin{aligned}
        p(w|X,y) &\propto \exp \left( -\frac{1}{2}(w-\mu_m)^\top \Lambda_m^{-1} (w-\mu_m) + \frac{1}{2}\mu_m\right)
    \end{aligned}`$











<br>

* [Back to Deep Learning MIT](../../main.md)