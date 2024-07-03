* [Back to Deep Learning MIT](../../main.md)

# 7.12 Dropout

#### Desc.)
- A computationally inexpensive but powerful method of [regularizing](../01/note.md#concept-regularization-in-deep-learning) a broad family of models
- A method of making [bagging](../11/note.md#concept-bagging-bootstrap-aggregating) practical for [ensembles](../11/note.md#concept-model-averaging-strategy-ensemble-model) of very many large neural networks
  - Recall that [bagging](../11/note.md#concept-bagging-bootstrap-aggregating) involves training multiple models, and evaluating multiple models on each test example.
  - This can be **impractical** when each model is a **large neural network**.
    - why?) Training and evaluating such networks is costly in terms of runtime and memory.
  - **Dropout** provides an inexpensive approximation to training and evaluating a [bagged ensemble](../11/note.md#concept-bagging-bootstrap-aggregating) of exponentially many neural networks.
    - How?)
      - Set up ensembles consisting of all sub-networks that can be formed by removing non-output units from an underlying base network.   
        ![](images/001.png)
        - cf.) There are multiple ways to remove a unit
          - We can effectively remove a unit from a network by **multiplying its output value by zero**.
          - For the [radial basis function](../../ch05/07/note.md#eg-gaussian-kernel-radial-basis-function-rbf) networks, take the difference between the unit's state and some reference value.













<br>

* [Back to Deep Learning MIT](../../main.md)