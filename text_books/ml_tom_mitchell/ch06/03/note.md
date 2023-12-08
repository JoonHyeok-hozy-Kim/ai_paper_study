* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 6.3 Bayes Theorem and Concept Learning

## 6.3.1 Brute-Force Bayes Concept Learning
- Settings)
  - The learner considers some finite hypothesis space $H$
  - $H$ is defined over the instance space $X$.
  - The task is to learn some target concept $c : X \rightarrow \lbrace 0,1 \rbrace$.
  - Assume sequenced $m$ training examples : $\langle \langle x_1, d_1 \rangle, \cdots, \langle x_m, d_m \rangle \rangle$
    - where $x_i$ is some instance from $X$
    - and $d_i$ is the target value of $x_i$.
      - i.e.) $d_i = c(x_i)$
  - Since we assumed the instances are in a sequence, we can simplify the target values as $D = \langle d_1, \cdots, d_m \rangle$.

<br>

### Model) Brute-Force MAP Learning Algorithm
#### Algorithm)
  1. For each hypothesis $h \in H$, calculate the posterior probability.
     - i.e.) $P(h|D) = \frac{P(D|h)P(h)}{P(D)}$
  2. Output the hypothesis $h_{MAP}$ with the highest posterior probability.
     - i.e.) $h_{MAP} = argmax_{h\in H} P(h|D)$
#### Desc.)
  - How to choose $P(D|h),P(h)$ and $P(D)$.
    - Assumptions)
       1. The training data $D$ is noise free.
          - $d_i = c(x_i)$
       2. The target concept $c$ is contained in the hypothesis space $H$.
       3. We have no a priori reason to believe that any hypothesis is more probable than any other.
    - Choices)
      - $P(h) = \frac{1}{|H|}$ where $|H|$ is the size of $H$.
        - why?) 
          - By the assumption 3, each $h \in H$ will have the same probability.
            - i.e.) Uniform Distribution : $H \sim U(0, |H|)$
      - $`P(D|h) = \left\lbrace \begin{array}{ll} 1 & if \space d_i=h(x_i), \forall d_i \in D \\ 0 & otherwise \end{array} \right.`$
        - i.e.) The probability of data $D$ given hypothesis $h$ is 1 if $D$ is consistent with $h$, and 0 otherwise. 
        - why?) 
          - By the assumption 1, $d_i = c(x_i)$. Assuming that $h$ is the correct description of $c$, $d_i=h(x_i)$.
      - $P(D) = \frac{|VS_{H,D}|}{|H|}$ where $VS_{H,D}$ is the [version space](../../ch02/05/note.md#concept-version-space) of $H$ w.r.t. $D$.
        - why?)
          - Recall the [theorem of total probability](../02/note.md#theorem-theorem-of-total-probability).
          - Thus, $`\begin{array}{ll} P(D) & = \Sigma_{h_i \in H} P(D|h_i)P(h_i) \\ & = \Sigma_{h_i \in VS_{H,D}} 1 \cdot \frac{1}{|H|} + \Sigma_{h_i \notin VS_{H,D}} 0 \cdot \frac{1}{|H|} \\ & = \frac{|VS_{H,D}|}{|H|} \end{array}`$
  - How to calculate $P(h|D)$.
    - $`P(h|D) = \frac{P(D|h)P(h)}{P(D)} = \left\lbrace\begin{array}{ll} \frac{1}{VS_{H,D}} & if \space h(x_i) = c(x_i)=d_i, \forall x_i \in X \\ 0 & otherwise. \end{array}\right.`$
      - where $h(x_i) = c(x_i)=d_i, \forall x_i \in X$ denotes the [consistent](../../ch02/05/note.md#concept-consistency) hypothesis
#### Analysis)
  - Every consistent hypothesis is a [MAP hypothesis](../02/note.md#concept-maximum-a-posteriori-hypothesis-map-hypothesis).
    - why?)
      - Every consistent hypothesis shares the same probability of $P(h|D)=\frac{1}{VS_{H,D}}$.
        - cf.) [Consistency](../../ch02/05/note.md#concept-consistency)
          - $h(x) = c(x)$
      - Recall that the definition of the MAP hypothesis is a hypothesis that maximizes $P(h|D)$.
      - Thus, every consistent hypothesis is a $h_{MAP}$.
#### Limit)
  - This algorithm may require significant computation.
    - why?) Calculating $P(h|D), \forall h \in H$ is costly!

<br><br>

## 6.3.2 MAP Hypotheses and Consistent Learners
### Concept) Consistent Learner
- Def.)
  - A learning algorithm is a **consistent learner** provided it outputs a hypothesis that commits zero errors over the training examples.

#### Prop.)
Under the following two [assumptions](#desc), every consistent learner outputs a MAP hypothesis
- Assumptions
  1. A uniform prior probability distribution over $H$
  2. The training data are deterministic and noise free.

<br>

#### e.g.) Find-S Algorithm
- Recall the [Find-S Algorithm](../../ch02/04/note.md#concept-find-s-algorithm).
- Props.)
  - Find-S searches the hypothesis space $H$ from specific to general hypotheses, outputting a maximally specific consistent hypothesis (i.e., a **maximally specific member** of the version space).
  - Since Find-S outputs a **consistent** hypothesis, we know that it will output a MAP hypothesis under the probability distributions $P(h)$ and $P(D|h)$ [defined above](#prop).
    - Problem) 
      - Find-S does not explicitly manipulate probabilities at all.
        - Still, by identifying distributions for $P(h)$ and $P(D|h)$ under which its output hypotheses will be MAP hypotheses, we have a useful way of characterizing the behavior of Find-S.
    - Question) 
      - Are there other probability distributions for $P(h)$ and $P(D|h)$ under which Find-S outputs MAP hypotheses?
      - Answer)
        - Yes. Because Find-S outputs a maximally specific hypothesis from the version space, its output hypothesis will be a MAP hypothesis relative to any prior probability distribution that favors more specific hypotheses.
          - It can be shown that Find-S outputs a MAP hypothesis assuming the prior distribution $\mathcal{H}$.
            - where $\mathcal{H}$ is any probability distribution $P(h)$ over $H$ that assigns $P(h_1) \ge P(h_2)$ if $h_1$ is more specific than $h_2$.

<br>

#### e.g.) Candidate-Elimination Algorithm
- Recall the [Candidate-Elimination Algorithm](../../ch02/05/note.md#254-candidate-elimination-learning-algorithm)
- [Inductive Bias](../../ch02/07/note.md#27-inductive-bias) was one way to characterize the assumptions implicit in learning algorithms.
  - We defined the **inductive bias** of a learning algorithm to be the set of assumptions $B$ sufficient to deductively justify the inductive inference performed by the learner.
    - e.g.) The inductive bias of the Candidate-Elimination Algorithm is the assumption that the target concept $c$ is included in the hypothesis space $H$.
  - Furthermore, we showed there that the output of this learning algorithm follows deductively from its inputs plus this implicit inductive bias assumption.
- Bayesian Interpretation provides an alternative way to characterize the assumptions implicit in learning algorithms.
  - How?)
    - Use the **probabilistic reasoning system** based on Bayes theorem.
      - Implicit Assumptions)
        - The prior probabilities over $H$ are given by the distribution $P(h)$
        - The strength of data in rejecting or accepting a hypothesis is given by $P(D|h)$.






<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)