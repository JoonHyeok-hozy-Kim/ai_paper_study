* [Back to Elements of Information Theory](../../main.md)

# 5.5 Kraft Inequality for Uniquely Decodable Codes

### Theorem 5.5.1) MacMillan
- Ideation)
  - The [previous bound](../04/note.md#theorem-541-bounds-on-the-optimal-code-length) is based on [Theorem 5.3.1](../03/note.md#theorem-531-lower-bound-for-the-expected-length-of-instantaneous-codeword) which assumes the codewords to be [instantaneous](../01/note.md#concept-prefix-code-instantaneous-code).
  - However, [instantaneous](../01/note.md#concept-prefix-code-instantaneous-code) is a strict assumption.
  - Instead, **unique decodability** is a larger concept that can be loosely applied more codewords.
- Theorem)
  - The codeword lengths of any **uniquely decodable** $`D`$-ary code must satisfy the [Kraft inequality](../02/note.md#theorem-521-kraft-inequality)
    - $`\sum D^{-l_i} \le 1`$
  - Conversely, given a set of codeword lengths that satisfy this [inequality](../02/note.md#theorem-521-kraft-inequality), it is possible to construct a **uniquely decodable** code with these codeword lengths.
- pf.)
  - Consider $`C^k`$, the $`k`$-th extension of the code.
    - i.e.) the code formed by the concatenation of $`k`$ repetitions of the given **uniquely decodable** code $`C`$
  - By the definition of **unique decodability**, the $`k`$th extension of the code is [nonsingular](../01/note.md#concept-non-singularity).
    - i.e.) It has a different string mapped to itself.
  - Since there are only $`D^n`$ different $`D`$-ary strings of length $`n`$, **unique decodability** implies that the number of code sequences of length $`n`$ in $`C^k`$ must be no greater than $`D^n`$.
  - Let $`l(x)`$ be the codeword lengths of the symbols $`x\in\mathcal{X}`$
  - Then














<br>

* [Back to Elements of Information Theory](../../main.md)