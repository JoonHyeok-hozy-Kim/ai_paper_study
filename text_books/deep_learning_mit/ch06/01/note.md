* [Back to Deep Learning MIT](../../main.md)

# 6.1 Example: Learning XOR
Let's compare a [linear model](#linear-model-case) and a [feedforward network](#simple-feedforward-network) for learning the [XOR problem](#concept-xor-function).

### Concept) XOR Function
- Def.)
  - An operation on two binary values, $`x_1`$ and $`x_2`$ such that
    - $`\begin{cases}
        1 & x_1 \ne x_2 \\
        0 & \textrm{otherwise}
      \end{cases}`$

### Settings)
- $`\mathbb{X} = \{[0,0]^\top, [0,1]^\top, [1,0]^\top, [1,1]^\top\}`$ : inputs
- $`y = f^\ast(x)`$ : the target we want to learn.
- $`y = f(x;\theta)`$ : the model that we will approximate to the target
  - Our learning algorithm will adapt the parameters $`\theta`$ to make $`f`$ as similar as possible to $`f^\ast`$.

<br>

### Linear Model Case)
- Linear Model Setup)
  - $`f(x;w,b) = x^\top w + b`$
- Suppose  we use MSE as the cost function.
    - MSE : $`\displaystyle J(\theta) = \frac{1}{4} \sum_{x\in\mathbb{X}}(f^\ast(x) - f(x;\theta))^2`$
- After minimizing $`J(\theta)`$ in closed form w.r.t. $`w,b`$ we get
  - $`w=0, b=\frac{1}{2}`$.
    - i.e.) The linear model outputs $`\frac{1}{2}`$ regardless of the input.

<br>

### Simple Feedforward Network
- Structure)
  - The Whole Model)
    - One hidden layer containing two hidden units.
    - $`f(x;W,c,w,b) = f^{(2)}(f^{(1)}(x))`$
  - Hidden Layer)
    - $`h = f^{(1)}(x;W,c)`$ : the hidden layer
      - where
        - $`W \in\mathbb{R}^{2\times 2}`$ : the weights matrix of a linear transformation
        - $`c \in\mathbb{R}`$ : the bias
    - Its output is used as the input of the output layer.
    - Use activation function $`g`$ to give nonlinearity.
      - $`h = g(Wx+c)`$
      - Using ReLU $`(g(z) = \max(0,z))`$, we get
        - $`h = \max(0, Wx+c)`$
  - Output layer)
    - $`y = f^{(2)}(h;w,b)`$.
      - where $`w,b \in \mathbb{R}`$
- Result)
  - Recall our final model was 
    - $`f(x;W,c,w,b) = w \cdot \max(0, xW+c) + b`$
  - Suppose we have the optimized result as below
    - $`W = \begin{bmatrix} 1&1\\1&1\\ \end{bmatrix}, c = \begin{bmatrix} 0\\-1 \end{bmatrix}, w = \begin{bmatrix} 1\\-2 \end{bmatrix}, b=0`$.
  - Let $`X`$ be the design matrix containing all four points in the binary input space.
    - i.e.) $`X = \begin{bmatrix} 0&0\\0&1\\1&0\\1&1\\ \end{bmatrix}`$
  - Then $`XW = \begin{bmatrix} 0&0\\0&1\\1&0\\1&1\\ \end{bmatrix}\begin{bmatrix} 1&1\\1&1\\ \end{bmatrix} = \begin{bmatrix} 0&0\\1&1\\1&1\\2&2\\ \end{bmatrix}`$.
  - Applying the bias $`c`$, we get
    - $`\begin{bmatrix} 0&-1\\1&0\\1&0\\2&1\\ \end{bmatrix}`$
      - cf.) All of the examples lie along a line with slope $`1`$.
        - i.e.) Linear!
  - Give nonlinearity using the ReLU.
    - $`\max\left(0, XW+c\right) = \begin{bmatrix} 0&0\\1&0\\1&0\\2&1\\ \end{bmatrix}`$
  - Finally, by multiplying the weights $`w`$, we get
    - $`\cdot \max(0, Wx+c)w = \begin{bmatrix} 0\\1\\1\\0\\ \end{bmatrix}`$








<br>

* [Back to Deep Learning MIT](../../main.md)