* [Back to Dive into Deep Learning](../../main.md)

# 4.1 Softmax Regression

## 4.1.1 Classification
#### Problem Setting) Image Classification
- Input : $2\times2$ grey scale image
  - Represent each pixel with $x_1, x_2, x_3, x_4$
- Output : Three categories of “cat”, “chicken”, and “dog”.
  - Using [the one-hot encoding](#concept-one-hot-encoding) below, we may represent as $`y \in \{(1, 0, 0), (0, 1, 0), (0, 0, 1)\}`$

#### Concept) One-Hot Encoding
- Desc.)
  - A vector with as many components as we have categories.
  - The component corresponding to a particular instance’s category is set to 1 and all other components are set to 0.

<br>

### 4.1.1.1 Linear Model
- Model)
  - Recall that we had 
    - 4 features : $x_1, x_2, x_3, x_4$
    - 3 classes of output : $`y \in \{(1, 0, 0), (0, 1, 0), (0, 0, 1)\}`$
      - Denote them as $o_1, o_2, o_3$
  - Thus, the linear model goes...
    - $`\begin{aligned}   o_1 &= x_1 w_{11} + x_2 w_{12} + x_3 w_{13} + x_4 w_{14} + b_1,\\   o_2 &= x_1 w_{21} + x_2 w_{22} + x_3 w_{23} + x_4 w_{24} + b_2,\\ o_3 &= x_1 w_{31} + x_2 w_{32} + x_3 w_{33} + x_4 w_{34} + b_3.   \end{aligned}`$
      - Simply put,
        - $`\mathbf{o} = \mathbf{W} \mathbf{x} + \mathbf{b}`$


- Desc.)
  - Fully connected Layer   
    ![](images/001.png)
- Problems)
  - $\displaystyle \sum_{i=1,2,3}o_i\ne 1$
    - i.e.) There is no guarantee that the outputs $`o_i`$ sum up to $`1`$ in the way we expect probabilities to behave.
  - $\exists o_i \notin [0,1]$
    - There is no guarantee that the outputs $`o_i`$ are even nonnegative, even if their outputs sum up to $`1`$, or that they do not exceed $`1`$.
- **Alternative Sol.)**
  - [Softmax Regression](#4112-softmax-model)

<br>

### 4.1.1.2 Softmax Model
#### Concept) Softmax Function
- Def.)
  - $\hat{\mathbf{y}} = \mathrm{softmax}(\mathbf{o}) \quad \textrm{where}\quad \hat{y}_i = \frac{\exp(o_i)}{\sum_j \exp(o_j)}$
- Prop.)
  - The softmax operation preserves the ordering among its arguments.
    - Thus, $\displaystyle {\arg\max}_j \hat{y_j} = {\arg\max}_j o_j$
- Vectorization)
  - For
    |Element|Desc.|
    |:-:|:-|
    |$n$ | the number of examples|
    |$d$ | the dimensionality of the problem|
    |$`\mathbf{X} \in \mathbb{R}^{n \times d}`$ | a minibatch|
    |$q$ | the number of categories|
    |$`\mathbf{W} \in \mathbb{R}^{d \times q}`$ | the weights|
    |$`\mathbf{b} \in \mathbb{R}^{1\times q}`$ | the bias, in the matrix form $`\mathbf{B} = \left[\begin{array}{c} \mathbf{b}\\\mathbf{b}\\\vdots\\\mathbf{b} \end{array}\right]\in \mathbb{R}^{n\times q}`$|
  - The Model)
    - $\mathbf{O} = \mathbf{X} \mathbf{W} + \mathbf{B}$
      - $`\displaystyle n \textrm{ examples} \left\{ \left[\begin{array}{cccc} o_{11}&o_{12}&\cdots&o_{1q}\\o_{21}&o_{22}&\cdots&o_{2q}\\\vdots&\vdots&\ddots&\vdots\\o_{n1}&o_{n2}&\cdots&o_{nq} \end{array}\right] \right. = \underbrace{\left[\begin{array}{cccc} x_{11}&x_{12}&\cdots&x_{1d}\\x_{21}&x_{22}&\cdots&x_{2d}\\\vdots&\vdots&\ddots&\vdots\\x_{n1}&x_{n2}&\cdots&x_{nd} \end{array}\right]}_{d \textrm{ features}} \; \underbrace{\left[\begin{array}{cccc} w_{11}&w_{12}&\cdots&w_{1q}\\w_{21}&w_{22}&\cdots&w_{2q}\\\vdots&\vdots&\ddots&\vdots\\w_{d1}&w_{d2}&\cdots&w_{dq}\end{array}\right]}_{q \textrm{ categories}} + \left[\begin{array}{c} \mathbf{b}\\\mathbf{b}\\\vdots\\\mathbf{b} \end{array}\right]`$
        - where $`\mathbf{b} = \left[\begin{array}{cccc} b_{1}&b_{2}&\cdots&b_{q} \end{array}\right]`$
    - $\hat{\mathbf{Y}} = \mathrm{softmax}(\mathbf{O})$
      - $`\displaystyle \left[\begin{array}{c} \hat{\mathbf{y}_1} \\ \hat{\mathbf{y}_2} \\ \vdots \\ \hat{\mathbf{y}_n} \end{array}\right] = \left[\begin{array}{c} \mathrm{softmax}(\mathbf{o}_1) \\ \mathrm{softmax}(\mathbf{o}_2) \\ \vdots \\ \mathrm{softmax}(\mathbf{o}_n) \end{array}\right]`$
        - where $`\mathbf{o}_i = \left[\begin{array}{cccc} o_{1}&o_{2}&\cdots&o_{q} \end{array}\right]`$
- cf.)
  - Care must be taken to avoid exponentiating and taking logarithms of large numbers, since this can cause numerical overflow or underflow.



<br><br>

## 4.1.2 Loss Function




<br>

* [Back to Dive into Deep Learning](../../main.md)