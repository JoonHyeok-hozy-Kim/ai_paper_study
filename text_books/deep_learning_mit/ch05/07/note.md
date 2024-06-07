* [Back to Deep Learning MIT](../../main.md)

# 5.7 Supervised Learning Algorithms

#### Props.)
- Training set of examples of inputs $`x`$ and outputs $`y`$ is given.
- In many cases the outputs $`y`$ must be provided by a human “supervisor.”

<br>

## 5.7.1 Probabilistic Supervised Learning
- Desc.)
  - Estimating a probability distribution $`p(y|x)`$
  - How?)
    - Use [maximum likelihood estimation](../05/note.md#concept-maximum-likelihood-principle) to fine the best parameter vector $`\theta`$ for a parametric family of distribution $`p(y|x;\theta)`$.
      - e.g.) Linear regression
        - $`p(y|x;\theta) = \mathcal{N}(y;\theta^\top x, I)`$
          - where
            - $`\theta^\top x`$ is the mean.
            - $`I`$ is the covariance matrix.
      - e.g.) Classification
        - We can generalize linear regression to the classification scenario by defining a probability distribution with two classes, class 0 and class 1.
          - The probability of class 1 determines the probability of class 0.
        - Use logistic sigmoid function $`\sigma(\cdot)`$ to squash the output of the linear function into the interval $`(0,1)`$.
          - $`p(y=1|x;\theta) = \sigma(\theta^\top x)`$
          - Why?)
            - Recall that the binary classification problem has only two outputs, 0 and 1.
          - Sol.)
            - Minimize the negative log-likelihood (NLL) using gradient descent.
              - why?) There is no closed-form solution for the logistic regression's optimal weights.

<br>

## 5.7.2 Support Vector Machines (SVM)
### Concept) Kernel
- How?)
  - Let 
    - $`\phi(\cdot)`$ : a feature function.
      - We will replace the input $`x`$ into the output of the feature function.
    - $`k(x, x^{(i)}) = \phi(x) \cdot \phi(x^{(i)})`$ : a kernel
      - $`\cdot`$ is the dot product.
        - i.e.) $`\phi(x) \cdot \phi(x^{(i)}) = \phi(x)^\top \phi(x^{(i)})`$
- Props.)
  - Linearity / Nonlinearity)
    - $`f(x)`$ is nonlinear w.r.t. $`x`$.
    - $`f(x)`$ is linear w.r.t. $`\phi(x)`$.
    - $`f(x)`$ is linear w.r.t. $`\alpha`$.
  - The kernel-based function is exactly equivalent to preprocessing the data by applying $`\phi(x)`$ to all inputs, then learning a linear model in the **new transformed space**.

#### E.g.) Gaussian Kernel (Radial Basis Function, RBF)
- Def.)
  - $`k(u,v) = \mathcal{N}(u-v; 0, \sigma^2 I)`$
    - where $`\mathcal{N}(x;\mu,\Sigma)`$ is the standard normal density.
- Props.)
  - Its value decreases along lines in $`v`$ space radiating outward from $`u`$.
  - The Gaussian kernel corresponds to a dot product in an infinite-dimensional space, but the derivation of this space is less straightforward than in our example of the min kernel over the integers.
  - We can think of the Gaussian kernel as performing a kind of template matching.
    - i.e.) A training example $`x`$ associated with training label $`y`$ becomes a template for class $`y`$.
    - e.g.) When a test point $`x'`$ is near $`x`$ according to Euclidean distance, the Gaussian kernel has a large response, indicating that $`x`$ is very similar to the $`x`$ template.
      - The model then puts a large weight on the associated training label $`y`$.

<br><br>

### Concept) Support Vector Machine (SVM)
- Desc.)
  - It is driven by a linear function $`w^\top x + b`$.
    - Similar to logistic regression.
  - It does not provide probability.
  - It outputs a class identity.
    - The SVM predicts that the **positive class** is present when $`w^\top x + b \gt 0`$.
    - The SVM predicts that the **negative class** is present when $`w^\top x + b \lt 0`$.
  - It uses [kernel](#concept-kernel) trick to make predictions.
    - The **kernel trick** consists of observing that **many machine learning algorithms** can be written exclusively in terms of **dot products between examples**.
      - e.g) Linear function $`w^\top x + b`$ can be rewritten as
        - $`\displaystyle w^\top x + b = b + \sum_{i=1}^m{\alpha_i x^\top x^{(i)}}`$
          - where
            - $`x^{(i)}`$ : an $`i`$-th training example
            - $`\alpha`$ : a vector of coefficients
    - Then we can make predictions using the function
      - $`\displaystyle f(x) = b + \sum_i \alpha_i k(x, x^{(i)})`$
- Advantages)
  - It allows us to **learn nonlinear models** as a function of $`x`$ using convex optimization techniques that are **guaranteed to converge** efficiently.
    - This is possible because we consider $`\phi`$ fixed and optimize only $`\alpha`$.
      - i.e.) The optimization algorithm can view the decision function as being linear in a different space.
  - It can enhance the computation by replacing the implementation of the [kernel function](#concept-kernel).
    - The kernel function $`k`$ often admits other implementations than constructing $`k(x, x^{(i)}) = \phi(x) \cdot \phi(x^{(i)})`$.
    - Some are significantly more computational efficient than naive $`k(x, x^{(i)}) = \phi(x) \cdot \phi(x^{(i)})`$.
- Drawback)
  - High computational cost of training when the dataset is large
    - Why?) 
      - The cost of evaluating the decision function is linear in the number of training examples.
      - i.e.) $`x^{(i)}`$ contributes a term $`\alpha_i k(x, x^{(i)})`$.
    - Sol.)
      - SVMs are able to mitigate this by learning an $`\alpha`$ vector that contains mostly zeros.
      - Classifying a new example then requires evaluating the kernel function only for the training examples that have non-zero $`\alpha_i`$. 
      - These training examples are known as **support vectors**.

<br><br>

## 5.7.3 Other Simple Supervised Learning Algorithms
### Concept) k-Nearest Neighbors
- Desc.)
  - A non-parametric learning algorithm
    - Thus, it is not restricted to a fixed number of parameters.
  - There is not even really a training stage or learning process.
    - Instead, at **test time**, when we want to produce an output $`y`$ for a new test input $`x`$, we find the k-nearest neighbors to $`x`$ in the training data $`X`$.
    - We then return the **average** of the corresponding $`y`$ values in the training set.
  - k-nearest neighbor can achieve very **high capacity**.
    - The high capacity of k-nearest neighbors allows it to obtain **high accuracy** given a large training set.
    - However, it does so at **high computational cost**.
    - Also, it may **generalize very badly given a small, finite training set**.
  - k-nearest neighbors cannot learn that one feature is more discriminative than another.
    - e.g.)
      - Suppose we have a model $`y=\alpha_1x_1+\alpha_2x_2+\alpha_3x_3+\cdots+\alpha_{100}x_{100}`$.
        - where $`y^{(i)} = x_1^{(i)}, \forall i`$
          - i.e.) $`y=x_1`$.
      - Nearest neighbor regression will not be able to detect the simple pattern that $`y=x_1`$.
      - Instead, the nearest neighbor of most points $`x`$ will be determined by the features $`x_2`$ through $`x_{100}`$, not by $`x_1`$ solely.
      - Thus the output on small training sets will essentially be random.

<br>

### Concept) Decision Tree
- Construction)
  - Each node of the decision tree is associated with a region in the input space.
  - Internal nodes break that region into one sub-region for each child of the node.
  - Space is thus sub-divided into non-overlapping regions, with a one-to-one correspondence between leaf nodes and input regions.
  - Each leaf node usually maps every point in its input region to the same output.
- Props.)
  - Can be considered as non-parametric if it is allowed to learn a tree of arbitrary size.
    - Still, decision trees are usually regularized with size constraints that turn them into parametric models in practice.

<br>

* [Back to Deep Learning MIT](../../main.md)