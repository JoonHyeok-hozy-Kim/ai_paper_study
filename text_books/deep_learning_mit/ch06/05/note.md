* [Back to Deep Learning MIT](../../main.md)

# 6.5 Back-Propagation and Other Differentiation Algorithms
- Consider a [feedforward neural network](../00/note.md#concept-deep-feedforward-network-multilayer-perceptron-mlp).
  - where
    - $`x`$ : input
    - $`\hat{y}`$ : output
     
#### Concept) Forward Propagation
- Desc.)
  - The inputs $`x`$ provide the initial information that then propagates up to the hidden units at each layer and finally produces.
  - It continues onward until it **produces a scalar [cost](../../ch04/03/note.md#concept-cost-function-loss-function-error-function)** $`J(\theta)`$.

#### Concept) Back-Propagation
- Desc.)
  - It allows the information from the cost to then flow backwards through the network, in order to **compute the [gradient](../../ch04/03/note.md#concept-gradient)**.
    - $`\nabla_x f(x,y)`$ : the gradient
      - where
        - $`f`$ : an arbitrary function
        - $`x`$ : a set of variables whose derivatives are desired
        - $`y`$ : an additional set variables that are inputs to the function but whose derivatives are not required
    - $`\nabla_\theta J(\theta)`$ : the gradient of the cost function with respect to the parameters
  - It refers **only** to the method for computing the gradient.
    - Other algorithms, such as [SGD](../../ch05/09/note.md#59-stochastic-gradient-descent), use the gradient to learn in the whole learning process.
  - In principle it can compute derivatives of any function.
    - i.e.) Not limited to [MLP](../00/note.md#concept-deep-feedforward-network-multilayer-perceptron-mlp)..

<br><br>

## 6.5.1 Computational Graphs
Use computational graph language to describe the [back-propagation](#concept-back-propagation) more precisely.

#### Concept) Node
- Desc.)
  - Each node in the graph indicates a variable.
  - The variable may be 
    - scalar
    - vector
    - matrix
    - tensor
    - a variable of another type

#### Concept) Operation
- Desc.)
  - An operation is a **simple function** of one or more variables.
  - Our graph language is accompanied by a set of allowable operations. 
  - Complex functions are composed of multiple operations.
  - Without loss of generality, we define an operation to **return only a single output variable**.
    - The output variable can have multiple entries, such as a vector.

<br>

#### e.g.)
![](images/001.png)

(a) $`z = xy`$ <br>
(b) $`\hat{y} = x^\top w + b`$ <br>
(c) $`H = \max(0, XW + b)`$ <br>
(d) $`\begin{cases}
    \hat{y} = x^\top x & \textrm{the prediction} \\
    u^{(3)} = \lambda \sum_i w_i^2 & \textrm{the weight decay} \\
\end{cases}`$ <br>



<br><br>

## 6.5.2 Chain Rule of Calculus




<br>

* [Back to Deep Learning MIT](../../main.md)