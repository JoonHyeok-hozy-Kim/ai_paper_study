* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 5.1 Motivation

#### Question) Why Evaluate the Performance of Learned Hypotheses
- To understand whether to use the hypothesis
- It is important to understand the likely errors inherent in estimating the accuracy of a learning method

<br>

#### Difficulty) Data is limited!
- Due to the limited data set available for learning, following two problems arise.
  1. Bias in the estimate
     - Desc.)
       - Fit with the training examples but show poor performance on the future examples.
       - This is especially likely when the learner considers a very rich hypothesis space, enabling it to overfit the training examples.
       - To prevent this, we test the hypothesis on some set of test **examples chosen independently** of the training examples and the hypothesis.
  2. Variance in the estimate
     - The measured accuracy can still vary from the true accuracy, depending on the makeup of the particular set of test examples.
     - The smaller the set of test examples, the greater the expected variance.












<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)