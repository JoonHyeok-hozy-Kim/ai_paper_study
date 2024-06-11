* [Back to Deep Learning MIT](../../main.md)

# 5.11 Challenges Motivating Deep Learning

## 5.11.1 The Curse of Dimensionality
- Desc.)
  - Many machine learning problems become exceedingly **difficult when the number of dimensions in the data is high**.
    - why?)
      - The number of possible distinct configurations of a set of variables increases **exponentially** as the number of variables increases.
      - Statistical Challenge
        - The number of possible configurations of $`x`$ is much larger than the number of training examples.
        - When estimating the probability density at some point $`x`$, we can just return the number of training examples in the same unit volume cell as $`x`$, divided by the total number of training examples.
        - When classifying an example, we can return the most common class of training examples in the same cell.
        - But, what if there is no training example near $`x`$?
        - This problem arises substantially as the dimensionality of the data increases.

<br><br>

## 5.11.2 Local Constancy and Smoothness Regulation
### Concept) Prior Belief
- Desc.)
  - In order to generalize well, machine learning algorithms need to be guided by **prior beliefs** about what kind of function they should learn.
  - Prior beliefs can be
    - in the form of probability distributions
    - directly influencing the function itself
    - indirectly acting on the parameters via their effect on the function

<br>

### Concept) Smoothness Prior (Local Constancy Prior)
- Desc.)
  - This [prior](#concept-prior-belief) states that the function we learn should not change very much within the region.
    - i.e.) $`f^\ast(x) \approx f^\ast(x+\epsilon)`$
      - If we know a good answer for an input $`x`$, then the answer is probably good in the neighborhood of $`x`$.
- Props.)
  - Many **simpler** algorithms rely exclusively on this prior to generalize well.
  - They fail to scale to the statistical challenges involved in solving AI-level tasks.
- e.g.)
  - $`k`$-nearest neighbors family of learning algorithms
    - These predictors are literally constant over each region containing all the points $`x`$ that have the same set of $`k`$ nearest neighbors in the training set.
    - For $`k=1`$, the number of distinguishable regions cannot exceed the number of training examples.
  - Kernel Machines
    - Consider the **local kernels** where $`k(u,v)`$ is large when $`u=v`$ and decreases as $`u`$ and $`v`$ grow farther apart from each other.
    - A local kernel can be thought of as a **similarity function** that performs template matching, by measuring how closely a test example $`x`$ resembles each training example $`x^{(i)}`$
  - Decision Trees
    - Decision trees break the input space into as many regions as there are leaves and use a separate parameter in each region.
    - If the target function requires a tree with at least $`n`$ leaves to be represented accurately, then at least $`n`$ training examples are required to fit the tree.
      - i.e.) A multiple of $`n`$ is needed to achieve some level of statistical confidence in the predicted output.

<br><br>

## 5.11.3 Manifold Learning
### Concept) Manifold
- Desc.)
  - A connected region
  - Mathematically, it is a set of points, associated with a neighborhood around each point. 
    - From any given point, the manifold locally appears to be a Euclidean space. 
      - e.g.) In everyday life, we experience the surface of the world as a 2-D plane, but it is in fact a spherical manifold in 3-D space.
  - In ML, it is a connected set of points that can be **approximated well** by considering only a small number of degrees of freedom, or dimensions, embedded in a higher-dimensional space.

<br>

### Concept) Manifold Learning
- Desc.)
  - Many machine learning problems seem hopeless if we expect the machine learning algorithm to learn functions with interesting **variations across all of** $`\mathbb{R}^n`$.
  - Manifold Learning algorithms assume that 
    - most of $`\mathbb{R}^n`$ consists of invalid input.
    - interesting inputs occur only along a collection of manifolds containing a small subset of points
      - with interesting variations in the output of the learned function occurring only along directions that lie on the manifold
      - or, with interesting variations happening only when we move from one manifold to another.


<br>

* [Back to Deep Learning MIT](../../main.md)