* [Back to Deep Learning MIT](../../main.md)

# 7.1 Parameter Norm Penalties

### Concept) Regularization in Deep Learning
- Def.)
  - Recall our [previous definition](../../ch05/02/note.md#concept-regularization).
  - Reducing the generalization error, not the training error.
- Props.)
  - Regularization of an estimator works by trading **increased** [bias](../../ch05/04/note.md#concept-bias) for **reduced** [variance](../../ch05/04/note.md#concept-variance-and-standard-error-of-estimator).
    - Recall the three situations regarding [underfitting and overfitting](../../ch05/02/note.md#concept-underfitting-vs-overfitting).
      - A model is trained either...
        - (1) excluded the true data generating process—corresponding to underfitting and inducing bias
          - i.e.) Underfitted
        - (2) matched the true data generating process
          - i.e.) Ideal Learning
        - (3) included the generating process but also many other possible generating processes
          - i.e.) Overfitted
      - The goal of regularization is to take a model from the (3) into the (2).

<br>

### Concept) Parameter Norm Penalty
- Desc.)
  - Used for regularization approaches based on limiting the capacity of models.
    - e.g.) neural networks, linear regression, or logistic regression
- In the Objective Function)
  - $`\tilde{J}(\theta; X, y) = J(\theta; X,y) + \alpha\Omega(\theta)`$
    - where
      - $`J(\theta; X,y)`$ : the standard objective function
      - $`\Omega(\theta)`$ : a parameter norm penalty
        - where $`\theta`$ denotes all of the parameters including weights $`w`$
      - $`\alpha\in[0,\infty)`$ : a hyperparameter that weights the relative contribution of the norm penalty term $`\Omega`$
- Props.)
  - For neural networks, we typically choose to use a parameter norm penalty $`\Omega`$ that **penalizes only the weights of the affine transformation at each layer** and **leaves the biases unregularized**.
    - Why?)
      - The **biases** typically require less data to fit accurately than the **weights**.
        - Each bias controls only a single variable.
      - On the other hand, each **weight** specifies how two variables interact.
        - Thus, fitting the weight well requires observing both variables in a variety of conditions.
      - Therefore, we do not induce too much variance by leaving the **biases** unregularized.
      - Also, regularizing the **bias** parameters can introduce a significant amount of underfitting.
  - $`w`$ indicates all of the **weights** that should be affected by the norm penalty.
    - The vector $`\theta`$ denotes all of the parameters.
  - In the context of neural networks, it is sometimes desirable to use a separate penalty with a different α coefficient for each layer of the network. 
    - Why?) It can be expensive to search for the correct value of multiple hyperparameters.
    - Still, it is reasonable to use the same weight decay at all layers just to reduce the size of search space.

<br><br>

## 7.1.1 L2 Parameter Regularization (Weight Decay)
- Def.)
  - $`\Omega(\theta) = \frac{1}{2} ||w||^2_2`$
    - where $`w`$ is the weight vector
- Other Names)
  - Weight Decay
  - Ridge Regression
  - Tikhonov Regularization
- Props.)
  - It **multiplicatively shrink the weight vector** by a constant factor on each step, just before performing the usual gradient update.
    - Refer to $`(1-\epsilon\alpha)`$ from [Analysis 7.1.1.1](#analysis-7111-weight-decreasing-effect-in-gradient-descent).
    - Refer to $`\frac{\lambda_i}{\lambda_i + \alpha}`$ from [Analysis 7.1.1.2](#analysis-7112-quadratic-approximation-to-the-objective-function)
  - It decays away the unimportant directions in the weight vector.
    - Desc.)
      - Only directions along which the parameters contribute significantly to reducing the objective function are preserved relatively intact.
      - In directions that do not **contribute to reducing the objective function**, a small eigenvalue of the Hessian tells us that **movement in this direction will not significantly increase the gradient**.
      - Components of the weight vector corresponding to such unimportant directions are decayed away through the use of the regularization throughout training.
    - Refer to [Analysis 7.1.1.3](#analysis-7113-decaying-the-unimportant-direction) for the graphical description.

<br>

### Analysis 7.1.1.1) Weight Decreasing Effect in Gradient Descent
- Consider an objective function $`\tilde{J} = \frac{\alpha}{2} w^\top x + J(w;X,y)`$.
- The corresponding parameter gradient can be calculated as
  - $`\nabla_w \tilde{J} = \alpha w + \nabla_w J(w;X,y)`$.
- Then we may update the weight as   
  $`w\leftarrow w - \epsilon \left( \alpha w + \nabla_w J(w;X,y) \right) = (1-\epsilon\alpha)w -\epsilon\nabla_w J(w;X,y)`$
  - Here, the weight is multiplicatively decreasing with the factor $`(1-\epsilon\alpha)`$.

<br>

### Analysis 7.1.1.2) Quadratic Approximation to the Objective Function
- Objective)
  - We will use the quadratic approximation to derive the equation that explains the relationship between the nonregularized optimal weight $`(w^\ast)`$ and the $`L^2`$ regularized optimal weights $`(\tilde{w})`$.
    - $`\tilde{w} = (H+\alpha I)^{-1}Hw^\ast`$
    - $`\tilde{w} = Q(\Lambda + \alpha I) \Lambda Q^\top w^\ast`$
1. $`\tilde{w} = (H+\alpha I)^{-1}Hw^\ast`$
   - Derivation) 
     - Put $`w^\ast = \arg\min_w J(w)`$.
     - Then the quadratic approximation of $`J`$ near $`w^\ast`$ goes
       - $`\hat{J} = J(w^\ast) + \frac{1}{2}(w-w^\ast)^\top H(w-w^\ast)`$
         - where $`H`$ is the [Hessian matrix](../../ch04/03/note.md#concept-hessian-matrix) of  $`J`$ w.r.t. $`w`$ evaluated at $`w^\ast`$
       - cf.) There is no first-order term in this quadratic approximation, because $`w^\ast`$  is defined to be a minimum where the gradient vanishes.
       - cf.) Also, $`H`$ is [positive semidefinite](../../ch02/07/note. md#concept-positivenegative-definite).
     - The minimum of $`\hat{J}`$ occurs where its gradient $`\nabla_w\hat{J}(w) = H(w-w^\ast)`$  is equal to $`0`$.
     - If we add the $`L^2`$ regularization to $`\hat{J}`$, the gradient goes
       - $`\nabla_w\hat{J}(w) = \alpha w + H(w-w^\ast)`$
         - Why?)
           - Recall that $`\nabla_w \tilde{J} = \alpha w + \nabla_w J(w;X,y)`$.
           - i.e.) If we add the $`L^2`$ regularization, the term $`\alpha w`$ is added to the  gradient.
     - Letting $`\tilde{w}`$ represent the location of the minimum, the equation goes,   
       $`\begin{aligned}
         & \; \nabla_w\hat{J}(w) = 0 \\
         \Leftrightarrow & \; \alpha \tilde{w} + H(\tilde{w}-w^\ast) = 0 \\
         \Leftrightarrow & \; (H+\alpha I)\tilde{w} = Hw^\ast \\
         \Rightarrow & \; \tilde{w} = (H+\alpha I)^{-1}Hw^\ast
       \end{aligned}`$
   - Meaning)
     - $`\alpha\rightarrow 0 \Rightarrow \tilde{w}\rightarrow w^\ast`$.
       - i.e.) The effect of the weight decay diminishes.
2. $`\tilde{w} = Q(\Lambda + \alpha I)^{-1} \Lambda Q^\top w^\ast`$
   - Derivation)
     - Recall that the [Hessian matrix](../../ch04/03/note.md#concept-hessian-matrix) $`H`$ is real and symmetric.
     - Thus, we can [eigendecompose](../../ch02/07/note.md#concept-eigendecomposition) it as
       - $`H = Q\Lambda Q^\top`$
         - where
           - $`\Lambda`$ : a diagonal matrix
           - $`Q`$ : an orthonormal basis of eigenvectors of $`H`$
     - Hence,     
       $`\begin{aligned}
         \tilde{w} &= (H+\alpha I)^{-1}Hw^\ast \\
         &= (Q\Lambda Q^\top +\alpha I)^{-1} Q\Lambda Q^\top w^\ast \\
         &= (Q (\Lambda + \alpha I) Q^\top)^{-1} Q\Lambda Q^\top w^\ast & \because QQ^\top = I \\
         &= Q(\Lambda + \alpha I)^{-1} \Lambda Q^\top w^\ast & \because Q^{-1} = Q^\top
       \end{aligned}`$
    - Meaning)
      - Each component of $`w^\ast`$ aligned with the $`i`$-th eigenvector of $`H`$ is rescaled by a factor of $`\frac{\lambda_i}{\lambda_i + \alpha}`$.
      - Thus, if $`\alpha`$ increase, the rescaling effect of the weight decay increases, which in turn reduces the weights more.
        - If $`\lambda_i \gg \alpha`$, the effect of regularization is relatively small.
        - If $`\lambda_i \ll \alpha`$, the components of $`w^\ast`$ will shrunk to have nearly zero magnitude.

<br>

### Analysis 7.1.1.3) Decaying the Unimportant Direction
<img src="images/001.png" width="400px">

- Assumptions)
  - $`w = (w_1,w_2)\in\mathbb{R}^2`$ : the two dimensional weight
  - **(1) The solid ellipses** represent contours of equal value of the **unregularized objective**. 
    - In $`w_1`$ direction (horizontal)
      - The eigenvalue of the Hessian of $`J`$ is small.
      - The objective function does not increase much when moving horizontally away from $`w^\ast`$.
    - In $`w_2`$ direction (vertical)
      - The objective function is very sensitive to vertical movements away from $`w^\ast`$.
  - **(2) The dotted circles** represent contours of equal value of the $`L^2`$ **regularizer**.
- Optimization)
  - At $`w=\tilde{w}`$, the two competing objectives reach an equilibrium.
  - Because **the objective function (1)** does not express a strong preference along the $`w_1`$ direction, **the regularizer (2)** has a strong effect on this axis.
    - Thus, **the regularizer (2)** pulls $`w_1`$ close to zero.
  - In the $`w_2`$ direction, **weight decay (2)** affects the position of $`w_2`$ relatively little.

<br>

### Analysis 7.1.1.4) L2 Regularization in Linear Regression
- Nonregularized Case)
  - The cost function goes $`(Xw-y)^\top (Xw-y)`$.
    - where
      - $`X`$ : the input design matrix
      - $`y`$ : the target
      - $`w`$ : the weights
  - Then, the normal equation can be derived as
    - $`w = (X^\top X)^{-1} X^\top y`$
- $`L^2`$ Regularized Case)
  - The cost function goes $`(Xw-y)^\top (Xw-y) + \frac{\alpha}{2}w^\top w`$.
  - Then the normal equation goes
    - $`w = (X^\top X + \alpha I)^{-1} X^\top y`$
- Comparison)
  - The $`X^\top X`$ terms in both normal equations are proportional to the covariance matrix $`\frac{1}{m}X^\top X`$.
    - where $`m`$ is the number of training examples.
  - In the regularized case, the constant $`\alpha`$ is added to the diagonal of $`X^\top X`$.
  - Since the diagonal entries of $`X^\top X`$ are the variances of the features, $`L^2`$ regularization causes the learning algorithm to “perceive” the input $`X`$ as having **higher variance**.
  - Thus, the regularization makes **it shrink the weights on features whose covariance with the output target is low** compared to this added variance.

<br><br>

## 7.1.2 L1 Regularization
- Def.)
  - $`\displaystyle \Omega(\theta) = ||w||_1 = \sum_i |w_i|`$
    - where $`w`$ is the model parameter vector
- Props.)
  - Its gradient does not provide clean algebraic solution quadratic approximations.
    - Refer to [Analysis 7.1.2.1](#analysis-7121-weight-decreasing-effect-in-gradient-descent)
  - Comparison with $`L^2 Regularization`$ : [Analysis 7.1.2.3](#analysis-7123-comparison-with-l2-regularization)


<br>

### Analysis 7.1.2.1) Weight Decreasing Effect in Gradient Descent
- Settings)
  - $`\tilde{J}(w;X,y) = \alpha||w||_1 + J(w;X,y)`$
    - where $`J(w;X,y)`$ is the nonregularized cost.
    - Refer to [parameter norm penalty](#concept-parameter-norm-penalty).
- Optimization)
  - The corresponding gradient can be computed as
    - $`\nabla_w \tilde{J}(w;X,y) = \alpha \; \textrm{sign}(w) + \nabla_w J(w;X,y)`$
      - where $`\textrm{sign}(w)`$ is the sign of $`w`$ applied element-wise.
- Analysis)
  - The regularization is a constant factor with a sign equal to $`\textrm{sign}(w_i)`$.
    - Recall that [Weigh Decay (L2) linearly scaled the gradient](#analysis-7111-weight-decreasing-effect-in-gradient-descent).
- Prop.)
  - The gradient does not provide clean algebraic solutions to quadratic approximations of $`J(w;X,y)`$
  - Instead, we apply Taylor approximation [in Analysis 7.1.2.2](#analysis-7122-taylor-approximation-to-the-objective-function).


<br>

### Analysis 7.1.2.2) Taylor Approximation to the Objective Function
- Settings)
  - $`\nabla_w \hat{J} = H(w-w^\ast)`$ : the gradient
    - where $`H`$ is the Hessian matrix of $`J`$ w.r.t. $`w`$ evaluated at $`w^\ast`$
    - Refer to [Analysis 7.1.1.2](#analysis-7112-quadratic-approximation-to-the-objective-function) for the notations.
  - Further assume that $`H`$ is diagonal.
    - i.e.) $`H = \textrm{diag}\left( [H_{1,1}, \cdots, H_{n,n}] \right)`$
      - where $`H_{i,i} \gt 0`$
    - Why doing this?)
      - The $`L^1`$ penalty does not admit clean algebraic expressions in the case of fully general Hessian.
      - This assumption holds if the data for the linear regression problem has been preprocessed to remove all correlation between the input features.
        - e.g.) [PCA](../../ch05/08/note.md#581-principal-component-analysis-pca)
- The Approximation at $`w = w^\ast`$
  - $`\displaystyle \hat{J}(w;X,y) = J(w^\ast; X, y) + \sum_i \left[ \frac{1}{2} H_{i,i} \left( w_i - w_i^\ast \right)^2 + \alpha|w_i| \right]`$
- Solution)
  - $`\displaystyle w_i = \textrm{sign}(w_i^\ast) \max\left\{ |w_i^\ast| - \frac{\alpha}{H_{i,i}} , \; 0 \right\}`$ for each dimension $`i`$
- Analysis)
  - Consider the case that $`w_i^\ast \gt 0, \forall i`$.
    - There can be two possible outcomes.
      1. $`\displaystyle w_i^\ast \le \frac{\alpha}{H_{i,i}}`$
         - Then, the optimal value is $`w_i = 0`$.
           - i.e.) The $`L^1`$ regularization overwhelms the contribution of $`J`$ to $`\tilde{J}`$
      2. $`\displaystyle w_i^\ast \gt \frac{\alpha}{H_{i,i}}`$
         - Then, the $`L^1`$ regularization shifts the optimal value of $`w_i`$ in that direction by a distance equal to $`\displaystyle\frac{\alpha}{H_{i,i}}`$.


<br>

### Analysis 7.1.2.3) Comparison with L2 Regularization
1. The $`L^1`$ regularization results in more [sparse](../10/note.md#concept-sparsity) solutions.
   - Why?)
     - [Recall that the solution](#analysis-7112-quadratic-approximation-to-the-objective-function) of the $`L^2`$ regularization was given by 
       - $`\tilde{w} = Q(\Lambda + \alpha I) \Lambda Q^\top w^\ast`$
     - Applying the [diagonal assumption](#analysis-7122-taylor-approximation-to-the-objective-function) and [positive definite](../../ch02/07/note.md#concept-positivenegative-definite) Hessian $`H`$ to the $`L^1`$ regularization we can get
       - $`\displaystyle \tilde{w}_i = \frac{H_{i,i}}{H_{i,i} + \alpha} w^\ast_i`$
         - Here, if $`w^\ast_i`$ is nonzero, $`\tilde{w}_i`$ remains nonzero.
         - Thus, $`L^1`$ regularization may cause the parameters to become sparse.
   - Application)
     - Sparsity can be extensively used for the **feature selection** mechanism.
       - cf.) **Feature selection** simplifies a machine learning problem by choosing which subset of the available features should be used.
       - e.g.) LASSO (Least Absolute Shrinkage and Selection Operator)
         - It integrates an $`L^1`$ penalty with a linear model and a least squares cost function.
         - The $`L^1`$ penalty causes a subset of the weights to become zero.
           - i.e.) Discard the corresponding feature.
2. Relationship with [MAP Bayesian Inference](../../ch05/06/note.md#561-maximum-a-posteriori-map-estimation)
   - $`L^2`$ regularization
     - [Recall](../../ch05/06/note.md#561-maximum-a-posteriori-map-estimation) that $`L^2`$ regularization was equivalent to MAP Bayesian inference with a Gaussian prior on weights.
   - $`L^1`$ regularization
     - The penalty $`\alpha\Omega(w) = \alpha\sum_i |w_i|`$ used to regularize a cost function is  equivalent to the log-prior term that is maximized by MAP Bayesian inference when the prior is an isotropic [Laplace distribution](../../ch03/09/note.md#concept-laplace-distribution) over $`w\in\mathbb{R}^n`$    
       $`\begin{aligned}
        p(w) &= \sum_i\log\textrm{Laplace}\left(w_i; 0, \frac{1}{\alpha}\right) \\
        &= -\alpha||w||_1 + n\log\alpha - n\log2
       \end{aligned}`$
       - From the point of view of learning via maximization w.r.t. $`w`$, we can ignore $`n\log\alpha - n\log2`$ terms, which are independent of $`w`$.


<br>

* [Back to Deep Learning MIT](../../main.md)