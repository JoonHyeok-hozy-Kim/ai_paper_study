* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 12.2 Inductive-Analytical Approaches to Learning
### 12.2.1 The Learning Problem
- Given)
  - A set of training examples $D$, possibly containing errors
  - A domain theory $B$, possibly containing errors
  - A space of candidate hypothesis $H$
- Determine)
  - A hypothesis that best fits the training examples and domain theory
    - How to measure the fit?)
      1. Use the combined measure of the following two errors.
         - Errors)
           - $error_D(h)$ : the proportion of examples from $D$ that are misclassified by $h$.
           - $error_B(h)$ : the probability that $h$ will disagree with $B$ on the classification of a randomly drawn instance
         - Combination)
           - $`\displaystyle \argmin_{h\in H} k_D \; error_D(h) + k_B \; error_B(h)`$














<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)