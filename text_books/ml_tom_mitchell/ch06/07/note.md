* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 6.7 Bayes Optimal Classifier

#### Def.)
Let $H$ be a hypothesis space and $V$ the example set.   
Then the Bayes Optimal Classifier is the value $v_j \in V$, for which $P(v_j|D) = \sum_{h_i \in H} P(v_j|h_i)P(h_i|D)$ is maximum.
- i.e.)
  - $argmax_{v_j \in V} P(v_j|D) \equiv argmax_{v_j \in V} \sum_{h_i \in H} P(v_j|h_i)P(h_i|D)$

<br>

#### Example)
- Setting
  - A hypothesis space contains three hypotheses, $h_1$, $h_2$, and $h_3$.
    - i.e.) $H = \lbrace h_1, h_2, h_3 \rbrace$.
  - The posterior probabilities of the hypotheses are...
    - $P(h_1|D) = 0.4$
    - $P(h_2|D) = 0.3$
    - $P(h_3|D) = 0.3$
  - Then $h_{MAP} = h_1$.
- Problem)
  - Suppose a new instance $x$ is encountered, which is classified positive by $h_1$, but negative by $h_2$ and $h_3$.
    - i.e.)
      - $P(\oplus|h_1) = 1$, $P(\ominus|h_1) = 0$
      - $P(\oplus|h_2) = 0$, $P(\ominus|h_2) = 1$
      - $P(\oplus|h_3) = 0$, $P(\ominus|h_3) = 1$
- Solution) Bayes Optimal Classifier
  - Choose $v_j \in V$ that maximizes $P(v_j|D) = \sum_{h_i \in H} P(v_j|h_i)P(h_i|D)$.
  - Then,
    - $P(\oplus|D) = \sum_{i=1}^3 P(\oplus|h_i)P(h_i|D) = 0.4 \times 1 + 0.3 \times 0 + 0.3 \times 0 = 0.4$
    - $P(\ominus|D) = \sum_{i=1}^3 P(\ominus|h_i)P(h_i|D) = 0.4 \times 0 + 0.3 \times 1 + 0.3 \times 1 = 0.6$
  - Therefore, choose $ominus$.
    - i.e.) $argmax_{v_j \in V} P(v_j|D)=\ominus$

<br>

#### Props.)
- Bayes Optimal Classifier is the best **classification** method **on average**.
  - i.e.) No other classification method using the same hypothesis space and same prior knowledge can outperform this method on average.
  - why?) This method maximizes the probability that the new instance is classified correctly, given the available data, hypothesis space, and prior probabilities over the hypotheses.
    - Consider it as the weighted vote among all members of the version space, with each candidate hypothesis weighted by its posterior probability.
- The predictions it makes can correspond to a hypothesis not contained in $H$.
  - One way to view this situation is to think of the Bayes optimal classifier as effectively considering a hypothesis space $H'$ different from the space of hypotheses $H$ to which Bayes theorem is being applied. 
  - In particular, $H'$ effectively includes hypotheses that perform comparisons between linear combinations of predictions from multiple hypotheses in $H$. 

<br>

#### Limit)
- Bayes Optimal Classifier can be quite costly to apply.
  - why?)
    - It computes the posterior probability for every hypothesis in $H$.
      - $P(h|D), \forall h \in H$ 
    - Then, it combines the predictions of each hypothesis to classify each new instance.
      - $\sum_{h_i \in H} P(v|h_i)P(h_i|D), \forall v \in V$
  - Alternative Solution)
    - [Gibbs Algorithm](../08/note.md#68-gibbs-algorithm)










<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)