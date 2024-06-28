* [Back to Deep Learning MIT](../../main.md)

# 7.5 Noise Robustness
### Tech.) Injecting noise to the **hidden units**
- In the general case, **noise injection** can be much more powerful than simply [shrinking the parameters](../01/note.md#concept-regularization-in-deep-learning).
- Refer to the [dropout algorithm](../12.note.md) for noise applied to the hidden units.

<br><br>

### Tech.) Injecting noise to weights
- It was primarily used in the context of recurrent neural networks.
- Interpretations)
  - A stochastic implementation of [Bayesian inference](../../ch05/06/note.md#56-bayesian-statistics) over the weights.
    - Desc.)
      - The Bayesian treatment of learning would consider the model weights to be uncertain and representable via a probability distribution that reflects this uncertainty. 
      - Adding noise to the weights is a practical, stochastic way to reflect this uncertainty.
  - A more traditional form of [regularization](../01/note.md#concept-regularization-in-deep-learning), encouraging stability of the function to be learned
    - e.g.) Regression Model
      - Settings)
        - $`\hat{y}(x)`$ : the model
        - $`y`$ : the target
        - $`\{(x^{(1)}, y^{(1)}), (x^{(2)}, y^{(2)}), \cdots, (x^{(m)}, y^{(m)}), \}`$ : $`m`$ training examples
        - $`J = \mathbb{E}_{p(x,y)}\left[ (\hat{y}(x)- y)^2 \right]`$ : the least-squares cost function
      - Adding Noise (Random Perturbation)
        - $`\epsilon_W \sim \mathcal{N}(\epsilon; 0, \eta I)`$ : the Gaussian noise on weights $`W`$
        - $`\hat{y}_{\epsilon_W}(x)`$ : the new model with noise
        - $`\begin{aligned}
            \hat{J}_W &= \mathbb{E}_{p(x,y,\epsilon_W)}\left[ (\hat{y}_{\epsilon_W}(x)- y)^2 \right] \\
            &= \mathbb{E}_{p(x,y,\epsilon_W)}\left[ \hat{y}_{\epsilon_W}(x)^2 -2y\hat{y}_{\epsilon_W}(x) - y^2 \right] \\
          \end{aligned}`$ : the new cost function
      - Optimization)
        - For small $`\eta`$, the minimization of $`\hat{J}_W`$ is equivalent to minimization of $`J`$ with an additional **regularization** term: $`\eta\mathbb{E}_{p(x,y)}\left[ ||\nabla_W \hat{y}(x)||^2 \right]`$
          - This regularization encourages the parameters to go to regions of parameter space where **small perturbations of the weights** have a relatively **small influence on the output**.
            - i.e.) It pushes the model into regions where the model is **relatively insensitive to small variations in the weights**, finding points that are not merely minima, but **minima surrounded by flat regions**.

<br><br>

### Tech.) Label Smoothing : Injecting noise at the output targets
- Ideation)
  - Most datasets have some amount of mistakes in the $`y`$ **labels**.
  - Thus, it can be harmful to maximize $`\log p(y | x)`$ when $`y`$ is a mistake.
  - One way to prevent this is to explicitly model the noise on the **labels**.
- Model)
  - Assume that for some small constant $`\epsilon`$, the training set label $`y`$ is correct with probability $`1-\epsilon`$.
    - Otherwise, any of the other possible labels might be correct.
    - Label smoothing regularizes a model based on a softmax with $`k`$ output values by replacing the hard $`0`$ and $`1`$ classification targets with targets of $`\frac{\epsilon}{k-1}`$ and $`1-\epsilon`$ respectively.
  - The standard cross-entropy loss may then be used with these soft targets.
  - Maximum likelihood learning with a softmax classifier and hard targets may actually never converge.
    - Why?)
      - The softmax can never predict a probability of exactly $`0`$ or exactly $`1`$, so it will continue to learn larger and larger weights, making more extreme predictions forever.
    - It is possible to prevent this scenario using other regularization strategies like [weight decay](../01/note.md#711-l2-parameter-regularization-weight-decay).


<br>

* [Back to Deep Learning MIT](../../main.md)