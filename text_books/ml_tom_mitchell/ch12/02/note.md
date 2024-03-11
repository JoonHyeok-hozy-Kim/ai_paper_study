* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 12.2 Inductive-Analytical Approaches to Learning
## 12.2.1 The Learning Problem
- Given)
  - A set of training examples $D$, possibly containing errors
  - A domain theory $B$, possibly containing errors
  - A space of candidate hypothesis $H$
- Determine)
  - A hypothesis that best fits the training examples and domain theory
    - How to measure the fit?)
      - Combine the following two errors.
         - Errors)
           - $error_D(h)$ : the proportion of examples from $D$ that are misclassified by $h$.
           - $error_B(h)$ : the probability that $h$ will disagree with $B$ on the classification of a randomly drawn instance
         - Combination)
           - $`\displaystyle \arg\min_{h\in H} k_D \; error_D(h) + k_B \; error_B(h)`$
             - where $k_D + k_B = 1$ : the weights
       - How to set weights?
         1. Arbitrary Setting
            - Prop.)
              - If we have a very poor theory and a great deal of reliable data, it will be best to weight $error_D(h)$ more heavily.
              - Given a strong theory and a small sample of very noisy data, the best results would be obtained by weighting $error_B(h)$ more heavily.
            - Drawback)
              - If the learner does not know in advance the quality of the domain theory or training data, it will be unclear how it should weight these two error components. 
         2. Bayesian Perspective
            - Use $P(h|D)$ for $k_D$ and $P(h|B)$ for $k_B$.
              - Desc.)
                - [Recall that Bayes theorem describes](../../ch06/02/note.md#concept-bayes-theorem) how to compute the **posterior probability** $P(h|D)$ of hypothesis $h$ given observed training data $D$.
                  - $`\displaystyle P(h|D)=\frac{P(h\cap D)}{P(D)}=\frac{P(D|h)P(h)}{P(D)}`$
                - Here, $P(D|h),P(h),P(D)$ consist prior knowledge.
                - Thus, we can consider them as the background knowledge or the domain theory.
                - Additionally, we may choose $h$ that maximizes the likelihood.
              - Drawback)
                - Bayes theorem implicitly assumes pe$ect knowledge about the probability distributions $P(D|h),P(h),P(D)$.
                - When these quantities are only imperfectly known, Bayes theorem alone does not prescribe how to combine them with the observed data.
                  - We may assume the prior probability distributions over $P(D|h),P(h),P(D)$.
                  - However, this requires additional knowledge about the priors over $P(D|h),P(h),P(D)$, so it does not really solve the general problem.

<br><br>

## 12.2.2 Hypothesis Space Search
#### Settings)
- $H$ : the hypothesis space
  - $h_0$ : the initial hypothesis where the search begins
- $O$ : the set of search operators that define individual search steps
- $G$ : the goal criterion that specifies the search objective

<br>

#### Three different methods for using prior knowledge to alter the search performed purely by inductive methods
1. [Use prior knowledge to derive an initial hypothesis from which to begin the search](../03/note.md).
   - Desc.)
     - The domain theory $B$ is used to construct an initial hypothesis $h_0$ that is consistent with $B$.
     - Then, a standard inductive method is applied, starting with $h_0$.
   - e.g.)
     - KBANN
       - It learns artificial neural networks.
       - It uses **prior knowledge** to design the interconnections and weights for an **initial network**.
         - This initial network will be perfectly consistent with the given domain theory.
       - Then, it inductively refines the initial network hypothesis using the Backpropagation algorithm and available data.
2. [Use prior knowledge to alter the objective of the hypothesis space search](../04/note.md).
   - Desc.)
     - The goal criterion $G$ is modified to require that the output hypothesis fits the **domain theory** as well as the **training examples**.
   - e.g.)
     - EBNN
        - It learns artificial neural networks.
        - EBNN performs gradient descent to optimize a modified criterion including an additional term that measures **the error of the learned network relative to the domain theory**.
          - cf.) Recall that original neural network algorithms performs gradient descent search to minimize **the squared error of the network over the training data**.
3. [Use prior knowledge to alter the available search steps](../05/note.md).
   - Desc.)
     - The set of search operators $O$ is altered by the domain theory.
   - e.g.)
     - FOCL
       - It learns sets of Horn clauses based on the [FOIL](../../ch10/05/note.md#concept-foil) system.
         - Recall that the FOIL system conducts a **greedy search** through the space of possible Horn clauses, at each step revising its current hypothesis by adding a single new literal.
       - FOCL uses the domain theory to expand the set of alternatives available when revising the hypothesis.
         - i.e.) $B$ is used to add the **multiple literals in a single search step**.
           - A.K.A. **Macro-Move**
             - Differ from the original FOIL that adds one clause in one step.
             - Ultimately alter the course of search!
               - why?)
                 - FOIL ends up with a hypothesis that is  consistent with the **data**!







<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)