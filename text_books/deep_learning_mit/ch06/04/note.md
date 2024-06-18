* [Back to Deep Learning MIT](../../main.md)

# 6.4 Architecture Design

### Concept) Architecture
- Desc.)
  - Overall structure of the network.
    - the number of units
    - the connections between units
    - layer arrangements

<br>

## 6.4.1 Universal Approximation Properties and Depth
### Theorem) Universal Approximation Theorem
- Why needed?)
  - Neural network problems are nonlinear.
  - Thus, convenient methods such as **convex optimization** for linear models cannot be applied to neural networks.
  - Instead, this theorem shows that regardless of what function we are trying to learn, a **large MLP** will be able to represent this function.
- Theorem)
  - Consider a feedforward network with...
    - a linear output layer 
    - at least one hidden layer with any [“squashing”](../../ch05/07/note.md#571-probabilistic-supervised-learning) activation function 
      - e.g.) logistic sigmoid activation function
  - This network can approximate any **Borel measurable** function from one finite-dimensional space to another with any desired non-zero amount of error, provided that the network is given enough hidden units.
    - cf.) Borel Measurability
      - For our purposes it suffices to say that any continuous function on a closed and bounded subset of $`\mathbb{R}^n`$ is **Borel measurable** and therefore may be approximated by a neural network.
      - A neural network may also approximate any function mapping from any finite dimensional discrete space to another.
- Meaning)
  - Regardless of what function we are trying to learn, we know that a large MLP will be able to represent this function.
  - However, we are NOT guaranteed that the training algorithm will be able to **learn** that function.
    - Why?)
      - The **optimization algorithm** used for training may not be able to find the value of the parameters that corresponds to the desired function.
      - The training algorithm might choose the wrong function due to overfitting.
- Prop.)
  - The theorem does not say how large this network should be to properly represent certain function.
    - cf.) *Barron 1993* provides some bounds on the size of a single-layer network needed to approximate a broad class of functions.
      - Unfortunately, in the worse case, an **exponential** number of hidden units may be required.
        - e.g.) Binary Case
          - Consider that there are $`2^{2^n}`$ possible binary functions on vectors $`v\in\{0,1\}^n`$.
          - Then, selecting one of such functions requires $`2^n`$ bits.
          - Thus, it requires $`O(2^n)`$ degrees of freedom.








<br>

* [Back to Deep Learning MIT](../../main.md)