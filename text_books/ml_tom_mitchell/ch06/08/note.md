* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 6.8 Gibbs Algorithm

#### Algorithm)
Consider a classification problem. (Refer to the [Bayes optimal classifier](../07/note.md#67-bayes-optimal-classifier) problem.)   
1. Choose a hypothesis $h$ from $H$ at random, according to the posterior probability distribution over $H$. 
2. Use $h$ to predict the classification of the next instance $x$. 

<br>

#### Props)
- The Gibbs Algorithm draws hypothesis at random according to the current posterior probability distribution.
  - It can be shown that under certain conditions the expected misclassification error for the Gibbs algorithm is **at most twice** the expected error of the [Bayes optimal classifier](../07/note.md#67-bayes-optimal-classifier) (Haussler et al. 1994).
    - More precisely, the expected value is taken over target concepts drawn at random according to the prior probability distribution assumed by the learner.
    -  Under this condition, the expected value of the error of the Gibbs algorithm is **at worst twice** the expected value of the error of the Bayes optimal classifier
   - Implication)
     - If the learner assumes a **uniform** prior over $H$, and if target concepts are in fact drawn from such a distribution when presented to the learner, then classifying the next instance according to a hypothesis drawn at random from the current version space (according to a uniform distribution), will have expected error at most twice that of the Bayes optimal classifier.












<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)