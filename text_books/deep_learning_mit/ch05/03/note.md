* [Back to Deep Learning MIT](../../main.md)

# 5.3 Hyperparameters and Validation Sets

### Concept) Hyperparameters
- Desc.)
  - Settings that we can use to control the behavior of the machine learning algorithms.
- e.g.)
  - The degree of the polynomial, which acts as a parameter.
  - $`\lambda`$ that controls the strength of [weight decay](../02/note.md#eg-weight-decay).

<br>

### Concept) Validation Set
- Def.)
  - The subset of data used to guide the selection of hyperparameters
- Desc.)
  - The setting must be a hyperparameter because it is not appropriate to learn that hyperparameter on the training set.
  - If learned on the training set, such hyperparameters would always choose the maximum possible model capacity, resulting in overfitting.
    - e.g.) Higher degree polynomial and $`\lambda = 0`$
  - Thus, it is important that the test examples are not used in any way to make choices about the model, including its hyperparameters.
  - To solve this problem, we need a **validation set** of examples that the training algorithm does not observe.
  - We always construct the validation set from the training data.
    - We split the training data into two disjoint subsets.
      - One of these subsets is used to learn the parameters. 
      - The other subset is our validation set, used to estimate the generalization error during or after training
      - Typically, one uses about 80% of the training data for training and 20% for validation.
 
<br><br>

### Concept) Cross-Validation
- Desc.)
  - When the dataset is too small, we may repeat the training and testing computation on different randomly chosen subsets or splits
 of the original dataset.
- e.g.)
  - k-fold cross-validation







<br>

* [Back to Deep Learning MIT](../../main.md)