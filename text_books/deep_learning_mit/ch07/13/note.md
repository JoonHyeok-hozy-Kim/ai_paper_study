* [Back to Deep Learning MIT](../../main.md)

# 7.13 Adversarial Training

### Concept) Adversarial Example
- Def.)
  - An input $`x'`$ near a data point $`x`$ s.t. the model output is very different at $`x'`$ compared to the one at $`x`$.

- e.g.)   
  <img src="images/001.png">

- Props.)
  - In many cases, $`x'`$ is so similar to $`x`$ that human observer cannot distinguish between them.

<br>

### Concept) Adversarial Training
- Desc.)
  - In many cases, neural networks have begun to reach human performance when evaluated on an **i.i.d.**
  - *Szegedy et al. (2014b)* found that even neural networks that perform at human level accuracy have a nearly 100% error rate on [adversarial examples](#concept-adversarial-example).
  - *Goodfellow et al. (2014b)* showed that one of the primary causes of these adversarial examples is excessive linearity.
    - Most models are composed of linear functions because they are easy to optimize.
    - However, the value of a linear function can change very rapidly if it has numerous inputs.
      - e.g.) $`\epsilon`$ change in input.
        - In a linear function with weights $`w`$, the total change will be $`\epsilon||w||_1`$.
        - In higher-dimensional functions, the change will be much greater.
  - Adversarial training discourages this highly sensitive **locally linear behavior** by encouraging the network to be locally constant in the neighborhood of the training data.
    - i.e.) explicitly introducing a local constancy prior into supervised neural nets
  - Adversarial training helps to illustrate the **power of using a large function family** in combination with aggressive regularization.
    - Purely linear models, like logistic regression, are not able to resist adversarial examples because they are forced to be linear.
    - Recall that neural networks are able to represent functions that can range from **nearly linear** to **nearly locally constant**.
    - Thus, neural networks have the flexibility to capture linear trends in the training data while still learning to **resist local perturbation**.
  - Adversarial examples provide a means of accomplishing **semi-supervised learning**.
    - How) Virtual Adversarial Examples, *Miyato et al., 2015*
      - Suppose a model has a quality.
      - At a point $`x`$ that is not associated with a label in the dataset, the model itself assigns some label $`\hat{y}`$.
        - The model’s label $`\hat{y}`$ may not be the true label.
        - But if the model is high quality, then $`\hat{y}`$ has a high probability of providing the true label.
      - Then we can seek an [adversarial example](#concept-adversarial-example) $`x'`$ s.t. the model outputs $`y' \ne \hat{y}`$.
      - The classifier may then be trained to assign the same label to $`x`$ and $`x'`$.
        - This encourages the classifier to learn a function that is robust to small changes anywhere along the manifold where the unlabeled data lies.










<br>

* [Back to Deep Learning MIT](../../main.md)