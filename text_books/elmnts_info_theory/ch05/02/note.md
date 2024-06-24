* [Back to Elements of Information Theory](../../main.md)

# 5.2 Kraft Inequality

### Theorem 5.2.1) Kraft Inequality
- Theorem)
  - For any [instantaneous code (prefix code)](../01/note.md#concept-prefix-code-instantaneous-code) over an alphabet of size $`D`$, the codeword lengths $`l_1, l_2, \cdots, l_m`$ must satisfy the inequality
    - $`\displaystyle \sum_i D^{-l_i} \le 1`$

<img src="images/001.png" width="300px">

- pf)
  - Consider a $`D`$-ary tree in which each node has $`D`$ children.
  - Let 
    - branches : represent the symbols of the codeword.
    - leaves : represent each codeword.
  - Then the path from the root traces out the symbols of the codeword.
  - And the no codeword is an ancestor of any other codeword on the tree.
    - Hence, each codeword eliminates its descendants as possible codewords.
  - Put $`l_{\max}`$ : the length of the longest codeword of the set of codewords.
  - Then, a codeword at level $`l_i`$ has $`D^{l_{\max} - l_i}`$ descendants at level $`l_{\max}`$.
    - Why?)   
      $`\begin{aligned}
        D   \textrm{ descendants} &\textrm{ at level } l_{i+1} \\
        D^2 \textrm{ descendants} &\textrm{ at level } l_{i+2} \\
        D^3 \textrm{ descendants} &\textrm{ at level } l_{i+3} \\
        &\vdots \\
        D^{l_{\max} - i} \textrm{ descendants} &\textrm{ at level } l_{\max} \\
      \end{aligned}`$
  - Also, these descendant sets must be **disjoint**.
    - e.g.) In the above image, the set of $`0`$'s descendants and that of $`10`$ are disjoint.
  - Hence, summing over all the codewords,
    - $`\displaystyle \sum_i D^{l_{\max} - l_i} \le D^{l_{\max}}`$
      - Why?)
        - $`\sum_i D^{l_{\max} - l_i}`$ is equal to the number of all nodes in this tree.
        - Since it is $`D`$-ary tree, the number of all nodes is $`\displaystyle\sum_{k=1}^{l_{\max}} D^{k-1} = \frac{D^{l_{\max}}-1}{D-1} \lt D^{l_{\max}}`$
        - $`\therefore \displaystyle \sum_i D^{l_{\max} - l_i} = \sum_{k=1}^{l_{\max}} D^{k-1}\le D^{l_{\max}}`$








<br>

* [Back to Elements of Information Theory](../../main.md)