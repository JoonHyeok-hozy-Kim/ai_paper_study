* [Back to Elements of Information Theory](../../main.md)

# 5.4 Bounds on the Optimal Code Length

### Theorem 5.4.1) Bounds on the Optimal Code Length
- Theorem)
  - Let 
    - $`l_1^\ast, l_2^\ast, \cdots, l_m^\ast`$ : the optimal codeword lengths for a source distribution $`\mathbf{p}`$ and a $`D`$-ary alphabet
    - $`L^\ast`$ : the expected length of an optimal code associated with $`l_i^\ast`$
      - i.e.) $`\displaystyle L^\ast = \sum_i p_i l_i^\ast`$
  - Then
    - $`H_D(X) \le L^\ast \lt H_D(X) + 1`$
      - i.e.) A code that achieves an expected description length $`L^\ast`$ within 1 bit of the lower bound $`H_D(X)`$.
- pf.)
  - From [Theorem 5.3.1](../03/note.md#theorem-531-lower-bound-for-the-expected-length-of-instantaneous-codeword), we obtained
    - $`H_D(X) \le L`$.
    - If $`L=H`$, then $`\displaystyle l_i = \log_D \frac{1}{p_i}`$`.
  - Since $`\log_D \frac{1}{p_i}`$` may not equal an integer, we round it up as
    - $`\displaystyle l_i = \left\lceil \log_D \frac{1}{p_i} \right\rceil`$
      - where $`\left\lceil x \right\rceil`$ is the smallest integer greater than or equal to $`x`$.
    - Then, these $`l_i`$s satisfy the [Kraft inequality](../02/note.md#theorem-521-kraft-inequality) since
      - $`\displaystyle \sum D^{-l_i} = \sum D^{-\left\lceil \log_D \frac{1}{p_i} \right\rceil} \le \sum D^{-\log_D \frac{1}{p_i}} = 1`$.
  - Then    
    $`\begin{aligned}
        & \log_D\frac{1}{p_i} \le l_i \lt \log_D\frac{1}{p_i} + 1 \\
        \Rightarrow & \; p_i \log_D\frac{1}{p_i} \le p_i  l_i \lt p_i \log_D\frac{1}{p_i} + p_i \\
        \Rightarrow & \; \sum p_i \log_D\frac{1}{p_i} \le \sum p_i  l_i \lt \sum \left(p_i \log_D\frac{1}{p_i} + p_i\right) \\
        \Leftrightarrow & \; H_D(X) \le L \lt H_D(X) + 1 & \because \sum p_i = 1 \\
    \end{aligned}`$
  - Consider that $`L^\ast \lt L = \sum p_i l_i`$.
    - $`\because L^\ast`$ is the length of the optimal code
  - Also, $`L^\ast \ge H_D`$ ($`\because`$ [Theorem 5.3.1](../03/note.md#theorem-531-lower-bound-for-the-expected-length-of-instantaneous-codeword)).
  - Therefore, $`H_D(X) \le L^\ast \lt L \lt H_D(X) + 1`$

<br><br>

### Concept) Reducing the Overhead per Symbol by Spreading out
- Problem)
  - Overhead of at most $`1`$ bit.
    - Why?) By [Theorem 5.3.1](../03/note.md#theorem-531-lower-bound-for-the-expected-length-of-instantaneous-codeword), $`l_i = \log_D \frac{1}{p_i}`$ is not always an integer.
- Sol.)
  - Reduce the overhead per symbol by spreading out over many symbols.
    - $`\displaystyle H(X) \le L_n \lt H(X) + \frac{1}{n}`$
      - where $`L_n`$ is the expected codeword length per input symbol.
- Settings)
  - A system in which we sent a sequence of $`n`$ symbols from $`X`$
    - where the symbols are drawn i.i.d. according to $`p(x)`$
      - For non-i.i.d. case, refer to [Theorem 5.4.2](#theorem-542).
    - i.e.) supersymbol from the alphabet $`\mathcal{X}^n`$
  - $`\begin{aligned}
      L_n &= \frac{1}{n}\sum p(x_1,x_2, \cdots, x_n) l(x_1,x_2, \cdots, x_n) \\
      &= \frac{1}{n} E_{p(x)} l(x_1,x_2, \cdots, x_n)
  \end{aligned}`$ : the expected codeword length per input symbol.
    - where $`l(x_1,x_2, \cdots, x_n)`$ is the length of the codeword $`(x_1,x_2, \cdots, x_n)`$.
- Derivation)
  - Apply the bound from [Theorem 5.4.1](#theorem-541-bounds-on-the-optimal-code-length) to the code as
    - $`H(X_1, X_2, \cdots, X_n) \le E l(X_1, X_2, \cdots, X_n) \lt H(X_1, X_2, \cdots, X_n) + 1 \; \cdots (A)`$
  - Since $`X_i \stackrel{i.i.d.}{\sim} P(X)`$,   
    $`\begin{aligned}
        H(X_1, X_2, \cdots, X_n) &= \sum_i H(X_i) & \because \textrm{Theorem 2.6.6} \\
        &= nH(X)
    \end{aligned}`$
    - cf.) [Theorem 2.6.6) Independence Bound on Entropy](../../ch02/06/note.md#theorem-266-independence-bound-on-entropy)
  - Dividing $`(A)`$ with $`n`$, we get
    - $`\displaystyle H(X) \le L_n \lt H(X) + \frac{1}{n}`$

<br><br>

### Theorem 5.4.2) 
- Theorem)
  - The minimum expected codeword length per symbol satisfies
    - $`\displaystyle \frac{H(X_1, X_2, \cdots, X_n)}{n} \le L_n^\ast \lt \frac{H(X_1, X_2, \cdots, X_n)}{n} +\frac{1}{n}`$
  - Moreover, if $`X_1, X_2, \cdots, X_n`$ is a [stationary](../../ch04/01/note.md#concept-stationary) stochastic process,
    - then $`L_n^\ast \rightarrow H(\mathcal{X})`$
- pf.)
  - Recall the [concept of reducing the overhead per symbol by spreading out over many symbols](#concept-reducing-the-overhead-per-symbol-by-spreading-out).
  - Applying the bound from [Theorem 5.4.1](#theorem-541-bounds-on-the-optimal-code-length), we had   
    $`\begin{aligned}
        & H(X_1, X_2, \cdots, X_n) \le E l(X_1, X_2, \cdots, X_n) \lt H(X_1, X_2, \cdots, X_n) + 1 \\
        \Rightarrow &\; \frac{H(X_1, X_2, \cdots, X_n)}{n} \le L_n \lt \frac{H(X_1, X_2, \cdots, X_n)}{n} +\frac{1}{n}
    \end{aligned}`$
  - By the definition of the [entropy rate](../../ch04/02/note.md#concept-entropy-rate-per-symbol), we get
    - $`\displaystyle \frac{H(X_1, X_2, \cdots, X_n)}{n} \rightarrow H(\mathcal{X})`$
  - Thus, $`n \rightarrow\infty \Rightarrow L_n^\ast \rightarrow H(\mathcal{X})`$
- Meaning)
  - We can think of the [entropy rate](../../ch04/02/note.md#concept-entropy-rate-per-symbol) as the expected number of bits per symbol required to describe the process.

<br><br>

### Theorem 5.4.3) Expected Length of a Wrong Code
- Ideation)
  - We try to estimate the true distribution $`\mathbf{p}`$ of the symbols.
  - But in practice, the wrong distribution $`\mathbf{q}`$ may be the best estimate that we can make of the unknown true distribution $`\mathbf{p}`$.
  - Then what is the expected length of the wrong code?
- Theorem)
  - The expected length under $`p(x)`$ of the code assignment $`l(x) = \left\lceil \log \frac{1}{q(x)} \right\rceil`$ satisfies
    - $`H(p) + D(p||q) \le E_p l(X) \lt H(p) + D(p||q) + 1`$
- pf.)
  - The lower bound can be derived as   
    $`\begin{aligned}
        E l(X) &= \sum_x p(x) \left\lceil \log \frac{1}{q(x)} \right\rceil \\
        &\ge \sum_x p(x) \left( \log \frac{1}{q(x)} \right) \\
        &= \sum_x p(x) \left( \log \frac{p(x)}{q(x)p(x)} \right) \\
        &= \sum_x p(x) \log \frac{p(x)}{q(x)} + \sum_x p(x) \log \frac{1}{p(x)} \\
        &= D(p||q) + H(p)
    \end{aligned}`$
  - The upper bound can be derived as   
    $`\begin{aligned}
        E l(X) &= \sum_x p(x) \left\lceil \log \frac{1}{q(x)} \right\rceil \\
        &\lt \sum_x p(x) \left( \log \frac{1}{q(x)} + 1 \right) \\
        &= \sum_x p(x) \left( \log \frac{p(x)}{q(x)p(x)} + 1 \right) \\
        &= \sum_x p(x) \log \frac{p(x)}{q(x)} + \sum_x p(x) \log \frac{1}{p(x)} + 1 & \because \sum_x p(x) = 1 \\
        &= D(p||q) + H(p) + 1
    \end{aligned}`$
  - Thus, $`H(p) + D(p||q) \le E_p l(X) \lt H(p) + D(p||q) + 1`$
- Meaning)
  - Believing that the distribution is $`q(x)`$ when the true distribution is $`p(x)`$ incurs a penalty of $`D(p||q)`$ in the average description length.





<br>

* [Back to Elements of Information Theory](../../main.md)