* [Back to Elements of Information Theory](../../main.md)

# 2.3 Relative Entropy and Mutual Information

### Concept) Relative Entropy (Kullback–Leibler Distance)
- Def.)
  - For $`p(x), q(x)`$ : probability mass functions
  - the relative entropy $`D(p||q)`$ is defined as
    - $`\displaystyle D(p||q) \equiv \sum_{x\in\mathcal{X}} p(x)\log\frac{p(x)}{q(x)} = E_p \log\frac{p(x)}{q(x)}`$
- Interpretations)
  - A measure of the distance between two distributions
    - However, it does not satisfy all the qualifications as a measure of distance.
      - e.g.) not symmetric, not satisfying triangle inequality, etc
  - An expected logarithm of the likelihood ratio
  - A measure of the inefficiency of assuming that the distribution is $`q`$ when the true distribution is $`p`$.
    - Application)
      - Suppose we calculated $`H(p)`$.
      - Then, $`H(q) = H(p) + D(p||q)`$
- Prop.)
  - Edge Cases)
    - $`\exists x \in \mathcal{X}`$ such that...
      - $`p(x) \gt 0, q(x)=0 \Rightarrow D(p||q) = \infty`$
      - $`p(x)= 0, q(x)=0 \Rightarrow D(p||q) = 0`$

<br>

### Concept) Mutual Information
- Def.)
  - 








<br>

* [Back to Elements of Information Theory](../../main.md)