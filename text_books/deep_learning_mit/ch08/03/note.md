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
  - Gradually decrease the learning rate $`\epsilon_k`$ at iteration $`k`$.
    - Why doing this?)
      - The SGD gradient estimator introduces a source of noise (the random sampling of m training examples) that does not vanish even when we arrive at a minimum.
        - cf.) For the batch gradient descents can reach 0 gradient, so the fixed learning rate is applicable.
    - Sufficient Condition)
      - $`\displaystyle \sum_{k=1}^\infty \epsilon_k = \infty \wedge \sum_{k=1}^\infty \epsilon_k^2 \lt \infty`$
      - How to implement this?)
        - Decay the learning rate linearly until iteration $`\tau`$:
          - $`\epsilon`$











<br>

* [Back to Deep Learning MIT](../../main.md)