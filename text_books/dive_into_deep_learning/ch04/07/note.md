* [Back to Dive into Deep Learning](../../main.md)

# 4.7. Environment and Distribution Shift

## 4.7.1 Types of Distribution Shift
- Assumption)
  - The training data was sampled from some distribution $p_S(\mathbf{x}, y)$
  - The test data consists of unlabeled examples drawn from $p_T(\mathbf{x}, y)$

### 4.7.1.1 Covariate Shift
- Assumption)
  - The distribution of inputs may change over time.
  - The labeling function does not change.
    - e.g.) the conditional distribution $P(y|\mathbf{x})$
- Prop.)
  - The problem arises due to a shift in the distribution of the covariates (features).
- e.g.)
  - The training set consists of photos, while the test set contains only cartoons.
  - Training on a dataset with substantially different characteristics from the test set can spell trouble absent a coherent plan for how to adapt to the new domain.


### 4.7.1.2 Label Shift
### 4.7.1.3 Concept Shift















<br>

* [Back to Dive into Deep Learning](../../main.md)