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
- Desc.)
  - Learning just one conditional statistic of $`y`$ given $`x`$
    - e.g.) Predicting $`\mathbb{E}(y)`$
- How?)
  - Use **functional** as the cost function
    - Def.) Functional
      - A mapping from functions to real numbers.
    - Meaning)
      - Learning is choosing a **function** rather than merely choosing a set of parameters.
    - Why is it possible?)
      - Recall that the neural network can represent any function $f$ from a wide class of functions.
        - where this class is 
          - limited only by features such as continuity and boundedness.
          - not limited to have a specific parametric form
      - Thus, we can design our **cost functional** to have its minimum occur at some specific function we desire.
    - e.g.)
      - Design a **cost functional** that has its minimum lie on the function that maps $`x`$ to $`\mathbb{E}(y|x)`$.
      - Using calculus of variations, we can optimize the following two problems.
        1. $`f^\ast = \arg\min_f \mathbb{E}_{\mathbf{x, y}\sim p_{\textrm{data}}} ||y-f(x)||^2`$ 
           - yields $`f^\ast(x) = \mathbb{E}_{\mathbf{y}\sim p_{\textrm{data}}(y|x)} [y]`$
           - meaning that if we could train on infinitely many samples from the true data generating distribution, minimizing the MSE cost function gives a function that predicts the mean of $`y`$ for each value of $`x`$.
        2. $`f^\ast = \arg\min_f \mathbb{E}_{\mathbf{x, y}\sim p_{\textrm{data}}} ||y-f(x)||_1`$ 
           - yields a function that predicts the median value of $`y`$ for each $`x`$.
           - This cost function is commonly called **mean absolute error**.
      - Unfortunately, **mean squared error** and **mean absolute error** often lead to poor results when used with gradient-based optimization.
      - Some output units that saturate produce very small gradients when combined with these cost functions. 
      - This is one reason that the cross-entropy cost function is more popular than mean squared error or mean absolute error, even when it is not necessary to estimate an entire distribution $`p(y | x)`$.


<br><br>

## 6.2.2 Output Units
- Desc.)
  - The choice of [cost function](#621-cost-functions) is tightly coupled with the choice of **output unit**.
    - e.g.)
      - Most of the time, we simply [use the cross-entropy](#6211-learning-conditional-distributions-with-maximum-likelihood) between the data distribution and the model distribution.
      - The choice of **how to represent the output** then determines the form of the cross-entropy function.
  - Any kind of neural network unit that may be used as an output can also be used as a hidden unit.
  - Assumption
    - The feedforward network provides a **set of hidden features** defined by $`h = f(x;\theta)`$.
    - The role of the **output layer** is then to provide some additional transformation from the features to complete the task that the network must perform.
- Types Covered
  - [Linear Units](#6221-linear-units-for-gaussian-output-distributions) for Gaussian Output Distributions
  - [Sigmoid Units](#6222-sigmoid-units-for-bernoulli-output-distributions) for Bernoulli Output Distributions
  - [Softmax Units](#6223-softmax-units-for-multinoulli-output-distributions) for Multinoulli Output Distributions

<br>

### 6.2.2.1 Linear Units for Gaussian Output Distributions
- Structure)
  - Given features $`h`$, a layer of linear output unit produce the a vector
    - $`\hat{y} = W^\top h + b`$
  - Linear output layers are often used to produce the mean of a conditional Gaussian distribution:
    - $`p(y|x) = \mathcal{N}(y;\hat{y}, I)`$
- Optimization) 
  - Maximizing the log-likelihood is then equivalent to minimizing the MSE.

<br>

### 6.2.2.2 Sigmoid Units for Bernoulli Output Distributions
- Problem)
  - Predicting the value of a **binary** variable $`y`$
- Choosing the Cost Function)
  - The maximum-likelihood approach is to define a Bernoulli distribution over $`y`$ conditioned on $`x`$.
    - i.e.) Predicting a single number $`P(y=1|x) \in [0,1]`$
  - Thus, the model **output** should be in the interval of $`[0,1]`$
- Output Candidates)
  1. Linear Unit : $`P(y=1|x) = \max\left\{ 0, \min\{1, w^\top h + b\} \right\}`$
     - Draw back)
       - Whenever $`w^\top h + b \notin [0,1]`$, the gradient of the output will be $`0`$.
       - Thus, the gradient descent will be very ineffective.
  2. Sigmoid Unit
     - Derivation)
       - Recall the [Logistic Sigmoid](../../ch03/10/note.md#concept-logistic-sigmoid) function $`\hat{y} = \sigma\left(w^\top h + b\right)`$
       - The above can be decomposed into the following two:
         1. A linear layer computing $`z = w^\top h + b`$.
            - The $`z`$ variable defining such a distribution over binary variables is called a **logit**.
         2. The sigmoid activation to convert $`z`$ into a probability.
       - Assume that the unnormalized log probabilities are linear in $`y`$ and $`z`$.
       - Then   
         $`\begin{aligned}
           \log \tilde{P}(y) &= yz \\
           \Rightarrow \tilde{P}(y) &= \exp(yz) \\
           \Rightarrow P(y) &= \frac{\exp(yz)}{\sum_{y'=0}^1 \exp(y'z)} & \textrm{: the normalized prob.} \\
           &= \sigma((2y-1)z) 
         \end{aligned}`$
- Back to the Cost Function)
  - Using the sigmoid unit, the loss function goes as   
    $`\begin{aligned}
      J(\theta) &= -\log p(y|x) \\
      &= -\log\sigma((2y-1)z) \\
      &= \varsigma((1-2y)z) & \textrm{Refer to the softplus function.}
    \end{aligned}`$
    - cf.) [Softplus function](../../ch03/10/note.md#concept-softplus)
- Analysis)
  - $`J(\theta)`$ saturates only when $`(1-2y)z \rightarrow -\infty`$
    - Meaning)
      - [Saturation](#6211-learning-conditional-distributions-with-maximum-likelihood) thus occurs only when the model already has the right answer.   
        $`\begin{cases}
          y=1 \wedge z \rightarrow \infty \\
          y=0 \wedge z \rightarrow -\infty \\
        \end{cases}`$
  - When $`z`$ has the wrong sign, $`(1-2y)z`$ may be simplified to $`|z|`$.
    - Then $`|z|\rightarrow\infty \Rightarrow \varsigma((1-2y)z) \rightarrow \textrm{sign}(z)`$.
      - Meaning)
        - In the limit of extremely incorrect $`z`$, the [softplus function](../../ch03/10/note.md#concept-softplus) does not shrink the gradient at all.
        - This property is very useful because it means that gradient-based learning can act to quickly correct a mistaken $`z`$. 
          - cf.) MSE saturates when $`\sigma(z)`$ saturates.
  - Analytically, the logarithm of the sigmoid is always defined and finite.
    - Why?)
      - The sigmoid returns values restricted to the open interval $`(0,1)`$
    - cf.)
      - In SW implementations, to avoid numerical problems, it is best to write the negative log-likelihood as a function of $`z`$, rather than as a function $`\hat{y}=\sigma(z)`$.
        - Why?)
          - $`\sigma(z) \rightarrow 0 \Rightarrow \log{\hat{y}}\rightarrow -\infty`$.

<br>

### 6.2.2.3 Softmax Units for Multinoulli Output Distributions
#### Concept) Softmax Unit
- Usage)
  - Multinoulli problem
    - Representing a probability distribution over a discrete variable with $`n`$ possible values (classes).
  - **Softmax function** can be used for that purpose.
    - Def.)
      - $`\displaystyle \textrm{softmax}(z)_i = \frac{\exp(z_i)}{\sum_j\exp(z_j)}`$
    - Prop.)
      - A generalization of the **sigmoid function** used to representing a probability distribution over a binary variable
      - As with the [logistic sigmoid](#6222-sigmoid-units-for-bernoulli-output-distributions), the use of the $`\exp`$ function works very well when training the **softmax** to output a target value $`y`$ using maximum log-likelihood.
- Model)
  - Goal) 
    - Getting an estimator for a discrete variable with $`n`$ possible classes
  - Estimator)  
    - $`\hat{y}\in\mathbb{R}^n`$
      - where $`\hat{y}_i = P(y=i|x)`$
  - Just like the [sigmoid unit](#6222-sigmoid-units-for-bernoulli-output-distributions), softmax unit can be decomposed into following two part:
    1. Generating the argument $`z\in\mathbb{R}^n`$ for the **softmax function**.
       - $`z = W^\top h + b`$
         - where $`h`$ is the input
    2. **Softmax Function** exponentiating and normalizing $`z`$ to obtain $`\hat{y}`$
       - Target)     
         Maximize $`\begin{aligned}
           \log{P(y=i;z)} &= \log{\textrm{softmax}(z)_i} \\
           &= z_i -\log\sum_j\exp(z_i) \\
         \end{aligned}`$
- Props.)
  - $`z_i`$ cannot saturate.
  - The above maximization problem can be modified to the negative log likelihood minimization problem.
    - $`\arg\min_z -\log{\textrm{softmax}(z)_i} = \arg\min_z -z_i +\log\sum_j\exp(z_i)`$
  - The negative log-likelihood cost function always strongly penalizes the most active incorrect prediction.
    - why?)
      - Consider that $`\log\sum_j\exp(z_i) \approx \max_j z_j`$.
        - Why?) 
          - $`|\max_j z_j - z_k| \le |\exp(\max_j z_j) - \exp(z_k)|`$
          - Consider the amplifying property of the $`\exp`$ function.
      - Thus, if the correct answer already has the largest input to the softmax, then the $`-z_i`$ term and the $`\log\sum_j\exp(z_j) \approx \max_j z_j = z_j`$ will roughly cancel out each other.
      - Hence, this example will then contribute little to the overall training cost, which will be dominated by other examples that are not yet correctly classified.
  - Softmax activation can saturate when the differences between input values become extreme.
    - cf.) Recall the case of the [sigmoid function](#6222-sigmoid-units-for-bernoulli-output-distributions) with extremely positive or negative inputs.
    - When the softmax saturates, many cost functions based on the softmax also saturate, unless they are able to invert the saturating activating function.
  - The softmax function provides a **continuous** and **differentiable** version of the $`\arg\max`$.
    - where $`\arg\max`$ result is represented as a one-hot vector, which is not **continuous** nor **differentiable**.

<br>

### 6.2.2.4 Other Output Types
- Common Assumption
  - $`p(y|x;\theta)`$ : a conditional distribution
  - $`-\log{p(y|x;\theta)}`$ : the cost function under the principle of maximum likelihood
  - $`f(x;\theta)`$ : a neural network model
    - where $`\omega = f(x;\theta)`$ : the output provides the parameters for a distribution over $`y`$
      - e.g.) $`\mu, \sigma^2`$
    - Thus, our loss function can be interpreted as $`-\log{p(y|\omega(x))}`$

#### Concept) Heteroscedastic Model
- Def.)
  - A model that predicts a different amount of variance in $`y`$ for different values of $`x`$.
  - The specification of variance is the output of the function $`f(\mathbf{x}|\theta)`$
- Tech.) How to represent the variance?
  1. Diagonal precision matrix $`\textrm{diag}(\beta)`$ where $`\beta = \frac{1}{\sigma^2}`$
     - The covariance matrix must be ensured to be [positive definite](../../ch02/07/note.md#concept-positivenegative-definite).
       - Why?)
         - The eigenvalues of the precision matrix are the reciprocals of the eigenvalues of the covariance matrix.
         - i.e.) The precision matrix should be positive as well.
     - e.g.) 
       - Suppose $`a`$ is the raw activation of the model used to determine the diagonal precision.
       - Then, we can use the softplus function to obtain a positive precision vector $`\beta = \varsigma(a)`$
  2. Non-Diagonal Case
     - If the covariance is full and conditional, then a parametrization must be chosen that guarantees positive definiteness of the predicted covariance matrix.
       - i.e.) $`\Sigma(x) = B(x)B^\top(x)`$ where $`B`$ is an unconstrained square matrix
     - In this case, since the matrix is full ranked, the computation of the likelihood is costly.
       - e.g.) $`d\times d`$ requires $`O(d^3)`$ computation for... 
         - the determinant
         - the inverse of $`\Sigma(x)`$
         - the eigenvalue decomposition of $`B(x)`$.

<br>

#### Concept) Gaussian Mixture
- Def.)
  - A representation for a conditional distribution $`p(y|x)`$ that can have several different peaks in $`y`$ space for the same value of $`x`$
    - $`\displaystyle p(y|x) = \sum_{i=1}^n p(c=i|x) \mathcal{N}(y;\mu^{(i)},\Sigma^{(i)}(x))`$
      - where $`n`$ is the number of mixture components $`p(c=i|x)`$

#### Concept) Mixture Density Network
- Def.)
  - A neural network with [Gaussian Mixture](#concept-gaussian-mixture) as its output.
- Props.)
  - It must have three outputs.
    1. A vector defining $`p(c=i|x)`$
    2. A matrix providing $`\mu^{(i)}(x)`$
    3. A tensor providing $`\Sigma^{(i)}(x)`$
  - Constraints
    - Mixture components $`p(c=i|x)`$
      - They must form a multinoulli distribution over the $`n`$ different components associated with latent variable $`c`$.
      - Thus, they can be simply obtained by a [softmax](#6223-softmax-units-for-multinoulli-output-distributions) over an $`n`$-dimensional vector.
    - Means $`\mu^{(i)}(x)`$
      - They indicate the mean associated with the $`i`$-th Gaussian components.
      - They are unconstrained.
      - For $`y\in\mathbb{R}^d`$, $`\mu^{(i)}(x) \in \mathbb{R}^{n\times d}`$
      - In practice, we do not know which component produced each observation. 
      - The expression for the negative log-likelihood naturally weights each example’s contribution to the loss for each component by the probability that the component produced the example.
    - Covariances $`\Sigma^{(i)}(x)`$
      - We typically use a diagonal matrix to avoid needing to compute determinants. 
      - As with learning the means of the mixture, maximum likelihood is complicated by needing to assign partial responsibility for each point to each mixture component. 
      - Gradient descent will automatically follow the correct process if given the correct specification of the negative log-likelihood under the mixture model.
  - Gradient-based optimization of conditional Gaussian mixtures (on the output of neural networks) can be unreliable, in part because one gets divisions (by the variance) which can be numerically unstable (when some variance gets to be small for a particular example, yielding very large gradients). 
    - Sols.)
      - Clip gradients (cf. 10.11.1) 
      - Scale the gradients heuristically


<br>

* [Back to Deep Learning MIT](../../main.md)