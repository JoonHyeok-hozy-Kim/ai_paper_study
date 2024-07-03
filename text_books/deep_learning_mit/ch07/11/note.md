* [Back to Deep Learning MIT](../../main.md)

# 7.11 Bagging and Other Ensemble Methods

### Concept) Model Averaging Strategy (Ensemble Model)
- Desc.)
  - Train several different models separately
  - Have all of the models vote on the output for test examples
- cf.) Ensemble Models : Techniques employing the Model Averaging Strategy

<br>

### Concept) Bagging (Bootstrap Aggregating)
- Desc.)
  - A technique for reducing generalization error by [combining several models](#concept-model-averaging-strategy-ensemble-model)
    - Why does this work?)
      - Different models usually do not make all the same errors on the test set.
      - e.g.)
        - Consider a simple ensemble model with $`k`$ regression models.
        - Each $`i`$-th model makes an error $`\epsilon_i`$ on each example.
          - where $`\epsilon_i`$ is drawn from a zero-mean multivariate normal distribution with
              - $`\mathbb{E}\left[ \epsilon_i^2 \right] = v`$
              - $`\mathbb{E}\left[ \epsilon_i \epsilon_j \right] = c`$
        - Then the error made by the average prediction of all the ensemble model is
          - $`\displaystyle \frac{1}{k}\sum_{i=1}^k \epsilon_i`$
        - Thus, the expected squared error of the ensemble predictor is   
          $`\begin{aligned}
            \mathbb{E}\left[ \left( \frac{1}{k}\sum_{i=1}^k \epsilon_i \right)^2 \right]
            &= \frac{1}{k^2} \mathbb{E}\left[ \sum_{i=1}^k \left( \epsilon_i^2 + \sum_{j\ne i} \epsilon_i \epsilon_j \right) \right] \\
            &= \frac{1}{k}v + \frac{k-1}{k} c
          \end{aligned}`$
        - Interpretation)
          - Case 1) $`c = v`$ : the errors are perfectly correlated.
            - Then the mean squared error goes
              - $`\displaystyle \mathbb{E}\left[ \left( \frac{1}{k}\sum_{i=1}^k \epsilon_i \right)^2 \right] = v`$
                - i.e.) The model averaging dose not work.
          - Case 2) $`c = 0`$ : the errors are perfectly uncorrelated
            - Then the mean squared error goes
              - $`\displaystyle \mathbb{E}\left[ \left( \frac{1}{k}\sum_{i=1}^k \epsilon_i \right)^2 \right] = \frac{1}{k}v`$
                - i.e.) The expected squared error of the ensemble decreases linearly with the ensemble size $`k`$.
          - Conclusion)
            - On average, the ensemble will perform at least as well as any of its members.
            - If the members make **independent** errors, the ensemble will perform significantly better than its members.
  - Bagging allows the same kind of model, training algorithm and objective function to be reused several times.
    - But different ensemble methods construct the ensemble of models in different ways.
  - Bagging involves constructing $`k`$ different **datasets**.
    - Each dataset...
      - has the **same number of examples** as the original dataset
      - is constructed by **sampling with replacement** from the original dataset.
    - Thus, with high probability, each dataset is missing some of the examples from the original dataset and also contains several duplicate examples.
  - Neural networks benefit from model averaging even if all of the models are trained on the same dataset.
    - Why?)
      - Neural networks have many points to customize.
        - Differences in...
          - random initialization
          - random selection of minibatches
          - hyperparameters
          - outcomes of non-deterministic implementations of neural networks 
  - Model averaging is an extremely powerful and reliable method for reducing generalization error.
    - but at the price of increased computation and memory...

<br><br>

### Concept) Boosting
- Desc.)
  - Recall that [Bagging](#concept-bagging-bootstrap-aggregating) is designed to make the ensemble **more regularized** than the individual models.
  - On the other hand, **Boosting** constructs an ensemble with **higher capacity** than the individual models.


<br>

* [Back to Deep Learning MIT](../../main.md)