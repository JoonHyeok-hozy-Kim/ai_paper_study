* [Back to Deep Learning MIT](../../main.md)

# 8.3 Basic Algorithms

## 8.3.1 Stochastic Gradient Descent
- Previous Desc.)
  - [Minibatch in 5.9.1](../../ch05/09/note.md#59-stochastic-gradient-descent)
    - $`\theta \leftarrow \theta - \epsilon g`$
      - where
        - $`\displaystyle g = \frac{1}{m'} \nabla_\theta\sum_{i=1}^{m'} L\left(x^{(i)},y^{(i)},\theta\right)`$
        - $`\epsilon`$ : the learning rate
  - [Minibatch in 8.1.3](../../ch08/01/note.md#813-batch-and-minibatch-algorithms)
    - SGD can obtain an **unbiased** estimate of the gradient by taking the average gradient on a minibatch of m examples drawn i.i.d from the data generating distribution.
- Algorithm)
  - Hyper Parameter
    - $`\epsilon_k`$ : the learning rate
  - Procedure)
    - Initialize $`\theta`$.
    - `while` stopping criterion not met `do`
      - Sample a minibatch of $`m`$ examples from the training set $`\{x^{(1)}, \cdots, x^{(m)}\}`$ with corresponding targets $`h^{(i)}`$.
      - Compute gradient estimate as
        - $`\displaystyle\hat{g} \leftarrow \hat{g} + \frac{1}{m}\nabla_\theta \sum_{i=1}^m L\left( f(x^{(i)};\theta), y^{(i)}\right)`$.
      - Apply update as
        - $`\theta \leftarrow \theta - \epsilon\hat{g}`$
    - `end while`
- Desc.)
  - Gradually decrease the **learning rate** $`\epsilon_k`$ at iteration $`k`$.
    - Why doing this?)
      - The SGD gradient estimator introduces a source of noise (the random sampling of m training examples) that does not vanish even when we arrive at a minimum.
        - cf.) For the batch gradient descents can reach 0 gradient, so the fixed learning rate is applicable.
    - Sufficient Condition)
      - $`\displaystyle \sum_{k=1}^\infty \epsilon_k = \infty \wedge \sum_{k=1}^\infty \epsilon_k^2 \lt \infty`$
      - How to implement this?)
        - Decay the learning rate linearly until iteration $`\tau`$:
          - $`\epsilon_k = (1-\alpha)\epsilon_0` + \alpha \epsilon_\tau`$
            - where $`\alpha = \frac{k}{\tau}`$
        - e.g.) Linear schedule
          - We should set $`\epsilon_0, \epsilon_\tau, \textrm{ and } \tau`$.
            - $`\tau`$ may be set to the number of iterations required to make a few hundred passes through the training set.
            - $`\epsilon_\tau`$ should be set to roughly 1% of the value of $`\epsilon_0`$.
            - $`\epsilon_0`$ should be chosen arbitrarily.
              - Monitor the first several iterations and use a learning rate that is higher than the best-performing learning rate at this time, but not so high that it causes severe instability.
                - Why?)
                  - If it is too large, the learning curve will show violent oscillations, with the cost function often increasing significantly. 
                    - Gentle oscillations are fine, especially if training with a stochastic cost function such as the cost function arising from the use of dropout. 
                    - If the learning rate is too low, learning proceeds slowly, and if the initial learning rate is too low, learning may become stuck with a high cost value.
                    - Typically, the optimal initial learning rate, in terms of total training time and the final cost value, is higher than the learning rate that yields the best performance after the first 100 iterations or so.
- Props.)
  - Computation time per update does not grow with the number of training examples.
    - For a large enough dataset, SGD may converge to within some fixed tolerance of its final test set error before it has processed the entire training set.
  - Convergence rate measurement using the **excess error** $`J(\theta) - \min_\theta J(\theta)`$
    - In case of convex problem, the excess error is $`\displaystyle O\left(\frac{1}{\sqrt{k}}\right)`$ after $`k`$ iterations.
      - cf.) For the strongly convex case, it is $`\displaystyle O\left(\frac{1}{k}\right)`$
      - cf.) The Cramer-Rao bound states that generalization error cannot decrease faster than $`\displaystyle O\left(\frac{1}{k}\right)`$.
      - cf.) Bottou and Bousquet (2008) argue that it therefore may not be worthwhile to pursue an optimization algorithm that converges faster than $`\displaystyle O\left(\frac{1}{k}\right)`$.
        - Why?)
          - Faster convergence presumably corresponds to overfitting




<br>

* [Back to Deep Learning MIT](../../main.md)