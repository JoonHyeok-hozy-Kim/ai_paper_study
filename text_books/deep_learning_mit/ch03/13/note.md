* [Back to Deep Learning MIT](../../main.md)

# 3.13 Information Theory

### Concept) Information Theory
- Desc.)
  - Information theory is a branch of applied mathematics that revolves around **quantifying how much information is present in a signal**.
  - In the context of machine learning, we can also **apply information theory to continuous variables** where some of these message length interpretations do not apply.
- Intuitions)
  - Quantifying Information
    - **Likely events** should have **low information** content
      - In the extreme case, events that are guaranteed to happen should have no information content whatsoever.
    - **Less likely events** should have **higher information content**.
    - Independent events should have additive information. For example, finding out that a tossed coin has come up as heads twice should convey twice as much information as finding out that a tossed coin has come up as heads once.

<br>

### Concept) Self-Information
- Def.)
  - The **self-information** of an event that $`\mathbf{x} = x`$ can be defined as
    - $`I(x) = -\log P(x)`$
      - Here, the log is the with base $`e`$.
      - Thus, $`I(x)`$ is written in units **nats**, instead of **bits**.
- Prop.)
  - Appropriate for discrete cases.
    - In case of continuous cases, use [entropy](#concept-shannon-entropy) instead.

### Concept) Shannon Entropy
- Why needed?)
  - To quantify the amount of uncertainty in an entire probability distribution
- Def.)
  - For $`\mathbf{x} \sim P`$ : a random variable with distribution $`P`$
    - $`H(\mathbf{x}) = \mathbb{E}_{\mathbf{x}\sim P} \left[ I(x) \right] = -\mathbb{E}_{\mathbf{x}\sim P}\left[ \log P(x) \right]`$
      - or simply $`H(P)`$
  - When $`\mathbf{x}`$ is continuous, the Shannon entropy is known as the **differential entropy**.
- Meaning)
  - The Shannon entropy of a distribution is the expected amount of information in an event drawn from that distribution.
  - It gives a lower bound on the number of bits needed on average to encode symbols drawn from a distribution $`P`$.
- Prop.)
  - Distributions that are nearly deterministic have low entropy.


<br>

### Concept) Kullback-Leiber (KL) Divergence
- Def.)
  - For separate probability distributions $`P(\mathbf{x})`$ and $`Q(\mathbf{x})`$ over the same random variable $`\mathbf{x}`$
    - $`\displaystyle D_{KL}(P||Q) = \mathbb{E}_{\mathbf{x}\sim P} \left[\log\frac{P(x)}{Q(x)}\right] = \mathbb{E}_{\mathbf{x}\sim P} \left[ \log{P(x)} - \log{Q(x)} \right]`$
- Meaning)
  - The measurement of difference between distributions.
  - In the discrete variable case,
    - $`D_{KL}(P||Q)`$ denotes the extra amount of information needed to send a message containing symbols drawn from probability distribution $`P`$, when use a code that was designed to minimize the length of messages drawn from probability distribution $`Q`$.
- Props.)
  - Non-negative
  - $`D_{KL}(P||Q) = 0`$
    - If $`\mathbf{x}`$ is discrete
      - $`P`$ and $`Q`$ are the same distribution 
    - If $`\mathbf{x}`$ is continuous
      - $`P`$ and $`Q`$ are equal [almost everywhere](../12/note.md#concept-almost-everywhere).
  - Not symmetric.
    - i.e.) $`D_{KL}(P||Q) \ne D_{KL}(Q||P)`$
    - Thus, Kullback-Leiber Divergence cannot be the distance formally.
      - But used as one on practice.

<br>

### Concept) Cross Entropy
- Def.)
  - $`H(P,Q) = H(P) + D_{KL}(P||Q) = -\mathbb{E}_{\mathbf{x}\sim P} \left[ \log{Q(x)} \right]`$

### Convention)
- $`\displaystyle 0\log0 \approx \lim_{x\rightarrow 0} x\log x = 0.`$



<br>

* [Back to Deep Learning MIT](../../main.md)