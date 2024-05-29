* [Back to Elements of Information Theory](../../main.md)

# 2.9 Sufficient Statistics

### Concept) Sufficient Statistics
- Def.)
  - Let
    - $`\{f_\theta(x)\}`$ : a family of probability mass (density) functions indexed by $`\theta`$.
    - $`X`$ : a sample from a distribution in $`\{f_\theta(x)\}`$
    - $`T(X)`$ : any statistic
  - $`T(X)`$ is said to be a **sufficient statistic** relative to the family $`\{f_\theta(x)\}`$
    - if $`\theta\rightarrow X\rightarrow T(X)`$
      - i.e.) $`X`$ is independent of $`\theta`$ given $`T(X)`$ for any distribution on $`\theta`$
- Meaning)
  - A statistic $`T(X)`$ is called sufficient for $`\theta`$ if it contains all the information in $`X`$ about $`\theta`$.
- Prop.)
  - By the [data-processing inequality](../08/note.md#concept-data-processing-inequality),
    - $`I(\theta; T(X)) \le I(\theta; X), \forall \theta`$
  - If $`I(\theta; T(X)) = I(\theta; X), \forall \theta`$, no information is lost.
- e.g.)
  - Bernoulli Distribution
    - Let
      - $`X_1, X_2, \cdots, X_n`$ : an iid sequence of coin tosses
        - where 
          - $`X_i \in \{0, 1\}`$
      - $`\theta`$ : an unknown parameter such that $`\theta = \textrm{Pr}(X_i=1)`$
      - $`\displaystyle T(X_1, X_2, \cdots, X_n) = \sum_{i=1}^n X_i`$
    - Then, we can show that given $`T`$, all sequences having the same number of $`1`$s are equally likely and independent of the parameter $`\theta`$.
      - i.e.)   
        $`\displaystyle\textrm{Pr}\left\{ (X_1, X_2, \cdots, X_n) = (x_1, x_2, \cdots, x_n) \middle| \sum_{i=1}^n X_i = k \right\} = \begin{cases}
            \frac{1}{_nC_k} & \textrm{if } \sum x_i = k \\
            0 & \textrm{otherwise}
        \end{cases}`$
  - Normal Distribution
  - Uniform distribution













<br>

* [Back to Elements of Information Theory](../../main.md)