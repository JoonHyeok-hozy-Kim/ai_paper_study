* [Back to Dive into Deep Learning](../../main.md)

# 5.5 Generalization in Deep Learning

### Review) Classical Learning vs Deep Learning 
- Classical Learning Theories
  - Linear Regression
  - Classification
- Procedures of the Classical Learning Theories
  1. Fitting the training data using methods like maximum likelihood parameters.
  2. Discovering general patterns from the dataset.
  3. Making predictions based on those patterns.
- Props.)
  - In classical methods, procedures for optimizing linear models and the statistical properties of the solutions are both described well by a comprehensive body of theory.
    - On the other hand, **deep learning** theories do not have strict explanations like the above...
      - i.e.) We do not know 
        - why the deep learning methods are able to optimize neural networks
        - how models learned by gradient descent manage to generalize so well, even on high-dimensional tasks
      - But it practice, they work well...
  - Overfitting Problem)
    - Recall that the classical models have the overfitting problem.
      - i.e.)
        - The difference between our **fit on the training data** and our **fit on the test data** is called the generalization gap and when this is large, we say that our models overfit to the training data.
    - In the classical view, the interpretation of the overfitting is that our models are too complex.
    - As a remedy, we had to shrink either
      - the number of features
      - the number of nonzero parameters learned
      - the size of the parameters as quantified.
    - However, in the deep learning, the trade-off between the overfitting and the generalization does not exist...
      - e.g.)
        - For classification problems, the deep learning models are typically expressive enough to perfectly fit every training example, even in datasets consisting of millions.
        - For many deep learning tasks (e.g., image recognition and text classification) we are typically choosing among model architectures, all of which can achieve arbitrarily **low training loss** (and zero training error).
        - It is often the case that despite **fitting the training data perfectly**, we can actually reduce the generalization error further by making the model even more **expressive**.
    - Therefore, the classical learning theory cannot explain why it is that deep neural networks generalize in the first place.

<br><br>

### Concept) Deep Learning vs Nonparametrics
#### Concept) Nonparametric
- Desc.)
  - Nonparametric methods tend to have a level of complexity that grows as the amount of available data grows.
- e.g.)
  - $k$-Nearest Neighbor Algorithm
    - How it works?)
      - At training time, the learner simply memorizes the dataset.
      - At prediction time, when confronted with a new point $\mathbf{x}$, the learner looks up the $k$ nearest neighbors.
        - We should specify some distance function $d$ that we specify some vector-valued basis function $\phi(\mathbf{x})$ for featurizing our data.
        - For any choice of the distance metric, we will achieve zero training error and eventually reach an optimal predictor.
        - However, different distance metrics $d$ encode different inductive biases and with a finite amount of available data will yield different predictors.

#### Analysis) Connection between large neural networks and nonparametric methods
*Jacot et al. (2018)*
- In the limit, as multilayer perceptrons with randomly initialized weights grow infinitely wide, they become equivalent to (nonparametric) kernel methods for a specific choice of the kernel function (essentially, a distance function), which they call the **neural tangent kernel**.

<br><br>

### Concept) Early Stopping
- Desc.)
  - A classic technique for regularizing deep neural networks
  - It constrains the number of epochs of training.
    - rather than directly constraining the values of the weights.
  - Theoretical Backgrounds)
    - *Zhang et al., 2021* : While deep neural networks are capable of fitting arbitrary labels, even when labels are assigned incorrectly or randomly, this capability only emerges over many iterations of training.
    - *Rolnick et al., 2017* : In the setting of label noise, neural networks tend to fit **cleanly labeled data first** and only **subsequently to interpolate the mislabeled data**.
    - *Garg et al., 2021* : Whenever a model has fitted the cleanly labeled data but not randomly labeled examples included in the training set, it has in fact generalized
- How?)
  - Monitor **validation error** throughout training (typically by checking once after each epoch) 
  - Cut off training when the validation error has not decreased by more than some small amount $\epsilon$ for some number of epochs.
    - A.K.A.) patience criterion

<br><br>

### Concept) Classical Regularization Methods
- Props.)
  - Recall the **weight decay** regularization methods for the classical learnings.
    - ridge regularization : $\ell_2$ penalty
    - lasso regularization : $\ell_1$ penalty
  - The benefits of regularization in deep learning implementations only make sense in **combination with the early stopping criterion**.
  - Still, the classical regularizers remain popular in deep learning implementations, even if the theoretical rationale for their efficacy may be radically different.


<br>

* [Back to Dive into Deep Learning](../../main.md)