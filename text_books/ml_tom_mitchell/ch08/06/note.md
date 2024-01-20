* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 8.6 Remarks on Lazy and Eager Learning

### Concept) Lazy Learning Methods
- Def.)
  - Learning methods that defer the decision of how to generalize beyond the training data until each new query instance is encountered.
- e.g.)
  - [k-Nearest Neighborhood Algorithm](../02/note.md#concept-k-nearest-neighbor-algorithm)
  - [Locally Weighted Regression](../03/note.md#83-locally-weighted-regression)
  - [Case-Based Reasoning](../05/note.md#concept-case-based-reasoning-cbr)

### Concept) Eager Learning Methods
- Def.)
  - Learning methods that generalize beyond the training data before observing the new query, committing at training time to the network structure and weights that define their approximations to the target functions.
- e.g.)
  - [Radial Basis Function](../04/note.md#concept-radial-basis-function-rbf)
  - Every other algorithm discussed before including [the Backpropagation algorithm](../../ch04/05/note.md#452-the-backpropagation-algorithm).

<br>

### Analysis) Lazy vs Eager Learning Method
1. Computation Time
   - Lazy methods will generally require less computation during training, but more computation when they must predict the target value for a new query.
2. The Classifications Results for New Queries
    |Methods|Lazy Methods|Eager Methods|
    |:-:|:-|:-|
    |When $x_q$ is queried.|Lazy methods may consider the query instance $x_q$, when deciding how to generalize beyond the training data $D$.|Eager methods cannot. By the time they observe the query instance $x_q$, they have already chosen their (global) approximation to the target function.|
    |Result|A lazy learner has the option of (implicitly) representing the target function by **a combination of many local approximations**.|An eager learner must commit at training time to **a single global approximation**.|

<br>

### Analysis) Eager Methods that Use Multiple Local Approximations?
- Candidate)
  - [Radial Basis Function](../04/note.md#84-radial-basis-functions) Network
    - Recall that RBF commits to **a global approximation** to the target function at training time.
      - where **the global function** is represented as a linear combination of multiple **local kernel functions**.
    - Nevertheless, because RBF learning methods must commit to the hypothesis before the query point is known, the local approximations they create are not specifically targeted to the query point to the same degree as in a lazy learning method.
      - Instead, RBF networks are built eagerly from local approximations centered around the training examples, or around clusters of training examples, but not around the unknown future query points.


<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)