* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 4.5 Multilayer Networks and the Backpropagation Algorithm
#### Concept) Multilayer Network
- The kind of multilayer networks learned by the Backpropagation Algorithm are capable of expressing a rich variety of nonlinear decision 
surfaces.
- Recall that single perceptrons can only express linear decision 
surfaces.
- This section discusses how to learn such multilayer networks using a gradient descent algorithm similar to that discussed in the previous section.

<br>

## 4.5.1 A Differentiable Threshold Unit
#### Concept) Unit Choice
- Candidates)
  - Linear Layers (X)
    - why?)
      - Multiple layers of cascaded linear units still produce only linear functions.
      - We prefer networks capable of representing highly **nonlinear functions**.
  - [Perceptron Units](../04/note.md#concept-learning-a-perceptron) (X)
    - why?)
      - Its discontinuous threshold makes it undifferentiable and hence unsuitable for gradient descent.
  - [Sigmoid Unit](#concept-sigmoid-unit) (O)
    - why?)
      - nonlinear
      - differentiable
  - Hyperbolic Tangent ($\tanh$) (O)

<br>

### Concept) Sigmoid Unit
- Def.)
  - The sigmoid unit computes its output $o$ as
    - $o=\sigma(\overrightarrow{w} \cdot \overrightarrow{x})$
      - where $\sigma(y) = \frac{1}{1+e^{-y}}$
  - $\sigma$ is often called the sigmoid function or a logistic function
- Props.)
  - Its output ranges between 0 and 1.
  - It increases monotonically with its input.
  - Called as a squashing function of the unit.
    - why?)
      - It maps a very large input domain to a small range of output ($[0, 1]$)
  - Easy to express its derivative.
    - $\frac{d \sigma(y)}{dy} = \sigma(y) \cdot (1-\sigma(y))$










<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)