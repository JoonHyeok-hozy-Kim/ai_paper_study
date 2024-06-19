* [Back to Elements of Information Theory](../../main.md)

# 4.4 Second Law of Thermodynamics

#### Concept) Entropy in Thermodynamics
- Def.)
  - The log of the number of microstates in the system
- Prop.)
  - Corresponds to the [entropy in Information Theory](../../ch02/01/note.md#concept-entropy) if all the states are equally likely.


<br>


## Concept) Second Law of Thermodynamics
- Statement)
  - The [entropy](#concept-entropy-in-thermodynamics) of an **isolated system** is non-decreasing.

<br>

## Analysis) Can entropy decrease?
- Assumption)
  - The [isolated system](#concept-second-law-of-thermodynamics) is modeled as a [Markov chain](../../ch04/01/note.md#concept-markov-chain-markov-process) with transitions obeying the physical laws governing the system.
    - Implicitness in this assumption)
      - What is the overall state of the system?
      - Do we know what the present state is?
      - Is the future of the system independent of the past?

### Case 1) Decreasing Relative Entropy
- Settings)
  - $`\mu_n, \mu_n'`$ : probability distributions on the state space of a Markov chain at time $`n`$
  - $`p, q`$ : the joint mass functions of $`\mu_n, \mu_n'`$ respectively
  - $`r(\cdot|\cdot)`$ : the probability transition function for the Markov chain
- Decrease)
  - [Relative entropy](../../ch02/03/note.md#concept-relative-entropy-kullbackleibler-distance) $`D(\mu_n||\mu_n')`$ **decreases** with $`n`$.
- pf.)
  - Consider that $`\begin{cases} p(x_n, x_{n+1}) = p(x_n)r(x_{n+1}|x_n) \\ q(x_n, x_{n+1}) = q(x_n)r(x_{n+1}|x_n) \\ \end{cases}`$.
  - By the [chain rule for relative entropy](../../ch02/05/note.md#theorem-253-chain-rule-for-relative-entropy)   
    $`\begin{aligned}
        D(p(x_n, x_{n+1}) || q(x_n, x_{n+1})) & = D(p(x_n) || q(x_n)) + D(p(x_{n+1}|x_n) || q(x_{n+1}|x_n)) & \cdots (A) \\
        &= D(p(x_{n+1}) || q(x_{n+1})) + D(p(x_n|x_{n+1}) || q(x_n|x_{n+1})) & \cdots (B) \\
    \end{aligned}`$
  - Recall that in the [Markov process](../../ch04/01/note.md#concept-markov-chain-markov-process), each random variable depends only on the one preceding it and is conditionally independent of all the other preceding random variables.
  - Since $`p,q`$ are derived from the Markov chain,
    - $`p(x_{n+1}|x_n) = q(x_{n+1}|x_n) = r(x_{n+1}|x_n)`$.
      - Thus, $`D(p(x_{n+1}|x_n) || q(x_{n+1}|x_n)) = 0. \; \cdots (A_1)`$
  - By [Thm.2.6.3](../../ch02/06/note.md#theorem-263-information-inequality), $`D(p(x_n|x_{n+1}) || q(x_n|x_{n+1})) \ge 0 \; \cdots (B_1)`$.
  - Thus,    
    $`\begin{aligned}
        D(p(x_n|x_{n+1}) || q(x_n|x_{n+1})) &= D(p(x_n) || q(x_n)) + D(p(x_{n+1}|x_n) || q(x_{n+1}|x_n)) - D(p(x_{n+1}) || q(x_{n+1})) \\
        &= D(p(x_n) || q(x_n)) - D(p(x_{n+1}) || q(x_{n+1})) & \because (A_1) \\
        &\ge 0 & \because (B_1) \\
    \end{aligned}`$   
  - Hence,   
    $`\begin{aligned}
        D(p(x_n) || q(x_n)) \ge D(p(x_{n+1}) || q(x_{n+1})) \stackrel{\textrm{by def.}}{\Leftrightarrow} D(\mu_n||\mu_n') \ge D(\mu_{n+1}||\mu_{n+1}')
    \end{aligned}`$
    - i.e.) The distance between the probability mass functions is **decreasing with time** $`n`$ for any Markov chain.
- e.g.)
  - The tax system for the redistribution of wealth in Canada and in England.
    - Let $`\mu_n, \mu_n'`$ represent the wealth among people in the two countries.
    - As the time goes, the relative entropy distance between the two distributions decreases with time.
    - The wealth distributions in Canada and England become more similar.

<br>

### Case 2) Decreasing Relative Entropy with Stationary Distribution
- Settings)
  - $`\mu_n`$ : a probability distribution on the state space of a Markov chain at time $`n`$ 
  - $`\mu`$ : a stationary distribution.
- Decrease)
  - [Relative entropy](../../ch02/03/note.md#concept-relative-entropy-kullbackleibler-distance) $`D(\mu_n||\mu)`$ between $`\mu_n`$ and $`\mu`$ **decreases** with $`n`$.
- pf.)
  - In [Case 1](#case-1-decreasing-relative-entropy), $`\mu_n'`$ was any distribution on the states at time n.
  - Now, put $`\mu = \mu_n', \forall n`$.
  - Then, by [Case 2](#case-1-decreasing-relative-entropy), $`D(\mu_n||\mu) \ge D(\mu_{n+1}||\mu)`$.
    - i.e.) Any state distribution gets closer and **closer to each stationary distribution** as time passes.
- Prop.)
  - The sequence $`D(\mu_n||\mu)`$ is monotonically non-increasing non-negative sequence.
    - Thus, it has limit.
      - This limit is zero if the stationary distribution is unique.


<br>

### Case 3) Increasing Entropy for Uniformly Distributed Stationary Distribution
- Increase)
  - Entropy **increases** if the stationary distribution is uniform.
- pf.)
  - Suppose the stationary distribution is the uniform distribution.
  - Then the relative entropy goes    
    $`\begin{aligned}
      D(\mu_n||\mu) &= \log|\mathcal{X}| - H(\mu_n) \\
      &= \log|\mathcal{X}| - H(X_n) \\
    \end{aligned}`$
  - Thus, the monotonic decrease in relative entropy implies a monotonic increase in entropy.


#### Concept) Doubly Stochastic
- Def.)
  - A [probability transition matrix](../../ch04/01/note.md#concept-probability-transition-matrix) $`[P_{ij}]`$ is called doubly stochastic if $`\sum_i P_{ij} = 1 \textrm{ and } \sum_j P_{ij} = 1`$
- Prop.)
  - The uniform distribution is a stationary distribution of $`P`$ iff. the probability transition matrix is **doubly stochastic**.

<br>

### Case 4) Increasing Conditional Entropy for Stationary Markov Process
- Increase)
  - [Conditional entropy](../../ch02/02/note.md#concept-conditional-entropy) $`H(X_n|X_1)`$ **increases** with $`n`$ for a [stationary](../01/note.md#concept-stationary) Markov process.
- pf 1.)   
  $`\begin{aligned}
    H(X_n|X_1) &\ge H(X_n|X_1, X_2) & \because \textrm{Conditioning reduces entropy.} \\
    &= H(X_n|X_2) & \because Markov Process \\
    &= H(X_{n-1}|X_1) & \because Stationarity \\
  \end{aligned}`$
- pf 2.)   
  - Considering the $`X_1\rightarrow X_{n-1} \rightarrow X_n`$ Markov process, the mutual information goes
    - $`I(X_1; X_{n-1}) \ge I(X_1; X_n)`$
  - By [Theorem 2.4.1](../../ch02/04/note.md#theorem-241), the above can be rewritten as
    - $`H(X_{n-1}) - H(X_{n-1}|X_1) \ge H(X_n) - H(X_n|X_1)`$.
  - By stationarity, $`H(X_{n-1}) = H(X_n)`$.
  - Thus, $`H(X_{n-1}|X_1) \le H(X_n|X_1)`$.

<br>

### Case 5) Shuffling Increases Entropy
- Increase)
  - Shuffles **increase** entropy.


<br>

* [Back to Elements of Information Theory](../../main.md)