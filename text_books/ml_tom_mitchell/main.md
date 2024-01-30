[Back to AI Main](../../README.md)

<br>

# Machine Learing
### Tom M. Mitchell

<br>

## 1. Introduction
|No.|Chapter|Keywords|
|:-:|:------|:-------|
|1.1|[Well-Posed Learning Problems](./ch01/01/note.md)|Learning|
|1.2|[Designing a Learning System](./ch01/02/note.md)|Experience, Target Function, Nonoperational Definition, Operational Description, Representation of a Target Function, Training Example, Estimation, Least Mean Square(LMS), Performance System, The Critic, The Generalizer, The Experiment Generator|

<br>

## 2. Concept Learning and The General-To-Specific Ordering
|No.|Chapter|Keywords|
|:-:|:------|:-------|
|2.2|[A Concept Learning Task](./ch02/02/note.md)|Concept Learning, Positive Example, Negative Example, Hypothesis, Inductive Learning Hypothesis|
|2.3|[Concept Learning as Search](./ch02/03/note.md)|Hypothesis Space, (Syntactically/Semantically) Distinct Hypotheses, General-To-Specific Ordering ($\geq_g$)|
|2.4|[Find-S: Finding a Maximally Specific Hypothesis](./ch02/04/note.md)|Find-S Algorithm|
|2.5|[Version Spaces and the Candidate-Elimination Algorithm](./ch02/05/note.md)|Consistency, Version Space, List-Then-Elimination Algorithm, Candidate-Elimination Algorithm, General Boundary, Specific Boundary, Version Space Representation Theorem|
|2.6|[Remarks on Version Spaces and Candidate-Elimination](ch02/06/note.md)|Query|
|2.7|[Inductive Bias](ch02/07/note.md)|Power Set, Unbiased Learner, Inductive Bias, Inductive Inference Systems|

<br>

## 3. Decision Tree Learning
|No.|Chapter|Keywords|
|:-:|:------|:-------|
|3.2|[Decision Tree Representation](./ch03/02/note.md)|Node, Branch|
|3.3|[Appropriate Problems for Decision Tree Learning](./ch03/03/note.md)||
|3.4|[The Basic Decision Tree Learning Algorithm](./ch03/04/note.md)|Entropy, Information Gain, ID3|
|3.5|[Hypothesis Space Search in Decision Tree Learning](./ch03/05/note.md)|ID3|
|3.6|[Inductive Bias in Decision Tree Learning](./ch03/06/note.md)|BFS-ID3, Preference Bias(Search Bias), Restriction Bias(Language Bias)|
|3.7|[Issues in Decision Tree Learning](./ch03/07/note.md)|Overfit, Training and Validation Approach, Reduced-Error Pruning, Rule Post-Pruning, Rule Antecedent(precondition), Rule Consequent(postcondition), Pessimistic Estimate, Split Information, Gain Ratio|

<br>

## 4. Artificial Neural Networks (ANNs)
|No.|Chapter|Keywords|
|:-:|:------|:-------|
|4.2|[Neural Network Representations](./ch04/02/note.md)|ALVINN|
|4.3|[Appropriate Problems for Neural Network Learning](./ch04/03/note.md)||
|4.4|[Perceptrons](./ch04/04/note.md)|Perceptron Training Rule, Threshold, Delta Rule, Gradient Descent, Stochastic Gradient Descent (Incremental Gradient Descent)|
|4.5|[Multilayer Networks and the Backpropagation Algorithm](./ch04/05/note.md)|Sigmoid Unit (logistic function), Momentum|
|4.6|[Remarks on the Backpropagation Algorithm](./ch04/06/note.md)|Generalization Accuracy, Weight Decay, k-fold Cross-Validation Approach|
|4.7|[An Illustrative Example: Face Recognition](./ch04/07/note.md)|1-of-n Output Encoding|
|4.8|[Advanced Topics in Artificial Neural Networks](./ch04/08/note.md)|Various Error Functions : Penalty Term, Derivative (Slope), Cross Entropy, Weight Sharing<br> Line Search<br> Conjugate Gradient<br> Recurrent Networks<br> Cascade-Corelation algorithm|

<br>

## 5. Evaluating Hypotheses
|No.|Chapter|Keywords|
|:-:|:------|:-------|
|5.1|[Motivations](./ch05/01/note.md)|Bias and Variance in an estimate|
|5.2|[Estimating Hypothesis Accuracy](./ch05/02/note.md)|Sample Error, True Error, Confidence Intervals|
|5.3|[Basics of Sampling Theory](./ch05/03/note.md)|The Central Limit Theorem, Estimator, Estimation Bias, Confidence Interval|
|5.5|[Difference in Error of Two Hypotheses](./ch05/05/note.md)|Hypothesis Testing|
|5.6|[Comparing Learning Algorithms](./ch05/06/note.md)|Paired Test, Paired t Test, k-Fold Method|

<br>

## 6. Bayesian Learning
|No.|Chapter|Keywords|
|:-:|:------|:-------|
|6.2|[Bayes Theorem](./ch06/02/note.md)|Maximum A Posteriori Hypothesis (MAP), Maximum Likelihood Hypothesis (ML)|
|6.3|[Bayes Theorem and Concept Learning](./ch06/03/note.md)|Brute-Force Bayes Concept Learning, Consistent Learner|
|6.4|[Maximum Likelihood and Least-Squared Error Hypothesis](./ch06/04/note.md)|Bayesian Justification for Least-Squared Error Hypothesis, Probability Density Function|
|6.5|[Maximum Likelihood Hypotheses for Predicting Probabilities](./ch06/05/note.md)|Neural Network for ML Hypothesis, Cross Entropy|
|6.6|[Minimum Description Length Principle](./ch06/06/note.md)|Minimum Description Length Principle(MDL)|
|6.7|[Bayes Optimal Classifier](./ch06/07/note.md)|Bayes Optimal Classifier (Bayes Optimal Learner)|
|6.8|[Gibbs Algorithm](./ch06/08/note.md)||
|6.9|[Naive Bayesian Classifier](./ch06/09/note.md)|Naive Bayesian Classifier $(v_{NB})$, m-Estimate of Probability, Equivalent Sample Size|
|6.10|[An Example: Learning to Classify Text](./ch06/10/note.md)|Text Classification Algorithm based on the naive Bayes classifier|
|6.11|[Bayesian Belief Networks](./ch06/11/note.md)|Joint Space, Joint Probability Distribution, Conditional Independence|
|6.12|[The EM Algorithm](./ch06/12/note.md)|(Ex.)Estimating Means of k Gaussians, The EM Algorithm|

<br>

## 7. Computational Learning Theory
|No.|Chapter|Keywords|
|:-:|:------|:-------|
|7.2|[Probably Learning an Approximately Correct Hypothesis](./ch07/02/note.md)|Probably Approximately Correct (PAC)<br> True Error / Training Error<br> PAC Learnability|
|7.3|[Sample Complexity for Finite Hypothesis Spaces](./ch07/03/note.md)|Sample complexity<br> Consistent Learner<br> Exhausted Version Space<br> General Bound on the Number of Training Examples<br> Agnostic Learner $${\color{red}(\textrm{Verification Required!})}$$, Hoeffding Bounds<br> **PAC-Learnability of Boolean Conjunctions** (O) / **Unbiased Learners** (X) / **k-Term DNF** (X) / **k-CNF** (O) |
|7.4|[Sample Complexity for Infinite Hypothesis Spaces](./ch07/04/note.md)|Shattering a Set of Instances<br> Vapnik-Chervonenkis Dimension (VC Dimension)<br> Upper/Lower Bound on Sample Complexity using $VC(H)$<br> G-composition of C,<br> VC dimension of Layered Acyclic Networks (Perceptron)<br>|
|7.5|[The Mistake Bound Model of Learning](./ch07/05/note.md)|The Mistake Bound Model : Find-S, Halving Algorithm<br>Optimal Mistake Bound<br> Weighted-Majority Algorithm : Mistake Bound $${\color{red}(\textrm{Verification Required!})}$$ <br>|

<br>

## 8. Instance-Based Learning
|No.|Chapter|Keywords|
|:-:|:------|:-------|
|8.2|[k-Nearest Neighbor Learning](./ch08/02/note.md)|- k-Nearest Neighbor Algorithm : Discrete(Classification) / Continuous <br> - Decision Surface <br> - Distance-Weighted Nearest Neighbor Algorithm <br> - Global Method (Shepard's Method) / Local Method <br> - Curse of Dimensionality <br> - kd-tree <br> - Terms) Regression, Residual, Kernel Function|
|8.3|[Locally Weighted Regression](./ch08/03/note.md)|- Locally Weighted Linear Regression|
|8.4|[Radial Basis Functions (RBF)](./ch08/04/note.md)|- Kernel Function, Gaussian|
|8.5|[Case-Based Reasoning (CBR)](./ch08/05/note.md)|The CADET System (Water Faucet)|
|8.6|[Remarks on Lazy and Eager Learning](./ch08/06/note.md)|Lazy Learning Methods vs Eager Learning Methods|

<br>

## 9. Genetic Algorithms
|No.|Chapter|Keywords|
|:-:|:------|:-------|
|9.2|[Genetic Algorithms](./ch09/02/note.md)|- Genetic Algorithms (GA) <br>- Bit String Representation <br> -  Crossover/Mutation Operator <br> - Fitness Function : Fitness Proportionate (Roulette Wheel) / Tournament / Rank Selection|
|9.3|[An Illustrative Example](./ch09/03/note.md)|- GABIL|
|9.4|[Hypothesis Space Search](./ch09/04/note.md)|- Crowding Problem <br> - The Schema Theorem|
|9.5|[Genetic Programming](./ch09/05/note.md)|- Genetic Programming (GP)|
|9.6|[Models of Evolution and Learning](./ch09/06/note.md)|- Lamarckian Evolution <br> - Baldwin Effect|
|9.7|[Parallelizing Genetic Algorithms](./ch09/07/note.md)|- Coarse Grain Approach, Fine Grain Approach|

<br>

## 10. Learning Sets of Rules
|No.|Chapter|Keywords|
|:-:|:------|:-------|
|10.2|[Sequential Covering Algorithms](./ch10/02/note.md)|- First-Order Rule <br> - Sequential Covering Algorithm  <br>- General to Specific (Beam) Search : CN2, AQ|
|10.4|[Learning First-Order Rules](./ch10/04/note.md)|- |




<br><br>

[Back to AI Main](../../README.md)