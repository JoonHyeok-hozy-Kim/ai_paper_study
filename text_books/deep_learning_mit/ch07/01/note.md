* [Back to Deep Learning MIT](../../main.md)

# 7.1 Parameter Norm Penalties

### Concept) Regularization in Deep Learning
- Def.)
  - Recall our [previous definition](../../ch05/02/note.md#concept-regularization).
  - Reducing the generalization error, not the training error.
- Props.)
  - Regularization of an estimator works by trading **increased** [bias](../../ch05/04/note.md#concept-bias) for **reduced** [variance](../../ch05/04/note.md#concept-variance-and-standard-error-of-estimator).
    - Recall the three situations regarding [underfitting and overfitting](../../ch05/02/note.md#concept-underfitting-vs-overfitting).
      - A model is trained either...
        - (1) excluded the true data generating process—corresponding to underfitting and inducing bias
          - i.e.) Underfitted
        - (2) matched the true data generating process
          - i.e.) Ideal Learning
        - (3) included the generating process but also many other possible generating processes
          - i.e.) Overfitted
      - The goal of regularization is to take a model from the (3) into the (2).

<br>

### Concept) Parameter Norm Penalty
- Desc.)
  - Used for regularization approaches based on limiting the capacity of models.
    - e.g.) neural networks, linear regression, or logistic regression
- In the Objective Function)
  - $`\tilde{J}(\theta; X, y) = J(\theta; X,y) + \alpha\Omega(\theta)`$
    - where
      - $`J(\theta; X,y)`$ : the standard objective function
      - $`\Omega(\theta)`$ : a parameter norm penalty
        - where $`\theta`$ denotes all of the parameters including weights $`w`$
      - $`\alpha\in[0,\infty)`$ : a hyperparameter that weights the relative contribution of the norm penalty term $`\Omega`$
- Props.)
  - For neural networks, we typically choose to use a parameter norm penalty $`\Omega`$ that **penalizes only the weights of the affine transformation at each layer** and **leaves the biases unregularized**.
    - Why?)
      - The **biases** typically require less data to fit accurately than the **weights**.
        - Each bias controls only a single variable.
      - On the other hand, each **weight** specifies how two variables interact.
        - Thus, fitting the weight well requires observing both variables in a variety of conditions.
      - Therefore, we do not induce too much variance by leaving the **biases** unregularized.
      - Also, regularizing the **bias** parameters can introduce a significant amount of underfitting.
  - $`w`$ indicates all of the **weights** that should be affected by the norm penalty.
    - The vector $`\theta`$ denotes all of the parameters.
  - In the context of neural networks, it is sometimes desirable to use a separate penalty with a different α coefficient for each layer of the network. 
    - Why?) It can be expensive to search for the correct value of multiple hyperparameters.
    - Still, it is reasonable to use the same weight decay at all layers just to reduce the size of search space.









<br>

* [Back to Deep Learning MIT](../../main.md)