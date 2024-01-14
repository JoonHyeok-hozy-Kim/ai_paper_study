* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 8.3 Locally Weighted Regression
- Objective)
  - An explicit approximation to the target function $f$ over a local region surrounding $x_q$
    - A generalization of [the nearest-neighbor approaches](../02/note.md#concept-k-nearest-neighbor-algorithm) that approximate the target function $f(x)$ at the single query point $x = x_q$
- Desc.)
  |Term|Desc.|
  |:-|:-|
  |Locally|The function is approximated based a only on data near the query point.|
  |Weighted|The contribution of each training example is weighted by its distance from the query point|
  |Regression|approximating real-valued functions|
- How?)
  - It uses nearby or distance-weighted training examples to form this local approximation to $f$.
    - e.g.) Functions that can be used for the approximation
      - [a linear function](#831-locally-weighted-linear-regression)
      - a quadratic function
      - a multilayer neural network
  - Procedure)
    - Given a new query instance $x_q$...
    - Construct an approximation $\hat{f}$ that fits the training examples in the neighborhood surrounding $x_q$.
    - Calculate the estimated target value for the query instance $\hat{f}(x_q)$
    - (Optional) Delete $\hat{f}$.

<br><br>

## 8.3.1 Locally Weighted Linear Regression
- Settings)
  - $f$ : the target function
  - $x_q$ : a query point
  - $D$ : training examples
- Model)
  - Approximation Function
    - $\hat{f}(x_q)=w_0+w_1a_1(x)+\cdots+w_na_n(x)$
      - where $a_i(x)$ denotes the value of the $i$th attribute of the instance $x$.
  - Loss Function
    - We need a loss function that emphasizes fitting the **local** training examples.
    - e.g.)
      1. Minimize the squared error over just the k nearest neighbors:
         - $E_1(x_q)\equiv\frac{1}{2}\Sigma_{x \in \lbrace k \textrm{-nearest neighbors of }x_q \rbrace} \left(f(x)-\hat{f}(x)\right)^2$
           - Advantage)
             - Low computational burden
           - Disadvantage
             - Does not consider the impacts of training examples outside the $k$-nearest neighborhood.
      2. Minimize the squared error over the entire set $D$ of training examples, while weighting the error of each training example by some decreasing function $K$ of its distance from $x_q$ :
         - $E_2(x_q)\equiv\frac{1}{2}\Sigma_{x \in D} \left(f(x)-\hat{f}(x)\right)^2 K(d(x_q, x))$
           - Advantage)
             - Considers the impacts of training examples outside the $k$-nearest neighborhood.
           - Disadvantage
             - Computationally too costly
      3. Combine the above two:
         - $E_3(x_q)\equiv\frac{1}{2}\Sigma_{x \in \lbrace k \textrm{ nearest neighbors of }x_q \rbrace} \left(f(x)-\hat{f}(x)\right)^2 K(d(x_q, x))$
           - Advantage)
             - Computational cost is independent of the total number of training example, but the size of $k$.
  - Gradient Descent Rule
    - Suppose we took the $E_3$ loss function.
    - Then $\Delta w_j = \eta \Sigma_{x \in \lbrace k \textrm{ nearest neighbors of }x_q \rbrace} \left\lbrace K(d(x_q, x)) \left(f(x)-\hat{f}(x)\right) a_j(x)\right\rbrace$




<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)