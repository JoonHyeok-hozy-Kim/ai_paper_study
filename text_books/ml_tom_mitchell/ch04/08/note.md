* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 4.8 Advanced Topics in Artificial Neural Networks

## 4.8.1 Alternative Error Functions
- Recall that gradient descent can be performed for any function $E$ that is differentiable with respect to the parameterized hypothesis space.
- Our Backpropagation algorithm used the sum of squared errors for $E$.
- Other forms of $E$ can be used as well.
  1. [Adding a penalty term for weight magnitude](#1-adding-a-penalty-term-for-weight-magnitude)
  2. [Adding a term for errors in the slope or derivative of the target function](#2-adding-a-term-for-errors-in-the-slope-or-derivative-of-the-target-function)
  3. [Minimizing the cross entropy of the network with respect to the target values](#3-minimizing-the-cross-entropy-of-the-network-with-respect-to-the-target-values)
  4. [Weight sharing (tying together) weights associated with different units or inputs](#4-weight-sharing-tying-together-weights-associated-with-different-units-or-inputs)

#### 1) Adding a penalty term for weight magnitude
- i.e.) Add a term to $E$ that increases with the magnitude of the weight vector.
  - This causes the gradient descent search to seek weight vectors with small magnitudes, thereby reducing the risk of overfitting.
  - One way of representation is...
    - $E(\overrightarrow{w}) \equiv \frac{1}{2} \Sigma_{d \in D} \Sigma_{k \in outputs} (t_{kd}-o_{kd})^2 + \gamma \Sigma_{i,j} w_{ji}^2$
      - As a result, in each iteration, the weight is multiplied by $(1-2\gamma\eta)$
      - Equivalent to [the weight decay](../06/note.md#option-2-use-the-weight-decay) strategy.

<br>

#### 2) Adding a term for errors in the slope or derivative of the target function
- In some cases, training information may be available regarding desired 
derivatives of the target function($t$) and the desired values($o$).
- e.g.)
  - Simard et al (1992)
  - Mitchell and Thrun (1993)
  - In both of these systems, the error function is modified to add a term measuring **the discrepancy between these training derivatives and the actual derivatives of the learned network**.
    - i.e.) $\frac{\partial t}{\partial x^j} - \frac{\partial o}{\partial x^j}$
  - One way of representation is...
    - $E(\overrightarrow{w}) \equiv \frac{1}{2} \Sigma_{d \in D} \Sigma_{k \in outputs} \left[ (t_{kd}-o_{kd})^2 + \mu \Sigma_{j \in inputs} \left( \frac{\partial t_{kd}}{\partial x_d^j} - \frac{\partial o_{kd}}{\partial x_d^j} \right)^2\right]$
      - where $x_d^j$ : the value of the $j$-th input unit for training example $d$
        - $\mu$ : a constant that determines the relative weight placed on fitting the training values versus the training derivative
    - Explanation)
      - $\frac{\partial t_{kd}}{\partial x_d^j}$ : the training derivative describing how the target output value $t_{kd}$ should vary with a change in the input $x_d^j$.
      - $\frac{\partial o_{kd}}{\partial x_d^j}$ : the actual learned network's derivative describing how the learned output value $t_{kd}$ should vary corresponding to the input $x_d^j$.

<br>

#### 3) Minimizing the cross entropy of the network with respect to the target values


<br>

#### 4) Weight sharing (tying together) weights associated with different units or inputs


<br><br>





<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)