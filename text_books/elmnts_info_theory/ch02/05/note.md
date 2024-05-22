* [Back to Elements of Information Theory](../../main.md)

# 2.5 Chain Rules for Entropy, Relative Entropy, and Mutual Information

### Prop.) General Multiplication Law of Conditional Probabilities
$`\begin{aligned}
    p(x_1, x_2, \cdots, x_n) &= p(x_1) p(x_2|x_1) p(x_3|x_1,x_2) \cdots p(x_n|x_1,\cdots,x_{n-1}) \\
    &= \displaystyle\prod_{i=1}^n p(x_i|x_1,\cdots,x_{i-1})
\end{aligned}`$
- Derivation)
  - The order of events.
    1. $`x_1`$ happens and its probability is $`p(x_1)`$.
    2. $`x_2`$ happens after $`x_1`$ and its probability is $`p(x_2|x_1)`$.
    3. $`x_3`$ happens after $`x_1,x_2`$ and its probability is $`p(x_3|x_1,x_2)`$.
    4. Thus, $`x_n`$ happens after $`x_1,x_2,\cdots,x_{n-1}`$ 
       - And its probability is $`p(x_n|x_1,\cdots,x_{n-1})`$.
  - Hence, the probability that $`x_1,\cdots,x_n`$ happens will be
    - $`p(x_1) p(x_2|x_1) p(x_3|x_1,x_2) \cdots p(x_n|x_1,\cdots,x_{n-1}) = \displaystyle\prod_{i=1}^n p(x_i|x_1,\cdots,x_{i-1})`$

<br>

### Theorem 2.5.1) Chain Rule for Entropy
$`\displaystyle H(X_1, X_2, \cdots, X_n) = \sum_{i=1}^n H(X_i|X_1, \cdots, X_{i-1})`$
- pf.)   
  - By definition, 
    - $`\displaystyle H(X_1, X_2, \cdots, X_n) = -\sum_{x_1, \cdots, x_n} p(x_1, \cdots, x_n) \log{p(x_1, \cdots, x_n)}`$.
  - Then by the [General Multiplication Law](#prop-general-multiplication-law-of-conditional-probabilities),   
    $`\begin{aligned}
        \displaystyle H(X_1, X_2, \cdots, X_n) &= -\sum_{x_1, \cdots, x_n} p(x_1, \cdots, x_n) \log{\prod_{i=1}^n p(x_i|x_1,\cdots,x_{i-1})} \\
        &= -\sum_{x_1, \cdots, x_n} \left(p(x_1, \cdots, x_n) \left(\sum_{i=1}^{n} \log{p(x_i|x_1,\cdots,x_{i-1})}\right)\right) \\
        &= -\sum_{x_1, \cdots, x_n}  \left(\sum_{i=1}^{n} p(x_1, \cdots, x_n) \log{p(x_i|x_1,\cdots,x_{i-1})}\right) \\
        &= -\sum_{i=1}^{n}\sum_{x_1, \cdots, x_n} p(x_1, \cdots, x_n) \log{p(x_i|x_1,\cdots,x_{i-1})} \\
    \end{aligned}`$.
  - Consider that $`\forall i < n`$ 
    - $`\displaystyle \sum_{x_1, \cdots, x_{i-1}, x_i, x_n} p(x_1, \cdots, x_{i-1}, x_i, x_n) \log{p(x_i|x_1,\cdots,x_{i-1})} = \sum_{x_1, \cdots, x_{i-1}, x_i} p(x_1, \cdots, x_{i-1}, x_i) \log{p(x_i|x_1,\cdots,x_{i-1})}`$
      - i.e.) Independent of $`x_n`$.
  - Thus,   
    $`\begin{aligned}
    \displaystyle H(X_1, X_2, \cdots, X_n) &= -\sum_{i=1}^{n} \left(\sum_{x_1, \cdots, x_i} p(x_1, \cdots, x_i) \log{p(x_i|x_1,\cdots,x_{i-1})}\right) \\
    &= \sum_{i=1}^{n} H(X_i|X_1,\cdots,X_{i-1})
    \end{aligned}`$

<br><br>

### Concept) Conditional Mutual Information
- Def.)
  - For random variables $`X,Y,Z`$
  - the **conditional mutual information** is defined by   
    $`\begin{aligned}
        I(X;Y|Z) &= H(X|Z) - H(X|Y,Z) \\
        &= E_{p(x,y,z)} \log\frac{p(X,Y|Z)}{p(X|Z)p(Y|Z)}
    \end{aligned}`$


<br>

* [Back to Elements of Information Theory](../../main.md)