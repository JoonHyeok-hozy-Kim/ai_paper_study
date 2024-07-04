[Back to AI Main](../../README.md)

<br>

# Deep Learning (2017, MIT)
*Ian Goodfellow, Yoshua Bengio, Aaron Courville*


## 2. Linear Algebra
|No.|Chapter|Keywords|
|:-:|:------|:-------|
|2.1|[Scalars, Vectors, Matrices, and Tensors](ch02/01/note.md)|- Transpose, Broadcasting|
|2.2|[Multiplying Matrices and Vectors](ch02/02/note.md)|- Hadamard Product <br> - Associative, Commutative <br> - System of Linear Equations|
|2.3|[Identity and Inverse Matrices](ch02/03/note.md)|- |
|2.4|[Linear Dependence and Span](ch02/04/note.md)|- Column Space, Singularity|
|2.5|[Norms](ch02/05/note.md)|- $L^p$ Norm, Max Norm, Frobenius Norm|
|2.6|[Special Kinds of Matrices and Vectors](ch02/06/note.md)|- Diagonal Matrix, Symmetric Matrix <br> - Unit Vector <br> - Orthogonality, Orthonormality, Orthogonal Matrix|
|2.7|[Eigendecomposition](ch02/07/note.md)|- Eigenvector, Eigenvalue <br> - Positive Definite, Negative Definite|
|2.8|[Singular Value Decomposition](ch02/08/note.md)|- $`A = UDV^\top`$|
|2.9|[The Moore-Penrose Pseudoinverse](ch02/09/note.md)|- $`\displaystyle A^{+} \equiv \lim_{\alpha\rightarrow 0} \left(A^\top A + \alpha I \right)^{-1} A^\top`$|
|2.10|[The Trace Operator](ch02/10/note.md)|- |
|2.11|[The Determinant](ch02/11/note.md)|- |
|2.12|[Principal Components Analysis](ch02/12/note.md)|- |

<br>

## 3. Probability and Information Theory
|No.|Chapter|Keywords|
|:-:|:------|:-------|
|3.2|[Random Variables](ch03/02/note.md)|- |
|3.3|[Probability Distributions](ch03/03/note.md)|- Probabilities Mass Function (PMF), Uniform Distribution <br> - Joint Probability Distribution <br>- Probabilities Density Function (PDF)|
|3.4|[Marginal Probability](ch03/04/note.md)|- |
|3.5|[Conditional Probability](ch03/05/note.md)|- The Chain Rule of Conditional Probabilities|
|3.7|[Independence and Conditional Independence](ch03/07/note.md)|- |
|3.8|[Expectation, Variance, and Covariance](ch03/08/note.md)|- Covariance Matrix|
|3.9|[Common Probability Distributions](ch03/09/note.md)|- Bernoulli,  Multinoulli (Cartegorical) <br> - Gaussian, Multivariate Normal Distribution <br> - Exponential, Laplace Distributions <br> - Dirac, Empirical Distribution <br> - Mixture Distribution, Latent Variable|
|3.10|[Useful Properties of Common Functions](ch03/10/note.md)|- Logistic Sigmoid, Softplus|
|3.11|[Bayes’ Rule](ch03/11/note.md)|- |
|3.12|[Technical Details of Continuous Variables](ch03/12/note.md)|- Measure Theory : Measure Zero, Almost Everywhere|
|3.13|[Information Theory](ch03/13/note.md)|- Self-Information <br> - (Shannon) Entropy <br> - Kullback-Leiber (KL) Divergence <br> - Cross Entropy|
|3.14|[Structured Probabilistic Models](ch03/14/note.md)|- Probability Distribution Factorization <br> - Structured Probabilistic Model (Graphical Model) : Directed/Undirected Model|

<br>

## 4 Numerical Computation
|No.|Chapter|Keywords|
|:-:|:------|:-------|
|4.1|[Overflow and Underflow](ch04/01/note.md)|- Softmax Function|
|4.2|[Poor Conditioning](ch04/02/note.md)|- Condition Number |
|4.3|[Gradient-Based Optimization](ch04/03/note.md)|- Objective Function (Criterion), Loss Function (Cost Function, Error Function) <br> - Derivative, Critical Point (Stationary Point), Gradient $`\nabla_x f(x)`$ <br> - Method of Steepest Descent, Learning Rate, Line Search <br> - Jacobian, Second Derivative, Hessian <br> - Directional Second Derivative, Second Derivative Test <br> - The Newton's Method <br> - First/Second-Order Optimization Algorithm <br> - Lipschitz Continuous / Lipschitz Constant <br> - Convex Optimization / Convex Functions|
|4.4|[Constrained Optimization](ch04/04/note.md)|- Karush-Kuhn-Tucker (KKT) Condition <br> - Generalized Lagrangian|
|4.5|[Example: Linear Least Squares](ch04/05/note.md)|- |

<br>

## 5. Machine Learning Basics
|No.|Chapter|Keywords|
|:-:|:------|:-------|
|5.1|[Learning Algorithms](ch05/01/note.md)|- Task $`(T)`$, Performance Measure $`(P)`$, Experience $`(E)`$ <br> - Supervised / Unsupervised Learning Algorithms <br> - Design Matrix|
|5.2|[Capacity, Overfitting and Underfitting](ch05/02/note.md)|- Generalization, Training Error vs Test Error, Data Generating Process (Distribution) <br> - Overfitting vs Underfitting, Capacity, Representational Capacity <br> - Non-Parametric Model <br> - Bayes Error <br> - The No Free Lunch Theorem <br> - Regularization: Weight Decay|
|5.3|[Hyperparameters and Validation Sets](ch05/03/note.md)|- Cross-Validation|
|5.4|[Estimators, Bias and Variance](ch05/04/note.md)|- Point Estimation, Function Estimation <br> - Bias, Variance, Standard Error, $`\textrm{MSE} = \textrm{Var} + \textrm{Bias}^2`$ <br> - Consistency|
|5.5|[Maximum Likelihood Estimation](ch05/05/note.md)|- Maximum Likelihood Principle $`\theta_{\textrm{ML}}`$ <br> - Supervised Learning and Maximum Likelihood Estimation : MSE vs ML|
|5.6|[Bayesian Statistics](ch05/06/note.md)|- Maximum A Posteriori (MAP) Estimation|
|5.7|[Supervised Learning Algorithms](ch05/07/note.md)|- Probabilistic Linear Regression, Logistics Regression <br> - Kernel Function, Gaussian Kernel (Radial Basis Function, RBF) <br> - Support Vector Machines (SVM) <br> - k-Nearest Neighbors <br> - Decision Tree|
|5.8|[Unsupervised Learning Algorithms](ch05/08/note.md)|- Principal Component Analysis (PCA) <br> - k-means Clustering|
|5.9|[Stochastic Gradient Descent](ch05/09/note.md)|- Minibatch|
|5.10|[Building a Machine Learning Algorithm](ch05/10/note.md)|- Combination of (Dataset / Cost Function / Optimization Procedure / Model)|
|5.11|[Challenges Motivating Deep Learning](ch05/11/note.md)|- The Curse of Dimensionality <br> - Prior Belief, Local Constancy, Smoothness Regulation <br> - Manifold Learning|

<br>

## 6. Deep Feedforward Networks
|No.|Chapter|Keywords|
|:-:|:------|:-------|
|6.0|[Deep Feedforward Networks](ch06/00/note.md)|- Deep Feedforward Network (Multilayer Perceptron, MLP) : layer, unit, depth, width, output layer, hidden layer|
|6.1|[Example: Learning XOR](ch06/01/note.md)|- |
|6.2|[Gradient-Based Learning](ch06/02/note.md)|- Cost Functions : Maximum Likelihood, Conditional Statistics <br> - Cost Functional, Calculus of Variation, Mean Absolute Error <br> - Output Units : Linear, Sigmoid, Softmax, Mixture Density Network (Gaussian Mixture)|
|6.3|[Hidden Units](ch06/03/note.md)|- Rectified Linear Unit (ReLU) : Absolute Value Rectification, Leaky ReLU, Maxout Unit <br> - Logistic Sigmoid $`(\sigma)`$ and Hyperbolic Tangent $`(\tanh)`$ <br> - Linear Hidden Unit, Softmax Unit, Radial Basis Function (RBF) Unit, Softplus Unit, Hard $`\tanh`$|
|6.4|[Architecture Design](ch06/04/note.md)|- Universal Approximation Theorem|
|6.5|[Back-Propagation and Other Differentiation Algorithms](ch06/05/note.md)|- Forward Propagation / Back-Propagation <br> - Computational Graph : Node, Operation <br> - Chain Rule : Scalar, Vector, Tensor <br>- Symbol-to-Number Differentiation / Symbol-to-Symbol Differentiation <br> - General Back-Propagation, Time Complexity of the Back-Propagation Algorithm, Dynamic Programming <br> - [Back-Propagation Example with a Diagram](ch06/05/note.md#657-example-back-propagation-for-mlp-training) <br> - Automatic Differentiation : Reverse/Forward Mode Accumulation <br> - Krylov Methods|

<br>

## 7. Regularization for Deep Learning
|No.|Chapter|Keywords|
|:-:|:------|:-------|
|7.1|[Parameter Norm Penalties](ch07/01/note.md)|- Parameter Norm Penalty <br> - $`L^2`$ Parameter Regularization (Weight Decay, Ridge Regression, Tikhonov Regularization) <br> - $`L^1`$ Regularization : Sparsity, Feature selection (LASSO)|
|7.2|[Norm Penalties as Constrained Optimization](ch07/02/note.md)|- Explicit Constraints instead of Penalties|
|7.3|[Regularization and Under-Constrained Problems](ch07/03/note.md)|- Regularization Guarantees Closed Form Solution|
|7.4|[Dataset Augmentation](ch07/04/note.md)|- Dataset Augmentation for Classification Problem|
|7.5|[Noise Robustness](ch07/05/note.md)|- Injecting noise to the hidden units <br> - Injecting noise to weights <br> - Label Smoothing : Injecting noise at the output targets|
|7.6|[Semi-Supervised Learning](ch07/06/note.md)|- |
|7.7|[Multi-Task Learning](ch07/07/note.md)|- |
|7.8|[Early Stopping](ch07/08/note.md)|- |
|7.9|[Parameter Tying and Parameter Sharing](ch07/09/note.md)|- |
|7.10|[Sparse Representations](ch07/10/note.md)|- Sparsity <br> - Orthogonal Matching Pursuit (OMP-k)|
|7.11|[Bagging and Other Ensemble Methods](ch07/11/note.md)|- Bagging (Bootstrap Aggregating), Model Averaging Strategy <br> - Boosting|
|7.12|[Dropout](ch07/12/note.md)|- Comparison with Bagging <br> - Inference|




<br><br>

[Back to AI Main](../../README.md)