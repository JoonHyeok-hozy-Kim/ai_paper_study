* [Back to Deep Learning MIT](../../main.md)

# 7.14 Tangent Distance, Tangent Prop, and Manifold Tangent Classifier

### Concept) Tangent Distance Algorithm
- Motivation)
  - Many ML algorithms aim to overcome [the curse of dimensionality](../../ch05/11/note.md#5111-the-curse-of-dimensionality) by assuming that the data lies near a low-dimensional manifold.
  - One of these attempts to take advantage of the [manifold hypothesis](../../ch05/11/note.md#5113-manifold-learning) is the **tangent distance** algorithm.
- Desc.)
  - Tangent Distance Algorithm is a non-parametric nearest-neighbor algorithm that uses a metric derived from knowledge of the [manifolds](../../ch05/11/note.md#concept-manifold) near which probability concentrates.
    - It does not use the the generic Euclidean distance
  - Assumptions)
    - Examples can be classified by the manifolds.
    - Examples in the same [manifolds](../../ch05/11/note.md#concept-manifold) share the same category.
  - Objective)
    - Classify the examples by the manifolds.
      - Since the classifier should be invariant to the local factors of variation that correspond to movement on the manifold, it would make sense to use as nearest-neighbor distance between points $`x_1`$ and $`x_2`$ the distance between the manifolds $`M_1`$ and $`M_2`$ to which they respectively belong.
      - But the computation for finding the nearest pair of points on $`M_1`$ and $`M_2`$ is difficult.
      - Instead, we may locally approximate $`M_i`$ by its **tangent plane** at $`x_i`$ and measure the distance between two tangents or between a tangent plane and a point.
      - That can be achieved by solving a low-dimensional linear system (in the dimension of the manifolds). 
        - This algorithm requires one to specify the tangent vectors.

<br><br>

### Concept) Tangent Propagation Algorithm 
- Desc.)
  - It trains a neural net classifier with an **extra penalty** to make each output $`f(x)`$ of the neural net **locally invariant to known factors** of variation.
  - These factors of variation correspond to movement along the manifold near which examples of the same class concentrate.
  - Local invariance is achieved by requiring...
    - $`\nabla_x f(x)`$ to be orthogonal to the known manifold tangent vectors $`v^{(i)}`$ at $`x`$
    - or equivalently that the directional derivative of $`f`$ at $`x`$ in the directions $`v^{(i)}`$ be small by adding a **regularization penalty** $`\Omega`$:
      - $`\displaystyle \Omega(f) = \sum_i\left( \left( \nabla_x f(x) \right)^\top v^{(i)} \right)^2`$
  - As with the [tangent distance algorithm](#concept-tangent-distance-algorithm), the tangent vectors are derived a **priori**, usually from the formal knowledge of the effect of transformations such as translation, rotation, and scaling in images.
  - Tangent prop has been used not just for supervised learning, but also in the context of reinforcement learning.
  - Tangent propagation is closely related to [dataset augmentation](../04/note.md#74-dataset-augmentation).
    - Why?)
      - In both cases, the user of the algorithm encodes his or her **prior knowledge** of the task by specifying a set of transformations that should not alter the output of the network.
    - Differences)
      - In the case of [dataset augmentation](../04/note.md#74-dataset-augmentation), the network is explicitly trained to correctly classify distinct inputs that were created by applying more than an infinitesimal amount of these transformations.
        - **Tangent propagation** does not require explicitly visiting a new input point.
      - Instead, **tangent propagation** analytically regularizes the model to resist perturbation in the directions corresponding to the specified transformation.
        - Drawbacks)
          1. **Tangent propagation** only regularizes the model to resist infinitesimal perturbation. 
             - Explicit [dataset augmentation](../04/note.md#74-dataset-augmentation) confers resistance to larger perturbations.
          2. The infinitesimal approach poses difficulties for models based on [rectified linear units](../../ch06/03/note.md#concept-rectified-linear-unit-relu).
             - These models can only shrink their derivatives by turning units off or shrinking their weights.
             - They are not able to shrink their derivatives by saturating at a high value with large weights, as [sigmoid or tanh units](../../ch06/03/note.md#632-logistic-sigmoid-and-hyperbolic-tangent) can.
  - Tangent propagation is related to **double backprop** and [adversarial training](../13/note.md#concept-adversarial-training).
    - **Double backprop** and [adversarial training](../13/note.md#concept-adversarial-training) both require that the model should be invariant to all directions of change in the input so long as the change is small.
      - **Double backprop** regularizes the Jacobian to be small.
      - [Adversarial training](../13/note.md#concept-adversarial-training) finds inputs near the original inputs and trains the model to produce the same output on these as on the original inputs.
    - **Tangent propagation** and [dataset augmentation](../04/note.md#74-dataset-augmentation) using manually specified transformations both require that the model should be invariant to certain specified directions of change in the input.

<br><br>

### Concept) Manifold Tangent Classifier
*Rifai et al., 2011c*
- Desc.)
  - The manifold tangent classifier **eliminates the need to know the tangent vectors a priori**.
  - The manifold tangent classifier use **autoencoders** to avoid needing user-specified tangent vectors.
    - why?) Autoencoders can estimate the manifold tangent vectors.
  - The algorithm proposed with the manifold tangent classifier is therefore simple:
    1. Use an autoencoder to learn the manifold structure by unsupervised learning
    2. Use these tangents to regularize a neural net classifier as in tangent prop


<br>

* [Back to Deep Learning MIT](../../main.md)