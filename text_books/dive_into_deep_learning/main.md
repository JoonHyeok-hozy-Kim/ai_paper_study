[Back to AI Main](../../README.md)

<br>

# Dive into Deep Learning
Visit [Dive into Deep Learning website](https://d2l.ai/index.html).

<br>

- [Installation](ch00/01/note.md) : ```jupyter notebook```
- [Notations](ch00/02/note.md)

## 2. Preliminaries
|No.|Chapter|Keywords|
|:-:|:------|:-------|
|2.1|[Data Manipulation](./ch02/01/note.md)|Tensor(Indexing, Slicing, Unary/Binary Operators, Concatenation, Broadcasting, Tensor Object Conversion(ndarray))|
|2.2|[Data Processing](./ch02/02/note.md)|pandas(CSV File Loading, Missing Value Treatment)|
|2.3|[Linear Algebra](./ch02/03/note.md)|Scalars, Vectors, Matrices, Tensors, Hadamard/Scalar Product, Reduction, Non-Reduction Sum, Dot Products, Matrix-Vector Products, Matrix-Matrix Multiplication, Norms|
|2.4|[Calculus](./ch02/04/note.md)|Derivatives, Differentiation, Visualization Tools (```matplotlib```), Gradients|
|2.5|[Automatic Differentiation](./ch02/05/note.md)|Backproagation, Autograd Package, Detaching Computation|
|2.6|[Probability and Statistics](./ch02/06/note.md)||

<br>

## 3. Linear Neural Networks for Regression
|No.|Chapter|Keywords|
|:-:|:------|:-------|
|3.1|[Linear Regression](./ch03/01/note.md)|- Affine Transformation <br> - Loss Function, Analytic Solution <br> - Minibatch Stochastic Gradient Descent <br> - Vectorization, Normal Distribution and Squared Loss|
|3.2|[Object-Oriented Design for Implementation](./ch03/02/note.md)|Designing APIs (Module, DataModule, Trainer class)|
|3.3|[Synthetic Regression Data](./ch03/03/note.md)|- Generating Dataset : ```SyntheticRegressionData``` <br> - Reading the Dataset : ```get_dataloader``` |
|3.4|[Linear Regression Implementation from Scratch](./ch03/04/note.md)|- Defining the Model<br>- Defining the Loss Function<br>- Defining the Optimization Algorithm<br>- Training|
|3.5|[Concise Implementation of Linear Regression](./ch03/05/note.md)|Using high-level APIs|
|3.6|[Generalization](./ch03/06/note.md)|Overfitting/Underfitting, Regularization, Polynomial Curve Fitting, Model Selection, Validation Set, K-fold Cross Validation|
|3.7|[Weight Decay](./ch03/07/note.md)|$\ell_2$ norm, ```torch.optim.SGD([{'weight_decay': self.wd}])```|

<br>

## 4. Linear Neural Networks for Classification
|No.|Chapter|Keywords|
|:-:|:------|:-------|
|4.1|[Softmax Regression](./ch04/01/note.md)|One-Hot Encoding, The Cross-Entropy Loss <br>Information Theory : Entropy, Surprisal|
|4.2|[The Image Classification Dataset](./ch04/02/note.md)|- MNIST <br> - Fashion-MNIST Dataset Loading|
|4.3|[The Base Classification Model](./ch04/03/note.md)|```Classifier```, ```accuracy()```|
|4.4|[Softmax Regression Implementation from Scratch](./ch04/04/note.md)|The Softmax Implementation, The Cross-Entropy Loss|
|4.5|[Concise Implementation of Softmax Regression](./ch04/05/note.md)|Overflow/Under Flow Prevention|
|4.6|[Generalization in Classification](./ch04/06/note.md)|- Empirical/Population Error <br>- Hoeffding Bound|
|4.7|[Environment and Distribution Shift](./ch04/07/note.md)|- Distribution Shift (Covariate / Label / Concept Shift), Nonstationary Distributions <br> - Empirical Risk Minimization Problem <br>- Confusion Matrix <br> - Batch Learning, Online Learning, Bandit Problems, Reinforcement Learning <br> - Fairness, Accountability, Transparency|

<br>

## 5. Multilayer Perceptrons
|No.|Chapter|Keywords|
|:-:|:------|:-------|
|5.1|[Multilayer Perceptrons](./ch05/01/note.md)|- Multilayer Perceptron (MLP) <br> - Activation Functions : ReLU, Sigmoid, Hyperbolic Tangent ($\tanh$)|
|5.2|[Implementation of Multilayer Perceptrons](./ch05/02/note.md)|- MLP Implementation from Scratch<br> - Concise MLP Implementation|
|5.3|[Forward Propagation, Backward Propagation, and Computational Graphs](ch05/03/note.md)|- Forward Propagation <br>- Backpropagation|
|5.4|[Numerical Stability and Initialization](ch05/04/note.md)|- Exploding/Vanishing Gradient <br> - Inherent Symmetry in Parametrization <br> - Parameter Initialization : Xavier Initialization|
|5.5|[Generalization in Deep Learning](ch05/05/note.md)|- Classical Learning vs Deep Learning <br> - Deep Learning vs Nonparametrics : Neural Tangent Kernel <br> - Early Stopping|
|5.6|[Dropout](ch05/06/note.md)|- Co-Adaptation, Injecting Noise|
|5.7|[Project: Predicting House Prices on Kaggle](ch05/07/note.md)|- ```download(url, folder, sha1_hash=None)``` <br> - ```extract(filename, folder)``` <br> - |

<br>

## 6. Builder's Guide
|No.|Chapter|Keywords|
|:-:|:------|:-------|
|6.1|[Layers and Modules](./ch06/01/note.md)|- Module <br> - ```Sequential``` (PyTorch)|
|6.2|[Parameter Management](./ch06/02/note.md)|- |
|6.3|[Parameter Initialization](./ch06/03/note.md)|- ```nn.init.normal_()```, ```nn.init.zeros_()```, ```nn.init.constant_()```, ```nn.init.xavier_uniform_()```|
|6.4|[Lazy Initialization](./ch06/04/note.md)|- |
|6.5|[Custom Layers](./ch06/05/note.md)|- |






<br><br>

[Back to AI Main](../../README.md)