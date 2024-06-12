* [Back to Elements of Information Theory](../../main.md)

# 4.2 Entropy Rate

### Concept) Entropy Rate (per Symbol)
- Def.)
  - The entropy of a stochastic process $`\{X_i\}`$ is defined by
    - $`\displaystyle H(\mathcal{X}) = \lim_{n\rightarrow\infty} H(X_1, X_2,\cdots, X_n)`$
      - when limit exists.
- e.g.)
  - Typewriter
    - Consider a typewriter that has $`m`$ equally likely output letters.
    - Then the typewriter can produce $`m^n`$ sequences of length $`n`$.
      - All of which are equally likely.
    - Hence, $`H(X_1, X_2, \cdots, X_n) = \log{m^n}`$
    - Therefore, the **entropy rate** is $`H(\mathcal{X}) = \log{m}`$ bits per symbol.
  - I.I.D.
    - Suppose $`X_1, X_2, \cdots \stackrel{i.i.d.}{\sim} p(x)`$.
    - Then, $`\displaystyle H(\mathcal{X}) = \lim_{n\rightarrow\infty}\frac{H(X_1, X_2, \cdots, X_n)}{n} = \lim_{n\rightarrow\infty}\frac{nH(X_1)}{n} = H(X_1)`$
  - Independent but Not Identically Distributed
    - $`\displaystyle H(X_1, X_2, \cdots, X_n) = \sum_{i=1}^n H(X_i)`$
      - cf.) Non-existing-limit case
        - A random binary sequence where
          - $`p_i = P(X_i=1) = \begin{cases}
            0.5 & \textrm{if } 2k \lt \log\log{i} \le 2k+1 \\
            0 & \textrm{if } 2k+1 \lt \log\log{i} \le 2k+2 \\
          \end{cases}`$
            - for $`k=0,1,2,\cdots`$
        - In this case, the average of $`H(X_i)`$ oscillates between 0 and 1.
        - Thus, $`H(\mathcal{X})`$ is not defined for this process.

<br>

### Concept) Conditional Entropy
- Def.)
  - $`\displaystyle H'(\mathcal{X}) = \lim_{n\rightarrow\infty} H(X_n|X_1, X_2,\cdots, X_{n-1})`$
    - when limit exists.

<br>

### Theorem 4.2.1) 
For a [stationary](../01/note.md#concept-stationary) stochastic process, [$`H(\mathcal{X})`$](#concept-entropy-rate-per-symbol) and [$`H'(\mathcal{X})`$](#concept-entropy-rate-per-symbol)









<br>

* [Back to Elements of Information Theory](../../main.md)