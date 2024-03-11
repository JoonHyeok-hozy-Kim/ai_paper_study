* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 12.2 Inductive-Analytical Approaches to Learning
### 12.2.1 The Learning Problem
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












<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)