* [Back to Dive into Deep Learning](../../main.md)

# 3.6 Generalization

#### Concept) Overfitting
The phenomenon of fitting closer to our training data than to the underlying distribution is called overfitting.

<br>

#### Concept) Regularization
Techniques for combatting [overfitting](#concept-overfitting) are often called regularization methods.

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
- Question)
  - When should we expect our training error to be close to the population error?

<br>

### 3.6.1 Model Complexity
#### Prop.) Complexity of a Model and the Size of the Data
- When we have simple models and abundant data, the training and generalization errors tend to be close. 
- When we work with more complex models and/or fewer examples, we expect the training error to go down but the generalization gap to grow.



<br>

* [Back to Dive into Deep Learning](../../main.md)