* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 2.7 Inductive Bias
#### Some questions for the Candidate-Elimination algorithm
* Recall that the [Candidate-Elimination algorithm](../05/note.md#254-candidate-elimination-learning-algorithm) will converge toward the true target concept under the following two conditions.
  1. Training examples are accurate.
  2. **Its initial hypothesis space contains the target concept.**
* What if the target concept is **NOT contained** in the hypothesis space?
* Can we avoid this difficulty by using a hypothesis space that includes every possible hypothesis? 
* How does **the size of the hypothesis space** influence the ability of the algorithm to generalize to unobserved instances?
* How does **the size of the hypothesis space** influence the number of training examples that must be observed?

<br><br>

## 2.7.1 A Biased Hypothesis Space
#### Example)
* Consider the three training examples as follows.
  ![](images/001.png)
  - The most specific hypothesis "consistent with Ex 1 and Ex 2" and "representable in the give hypothesis space $H$" is $\langle ?, Warm, Normal, Strong, Cool, Change \rangle$.











<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)