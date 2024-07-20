* [Back to Elements of Information Theory](../../main.md)

# 5.10 Competitive Optimality of the Shannon Code
- Desc.)
  - We want to compare the performance of each coding techniques.
  - We have shown that [Huffman coding is optimal](../08/note.md#58-optimality-of-huffman-codes).
    - However, it does not mean that Huffman code is always the best.
      - Why?) There are codes that assign short codewords to infrequent source symbols.
  - Still, we want to figure out the comparative optimality of each code.
    - How?)
      - Compare each code with length.
      - Shorter code is more efficient than the longer one.
  - Nevertheless, dealing with Huffman code **lengths** is difficult.
    - Why?)
      - There is no explicit expression for the codeword lengths.
  - Instead, we consider the [Shannon code](../07/note.md#prop4-shannon-code) with the codeword lengths $`l(x) = \left\lceil \log\frac{1}{p(x)} \right\rceil`$.
  - By [Theorem 5.10.1](#theorem-5101), [Theorem 5.10.2](#theorem-5102), and [its Corollary](#corollary-5102) we can conclude that Shannon coding is optimal under variety of criteria.
    - i.e.) [Shannon coding](../07/note.md#prop4-shannon-code) is robust w.r.t. the payoff function.

<br><br>

### Theorem 5.10.1)
- Theorem)
  - Let
    - $`l(x)`$ : the codeword lengths associated with the [Shannon code](../07/note.md#prop4-shannon-code)
    - $`l'(x)`$ : the codeword lengths associated with any other uniquely decodable code
  - Then
    - $`\displaystyle \textrm{Pr}(l(X) \ge l'(X) + c) \le \frac{1}{2^{c-1}}`$
      - e.g.)
        - The probability that $`l'(X)`$ is 5 or more bits shorter than $`l(X)`$ is less than $`\frac{1}{16}`$
- pf.)   
  $`\begin{aligned}
    \textrm{Pr}(l(X) \ge l'(X) + c) 
    &= \textrm{Pr} \left( \left\lceil \log\frac{1}{p(X)} \right\rceil \ge l'(X) + c \right) \\
    &\le \textrm{Pr} \left( \log\frac{1}{p(X)} \ge l'(X) + c - 1 \right) \\
    &= \textrm{Pr} \left( p(X) \le 2^{-l'(X) - c + 1} \right) \\
    &= \sum_{x: \; p(x) \le 2^{-l'(x) - c + 1}} p(x) \\
    &\le \sum_{x: \; p(x) \le 2^{-l'(x) - c + 1}} 2^{-l'(x) - c + 1} & \because \textrm{We only consider } x \textrm{ s.t. } p(x) \le 2^{-l'(x) - c + 1}. \\
    &\le \sum_x 2^{-l'(x) - c + 1} & \because 2^{-l'(x) - c + 1} \ge 0, \; \forall x \\
    &= \sum_x \left(2^{-l'(x)} 2^{-(c-1)}\right) = 2^{-(c-1)} \left( \sum_x 2^{-l'(x)} \right) \\
    &\le 2^{-(c-1)} & \because \sum 2^{-l'(x)} \le 1 \textrm{ by Kraft Inequality}
  \end{aligned}`$



<br><br>

### Theorem 5.10.2)




<br><br>

### Corollary 5.10.2)




<br><br>










<br>

* [Back to Elements of Information Theory](../../main.md)