* [Back to Deep Learning MIT](../../main.md)

# 8.1 How Learning Differs from Pure Optimization

### Concept) Indirectness of Machine Learning Optimization
- In the pure optimization problems, the goal is to optimize the cost function $`J`$.
- However, in machine learning, the goal is to optimize the performance measure $`P`$.
  - The problem is that $`P`$ is defined w.r.t. the **test set**.
  - Thus, we should optimize $`P`$ indirectly by reducing a different [cost function](#concept-cost-function-in-machine-learning) $`J(\theta)`$.
    - But optimizing $`J(\theta)`$ does NOT guarantee the optimization of $`P`$.

<br>

### Concept) Cost Function in Machine Learning
- Def.)
  - $`J(\theta) \equiv \mathbb{E}_{(x,y)\sim\hat{p}_{\textrm{data}}} L(f(x;\theta), y)`$ : the cost function over the training set
    - where
      - $`\hat{p}_{\textrm{data}}`$ : the training set
      - $`L`$ : the per-example loss function
      - $`f(x;\theta)`$ : the predicted output when the input is $`x`$
      - $`y`$ : the target output in the supervised learning
  - $`J^\ast (\theta) \equiv \mathbb{E}_{(x,y)\sim p_{\textrm{data}}} L(f(x;\theta), y)`$ : the cost function over the data generating distribution
    - where
      - $`p_{\textrm{data}}`$ : the data generating distribution

<br>

## 8.1.1 Empirical Risk Minimization
### Concept) Risk
- Desc.)
  - The goal of a machine learning algorithm is to reduce the expected generalization error given by equation 
    - $`J^\ast (\theta) \equiv \mathbb{E}_{(x,y)\sim p_{\textrm{data}}} L(f(x;\theta), y)`$
  - This quantity is known as the **risk**.

<br>

### Concept) Empirical Risk
- Def.)
  - Expected loss on the training set
    - $`\displaystyle\mathbb{E}_{x,y\sim\hat{p}_{\textrm{data}}(x,y)} \left[ L(f(x;\theta), y) \right] = \frac{1}{m}\sum_{i=1}^m L\left(f\left(x^{(i)}; \theta\right), y^{(i)}\right)`$
      - where $`m`$ is the number of training examples.

<br>

### Concept) Empirical Risk Minimization
- Def.)
  - The training process based on minimizing [average training error](#concept-empirical-risk)
- Desc.)
  - The expectation of [the risk](#concept-risk) is taken over the true underlying distribution $`p_{\textrm{data}}`$.
  - If we knew the true distribution $`p_{\textrm{data}}(x,y)`$, [risk](#concept-risk) minimization would be an optimization task solvable by an optimization algorithm.
  - However, when we do not know $`p_{\textrm{data}}(x,y)`$ but only have a **training set** of samples, we have a machine learning problem.
  - The simplest way to convert a machine learning problem back into an optimization problem is to minimize the **expected loss on the training**, i.e. the [empirical risk](#concept-empirical-risk)
- Drawbacks)
  - Empirical risk minimization is prone to [overfitting](../../ch05/02/note.md#concept-underfitting-vs-overfitting).
    - Why?)
      - Models with high capacity can simply memorize the training set.
  - In many cases, empirical risk minimization is not really feasible.
    - Why?)
      - Many useful loss functions, such as 0-1 loss, have no useful derivatives.
      - Thus, the most effective modern optimization algorithms based on gradient descent are not applicable.
- Props.)
  - Due to critical drawbacks above, we must use a slightly different approach.

<br><br>

## 8.1.2 Surrogate Loss Functions and Early Stopping
### Concept) Surrogate Loss Function
- Def.)
  - A proxy for the target loss function, which is usually intractable.
- e.g.)
  - Exactly minimizing the expected 0-1 loss is typically intractable even for a linear classifier.
    - The negative log-likelihood of the correct class is used as the **surrogate loss function**.
    - The negative log-likelihood allows the model to estimate the conditional probability of the classes, given the input, and if the model can do that well, then it can pick the classes that yield the least classification error in expectation.
- Props.)
  - In some cases, a surrogate loss function results in being able to learn more.
    - e.g.) Using the **log-likelihood surrogate** to train the 0-1 loss.
      - Even after the **training set** 0-1 loss has reached zero, the **test set** 0-1 loss often continues to decrease for a long time.
      - This is because even when the expected 0-1 loss is zero, one can **improve the robustness** of the classifier by further pushing the classes apart from each other
        - i.e.)
          - obtaining a more confident and reliable classifier
          - extracting more information from the training data than would have been possible by simply minimizing the average 0-1 loss on the training set.
  - Early Stopping problem.
    - Recall that in [the empirical risk minimization](#concept-empirical-risk-minimization), we optimize for the training data, not the data generating distribution.
    - Then the training algorithms do not usually halt at a local minimum.
    - Instead, a machine learning algorithm usually minimizes a surrogate loss function but halts when a convergence criterion based on [early stopping](../../ch07/08/note.md#78-early-stopping) is satisfied.
    - Typically the early stopping criterion is based on the true underlying loss function, not the **surrogate loss function**.
    - Thus, training often halts while the surrogate loss function still has large derivatives.

<br><br>

## 8.1.3 Batch and Minibatch Algorithms
- Prop.)
  - The objective functions of ML algorithms usually decomposes as a sum over the training examples.
    - why?) They use **only a subset** of the terms of the full cost function for computing each update to the parameters.
    - e.g) Maximum Likelihood estimation
      - $`\displaystyle \theta_{ML} = \arg\max_\theta \sum_{i=1}^m \log p_{\textrm{model}} \left( x^{(i)}, y^{(i)}; \theta \right)`$
        - Maximizing this sum is equivalent to maximizing the **expectation** over the empirical distribution defined by the training set:
          - $`J(\theta) = \mathbb{E}_{\mathbf{x, y}\sim\hat{p}_{\textrm{data}}} \log p_{\textrm{model}} \left( x, y; \theta \right)`$
    - Efficiency
      - e.g.) Consider the problem of getting the gradient as
        - $`\nabla_\theta J(\theta) = \mathbb{E}_{\mathbf{x, y}\sim\hat{p}_{\textrm{data}}} \nabla_\theta \log p_{\textrm{model}} \left( x, y; \theta \right)`$
          - Consider that the sample standard error of the mean was $`\sigma/\sqrt{n}`$.
          - Thus, if we compare the training set of sizes $`\begin{cases} n_1 = 100 \\ n_2 = 10000 \end{cases}`$, $`n_2`$ requires 100 times more computation for reducing the standard error of the mean only by a factor of 10.

<br>

#### Concept) Batch Gradient Method (Deterministic Gradient Method) 
- Def.)
  - Optimization algorithms that use the entire training set.

<br>

#### Concept) Stochastic Gradient Method (Online Gradient Method)
- Def.)
  - Optimization algorithms that use only a single example at a time.
  - The term **online** is usually reserved for the case where the examples are drawn from a stream of continually created examples rather than from a fixed-size training set over which several passes are made.

<br>

### Tech.) Factors for Setting Minibatch Sizes
- Larger batches provide a more accurate estimate of the gradient.
  - But the returns are NOT linear.
- Multicore architectures are usually underutilized by extremely **small batches**. 
  - This motivates using some absolute **minimum** batch size, below which there is no reduction in the time to process a minibatch.
- If all examples in the batch are to be processed in parallel (as is typically the case), then the amount of memory scales with the batch size. 
  - For many hardware setups this is the limiting factor in batch size.
- Some kinds of hardware achieve better runtime with specific sizes of arrays. 
  - GPU
    - it is common for power of 2 batch sizes to offer better runtime. 
    - Typical power of 2 batch sizes range from 32 to 256, with 16 sometimes being attempted for large models.
- Small batches can offer a [regularizing](../../main.md/#7-regularization-for-deep-learning) effect, perhaps due to the **noise** they add to the learning process. 
  - Generalization error is often best for a batch size of 1. 
  - Training with such a **small batch size** might require a **small learning rate** to maintain stability due to the high variance in the estimate of the gradient. 
  - The total runtime can be very high due to the need to make more steps, both because of the reduced learning rate and because it takes more steps to observe the entire training set.

<br>

### Prop.) Sensitivity to Sampling Errors
- Some algorithms are more sensitive to sampling error than others.
  - Why?)
    - Some use information that is difficult to estimate accurately with few samples.
    - Some use information in ways that amplify sampling errors more.
  - e.g.)
    - Methods that compute updates based only on the gradient $`\mathbf{g}`$ are usually relatively robust and can handle smaller batch sizes like 100.
    - Second-order methods, which use also the Hessian matrix $`H`$ and compute updates such as $`H^{−1}\mathbf{g}`$, typically require much larger batch sizes like 10,000.
      - These large batch sizes are required to minimize fluctuations in the estimates of $`H^{−1}\mathbf{g}`$.
      - If $`H`$ is estimated perfectly but has a poor condition number, the multiplication by $`H^{-1}`$ amplifies pre-existing estimation errors in $`\mathbf{g}`$.
        - Thus, very small change in the estimate of $`\mathbf{g}`$ can cause large changes in the update $`H^{-1}\mathbf{g}`$
- Minibatches must be selected randomly.
  - why?)
    - Computing an **unbiased estimate** of the expected gradient from a set of samples requires that those **samples be independent**.
    - We also wish for two subsequent gradient estimates to be independent from each other, so two subsequent minibatches of examples should also be independent from each other.
- We can compute entire separate updates over different examples in parallel.
  - i.e.)
    - Simultaneously computing the update that minimize $`J(X_1)`$, we can compute update for other minibatches $`X_2, X_3, \cdots`$ and so on.
- **Minibatch Stochastic Gradient Descent** follows the gradient of the true generalization error so long as no examples are repeated.


<br>

* [Back to Deep Learning MIT](../../main.md)