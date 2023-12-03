* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 5.5 Difference in Error of Two Hypotheses

#### Concept) Estimating the Difference between the True Errors of Two Hypotheses
- Setting)
  - Hypothesis $h_1$ tested on a sample $S_1$ containing $n_1$ randomly drawn examples.
  - Hypothesis $h_2$ tested on a sample $S_2$ containing $n_2$ randomly drawn examples.
- Model)
  - We want to know the difference between the true errors of the hypotheses above.
    - $d \equiv error_D(h_1) - error_D(h_2)$
  - Since we do not know the true errors, we can use sample errors to estimate the difference $d$.
    - $\hat{d} \equiv error_{S_1}(h_1) - error_{S_2}(h_2)$
      - $E[\hat{d}] = d$.
        - i.e. $\hat{d}$ is an unbiased estimator.
  - Assuming that $n_1$ and $n_2$ are large enough, $error_{S_1}(h_1)$ and $error_{S_2}(h_2)$ both follow the Normal distribution.
  - Thus, $\hat{d} \sim N(d, \sigma_{\hat{d}}^2)$.
    - where $\sigma_{\hat{d}}^2 \approx \frac{error_{S_1}(h_1) (1-error_{S_1}(h_1))}{n_1} + \frac{error_{S_2}(h_2) (1-error_{S_2}(h_2))}{n_2}$.
  - Hence, we can get the confidence interval for $d$ as follows.
    - $\hat{d} \pm z_N \sigma_{\hat{d}}$


<br><br>

## 5.5.1 Hypothesis Testing
#### Question)
What is the probability that $error_D(h_1) > error_D(h_2)$?








<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)