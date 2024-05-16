* [Back to Deep Learning MIT](../../main.md)

# 3.12 Technical Details of Continuous Variables
A brief sketch of the measure theory

<br>

### Concept) Measure Theory
- Objective)
  - Get a characterization of the set of **sets** that we can compute the probability of without encountering paradoxes.
    - Why sets?)
      - Recall that we defined the [probability density function of a continuous variable](../03/note.md#concept-probability-density-function-pdf) as follows. 
        - Def.)
          - For
            - $`\mathbb{S}`$ : a set
            - $`\mathbf{x} \in \mathbb{S}`$ : a continuous vector random variable
          - The probability of $`\mathbf{x}`$ is given by $`\displaystyle\int_\mathbb{S}p(x)`$.
      - However, some choices of $`\mathbb{S}`$ can produce paradox.
        - e.g.)
          - Consider $`\mathbb{S}_1`$ and $`\mathbb{S}_2`$ such that
            - $`p(x\in\mathbb{S}_1)+p(x\in\mathbb{S}_2)\gt1`$ but $`\mathbb{S}_1\cap\mathbb{S}_2 = \emptyset`$
    - Remedy)
      - **Measure theory** can characterize sets and provide ways to avoid such confusions.

<br>

#### Concept) Measure Zero
- Desc.)
  - A rigorous way of describing that **a set of points is negligibly small** in the measure theory.
- e.g.)
  - Consider $`\mathbb{R}^2`$.
    - A point has no volume.
    - A line, which is the set of points, has the zero volume.
  - The set of all the rational numbers has measure zero.


#### Concept) Almost Everywhere
- Desc.)
  - A property that holds **almost everywhere** holds throughout all of space **except** for on a set of [measure zero](#concept-measure-zero).
  - Because the exceptions occupy a negligible amount of space, they can be **safely ignored** for many applications.
  - Some important results in probability theory hold for all **discrete values** but only hold *“almost everywhere”* for **continuous values**.


<br>

#### Analysis) Handling Deterministic Functions
- Case)
  - Settings)
    - $`\mathbf{x, y}`$ : random variables
      - such that $`y = g(x)`$
        - where $`g`$ is invertible, continuous, and differentiable.
  - Problem)
    - $`p_y(y) \ne p_x(g^{-1}(y))`$
      - Why?)
        - $`g`$ expands/contracts the space!
      - e.g.)
        - Suppose $`\mathbf{y} = \frac{\mathbf{x}}{2} \textrm{ and } \mathbf{x}\sim U(0,1)`$.
        - If $`p_y(y) = p_x(g^{-1}(y)) = p_x(2y)`$ then $`p_y =\begin{cases}
            1 & y\in[0,\frac{1}{2}] \\ 0 & \textrm{otherwise}
        \end{cases}`$.
            - Thus, $`\displaystyle\int p_y(y)dy = \frac{1}{2} \cdots\otimes`$
      - Sol.)
        - Scalar Case)
          - Here, we should preserve the property $`|p_y(y)dy| = |p_y(g(x))dy| = |p_x(x)dx|`$.
            - So that $`\displaystyle\int p_y(y)dy = \int p_x(x)dy = 1`$.
          - Then $`\displaystyle p_y(y) = p_x(g^{-1}(y))\left|\frac{\partial x}{\partial y}\right|`$
            - or equivalently $`\displaystyle p_x(x) = p_y(g(x))\left|\frac{\partial g(x)}{\partial x}\right|`$
        - Higher Dimensions)
          - The derivative generalizes to the determinant of the Jacobian matrix.
            - $`\displaystyle p_x(x) = p_y(g(x))\left|\det\left(\frac{\partial g(x)}{\partial x}\right) \right|`$






<br>

* [Back to Deep Learning MIT](../../main.md)