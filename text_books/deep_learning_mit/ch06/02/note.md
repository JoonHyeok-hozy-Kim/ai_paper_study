* [Back to Deep Learning MIT](../../main.md)

# 6.2 Gradient-Based Learning
- Props.)
  - The **nonlinearity** of a neural network causes most interesting **loss functions** to become **non-convex**.
  - Thus, neural networks are usually trained by using **iterative**, **gradient-based** optimizers that merely drive the cost function to a very low value.
    - Cannot utilize the linear equation solvers used to train linear regression models or the convex optimization algorithms with global convergence guarantees used to train logistic regression or SVMs.
  - [Stochastic gradient descent](../../ch05/09/note.md#59-stochastic-gradient-descent) applied to non-convex loss functions 
    - has NO convergence guarantee.
      - cf.) Recall that [convex optimization](../../ch04/03/note.md#concept-convex-optimization) converges starting from any initial parameters.
    - is sensitive to the values of the initial parameters.
      - Thus, the parameter initialization is crucial to [feedforward networks](../00/note.md#concept-deep-feedforward-network-multilayer-perceptron-mlp).
  - Training a neural network is not much different from training any other model.
    - Choose a [cost function](#621-cost-functions).
    - Choose [how to represent the output](#622-output-units) of the model.

## 6.2.1 Cost Functions
- Desc.)
  - The cost functions for neural networks are more or less the **same** as those for other parametric models, such as linear models.
  - Two options
    1. [Learning Conditional Distributions with Maximum Likelihood](#6211-learning-conditional-distributions-with-maximum-likelihood)
    2. [Learning Conditional Statistics](#6212-learning-conditional-statistics)

### 6.2.1.1 Learning Conditional Distributions with Maximum Likelihood
- Def.)
  - $`\displaystyle J(\theta) = -\mathbb{E}_{\mathbf{x, y}\sim\hat{p}_{\textrm{data}}} \log{p_{\textrm{model}}(y|x)}`$
- Meaning)
  - The negative log-likelihood
  - The cross entropy between the training data and the model distribution.
- Prop.)
  - The specific form of the cost function changes from model to model, depending on the specific form of $`p_{\textrm{model}}`$.
  - The expansion of the above equation typically yields some terms that do not depend on the model parameters and may be discarded.
    - e.g.) $`p_{\textrm{model}}(y|x) = \mathcal{N}(y;f(x;\theta), I)`$
      - Then we recover the MSE cost given by
        - $`\displaystyle J(\theta) = \frac{1}{2}\mathbb{E}_{\mathbf{x, y}\sim\hat{p}_{\textrm{data}}} ||y-f(x;\theta)||^2 + C`$
      - Here, the constant term $`C`$ is based on the variance of the Gaussian distribution.
      - Since we assumed the variance be $`I`$, $`C`$ does not depend on $`\theta`$.
      - Thus, $`C`$ can be discarded.
  - Easy to use.
    - i.e.) Using maximum likelihood removes the burden of designing cost functions for each model.
      - Model : $`p(y|x)`$
      - Cost Function : $`\log{p(y|x)}`$
  - Negative log-likelihood provides a large cost function, predictable enough to serve as a good guide for the learning algorithm.
    - Why matters?)
      - Functions that **saturate** (become very flat) undermine this objective because they make the **gradient become very small**.
      - In many cases this happens because the **activation functions** used to produce the output of the hidden units or the output units saturate.
        - e.g.) Many output units involve an $`\exp`$ function that can saturate when its argument is very negative.
          - i.e.) $`x\rightarrow -\infty \Rightarrow \exp(x)\rightarrow 0`$
      - The negative log-likelihood helps to avoid this problem for many models.
  - The cross entropy usually does not have a **minimum value** when applied to the models commonly used in practice.
    - Thus, we can assign extremely high density to the correct training set outputs, resulting in cross-entropy approaching negative infinity.
    - Most models cannot do this.
      - e.g.) Logistic Regression cannot assign $`p\approx 0 \vee p\approx 1`$.



<br>

### 6.2.1.2 Learning Conditional Statistics


<br><br>

## 6.2.2 Output Units








<br>

* [Back to Deep Learning MIT](../../main.md)