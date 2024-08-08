* [Back to Deep Learning MIT](../../main.md)

# 8.4 Parameter Initialization Strategies

### Why needed?)
- Training algorithms for deep learning models are usually iterative in nature.
- Thus, they require the users to specify some **initial points** from which to begin the iterations.
- Most algorithms are strongly affected by the choice of initialization.
  - which makes training deep models a sufficiently difficult task 
- The initial point can determine whether the algorithm converges at all.
  - Some initial points are so unstable that the algorithm encounters numerical difficulties and fails altogether.
- The initial point can determine how quickly learning converges and whether it converges to a point with high or low cost.

<br>

### Current Trend)
- Modern initialization strategies are simple and heuristic.
  - Why?)
    - Designing improved initialization strategies is a difficult task because **neural network optimization** is not yet well understood.
  - Thus, most initialization strategies are based on achieving some nice properties when the network is initialized.
    - What is known for certainty)
      - The initial parameters need to **break symmetry** between different units.
        - i.e.) If two hidden units with the same activation function are connected to the same inputs, then these units must have different initial parameters.
          - If not, then a deterministic learning algorithm applied to a deterministic cost and model will constantly update both of these units in the same way.
  - How?)
    - Typically, we set the biases for each unit to heuristically chosen constants, and initialize only the weights randomly.
      - When using Gaussian or uniform distribution, the scale of the initial distribution does have a large effect on both the outcome of the optimization procedure and on the ability of the network to generalize.
    - Extra parameters are usually set to heuristically chosen constants much like the biases are.
      - e.g.) parameters encoding the conditional variance of a prediction
    - Larger initial weights will yield a stronger **symmetry breaking** effect.
      - However, they may result in [exploding values](../02/note.md#concept-vanishing-and-exploding-gradient-problem) during forward propagation or back-propagation.
      - In recurrent networks, large weights can also result in **chaos**.

<br>

### Analysis) Initialization on the Optimization and Regularization Perspective
- The **optimization** perspective suggests that the weights should be large enough to propagate information successfully, 
- On the other hand, some **regularization** concerns encourage making them smaller.









<br>

* [Back to Deep Learning MIT](../../main.md)