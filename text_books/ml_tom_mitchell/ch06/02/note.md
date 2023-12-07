* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 6.2 Bayes Theorem

#### Concept) Bayes Theorem
- Why needed?)
  - In ML, we want to find the most probable hypothesis, given the data $D$.
  - Bayes theorem provides a way to calculate the probability of a hypothesis based on its prior probability, the probabilities of observing various data given the hypothesis, and the observed data itself.
- Def.)
  - Let
    - $P(h)$ : the **prior probability** of a hypothesis $h$
      - i.e.) the probability of $h$ before we have observed the training data
    - $P(D)$ : the prior probability that training data $D$ will be observed.
      - i.e.) the probability of $D$ given no knowledge about which hypothesis holds
    - $P(D|h)$ : the probability of observing data $D$ given some world in which hypothesis $h$ holds.
    - $P(h|D)$ : the **posterior probability** of $h$
      - i.e.) the probability that $h$ holds given the observed training data $D$.
      - It reflects the influence of the training data $D$.
        - cf.) $P(h)$ was independent of $D$.
  - Then
    - $P(h|D) = \frac{P(D|h)P(h)}{P(D)}$
- Props.)
  - $\Delta P(D|h) \gt 0 \Rightarrow \Delta P(h|D) \gt 0$
    - If the probability of $D$ given some world $h$ holds increases, $P(h|D)$ increases.
  - $\Delta P(h) \gt 0 \Rightarrow \Delta P(h|D) \gt 0$
    - If the probability of $h$ increases, $P(h|D)$ increases.
  - $\Delta P(D) \gt 0 \Rightarrow \Delta P(h|D) \lt 0$
    - If the probability of $D$ independent of $h$ increases, $P(h|D)$ decreases.

<br>

#### Concept) Maximum A Posteriori Hypothesis (MAP Hypothesis)
- Desc.)
  - Among various candidate hypotheses in the hypotheses space $H$,
  - Given the observed data $D$,
  - We want to find the most probable hypothesis $h \in H$.
    - i.e.) $`\begin{array}{lll} h_{MAP} & \equiv argmax_{h\in H} P(h|D) & \\ & \equiv argmax_{h\in H} \frac{P(D|h)P(h)}{P(D)} & \\ & \equiv argmax_{h\in H} P(D|h)P(h) & (\because P(D) \space is \space independent \space of \space h) \end{array}`$


<br>

#### Concept) Maximum Likelihood Hypothesis (ML Hypothesis)
- Desc.)
  - Assuming that $H$ is equally probable a priori
    - i.e.) $P(h_i) = P(h_j), \forall h_i, h_j \in H$
  - We may consider only the term $P(D|h)$ to find the most probable hypothesis.
  - $P(D|h)$ is called the **likelihood** of the data $D$ given $h$.
  - Any hypothesis that maximizes P(D|h) is called a **maximum likelihood hypothesis**.
    - i.e.) $h_{ML} \equiv argmax_{h \in H} P(D|h)$










<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)