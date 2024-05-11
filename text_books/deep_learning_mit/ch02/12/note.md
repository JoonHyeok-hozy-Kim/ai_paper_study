* [Back to Deep Learning MIT](../../main.md)

# 2.12 Example: Principal Components Analysis

### E.g.) Deriving Principal Components Analysis (PCA) 
- Objective)
  - Derive Principal Components Analysis (PCA) using only knowledge of basic linear algebra.
  - Apply lossy compression.
    - i.e.) Store the points in a way that requires less memory but may lose some precision.
- Settings)
  - $`\lbrace x^{(1)}, \cdots, x^{(m)} \rbrace \in \mathbb{R}^n`$ : a collection of $`m`$ points in $`\mathbb{R}^n`$
  - $`c^{(i)} \in \mathbb{R}^l`$ : the code vector corresponding with $`x^{(i)} \in \mathbb{R}^l`$
    - where
      - $`l \lt n`$ : $`c^{(i)}`$ becomes the lower-dimensional version of $`x^{(i)}`$.
- Goal)
  - Find the encoding / decoding function such that
    - $`f(x) = c`$ : the encoding function
    - $`g(f(x)) \approx x`$ : the decoding function
      - Then 
        - $`g(c) = Dc`$
          - where $`D \in \mathbb{R}^{n\times l}`$
      - i.e.) We want to find $`D`$!
- Assumption)
  - Minimizing the distance between $`x`$ and $`g(c)`$.
    - Put $`\displaystyle c^\ast = {\arg\min}_c {}`$
  - There can be many $`D`$ that may sat














<br>

* [Back to Deep Learning MIT](../../main.md)