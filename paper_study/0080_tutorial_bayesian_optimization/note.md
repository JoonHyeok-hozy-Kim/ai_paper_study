* [Back to Main](../../README.md)
---

# A Tutorial on Bayesian Optimization
### Peter I. Frazier
* [Read Paper](../paper_pdfs/240827%20A%20Tutorial%20on%20Bayesian%20Optimization.pdf)

---

## 1. Introduction
### Concept) Bayesian Optimization (BayesOpt)
- Def.)
  - A class of machine-learning-based optimization methods focused on solving the problem
    - $`\displaystyle\max_{x\in A} f(x)`$
      - where the feasible set and objective function typically have the following properties:
        - The input $`x\in \mathbb{R}^d`$
          - $`d`$ is not too large
          - Typically, $`d\le 20`$ in most successful applications of BayesOpt.
        - The feasible set $`A`$ is a simple set, in which it is easy to assess membership.
          - Typically $`A`$ is a hyper-rectangle $`\{x\in\mathbb{R}^d : a_i \le x_i \le b_i\}`$ or the $`d\textrm{-dimensional simplex } \{x\in\mathbb{R}^d : \sum_i x_i = 1\}`$
        - The objective function $`f`$ is continuous.
          - This will typically be required to model $`f`$ using Gaussian process regression.
        - $`f`$ is “expensive to evaluate”
          - i.e.) Each evaluation takes a substantial amount of time or monetary/opportunity cost
        - $`f`$ is a “black box.”
          - i.e.) $`f`$ lacks known special structure like concavity or linearity that would make it easy to optimize using techniques that leverage such structure to improve efficiency.



---
* [Back to Main](../../README.md)