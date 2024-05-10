* [Back to Deep Learning MIT](../../main.md)

# 2.5 Norms

### Concept) Norm
- Def.)
  - A norm is a function that satisfies
    1. $`f(x) = 0 \Rightarrow x = 0`$
    2. $`f(x+y) \le f(x) + f(y)`$ : the triangle inequality
    3. $`\forall \alpha\in\mathbb{R},\; f(\alpha x) = |\alpha| f(x)`$
- Prop.)
  - The dot product of two vectors can be rewritten in terms of norms.
  - e.g.)
    - For $`x,y \in \mathbb{R}^n`$, $`\theta`$ the angle between $`x`$ and $`y`$
      - $`x^\top y = ||x||_2 ||y||_2 \cos\theta`$

<br>

- Concept) The $`L^p`$ Norm 
  - Def.)
    - $`\displaystyle ||x||_p = \left(\sum_i|x_i|^p\right)^{\frac{1}{p}}`$ where $`p \ge 1`$.
  - e.g.)
    - The $`L^2`$ Norm
      - i.e.) 
        - Euclidean Norm : the Euclidean distance from the origin to the point identified by $`x`$.
      - Usage)
        - Measuring the size of vector $`x`$ : $`x^\top x`$
      - Prop.)
        - The derivatives of the **squared** $L^2$ norm w.r.t. each element of $x$ each **depend** only **on** the corresponding **element** of $x$.
          - But the squared $L^2$ norm is undesirable in many contexts.
            - Why?)
              - It increases very slowly near the origin.
            - Instead, use the $L^1$ norm.
        - All derivatives of the $L^2$ norm depend on the entire vector $x$.
    - The $`L^1`$ Norm
      - Def.)
        - $`\displaystyle ||x||_1 = \sum_i|x_i|`$
      - Usage)
        - The $L^1$ norm is commonly used in machine learning when the difference between zero and nonzero elements is very important.


<br>

#### Concept) Max Norm
- Def.)
  - The absolute value of the element with the largest magnitude in the vector.
  - $`\displaystyle ||x||_\infty = \max_i |x_i|`$


<br>

#### Concept) Frobenius Norm
- Def.)
  - For a matrix $`A`$,
    - $`\displaystyle||A||_F = \sqrt{\sum_{i,j} A_{i,j}^2}`$
- Prop.)
  - Measures the size of a matrix.





<br>

* [Back to Deep Learning MIT](../../main.md)