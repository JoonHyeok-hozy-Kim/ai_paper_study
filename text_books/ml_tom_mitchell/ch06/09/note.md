* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 6.9 Naive Bayes Classifier

### Concept) Naive Bayes Classifier
- Settings)
  - Assume that each instance $x$ is described by a conjunction of attribute values, $`a_1, a_2, \cdots, a_n`$.
    - i.e.) $`a_1 \wedge a_2 \wedge \cdots \wedge a_n`$
  - Also, the target function $`f(x)`$ can take on any value from some finite set $`V`$.
  - The tuple of attribute values $`\langle a_1, a_2, \cdots, a_n \rangle`$ describes,
    - a set of training examples of the target function
    - a new instance that will be estimated.
- Idea)
  - Recall the Maximum A Posteriori Hypothesis (MAP).
    - $`\begin{array}{ll} v_{MAP} &=argmax_{v_j \in V} P(v_j|a_1, \cdots, a_n) \\&=argmax_{v_j \in V} \frac{P(a_1, \cdots, a_n|v_j)P(v_j)}{P(a_1, \cdots, a_n)} \\&=argmax_{v_j \in V} P(a_1, \cdots, a_n|v_j)P(v_j) \end{array}`$
  - But the problem is that we do not know $P(a_1, \cdots, a_n|v_j)$
  - What if we further assume that the attribute values are conditionally independent given the target value.
    - i.e.) $P(a_1, a_2, \cdots, a_n|v_j) = \prod_i P(a_i|v_j)$
- Derivation)
  - $`\begin{array}{ll} v_{NB} &=argmax_{v_j \in V} P(a_1, \cdots, a_n|v_j)P(v_j) \\&=argmax_{v_j \in V} P(v_j) \prod_i P(a_i|v_j) \end{array}`$
    - where $v_{NB}$ denotes the target value output by the naive Bayes classifier.
  - How to get $P(a_i|v_j), \forall i$
    - Count the frequencies of an attribute $a_i$ appeared in training examples with the target value $v_j$.
- Props.)
  - Whenever the naive Bayes assumption of **conditional independence** is satisfied, this naive Bayes classification $v_{NB}$ is identical to the MAP classification.
  - In naive Bayes learning method, there is no explicit search through the space of possible hypotheses.
    - $P(a_1, \cdots, a_n|v_j)$

<br><br>

## 6.9.1 An Illustrative Example
- Recall the problem we covered in [Decision Tree Learning](../../ch03/02/note.md#ex-play-tennis).
  - A set of 14 training examples as below.   
    ![](../../ch03/04/images/004.png)

#### Objective)
Predict the target value (yes or no) of the target concept $PlayTennis$ for the following new instance.
- $\langle Outlook=sunny, Temperature=cool, Humidity=high, Wind=strong \rangle$

<br>

#### Solution)
- The naive Bayesian Classifier, $v_{NB}$ goes...
  - $`\begin{array}{ll} v_{NB} &= argmax_{v_j \in \lbrace yes,no \rbrace} P(v_j) \prod_i P(a_i|v_j) \\&= argmax_{v_j \in \lbrace yes,no \rbrace} P(v_j) \left[ P(Outlook=sunny|v_j)\cdot P(Temperature=cool|v_j)\cdot  P(Humidity=high|v_j)\cdot  P(Wind=strong|v_j)\cdot\right] \end{array}`$
- Let's count the frequencies.
  - Case 1) $v_j = yes$
    - $P(PlayTennis=yes) = \frac{9}{14}$
    - $P(Outlook=sunny|PlayTennis=yes) = \frac{2}{9}$
    - $P(Temperature=cool|PlayTennis=yes) = \frac{3}{9}$
    - $P(Humidity=high|PlayTennis=yes) = \frac{3}{9}$
    - $P(Wind=strong|PlayTennis=yes) = \frac{3}{9}$
      - Thus, $P(yes) \prod_i P(a_i|yes) = \frac{9}{14} \times \frac{2}{9} \times \frac{3}{9}\times \frac{3}{9} \times \frac{3}{9} = 0.0053$
  - Case 2) $v_j = no$
    - $P(PlayTennis=no) = \frac{5}{14}$
    - $P(Outlook=sunny|PlayTennis=no) = \frac{3}{5}$
    - $P(Temperature=cool|PlayTennis=no) = \frac{1}{5}$
    - $P(Humidity=high|PlayTennis=no) = \frac{4}{5}$
    - $P(Wind=strong|PlayTennis=no) = \frac{3}{5}$
      - Thus, $P(no) \prod_i P(a_i|no) = \frac{5}{14} \times \frac{3}{5} \times \frac{1}{5}\times \frac{4}{5} \times \frac{3}{5} = 0.0206$
- Therefore, $v_{NB} = no$.
- Furthermore, the conditional probability that the target value is $no$, given the observed attribute values is $\frac{0.0206}{0.0206+0.0053} = 0.795$

<br>

### 6.9.1.1 Estimating Probabilities
- Motivation)
  - Recall we estimated $P(a_i|v_j)$.
  - Put 
    - $n$ : the total number of examples that satisfies $v_j$.
    - $n_c$ : the number of examples that satisfies $a_i$ and $v_j$.
      - e.g.) $P(Wind=strong|PlayTennis=no) = \frac{3}{5}$
        - Then, $n=5$ and $n_c=3$
  - What if $n_c$ is very small? Then $\frac{n_c}{n} \approx 0$.
    - Problems)
      - $\frac{n_c}{n}$ produces a biased underestimate of the probability.
      - When this probability estimate is zero, this probability term will dominate the Bayes classifier.
        - i.e.) $P(a_1, \cdots, a_n|v_j)P(v_j) = P(v_j) \prod_i P(a_i|v_j) = P(v_j) P(a_1|v_j) \cdots 0 \cdots P(a_n|v_j)=0$
- Solution)
  - $m$-estimate of probability : $\frac{n_c+mp}{n+m}$
    - where
      - $p$ : the prior estimate of the probability desired to be determined.
        - Typically assumes uniform priors.
          - i.e.) 
            - Suppose an attribute has $k$ possible values.
            - Then, set $p=\frac{1}{k}$.
      - $m$ : a constant called the equivalent sample size
        - It determines how heavily to weight $p$ relative to the observed data.


<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)