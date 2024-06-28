* [Back to Deep Learning MIT](../../main.md)

# 7.6 Semi-Supervised Learning
- Desc.)
  - In the context of deep learning, semi-supervised learning usually refers to learning a representation $`h = f(x)`$.
  - The goal is to learn a representation so that **examples from the same class have similar representations**.
- Implementations)
  - **Unsupervised** learning can provide useful cues for how to group examples in representation space.
    - Examples that **cluster** tightly in the input space should be mapped to similar representations.
    - A linear classifier in the new space may achieve better generalization in many cases.
      - A long-standing variant of this approach is the application of [principal components analysis (PCA)](../../ch05/08/note.md#581-principal-component-analysis-pca) as a **pre-processing** step before applying a classifier.
  - Constructing models in which a generative model of either $`P(\mathbf{x})`$ or $`P(\mathbf{x, y})`$ shares parameters with a discriminative model of $`P(\mathbf{y|x})`$.
    - i.e.) Combining **unsupervised** and **supervised** components in the model
    - Then, trade-off the **supervised** criterion $`-\log P(\mathbf{y|x})`$ with the **unsupervised** criterion of $`-\log P(\mathbf{x})`$ or the **generative** one of $`-\log P(\mathbf{x,y})`$.
    - The **generative** criterion then expresses a particular form of prior belief about the solution to the supervised learning problem.
      - The structure of $`P(\mathbf{x})`$ is connected to the structure of $`P(\mathbf{y|x})`$ in a way that is captured by the shared parametrization.
      - By controlling how much of the **generative** criterion is included in the total criterion, one can find a better trade-off than with a **purely generative** or a **purely discriminative** training criterion.
  - *Salakhutdinov and Hinton (2008)* describe a method for learning the [kernel function](../../ch05/07/note.md#concept-kernel) of a kernel machine used for regression, in which the usage of unlabeled examples for modeling $`P(\mathbf{x})`$ improves $`P(\mathbf{y|x})`$ quite significantly. 














<br>

* [Back to Deep Learning MIT](../../main.md)