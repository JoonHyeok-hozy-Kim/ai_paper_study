* [Back to Deep Learning MIT](../../main.md)

# 7.9 Parameter Tying and Parameter Sharing
#### Objective)
- Find ways to describe dependencies between model parameters

### Concept) Dependency of Closeness
- Desc.)
  - A common type of dependency that we often want to express is that certain parameters should be close to one another.
  - If the task of two models are similar enough, we may assume that the model parameters should be close to each other.

#### Tech. 1) Parameter Tying
- Settings)
  - Model $`A`$ with parameters $`w^{(A)}`$
    - $`\hat{y}^{(A)} = f(w^{(A)}, x)`$
  - Model $`B`$ with parameters $`w^{(B)}`$
    - $`\hat{y}^{(B)} = g(w^{(B)}, x)`$
- Target)
  - We want to express $`w_i^{(A)}\approx w_i^{(B)}, \forall i`$
- Sol.)
  - Use [parameter norm penalty (regularization)](../01/note.md#concept-parameter-norm-penalty).
    - e.g.) $`L^2`$ Penalty
      - $`\Omega(w^{(A)}, w^{(B)}) = ||w^{(A)} - w^{(B)}||_2^2`$
- Usage)
  - *Lasserre et al. (2006)* regularized the parameters of one model, trained as a classifier in a supervised paradigm, to be close to the parameters of another model, trained in an unsupervised paradigm (to capture the distribution of the observed input data).

<br>

#### Tech. 2) Parameter Sharing
- Desc.)
  - Force sets of parameters to be equal.
  - Various models or model components are sharing a unique set of parameters.
- Advantage)
  - Only a subset of the parameters (the unique set) need to be stored in memory.
    - This can lead to significant reduction in the memory footprint of the model.
    - e.g.) Convolutional Neural Networks (CNN)



<br>

* [Back to Deep Learning MIT](../../main.md)