* [Back to Deep Learning MIT](../../main.md)

# 6.5 Back-Propagation and Other Differentiation Algorithms

#### Concept) Forward Propagation / Back-Propagation
- Consider a [feedforward neural network](../00/note.md#concept-deep-feedforward-network-multilayer-perceptron-mlp).
  - where
    - $`x`$ : input
    - $`\hat{y}`$ : output
- Forward Propagation)
  - The inputs $`x`$ provide the initial information that then propagates up to the hidden units at each layer and finally produces.
  - It continues onward until it **produces a scalar [cost](../../ch04/03/note.md#concept-cost-function-loss-function-error-function)** $`J(\theta)`$.
- Back-Propagation)
  - It allows the information from the cost to then flow backwards through the network, in order to **compute the [gradient](../../ch04/03/note.md#concept-gradient)**.
  - It refers **only** to the method for computing the gradient.
    - Other algorithms, such as [SGD](../../ch05/09/note.md#59-stochastic-gradient-descent), use the gradient to learn in the whole learning process.
  - In principle it can compute derivatives of any function.
    - i.e.) Not limited to [MLP](../00/note.md#concept-deep-feedforward-network-multilayer-perceptron-mlp)..














<br>

* [Back to Deep Learning MIT](../../main.md)