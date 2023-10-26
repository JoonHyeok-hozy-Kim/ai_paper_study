# Maximum-Likelihood Estimation

<br>

## Notations
* $\theta = [\theta_1, \theta_2, \dots, \theta_r]^T$ : a set of parameters.
* $x$ : data observed from a distribution $X$ with pdf $f_X(x|\theta)=f(x|\theta)$
* $x_1, x_2, ..., x_N$ : a sequence of outcomes of the random variables $X_1, X_2, ..., X_N$ that have been observed.
* $X_i$ is independent of $X_j$ for $i \ne j$.

<br><br>

## Concept) Likelihood Function
* Notation)
  * $l_x(\theta;x_1,x_2, ..., x_N)=f(x_1,x_2, ..., x_N|\theta) = f(x|\theta)$

* Def.)
  * A function of the **parameter** $\theta$ with the samples $x$ fixed.
    * cf.) In case of pdf, parameter is considered to be fixed.

<br><br>

## Concept) Maximum-Likelihood Estimation
* Def.) Maximum-Likelihood Estimation
  * A means of estimating parameters of a distribution.
  * Get the ML estimate of the parameter $\theta$ that maximizes the likelihood function.
    * $\theta_{ML} = arg max_\theta \space l_x(\theta)$
* Goal)
  * Determine the parameter $\theta$ for which the probability of observing the outcome $x=x_1, x_2, ..., x_N$ as high as possible.
* Props.)
  * The goal of the ML estimation is to maximize the likelihood function.
  * The exact value of the likelihood function is not considered.
    * All we need is the parameters that maximizes the likelikhood.
      * Thus...
        * Ignore or suppress constants in the likelihood function.
        * Commonly use the **logarithm likelihood function** (or the **log-likelihood-function**) for the useful properties of the log function.
          * $L_x(\theta) = \log{l_x(\theta)}$
          * Necessary but not sufficient condition for this.
            * $`\nabla_\theta l_x(\theta)|_{\theta=\theta_{ML}} = \nabla_\theta \log{L_x}(\theta)|_{\theta=\theta_{ML}}=0`$
              * where $`\nabla_\theta = \left[ \begin{array}{c} \frac{\partial}{\partial \theta_1} \\ \frac{\partial}{\partial \theta_2} \\ \vdots \\ \frac{\partial}{\partial \theta_r} \\  \end{array} \right]`$