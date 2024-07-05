* [Back to Elements of Information Theory](../../main.md)

# 5.5 Kraft Inequality for Uniquely Decodable Codes

### Theorem 5.5.1) McMillan Inequality
- Ideation)
  - The [previous bound](../04/note.md#theorem-541-bounds-on-the-optimal-code-length) is based on [Theorem 5.3.1](../03/note.md#theorem-531-lower-bound-for-the-expected-length-of-instantaneous-codeword) which assumes the codewords to be [instantaneous](../01/note.md#concept-prefix-code-instantaneous-code).
  - However, [instantaneous](../01/note.md#concept-prefix-code-instantaneous-code) is a strict assumption.
  - Instead, [unique decodability](../01/note.md#concept-unique-decodability) is a larger class that can be loosely applied more codewords.
  - Using this theorem, we can utilize a more generalized bound.
- Theorem)
  - The codeword lengths of any [uniquely decodable](../01/note.md#concept-unique-decodability) $`D`$-ary code must satisfy the [Kraft inequality](../02/note.md#theorem-521-kraft-inequality)
    - $`\sum D^{-l_i} \le 1`$
  - Conversely, given a set of codeword lengths that satisfy the [Kraft inequality](../02/note.md#theorem-521-kraft-inequality), it is possible to construct a [uniquely decodable](../01/note.md#concept-unique-decodability) code with these codeword lengths.
- pf.)
  - Let
    - $`C`$ : a [uniquely decodable](../01/note.md#concept-unique-decodability) code
    - $`C^k`$, the $`k`$-th [extension](../01/note.md#concept-extension-of-a-code) of the code.
      - i.e.) the code formed by the concatenation of $`k`$ repetitions of $`C`$
  - Consider the concept of the [unique decodability](../01/note.md#concept-unique-decodability).
    - By the definition of **unique decodability**, $`C^k`$ is [nonsingular](../01/note.md#concept-non-singularity).
      - i.e.) It has a distinct string mapped to $`C^k`$.
    - Since there are only $`D^n`$ different $`D`$-ary strings of length $`n`$, 
      - [unique decodability](../01/note.md#concept-unique-decodability) implies that the number of code sequences of length $`n`$ in $`C^k`$ must be no greater than $`D^n`$.
  - Let $`l(x)`$ be the **codeword lengths** of the symbols $`x\in\mathcal{X}`$
  - Then the length of the code sequence for $`C^k`$ is
    - $`\displaystyle l(x_1,x_2, \cdots, x_k) = \sum_{i=1}^k l(x_i)`$
  - Our target is to prove $`\displaystyle \sum_{x\in\mathcal{X}} D^{-l(x)} \le 1`$ for $`C^k`$.
    - Then   
      $`\begin{aligned}
        \left( \sum_{x\in\mathcal{X}}  D^{-l(x)} \right)^k 
        &= \sum_{x_1\in\mathcal{X}} \sum_{x_2\in\mathcal{X}} \cdots \sum_{x_k\in\mathcal{X}} D^{-l(x_1)} D^{-l(x_2)} \cdots D^{-l(x_k)} \\
        &= \sum_{x_1, x_2, \cdots, x_k\in\mathcal{X}^k} D^{-l(x_1)} D^{-l(x_2)} \cdots D^{-l(x_k)} \\
        &= \sum_{x^k\in\mathcal{X}^k} D^{\sum_{i=1}^k l(x_i)} = \sum_{x^k\in\mathcal{X}^k} D^{-l(x^k)} & \because -\sum_{i=1}^k l(x_i) = l(x_1, x_2, \cdots, x_k) \\
      \end{aligned}`$
  - Consider that   
    $`\begin{aligned}
      \sum_{x^k\in\mathcal{X}^k} D^{-l(x^k)} = \sum_{m=1}^{k l_{\max}} a(m) D^{-m}
    \end{aligned}`$
    - where
      - $`l_{\max}`$ : the maximum codeword length
      - $`a(m)`$ : the number of source sequences $`x^k`$ mapping into codewords of length $`m`$
        - Since the code is [uniquely decodable](../01/note.md#concept-unique-decodability), 
          - there is at most one sequence mapping into each code $`m`$-sequence.
          - there are at most $`D^m`$ code $`m`$-sequences.
        - Thus, $`a(m) \le D^m`$
  - Hence,   
    $`\begin{aligned}
      &\displaystyle \left( \sum_{x\in\mathcal{X}}  D^{-l(x)} \right)^k = \sum_{m=1}^{k l_{\max}} a(m) D^{-m} \le \sum_{m=1}^{k l_{\max}} D^m D^{-m} = k l_{\max} \\
      \Rightarrow & \; \sum_j D^{-l_j} \le (k l_{\max})^{1/k}
    \end{aligned}`$
  - Then,   
    $`\displaystyle k\rightarrow\infty \Rightarrow (k l_{\max})^{1/k}\rightarrow 1 \Rightarrow \sum_j D^{-l_j} \le 1`$

<br><br>

### Corollary 5.5.1) 
- Theorem)
  - A [uniquely decodable](../01/note.md#concept-unique-decodability) code for an infinite source alphabet $`\mathcal{X}`$ also satisfies the [Kraft inequality](../02/note.md#theorem-521-kraft-inequality).
- pf.)
  - Consider that any subset of a **uniquely decodable** code is also **uniquely decodable**.
  - Thus, by the [MacMillan Theorem](#theorem-551-macmillan), any finite subset of the infinite set of codewords satisfies the Kraft inequality.
  - Hence, $`\displaystyle \sum_{i=1}^\infty D^{-l_i} = \lim_{N\rightarrow\infty} \sum_{i=1}^N D^{-l_i} \le 1`$
  - Given a set of word lengths $`l_1, l_2, \cdots`$ that satisfy the Kraft inequality,
    - by the [Theorem 5.3.1](../03/note.md#theorem-531-lower-bound-for-the-expected-length-of-instantaneous-codeword) and the [Theorem 5.4.1](../04/note.md#theorem-541-bounds-on-the-optimal-code-length),
    - we can construct an [instantaneous](../01/note.md#concept-prefix-code-instantaneous-code) code.
  - Since [instantaneous](../01/note.md#concept-prefix-code-instantaneous-code) codes are [uniquely decodable](../01/note.md#concept-unique-decodability), we have constructed a uniquely decodable code with an infinite number of codewords. 
  - Therefore, the [MacMillan Theorem](#theorem-551-macmillan) also applies to infinite alphabets.
- Interpretation)
  - The [bounds derived on the optimal codeword length](../03/note.md#theorem-531-lower-bound-for-the-expected-length-of-instantaneous-codeword) holds even when we expand the class of allowed codes to the class of all [uniquely decodable](../01/note.md#concept-unique-decodability) codes.


<br>

* [Back to Elements of Information Theory](../../main.md)