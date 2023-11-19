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
      - Denote $\overrightarrow{w} \cdot \overrightarrow{x} = net$
  - $\sigma$ is often called the sigmoid function or a logistic function
- Props.)
  - Its output ranges between 0 and 1.
  - It increases monotonically with its input.
  - Called as a squashing function of the unit.
    - why?)
      - It maps a very large input domain to a small range of output ($[0, 1]$)
  - Easy to express its derivative.
    - $\frac{d \sigma(y)}{dy} = \sigma(y) \cdot (1-\sigma(y))$

![](images/001.png)

<br><br>

## 4.5.2 The Backpropagation Algorithm
#### Def.) Training Error for the Multiple Output Units
- $E(\overrightarrow{w}) \equiv \frac{1}{2} \Sigma_{d \in D} \Sigma_{k \in outputs} (t_{kd} - o_{kd})^2$
  - where $outputs$ is the set of output units in the network
    - $t_{kd}$ : target value associated with the $k$-th output unit and training example $d$
    - $o_{kd}$ : output value associated with the $k$-th output unit and training example $d$
- Why needed?)
  - We are considering networks with multiple output units rather than single units as before.
    - Refer to the [previous single layered gradient descent](../04/note.md#settings)'s training error.

<br>

### Concept) The Backpropagation Algorithm
- Algorithm)
  - Inputs) ```backpropagation(training_examples, eta, n_in, n_out, n_hidden)```
    - $training-example$
      - a pair of form $\langle \overrightarrow{x}, \overrightarrow{t} \rangle$
        - where $\overrightarrow{x}$ : the vector of network input values
          - $\overrightarrow{t}$ : the vector of target network output values.
    - $\eta$ : the learning rate
    - $n_{in}$ : the number of network inputs
    - $n_{out}$ : the number of network units
    - $n_{hidden}$ : the number of units in the hidden layer
  - Notations)
    - Each node is assigned with an index.
    - $x_{ji}$ : the input from unit $i$ into unit $j$. 
    - $w_{ji}$ : the weight from unit $i$ to unit $j$. 
    - $\delta_n$ : the error term associated with unit $n$.
      - Similar to the term $(t-o)$ of [the delta training rule](../04/note.md#443-gradient-descent-and-the-delta-rule).
      - $\delta_n = -\frac{\partial E}{\partial net_n}$
  - Procedures)
    1. Create a feed-forward network with $n_{in}$ inputs, $n_{hidden}$ hidden units, and $n_{out}$ output units. 
    2. Initialize all network weights to small random numbers (e.g., between -.05 and .05). 
    3. Until the termination condition is met, do...
       - For each $\langle \overrightarrow{x}, \overrightarrow{t} \rangle$ in $training-example$, do...
          - Propagate the input forward through the network:
            - Input the instance $\overrightarrow{x}$ to the network and compute the output $o_u$ of every unit $u$ in the network.
          - Propagate the errors backward through the network:
            1. For each network output unit $k$, calculate its error term $\delta_k$
               - $\delta_k \leftarrow o_k(1-o_k)(t_k-o_k)$
            2. For each hidden unit $h$, calculate its error term  $\delta_h$
               - $\delta_h \leftarrow o_h(1-o_h) \Sigma_{k \in  outputs} w_{kh} \delta_k$
            3. Update each network weight $w_{ji}$
               - $w_{ji} \leftarrow w_{ji} + \Delta w_{ji}$
                 - where $\Delta w_{ji} = \eta \delta_j x_{ji}$

- Props.)
  - Multilayer network can have multiple local minima in their error surfaces.
    - Thus, the gradient descent does not guaranteed the converge toward the global minimum.
    - Still, Backpropagation algorithm is known to produce excellent results.



<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)