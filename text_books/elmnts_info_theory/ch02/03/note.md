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
  - For
    - $`X,Y`$ : random variables
    - $`p(x,y)`$ : the joint probability mass function
    - $`p(x), p(y)`$ : the marginal probability mass function of $`x,y`$ respectively
  - the mutual information $`I(X;Y)`$ is the relative entropy between the joint distribution and the product distribution:
    - $`\displaystyle I(X;Y) = \sum_{x\in\mathcal{X}} \sum_{y\in\mathcal{Y}} p(x,y) \log\frac{p(x,y)}{p(x)p(y)}`$
- Interpretations)
  - A measure of the amount of information that one random variable contains about another random variable
- Props.)
  - $`\displaystyle I(X;Y) = D(p(x,y)||p(x)p(y))`$
  - $`\displaystyle I(X;Y) = E_{p(x,y)}\log\frac{p(X,Y)}{p(X)p(Y)}`$
  - [Theorems w.r.t. Entropy](../04/note.md#theorem-241)

#### E.g.)
- Settings)
  - $`\mathcal{X} = \lbrace 0, 1 \rbrace`$
  - $`p,q`$ : distributions on $`\mathcal{X}`$
    - where
      - $`p(x) = \begin{cases} 1-r & x=0 \\ r & x=1 \end{cases}`$
      - $`q(x) = \begin{cases} 1-s & x=0 \\ s & x=1 \end{cases}`$
- Then
  - $`D(p||q) = \begin{array}{ccc}
    \underbrace{(1-r)\log\frac{1-r}{1-s}} & + & \underbrace{r\log\frac{r}{s}} \\
    x=1 && x=0
  \end{array}`$
  - $`D(q||p) = \begin{array}{ccc}
    \underbrace{(1-s)\log\frac{1-s}{1-r}} & + & \underbrace{s\log\frac{s}{r}} \\
    x=1 && x=0
  \end{array}`$
- Cases with Values)
  - $`r=s=\frac{1}{2}`$
    - $`D(p||q) = D(q||p) = 0`$
  - $`r=\frac{1}{2}, s=\frac{1}{4}`$
    - $`D(p||q) = \frac{1}{2}\log\frac{1/2}{3/4} + \frac{1}{2}\log\frac{1/2}{1/4} = 1-\frac{\log3}{2}`$
    - $`D(q||p) = \frac{3}{4}\log\frac{3/4}{1/2} + \frac{1}{4}\log\frac{1/4}{1/2} = \frac{3}{4}\log3 - 1`$
    - Thus, $`D(p||q) \ne D(q||p)`$
      

<br>

* [Back to Elements of Information Theory](../../main.md)