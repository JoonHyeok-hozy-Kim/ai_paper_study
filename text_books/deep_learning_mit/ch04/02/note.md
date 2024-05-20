* [Back to Deep Learning MIT](../../main.md)

# 4.2 Poor Conditioning

### Concept) Conditioning
- Def.)
  - Conditioning refers to **how rapidly a function changes with respect to small changes in its inputs**.
- Related Problems)
  - Functions that change rapidly when their inputs are perturbed slightly can be problematic for scientific computation because rounding errors in the inputs
 can result in large changes in the output.

<br>

### Concept) Condition Number
- Def.)
  - Let
    - $`f(x) = A^{-1}x`$ : a function
      - where
        - $`A \in \mathbb{R}^{n\times n}`$ : a matrix that has an eigenvalue decomposition
  - Then, $`f(x)`$'s condition number is defined by
    - $`\displaystyle\max_{i,j}\left|\frac{\lambda_i}{\lambda_j}\right|`$
      - i.e.) The ratio of the magnitude of the largest and smallest eigenvalue.
- Prop.)
  - When this number is large, matrix inversion is particularly sensitive to error in the input.
  - This sensitivity is an intrinsic property of the matrix itself, not the result of rounding error during matrix inversion.
    - Poorly conditioned matrices amplify pre-existing errors when we multiply by the true matrix inverse.








<br>

* [Back to Deep Learning MIT](../../main.md)