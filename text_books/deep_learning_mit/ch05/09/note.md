* [Back to Deep Learning MIT](../../main.md)

# 5.9 Stochastic Gradient Descent
- Desc.)
  - Large datasets are
    - necessary for good generalization
    - **computationally costly**.
      - Why?)
        - Recall that cost function used by a ML algorithm often decomposes as a sum over training examples of some per-example loss function.
          - $`\displaystyle J(\theta) = \mathbb{E}_{\mathbf{x},y\sim\hat{p}_{\textrm{data}}} L(x,y,\theta) = \frac{1}{m}\sum_{i=1}^m L\left(x^{(i)},y^{(i)},\theta\right)`$
            - where $`L`$ is the per-example loss $`L(x,y,\theta) = -\log{p(y|x;\theta)}`$.
        - Then the gradient can be calculated as
          - $`\displaystyle \nabla_\theta J(\theta) = \frac{1}{m}\sum_{i=1}^m \nabla_\theta L\left(x^{(i)},y^{(i)},\theta\right)`$
            - which cost is $`O(m)`$
- Derivation)
  - Instead, sample a minibatch of examples of size $`m'`$ uniformly drawn from the training set.
    - $`\mathbb{B} = \left\{ x^{(1)}, \cdots, x^{(m')} \right\}`$
    - $`m'`$ is usually held fixed as the training set size $`m`$ grows.
  - Then the estimate of the gradient is formed as
    - $`\displaystyle g = \frac{1}{m'} \nabla_\theta\sum_{i=1}^{m'} L\left(x^{(i)},y^{(i)},\theta\right)`$.
  - Thus, the gradient descent goes
    - $`\theta \leftarrow \theta - \epsilon g`$
      - where $`\epsilon`$ is the learning rate.
- Props.)
  - The optimization algorithm may not be guaranteed to arrive at even a local minimum in a reasonable amount of time, but it often finds a very low value of the cost function quickly enough to be useful.
  - For a fixed model size, the cost per SGD update does not depend on the training set size $`m`$.
  - The asymptotic cost of training a model with SGD is $`O(1)`$ as a function of $`m`$.
    - Why?)
      - The number of updates required to reach convergence usually increases with training set size.
      - However, as $`m`$ approaches infinity, the model will eventually converge to its best possible test error before SGD has sampled every example in the training set.
      - Increasing $`m`$ further will not extend the amount of training time needed to reach the model’s best possible test error.
    - cf.) Kernel Trick
      - Prior to the advent of deep learning, the main way to learn nonlinear models was to use the **kernel trick** in combination with a linear model.
      - Many kernel learning algorithms require constructing an $`m\times m`$ matrix $`G_{i,j} = k(x^{(i)}, x^{(j)})`$













<br>

* [Back to Deep Learning MIT](../../main.md)