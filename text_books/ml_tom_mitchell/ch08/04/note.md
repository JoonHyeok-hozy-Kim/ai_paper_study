* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 8.4 Radial Basis Functions
A smooth linear combination of many local 
approximations to the target function.

### Concept) Radial Basis Function
- Def.)
  - $\hat{f}(x)=w_0 + \Sigma_{u=1}^k w_uK_u(d(x_u,x))$
    - where
      - $k$ : a user-provided number of kernel functions to be included
        - [Suggestions for choosing k](#tech-how-to-choose-the-number-of-hidden-units)
      - $x_u$ : an instance from $X$ 
      - $K_u(d(x_u,x))$ : the kernel function
        - $\frac{\partial \; K_u(d(x_u,x))}{\partial \; d(x_u,x)} \lt 0$
          - Gaussian is commonly used.
            - $K_u(d(x_u,x))=e^{\frac{1}{2\sigma_u^2} d^2(x_u,x)}$
              - where $K_u$ is centered at the point $x_u$ with some variance $\sigma_u^2$.

![](images/001.png)

- Procedures)
  1. $k$ is determined.
     - i.e.) the number of hidden units
  2. For each hidden unit $u$...
     - Choose the values of $x_u$ and $\sigma_u^2$.
     - Define $K_u(d(x_u,x))$ with $x_u$ and $\sigma_u^2$.
  3. Train the weights $w_u$.
     - How?)
       - $\arg\min_{\mathbf{w}} E\equiv\frac{1}{2}\sum_{x\in D} \left( f(x)-\hat{f}(x) \right)^2$
         - where $\mathbf{w}=[w_1, \cdots, w_u]$
- Analysis)
  - $\hat{f}(x)=w_0 + \Sigma_{u=1}^k w_uK_u(d(x_u,x))$ can approximate any function with arbitrarily small error.
    - Assumptions)
      - A sufficiently large number $k$ of such Gaussian kernels are provided.
      - The width $\sigma^2$ of each kernel can be separately specified.
    - Refer to *Hartman et al. (1990)*
  - Radial Basis Function can be seen as a **two-layered network**.
    1. A Layer of units computes the values of the various $K_u(d(x_u,x))$.
    2. Another layer computes the linear combination of the first layer unit values.



<br>

#### Tech) How to Choose the Number of Hidden Units












<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)