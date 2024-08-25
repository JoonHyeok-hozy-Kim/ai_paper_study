* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 6.6 Minimum Description Length Principle

## Concept) Minimum Description Length (MDL) Principle
#### Motivation) Can we prevent overfitting using MDL?
  - Consider the problem of designing a code to transmit messages drawn at random, where the probability of encountering message $i$ is $p_i$.
    - Assigning shorter codes to the most probable message will be efficient.
    - According to Shannon and Weaver (1949), the optimal code assigns $-\log_2 p_i$ bits to encode message $i$.
      - Def.) Description Length of Message $i$ w.r.t. $C$.
        - Meaning)
          - the number of bits required to encode message i using code C
        - Notation)
          - $L_C(i)$
  - $h_{MAP}$ can be modified to a similar shape with $L_C(i)$.   
    $`\begin{array}{ll} h_{MAP} &= \displaystyle\arg\max_{h \in H} P(D|h)P(h) \\
    &= \displaystyle\arg\max_{h \in H} \log_2{P(D|h)}\log_2{P(h)} \\
    &= \displaystyle\arg\min_{h\in H} -\log_2{P(D|h)} -\log_2{P(h)} \end{array}`$
  - Can we apply MDL to choosing a hypothesis?

<br>

#### Def.) Minimum Description Length (MDL) Principle
$`h_{MAP} = \displaystyle\arg\max_{h \in H} L_{C_H}(h) + L_{C_{D|h}}(D|h)`$
- where $`C_H`$ and $`{C_{D|h}}`$ are the optimal encodings for $`H`$ and for $`D`$ given $`h`$, respectively.

- How?)
  - Recall that $h_{MAP} = \displaystyle\arg\min_{h\in H} -\log_2{P(D|h)} -\log_2{P(h)}$ 
    - $-\log_2{P(h)}$
      - the description length of $h$ under the optimal encoding for the hypothesis space $H$. 
        - i.e.) the size of the description of hypothesis $h$ using this optimal representation.
        - $L_{C_H}(h) = -\log_2{P(h)}$
          - where $C_H$ is the optimal code for hypothesis space $H$.
    - $-\log_2{P(D|h)}$
      - the description length of the training data $D$ given hypothesis $h$, under its optimal encoding.
        - $L_{C_{D|h}}(D|h) = -\log_2{P(D|h)}$
          - where ${C_{D|h}}$ is the optimal code for describing data $D$ assuming that both the sender and receiver know the hypothesis $h$.
  - Therefore, $h_{MAP} = \displaystyle\arg\max_{h \in H} L_{C_H}(h) + L_{C_{D|h}}(D|h)$
    - where $C_H$ and ${C_{D|h}}$ are the optimal encodings for $H$ and for $D$ given $h$, respectively. 

#### Props.)
- If we choose $C_1$ to be the optimal encoding of hypotheses $C_H$, and if we choose $C_2$ to be the optimal encoding $C_{D|h}$, then $h_{MDL} = h_{MAP}$.
- Intuitively, we can think of the MDL principle as recommending the **shortest** method for re-encoding the training data
  - where we count both the size of the hypothesis and any additional cost of encoding the data given this hypothesis.

<br>

#### e.g.) Decision Tree Learning
- What should we choose for $C_1$ and $C_2$?
  - $C_1$ : encoding of decision trees
    - e.g.) the number of nodes in the tree and with the number of edges
  - $C_2$
    - Suppose the sequence of instances $\langle x_1, \cdots, x_m \rangle$ is already known to both the transmitter and receiver.
      - Then, the transmitter need to send only the classification results, $\langle f(x_1), \cdots, f(x_m) \rangle$
    - Cases
      - If $h$ works perfect and classifies the input data 100% accurately, no data should be transmitted.
        - why?)
          - The receiver can use $C_1$ and calculate the result by him/herself.
      - If some examples are misclassified by $h$, then we need to send which one is misclassified.
        - Then the information will be consisted of...
          - At most $-\log_2 \frac{1}{m} = \log_2m$ bits
          - At most $-\log_2 \frac{1}{k} = \log_2k$ bits
            - where $k$ is the number of possible classifications.
- Interpretation)
  - The hypothesis $h_{MDL}$ under the encodings $C_1$ and $C_2$ is the one that minimizes the sum of these description lengths.
  - Thus the MDL principle provides a way of trading off hypothesis complexity for the number of errors committed by the hypothesis.
  - It might select a **shorter hypothesis** that makes a few errors over a longer hypothesis that perfectly classifies the training data.
  - It provides one method for **dealing with the issue of overfitting the data**.

#### Limit)
- We cannot get $P(h)$ and $P(D|h)$ in reality.
  - Recall that $h_{MDL} = h_{MAP}$ if... 
    - the size of hypothesis $h$ is $-\log{P(h)}$ 
    - a representation for exceptions is chosen so that the encoding length of $D$ given $h$ is equal to $-\log_2{P(D|h)}$.










<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)