* [Back to Deep Learning MIT](../../main.md)

# 2.12 Example: Principal Components Analysis

### E.g.) Deriving Principal Components Analysis (PCA) 
- Objective)
  - Derive Principal Components Analysis (PCA) using only knowledge of basic linear algebra.
  - Apply lossy compression.
    - i.e.) Store the points in a way that requires less memory but may lose some precision.
- Settings)
  - $`\lbrace x^{(1)}, \cdots, x^{(m)} \rbrace \in \mathbb{R}^n`$ : a collection of $`m`$ points in $`\mathbb{R}^n`$
  - $`c^{(i)} \in \mathbb{R}^l`$ : the code vector corresponding with $`x^{(i)} \in \mathbb{R}^l`$
    - where
      - $`l \lt n`$ : $`c^{(i)}`$ becomes the lower-dimensional version of $`x^{(i)}`$.
  - $`f(x) = c`$ : the encoding function
  - $`g(f(x)) \approx x`$ : the decoding function
    - Put $`g(c) = Dc`$
      - where $`D \in \mathbb{R}^{n\times l}`$
    - i.e.) We want to find $`D`$!
- Assumption)
  - Minimizing the distance between $`x`$ and $`g(c)`$ will be the optimal solution.
    - We will use [the $`L^2`$ norm](../05/note.md#concept-norm) to measure the distance.
    - Put $`\displaystyle c^\ast = {\arg\min_c} ||x - g(c)||_2`$
  - $`D`$ is an [orthogonal matrix](../06/note.md#concept-orthogonal-matrix).
    - Why?)
      - There can be many matrices that satisfies the above $`c^\ast`$.
      - We want to give a unique solution to the problem by setting all of the columns of $`D`$ to have unit norm.
        - Then, $`D^\top D = I_l \; (\because D \in \mathbb{R}^{n\times l})`$ 
- Derivation)
  - Optimizing $`c^\ast`$
    - $`\begin{aligned}
      \displaystyle c^\ast & = \arg\min_c \; ||x - g(c)||_2 & \\
      & = \arg\min_c \; (||x - g(c)||_2)^2 & \because ||x - g(c)||_2 \textrm{ is monotonically increasing.} \\
      & = \arg\min_c \; (x-g(x))^\top (x-g(c)) & \\
      & = \arg\min_c \; x^\top x - 2x^\top g(c) + g(c)^\top g(c) & \because x, g(c) \in \mathbb{R}^n \Rightarrow x^\top g(c) = g(c)^\top x \\
      & = \arg\min_c \; - 2x^\top g(c) + g(c)^\top g(c) & \because x^\top x \textrm{ does not depend on } c \\
      & = \arg\min_c \; - 2x^\top Dc + c^\top D^\top Dc & \because g(c) = Dc \\
      & = \arg\min_c \; - 2x^\top Dc + c^\top c & \because D \textrm{ is an orthogonal matrix} \\
    \end{aligned}`$
    - Using the vector calculus we may optimize the above problem as follows.   
      $`\begin{aligned}
        \nabla_c \left( - 2x^\top Dc + c^\top c \right) = 0 \\
        -2D^\top x + 2c = 0 \\
        c = D^\top x
      \end{aligned}`$
    - Thus, we can use $`f(x) = D^\top x`$ as our encoder function.
    - Hence, our PCA reconstruction operation $`r(x)`$ can be defined as
      - $`r(x) = g(f(x)) = DD^\top x`$
  - Optimizing $`D`$
    - Ideation)
      - Recall that we defined $`D`$ as an [orthogonal matrix](../06/note.md#concept-orthogonal-matrix).
      - But there can be many candidates for this assumption.
      - If we find $`D`$ such that minimizes its [Frobenius Norm](../05/note.md#concept-frobenius-norm) there are two gains.
        1. **Dimensionality Reduction**
           - Minimizing the Frobenius norm of $`D`$ leads to a lower-dimensional representation of the data. 
           - This is achieved by shrinking the magnitude of the matrix elements, effectively removing redundant or less significant information.
        2. **Variance Maximization** 
           - Maximizing the variance of the projected data ensures that the data points are spread out as much as possible in the lower-dimensional space. 
           - This is achieved by maximizing the squared distances between the projected data points.
    - Goal)
      - Find $`D`$ that minimizes its [Frobenius Norm](../05/note.md#concept-frobenius-norm)
        - Put $`\displaystyle D^\ast = \arg\min_D \sqrt{\sum_{i,j}\left( {x^{(i)}}_j - r(x^{(i)})_j \right)}`$
          - subject to $`D^\top D = I_l`$
    - Derivation)
      - For simplicity, consider the case $`l=1`$.
        - Then, $`D`$ is a just a single vector, $`d`$.
        - We can rewrite $`D^\ast`$ as $`d^\ast`$ as follows.   
           $`\begin{aligned}
            \displaystyle d^\ast & = \arg\min_d \sum_i \left(||x^{(i)} - d^\top x^{(i)}d||_2\right)^2 & \textrm{ subject to } ||d||_2 = 1 \\
            & = \arg\min_d \sum_i \left(||x^{(i)} - {x^{(i)}}^\top d d||_2\right)^2 &  \because d^\top x^{(i)} = {x^{(i)}}^\top d \textrm{ is scalar.}
          \end{aligned}`$
        - Let $`X \in \mathbb{R}^{m\times n}`$ be the matrix defined by stacking all of the vectors describing the points.
          - i.e.) $`X = \left[ \begin{array}{c}
            {x^{(1)}}^\top \\ \vdots \\ {x^{(m)}}^\top 
          \end{array} \right] \textrm{ where } {x^{(i)}} \in \mathbb{R}^n \textrm{ was the column vector.}`$
        - Then, we can rewrite $`d^\ast`$ as follows.    
           $`\begin{aligned}
            \displaystyle d^\ast & = \arg\min_d \left(||X - Xdd^\top ||_F \right)^2 \; \textrm{ subject to } d^\top d = 1 \\
            & = \arg\min_d \textrm{Tr}\left(\left( X-Xdd^\top \right)^\top \left( X-Xdd^\top \right)\right) \\
            & = \arg\min_d \textrm{Tr} \left( X^\top X - X^\top X dd^\top -dd^\top X^\top X + dd^\top X^\top Xdd^\top \right) \\
            & = \arg\min_d \textrm{Tr}(X^\top X) - \textrm{Tr}(X^\top X dd^\top) - \textrm{Tr}(dd^\top X^\top X) + \textrm{Tr}(dd^\top X^\top Xdd^\top) \\
            & = \arg\min_d - \textrm{Tr}(X^\top X dd^\top) - \textrm{Tr}(dd^\top X^\top X) + \textrm{Tr}(dd^\top X^\top Xdd^\top) \; \because X^\top X \textrm{ is indep. of } d \\
            &= \arg\min_d -2 \textrm{Tr}(X^\top X dd^\top) + \textrm{Tr}( X^\top Xdd^\top dd^\top) \; \because \textrm{Tr}(AB) = \textrm{Tr}(BA) \\
            & (\textrm{Applying the constraint } d^\top d = 1) \\
            &= \arg\min_d -2 \textrm{Tr}(X^\top X dd^\top) + \textrm{Tr}( X^\top Xdd^\top) \; \textrm{ subject to } d^\top d = 1 \\
            &= \arg\min_d - \textrm{Tr}(X^\top X dd^\top) \; \textrm{ subject to } d^\top d = 1 \\
            &= \arg\max_d \textrm{Tr}(X^\top X dd^\top) \; \textrm{ subject to } d^\top d = 1 \\
            &= \arg\max_d \textrm{Tr}(d^\top X^\top X d) \; \textrm{ subject to } d^\top d = 1. \; (\because \textrm{Tr}(AB) = \textrm{Tr}(BA))  \\
          \end{aligned}`$
        - Now we can solve the above problem with the [eigendecomposition](../07/note.md#concept-eigendecomposition).
          - Why?)
            - The optimal $`d`$ is given by the eigenvector of $`X^\top X`$ corresponding to the largest eigenvalue.
      - Now consider $`l \gt 1`$.
        - Then the matrix $`D`$ is given by the $`l`$ eigenvectors corresponding to the largest eigenvalues.













<br>

* [Back to Deep Learning MIT](../../main.md)