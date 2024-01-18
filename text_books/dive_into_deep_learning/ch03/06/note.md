* [Back to Dive into Deep Learning](../../main.md)

# 3.6 Generalization

#### Concept) Overfitting
The phenomenon of fitting closer to our training data than to the underlying distribution is called overfitting.

<br>

#### Concept) Regularization
Techniques for combatting [overfitting](#concept-overfitting) are often called [regularization methods](../07/note.md#37-weight-decay).

<br><br>

## 3.6.1 Training Error and Generalization Error
- Settings)
  - $R_{emp}$ : the training error calculated on the training dataset
  - $R$ : the generalization error which is an expectation taken w.r.t. the underlying distribution
- Then $R_{emp}$ and $R$ can be expressed as below.
  - $`R_\textrm{emp}[\mathbf{X}, \mathbf{y}, f] = \frac{1}{n} \sum_{i=1}^n l(\mathbf{x}^{(i)}, y^{(i)}, f(\mathbf{x}^{(i)}))`$
    - The sum of errors calculated from the training dataset.
  - $`R[p, f] = E_{(\mathbf{x}, y) \sim P} [l(\mathbf{x}, y, f(\mathbf{x}))] =
   \int \int l(\mathbf{x}, y, f(\mathbf{x})) p(\mathbf{x}, y) \;d\mathbf{x} dy`$
    - The sum(integral) of errors from an infinite stream of additional data examples drawn from the same underlying data distribution.
    - But nobody knows what the pdf of the underlying distribution, $p(\mathbf{x}, y)$, is.
- Concept) Generalization Gap
  - $R_{emp}-R$
- Question)
  - When should we expect our training error to be close to the population error?

<br>

### 3.6.1.1 Model Complexity
#### Prop.) Complexity of a Model and the Size of the Data
- When we have simple models and abundant data, the training and generalization errors tend to be close. 
- When we work with more complex models and/or fewer examples, we expect the training error to go down but the generalization gap to grow.

<br>

#### Objective)
A hypothesis that **could not explain** any observations we might conceivably make and yet nevertheless **happens to be compatible with** those observations that we in fact make.

<br><br>

## 3.6.2 Underfitting or Overfitting?
### Concept) Underfitting
- Situation)
  - The training error and the validation error are both substantial but there is a little gap between them $(R_{emp}\approx R)$.
- Prop.)
  - If the model is unable to reduce the training error, that could mean that our model is too simple to capture the pattern that we are trying to model.
    - i.e.) insufficiently expressive
    - Need more complex model!

<br>

### Concept) Overfitting
- Situation)
  - The training error is significantly lower than the validation error.
- Props.)
  - Overfitting is not always a bad thing
    - In deep learning especially, the best predictive models often perform far better on training data than on holdout data.
    - Ultimately, we usually care about driving the generalization error lower, and only care about the generalization gap insofar as it becomes an obstacle to that end.

<br>

### 3.6.2.1 Polynomial Curve Fitting
- Props.)
  - A higher-order polynomial function is more **complex** than a lower-order polynomial function, since the higher-order polynomial has more parameters and the model function’s selection range is wider.
  - Higher-order polynomial functions should always achieve lower (at worst, equal) training error relative to lower-degree polynomials.   
    ![](images/001.png)

<br>

### 3.6.2.2 Dataset Size
- Props.)
  - As we increase the amount of training data, the generalization error typically decreases.
  - In general, more data never hurts.

<br><br>

## 3.6.3 Model Selection
#### Concept) Model Selection
- Choosing among many models is called model selection.
  - Many Models?
    - Different architectures, training objectives, selected features, data preprocessing, learning rates, and other hyper parameters
- How do we choose?
  - Split data into Training / Validation / Test dataset.
  - Use validation set to choose the model.
    - Why not use the test dataset?
      - To prevent overfitting the test data
      - Adopt a separate data set called the validation set to choose the best hyper parameters.


<br>

### 3.6.3.1 Cross-Validation
- Why needed?)
  - What if the training data is so scarce that we cannot afford a validation set separately?
- e.g.) [K-Fold Cross Validation](#concept-k-fold-cross-validation)

<br>

#### Concept) K-Fold Cross Validation
- Procedure)
  - Split data into $K$ non-overlapping subsets.
  - For each subset $i\in \lbrace 1, 2, \cdots, K\rbrace$...
    - Use $i$-th subset on the validation and the rest $K-1$ subsets on training.
  - Average over the results from the $K$ experiments.



<br>

* [Back to Dive into Deep Learning](../../main.md)