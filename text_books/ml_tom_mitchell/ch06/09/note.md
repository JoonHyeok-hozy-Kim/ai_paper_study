* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 6.9 Naive Bayes Classifier

### Concept) Naive Bayes Classifier
- Settings)
  - Assume that each instance $x$ is described by a conjunction of attribute values, $a_1, a_2, \cdots, a_n$.
  - Also, the target function $f(x)$ can take on any value from some finite set $V$.
  - The tuple of attribute values $\langle a_1, a_2, \cdots, a_n \rangle$ describes,
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
    - Count the frequencies of an attribute $a_i$ appeared in a training example $v_j$.
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

* [Back to Machine Learning Tom Mitchell Main](../../main.md)