* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 8.4 Radial Basis Functions
A smooth linear combination of many local 
approximations to the target function.

### Concept) Radial Basis Function
- Def.)
  - $\hat{f}(x)=w_0 \Sigma_{u=1}^k w_uK_u(d(x_u,x))$
    - where
      - $k$ : a user-provided number of kernel functions to be included
        - [Suggestions for choosing k](#tech-how-to-choose-the-number-of-hidden-units)
      - $x_u$ : an instance from $X$ 
      - $K_u(d(x_u,x))$ : the kernel function
        - $\frac{\partial \; K_u(d(x_u,x))}{\partial \; d(x_u,x)} \lt 0$
          - Gaussian is commonly used.
            - $K_u(d(x_u,x))=e^{\frac{1}{2\sigma_u^2} d^2(x_u,x)}$
              - where $K_u$ is centered at the point $x_u$ with some variance $\sigma_u^2$.
- Analysis
            - *Hartman et al. (1990)*
              - The functional form of Equation (8.8) can 
approximate any function with arbitrarily small error, provided a sufficiently large 
number k of such Gaussian kernels and provided the width a2 of each kernel can 
be separately specified



<br>

#### Tech) How to Choose the Number of Hidden Units












<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)