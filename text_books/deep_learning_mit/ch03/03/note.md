* [Back to Deep Learning MIT](../../main.md)

# 3.3 Probability Distributions

### Def.) Probability Distribution
- A description of how likely a random variable or set of random variables is to take on each of its possible states.

<br>

## 3.3.1 Discrete Variables and Probability Mass Functions
### Concept) Probabilities Mass Function (PMF)
- Desc.)
  - A way of describing a [probability distribution](#def-probability-distribution) over **discrete** variables.
  - We must infer which probability mass function to use  based on the identity of the random variable, rather than the name of the function.
    - i.e.) Usually, $`P(\mathbf{x}) \ne P(y)`$ 
- Notation)
  - $`P`$ : a probability mass function (PMF)
    - $`\mathbf{x}\sim P(\mathbf{x})`$ : the random variable $`\mathbf{x}`$ has the probability distribution of $`P`$
    - $`P(x)`$ : the probability that $`\mathbf{x} = x`$
- Props.)
  - The domain of $`P`$ must be the set of all possible states of $`\mathbf{x}`$.
  - $`\forall x \in \mathbf{x}, \; 0 \le P(x) \le 1`$
  - $`\displaystyle \sum_{x\in \mathbf{x}} P(x) = 1`$
    - i.e.) Normalization

<br>

### Concept) Joint Probability Distribution
- Def.)
  - A probability distribution function that acts on many variables at the same time
- Notation)
  - $`P(\mathbf{x}=x, \mathbf{y}=y)`$ the probability that $`\mathbf{x} = x, \mathbf{y}=y`$

<br><br>

### Concept) Uniform Distribution
- Def.)
  - A single discrete random variable $`\mathbf{x}`$ with $`k`$ different states.
- Notation)
  - $`\displaystyle P(\mathbf{x} = x_i) = \frac{1}{k}, \; \forall i`$
  - $`u(x;a,b)`$ : $`x`$ parameterized by $`a,b`$
  - $`\mathbf{x} \sim U(a,b)`$
- Prop.)
  - $`\displaystyle \sum_i P(\mathbf{x} = x_i) = \sum_i \frac{1}{k} = \frac{k}{k} = 1`$

<br><br>

## 3.3.2 Continuous Variables and Probability Density Functions
### Concept) Probability Density Function (PDF)
- Def.)
  - A way of describing a [probability distribution](#def-probability-distribution) over **continuous** variables.
- Notation)
  - $`p`$ : a probability density function (PDF)
- Prop.)
  - The domain of $`p`$ must be the set of all possible states of $`\mathbf{x}`$.
  - $`\forall x \in \mathbf{x}, \; p(x) \ge 0`$
    - cf.) $`p(x) \le 1`$ is not required!
  - $`\displaystyle \int p(x) dx = 1`$





<br>

* [Back to Deep Learning MIT](../../main.md)