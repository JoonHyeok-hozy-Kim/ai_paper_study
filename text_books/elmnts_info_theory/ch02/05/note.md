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
    4. Likewise, $`x_n`$ happens after $`x_1,x_2,\cdots,x_{n-1}`$ 
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
        &= -\sum_{i=1}^{n}\sum_{x_1, \cdots, x_n} p(x_1, \cdots, x_n) \log{p(x_i|x_1,\cdots,x_{i-1})} \\
    \end{aligned}`$.
  - Consider $`\forall i < n`$. 
    - Then,    
      $`\displaystyle \sum_{x_1, \cdots, x_{i-1}, x_i, x_n} p(x_1, \cdots, x_{i-1}, x_i, x_n) \log{p(x_i|x_1,\cdots,x_{i-1})} = \sum_{x_1, \cdots, x_{i-1}, x_i} p(x_1, \cdots, x_{i-1}, x_i) \log{p(x_i|x_1,\cdots,x_{i-1})}`$
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

<br><br>

### Theorem 2.5.2) Chain Rule for Information
$`\displaystyle I(X_1, X_2, \cdots, X_n; Y) = \sum_{i=1}^n I(X_i; Y|X_1, X_2, \cdots, X_{i-1})`$
- pf.)   
  - By [Thm. 2.4.1 (2.43)](../04/note.md#243),
    - $`I(X_1, X_2, \cdots, X_n; Y) = H(X_1, X_2, \cdots, X_n) - H(X_1, X_2, \cdots, X_n|Y)`$
  - By [the Chain Rule for Entropy](#theorem-251-chain-rule-for-entropy),   
    $`\displaystyle = \sum_{i=1}^n H(X_i|X_1, \cdots, X_{i-1}) - \sum_{i=1}^n H(X_i|X_1, \cdots, X_{i-1}, Y)`$
  - By the definition of [the Conditional Mutual Information](#concept-conditional-mutual-information),   
    $`= \displaystyle = \sum_{i=1}^n I(X_i; Y|X_1, \cdots, X_{i-1})`$

<br><br>

### Concept) Conditional Relative Entropy
- Def.)
  - For joint probability mass functions $`p(x,y)`$ and $`q(x,y)`$
  - the **conditional relative entropy** $`D(p(y|x) || q(y|x))`$ is the average of the [relative entropies (K-L Divergence)](../03/note.md#concept-relative-entropy-kullbackleibler-distance) between $`p(x,y)`$ and $`q(x,y)`$ over $`p(x)`$.
    - i.e.)   
      $`\begin{aligned}
        D(p(y|x) || q(y|x)) &\equiv \sum_x p(x) \sum_y p(y|x) \log\frac{p(y|x)}{q(y|x)} \\
        &= \sum_x\sum_y p(x)  p(y|x) \log\frac{p(y|x)}{q(y|x)} \\
        &= \sum_x\sum_y p(x,y) \log\frac{p(y|x)}{q(y|x)} \\
        &= E_{p(x,y)}\log\frac{p(Y|X)}{q(Y|X)}
      \end{aligned}`$
- Props.)
  - Consider that the notation $`D(p(y|x) || q(y|x))`$ omits mentioning the distribution $`p(x)`$.

<br><br>

### Theorem 2.5.3) Chain Rule for Relative Entropy
$`D(p(x,y) || q(x,y)) = D(p(x) || q(x)) + D(p(y|x) || q(y|x))`$
- pf.)
  - By the definition of the [relative entropy (K-L Divergence)](../03/note.md#concept-relative-entropy-kullbackleibler-distance),   
    $`\begin{aligned}
      D(p(x,y)||q(x,y)) & = \sum_x\sum_y p(x,y)\log\frac{p(x,y)}{q(x,y)} \\
      & = \sum_x\sum_y p(x,y)\log\frac{p(y|x)p(x)}{q(y|x)q(x)} \\
      & = \sum_x\sum_y p(x,y)\log\frac{p(x)}{q(x)} + \sum_x\sum_y p(x,y)\log\frac{p(y|x)}{q(y|x)} \\
      &= D(p(x)||q(x)) + D(p(y|x)||q(y|x))
    \end{aligned}`$
    - cf.) Refer to the definition of the [conditional relative entropy](#concept-conditional-relative-entropy).



<br>

* [Back to Elements of Information Theory](../../main.md)