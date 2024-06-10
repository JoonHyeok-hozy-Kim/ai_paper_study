* [Back to Deep Learning MIT](../../main.md)

# 5.11 Challenges Motivating Deep Learning

## 5.11.1 The Curse of Dimensionality
- Desc.)
  - Many machine learning problems become exceedingly **difficult when the number of dimensions in the data is high**.
    - why?)
      - The number of possible distinct configurations of a set of variables increases **exponentially** as the number of variables increases.
      - Statistical Challenge
        - The number of possible configurations of $`x`$ is much larger than the number of training examples.
        - When estimating the probability density at some point $`x`$, we can just return the number of training examples in the same unit volume cell as $`x`$, divided by the total number of training examples.
        - When classifying an example, we can return the most common class of training examples in the same cell.
        - But, what if there is no training example near $`x`$?
        - This problem arises substantially as the dimensionality of the data increases.

<br><br>

## 5.11.2 Local Constancy and Smoothness Regulation









<br>

* [Back to Deep Learning MIT](../../main.md)