* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 6.5 Maximum Likelihood Hypotheses for Predicting Probabilities

#### Objective) Learn to Predict Probabilities.
How can we train a model that learns a nondeterministic(probabilistic) function that outputs the probability of certain phenomenon?
- e.g.)
  - Patient Example
    - Suppose we are given the data ov a collection of patients exhibiting the same set of observable symptoms.
    - The 92% of them survived and the 8% did not.
    - Then, what is the probability that a patient survive, given a certain symptoms?
  - Credit History Example
    - Suppose we have the past credit histories of multiple loan applicants.
    - What is the probability of a certain loan applicant will successfully repays the loan, given his/her credit history?

<br>

#### Problem Setting)
- $X$ : an instant space with $x \in X$
- $D$ : the dataset with $d \in D$
- $f : X \rightarrow \lbrace 0, 1 \rbrace$ : a nondeterministic(probabilistic) function
- We want to find a function $f'$ which outputs the probability that $f(x)=1$.
  - i.e.) $f' : X \rightarrow [0,1]$ such that $f'(x) = P(f(x)=1)$
- We will use the neural network learning.

<br>

#### Solution) Train a Neural Network for ML Hypothesis
- Assumptions)
  - $x_i$ and $d_i$ are both random variables.
    - Why $x_i$ is a random variable?
      - In our [previous analysis](../04/note.md#prop-bayesian-justification-for-least-squared-error-hypothesis), we ordered the training data into $D=\lbrace \langle x_1, d_1 \rangle, \cdots, \langle x_m, d_m \rangle \rbrace$.
        - This simplifies the analysis by making an instance $x_i$ dependent on the data $d_i$.
      - However, by forgoing the simplicity, we can demonstrate that $x_i$ has no impact on the final outcome.
        - Then, we can say that $x_i$ is independent of any hypothesis $h$.
        - Still, $d_i$ is strongly dependent on $h$.
- Derivation) ML Hypothesis
  - Recall that $h_{ML} = argmax_{h \in H} P(D|h)$.
  - Let's define $P(D|h)$ first.
    - $P(D|h) = \Pi_{i=1}^m P(x_i, d_i|h)$
      - why?)
        - $x_i$ and $d_i$ are random variables 
        - $x_i$ is independent of $h$
    - $P(D|h) = \Pi_{i=1}^m P(d_i|h,x_i)P(x_i)$
      - why?)
        - $x_i$ is independent of $h$
        - Recall the [Theorem of Total Probability](../02/note.md#theorem-theorem-of-total-probability).
    - $P(D|h) = \Pi_{i=1}^m {h(x_i)}^{d_i}{(1-h(x_i))}^{1-d_i}P(x_i)$
      - why?)
        - Put $`P(d_i|h,x_i) = \left\lbrace\begin{array}{cc} h(x_i) & if \space d_i=1 \\ 1-h(x_i) & if \space d_i=0 \end{array}\right.`$
          - why?)
            - Our goal was to get the probability that $d_i=1$ for a single instance $x_i$, given a world in which hypothesis $h$ holds.
            - Recall that $h$ is our hypothesis regarding the target function, which computes this very probability.
              - Thus, $P(d_i=1|h,x_i)=h(x_i)$.
              - Considering the case of $d_i=0$, $P(d_i|h,x_i)$ can be written as the above.
        - Moreover, the below notation is equivalent to the above.
          - $P(d_i|h,x_i) = {h(x_i)}^{d_i}{(1-h(x_i))}^{1-d_i}$
        - Hence, substitute $P(d_i|h,x_i)$ with ${h(x_i)}^{d_i}{(1-h(x_i))}^{1-d_i}$.
  - Now, let's setup the ML hypothesis using the $P(D|h)$ above.
    - $h_{ML} = argmax_{h \in H} \Pi_{i=1}^m {h(x_i)}^{d_i}{(1-h(x_i))}^{1-d_i}P(x_i)$.
  - Let's derive the $h_{ML}$.
    - $h_{ML} = argmax_{h \in H} \Pi_{i=1}^m {h(x_i)}^{d_i}{(1-h(x_i))}^{1-d_i}$.
      - why?)
        - $P(x_i)$ is independent of $h$ so it can be regarded as a constant.
    - $h_{ML} = argmax_{h \in H} \Sigma_{i=1}^m d_i \ln{{h(x_i)}} + (1-d_i) \ln{(1-h(x_i))}$.
      - why?)
        - Assuming $\ln{h}$ is a monotonic function of $h$, we may apply the log likelihood.
      - cf.) The similarity with the general form of the entropy function : $-\Sigma_i p_i \log{p_i}$
        - Because of this similarity, the negation of the above quantity is sometimes called the cross entropy.
- Optimization) Gradient Descent
  - Recall that we utilize the neural network learning.
    - For simplicity, assume that our network is constructed from a single layer of [sigmoid unit](../../ch04/05/note.md#concept-sigmoid-unit)s.
      - The output $o=\sigma(\overrightarrow{w}, \overrightarrow{x})$
        - where $\sigma(y)=\frac{1}{1+e^{-y}}$
      - Then, $\frac{d\sigma(y)}{dy}= \sigma(y)(1-\sigma(y))$
  - We should define how we will derive a **weight-training rule** for neural network learning.
  - We will use the gradient descent method.
    - Put $G(h,D) = d_i \ln{{h(x_i)}} + (1-d_i) \ln{(1-h(x_i))}$.
    - Then, the gradient of $G(h, D)$ is given by the vector of partial derivatives of $G(h, D)$ with respect to the various network weights that define the hypothesis $h$ represented by the learned network.
    - $`\begin{array}{ll} \frac{\partial G(h,D)}{\partial w_{jk}} & = \Sigma_{i=1}^m \frac{\partial G(h,D)}{\partial h(x_i)} \frac{\partial h(x_i)}{\partial w_{jk}} \\ & = \Sigma_{i=1}^m \frac{\partial (d_i \ln{{h(x_i)}} + (1-d_i) \ln{(1-h(x_i))})}{\partial h(x_i)} \frac{\partial h(x_i)}{\partial w_{jk}} \\ & = \Sigma_{i=1}^m \frac{d_i-h(x_i)}{h(x_i)(1-h(x_i))} \frac{\partial h(x_i)}{\partial w_{jk}}  \end{array}`$
    - Recall that we assumed a single layer of sigmoid units.
      - Thus, $\frac{\partial h(x_i)}{\partial w_{jk}} = \sigma'(x_i)x_{ijk} = h(x_i)(1-h(x_i))x_{ijk}$
        - where $x_{ijk}$ is the $k$-th input to the unit $j$ for the $i$-th training example.
      - Hence, $`\begin{array}{ll} \frac{\partial G(h,D)}{\partial w_{jk}} & = \Sigma_{i=1}^m \frac{d_i-h(x_i)}{h(x_i)(1-h(x_i))} \frac{\partial h(x_i)}{\partial w_{jk}} \\ &= \Sigma_{i=1}^m \frac{d_i-h(x_i)}{h(x_i)(1-h(x_i))} h(x_i)(1-h(x_i))x_{ijk}  \\ &= \Sigma_{i=1}^m (d_i-h(x_i))x_{ijk} \end{array}`$
    - Because we seek to maximize rather than minimize $P(D|h)$, we perform gradient **ascent** rather than gradient descent search.
      - Thus, on each iteration of the search the weight vector is adjusted in the direction of the gradient, using the weight-update rule
        - $w_{jk} \leftarrow w_{jk} + \Delta w_{jk}$
          - where $\Delta w_{jk} = \eta \Sigma_{i=1}^m(d_i-h(x_i)) x_{ijk}$
            - where $\eta$ is the learning rate.
- Analysis)
  - Comparison with the [Backpropagation Algorithm](../../ch04/05/note.md#452-the-backpropagation-algorithm).
    - Recall that the weight-update rule of the Backpropagation Algorithm was to **minimize** the sum of squared errors between predicted and observed network outputs.
      - i.e.) $E(\overrightarrow{w}) \equiv \frac{1}{2} \Sigma_{d \in D} \Sigma_{k \in outputs} (t_{kd} - o_{kd})^2$
    - The Backpropagation Algorithm's weight-updating rule can be re-expressed using our current notation as follows.
      - $w_{jk} \leftarrow w_{jk} + \Delta w_{jk}$
        - where $\Delta w_{jk} = \eta \Sigma_{i=1}^m h(x_i)(1-h(x_i)) (d_i-h(x_i)) x_{ijk}$
    - Meanwhile, the ML hypothesis weight-update rule was to **maximize** the likelihood.
      - As a result, it minimizes cross entropy.
    - Interestingly, these two weight update rules converge toward maximum likelihood hypotheses in two different settings.
      1. The rule that minimizes sum of squared error seeks the maximum likelihood hypothesis under the assumption that the training data can be modeled by Normally distributed noise added to the target function value. 
      2. The rule that minimizes cross entropy seeks the maximum likelihood hypothesis under the assumption that the observed boolean value is a probabilistic function of the input instance. 





<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)