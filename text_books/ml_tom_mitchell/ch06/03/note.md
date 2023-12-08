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

#### Model) Brute-Force MAP Learning Algorithm
- Algorithm)
  1. For each hypothesis $h \in H$, calculate the posterior probability.
     - i.e.) $P(h|D) = \frac{P(D|h)P(h)}{P(D)}$
  2. Output the hypothesis $h_{MAP}$ with the highest posterior probability.
     - i.e.) $h_{MAP} = argmax_{h\in H} P(h|D)$
- Desc.)
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
      - $`P(D|h) = \left\lbrace \begin{array}{ll} 1 & if \space d_i=h(x_i), \forall d_i \in D \\ 0 & otherwise \end{array} \right.`$
        - i.e.) The probability of data $D$ given hypothesis $h$ is 1 if $D$ is consistent with $h$, and 0 otherwise. 
        - why?) 
          - By the assumption 1, $d_i = c(x_i)$. Assuming that $h$ is the correct description of $c$, $d_i=h(x_i)$.
      - $P(D) = \frac{|VS_{H,D}|}{|H|}$ where $VS_{H,D}$ is the [version space](../../ch02/05/note.md#concept-version-space) of $H$ w.r.t. $D$.
- Limit)
  - This algorithm may require significant computation.
    - why?) Calculating $P(h|D), \forall h \in H$ is costly!










<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)