* [Back to Deep Learning MIT](../../main.md)

# 5.6 Bayesian Statistics
### Review) Frequentist Statistics
- Props.)
  - $`\theta`$ is fixed but unknown.
  - $`\hat{\theta}`$ is a random variable 
    - i.e.) $`\hat{\theta}`$ is a function of the dataset.
- e.g.)
  - Linear Regression
  - [Maximum Likelihood Estimation](../05/note.md#concept-maximum-likelihood-principle)

<br>

### Concept) Bayesian Statistics
- Desc.)
  - The Bayesian uses **probability** to reflect degrees of certainty of states of knowledge.
  - The dataset is directly observed and so is not random.
  - The true parameter $`\theta`$ 
    - Assumed to be unknown or uncertain
    - Represented as a random variable using the **prior probability distribution** $`p(\theta)`$.
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
           - The **Bayesian approach** is to make predictions using a **full distribution** over $`\theta`$.
             - e.g.) 
               - Suppose we observed i.i.d. $`m`$ examples.
               - Then we can predict the distribution over the next data sample $`x^{(m+1)}`$ as
                 - $`\displaystyle p(x^{(m+1)}|x^{(1)},\cdots, x^{(m)}) = \int p(x^{(m+1)}|\theta) p(\theta | x^{(1)},\cdots, x^{(m)}) d\theta`$
                   - why?)      
                     - Put 
                       $`\begin{cases}
                         p(X_1) = p(x^{(1)},\cdots, x^{(m)}) \\
                         p(X_2) = p(x^{(m+1)}) \\
                       \end{cases}`$
                     - Then   
                       $`p(x^{(m+1)}|x^{(1)},\cdots, x^{(m)}) = p(X_2|X_1)`$.
                     - Consider that   
                      $`\begin{aligned}
                        p(X_2|X_1) &= \frac{p(X_1, X_2)}{p(X_1)} \\
                        &= \int \frac{p(X_1,X_2|\theta)p(\theta)}{p(X_1)} d\theta &\because p(X) = \int p(X|\theta)p(\theta) d\theta \\
                        &= \int \frac{p(X_2|\theta)p(X_1|\theta)p(\theta)}{p(X_1)} d\theta &\because \forall i, x^{(i)}\textrm{ is i.i.d.} \\
                        &= \int \frac{p(X_2|\theta)p(\theta|X_1)p(X_1)}{p(X_1)} d\theta \\
                        &= \int p(X_2|\theta)p(\theta|X_1) d\theta \\
                        &= \int p(x^{(m+1)}|\theta) p(\theta | x^{(1)},\cdots, x^{(m)}) d\theta
                      \end{aligned}`$   
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
    - Expressed as a Gaussian conditional distribution on $`y^{(\textrm{train})}`$, we can [normalize the Multivariate Gaussian](../../ch03/09/note.md#concept-multivariate-normal-distribution) as below:  
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
  - Since we determined the prior distributions $`p(y|X,w)`$ and $`p(w)`$, we can determine the **posterior distribution over the model parameters** as   
    $`\begin{aligned}
        p(w|X,y) &\propto p(y|X,w)p(w) \\
        &\propto \exp\left( -\frac{1}{2} \left(y - Xw \right)^\top  \left(y - Xw \right) \right) \left( -\frac{1}{2} \left(w - \mu_0 \right)^\top \Lambda_0^{-1} \left(w - \mu_0 \right) \right) \\
        &\propto \exp\left( -\frac{1}{2} \left( \left(y - Xw \right)^\top  \left(y - Xw \right) + \left(w - \mu_0 \right)^\top \Lambda_0^{-1} \left(w - \mu_0 \right) \right) \right) \\
        &\propto \exp\left( -\frac{1}{2} \left( -2y^\top Xw + w^\top X^\top Xw + w^\top \Lambda_0^{-1}w -2\mu_0 \right) \right) \\
    \end{aligned}`$
  - Put
    - $`\Lambda_m = (X^\top X + \Lambda_0^{-1})^{-1}`$
    - $`\mu_m = \Lambda_m(X^\top y + \Lambda_0^{-1}\mu_0)`$
  - Then   
    $`\begin{aligned}
        p(w|X,y) &\propto \exp \left( -\frac{1}{2}(w-\mu_m)^\top \Lambda_m^{-1} (w-\mu_m) + \frac{1}{2}\mu_m \Lambda_m^{-1}\mu_m  \right) \\
        &\propto \exp \left( -\frac{1}{2}(w-\mu_m)^\top \Lambda_m^{-1} (w-\mu_m)\right) \\
    \end{aligned}`$
- Props.)
  - Compared to the [Frequentist Statistics](#review-frequentist-statistics)...
    - If $`\mu_0=0`$ and $`\Lambda_0 = \frac{1}{\alpha}I`$
      - $`\mu_m`$ gives the same estimate of $`w`$ as the frequentist linear regression with the weight decay penalty of $`\alpha w^\top w`$.
    - The Bayesian estimate is undefined if $'\alpha= 0`$.
      - i.e.) Not allowed to begin the Bayesian learning process with an infinitely wide prior on $`w`$.
    - The Bayesian estimate provides a covariance matrix, showing **how likely all the different values** of $`w`$ are, rather than providing only the estimate $`\mu_m`$

<br>

## 5.6.1 Maximum A Posteriori (MAP) Estimation
- Why needed?)
  - Recall that the Bayesian estimate provides a covariance matrix, showing **how likely all the different values** of $`w`$ are, rather than providing only the estimate $`\mu_m`$.
  - However, such models are intractable.
  - Instead, we need a point estimate that offers a tractable approximation.
  - MAP can provide a point estimate using the Bayesian statistics.
- Def.)
  - The MAP estimate chooses the point of maximal posterior probability.
    - $`\displaystyle\theta_{\textrm{MAP}} \equiv \arg\max_\theta p(\theta|x) = \arg\max_\theta \log{p(x|\theta)} + \log{p(\theta)}`$
- Prop.)
  - As with full Bayesian inference, MAP Bayesian inference has the advantage of leveraging **information that is brought by the prior** and **cannot be found in the training data**.
    - This additional information helps to reduce the variance in the MAP point estimate.
    - However, it does so at the price of increased bias
  - Many **regularized** estimation strategies, such as maximum likelihood learning regularized with weight decay, can be interpreted as making the MAP approximation to Bayesian inference.
    - e.g.)
      - MAP Bayesian inference with a Gaussian prior on the weights corresponds to weight decay.
        - Consider a linear regression model with a Gaussian prior on the weights $`w`$.
        - If this prior is given by $`\mathcal{N}(w;0,\frac{1}{\lambda}I)`$
          - then $`\log{p(x|\theta)} + \log{p(\theta)} \propto \lambda w^\top w`$.

<br>

* [Back to Deep Learning MIT](../../main.md)