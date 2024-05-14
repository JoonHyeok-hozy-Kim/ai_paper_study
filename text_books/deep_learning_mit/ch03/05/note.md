* [Back to Deep Learning MIT](../../main.md)

#  3.5 Conditional Probability

### Concept) Conditional Probability
- Def.)
  - the probability of some event, given that some other event has happened
  - $`\displaystyle P(\mathbf{y} = y | \mathbf{x} = x) = \frac{P(\mathbf{y} = y, \mathbf{x} = x)}{P(\mathbf{x} = x)}`$
    - where $`{P(\mathbf{x} = x)} \gt 0`$
      - i.e.) We cannot compute the conditional probability conditioned on an event that never happens.

<br>

### Concept) The Chain Rule of Conditional Probabilities
- Def.)
  - Any [joint probability distribution](../03/note.md#concept-joint-probability-distribution) over many random variables may be decomposed into [conditional distributions](#concept-conditional-probability) over only **one** variable.
    - i.e.)
      - Let
        - $`\mathbf{x^{(1)}}, \mathbf{x^{(2)}}, \cdots, \mathbf{x^{(n)}}`$ : random variables.
      - Then
        - $`\displaystyle P\left(\mathbf{x^{(1)}}, \mathbf{x^{(2)}}, \cdots, \mathbf{x^{(n)}}\right) = P\left(\mathbf{x^{(1)}}\right) \cdot \prod_{i=2}^n P\left(\mathbf{x^{(i)}} | \mathbf{x^{(1)}}, \cdots, \mathbf{x^{(i-1)}}\right)`$
    - e.g.)   
      $`\begin{aligned}
        P(a,b,c) & = P(a|b,c) \cdot P(b,c) \\
        & = P(a|b,c) \cdot \left( P(b|c) P(c) \right)
      \end{aligned}`$


<br>

* [Back to Deep Learning MIT](../../main.md)