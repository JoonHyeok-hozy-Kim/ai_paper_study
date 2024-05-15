* [Back to Deep Learning MIT](../../main.md)

#  3.10 Useful Properties of Common Functions

### Concept) Logistic Sigmoid
- Def.)
  - $`\displaystyle\sigma(x) = \frac{1}{1+\exp{-x}}`$
- Usages)
  - Generating $`\phi`$ of the [Bernoulli distribution](../09/note.md#391-bernoulli-distribution).

<br>

### Concept) Softplus
- Def.)
  - $`\varsigma(x) = \log{(1+\exp(x))}`$
    - cf.) A smoothed version of the function $`x^{+} = \max(0, x)`$
- Usages)
  - Generating $`\sigma, \beta`$ of the [Gaussian distribution](../09/note.md#393-gaussian-distribution-normal-distribution).

![](images/001.png)







<br>

* [Back to Deep Learning MIT](../../main.md)