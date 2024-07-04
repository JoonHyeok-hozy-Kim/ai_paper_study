* [Back to Deep Learning MIT](../../main.md)

# 7.12 Dropout

## Desc.)
- A computationally inexpensive but powerful method of [regularizing](../01/note.md#concept-regularization-in-deep-learning) a broad family of models
- A method of making [bagging](../11/note.md#concept-bagging-bootstrap-aggregating) practical for [ensembles](../11/note.md#concept-model-averaging-strategy-ensemble-model) of very many large neural networks
  - Recall that [bagging](../11/note.md#concept-bagging-bootstrap-aggregating) involves training multiple models, and evaluating multiple models on each test example.
  - This can be **impractical** when each model is a **large neural network**.
    - why?) Training and evaluating such networks is costly in terms of runtime and memory.
  - **Dropout** provides an inexpensive approximation to training and evaluating a [bagged ensemble](../11/note.md#concept-bagging-bootstrap-aggregating) of exponentially many neural networks.
    - How?)
      - Set up ensembles consisting of all sub-networks that can be formed by removing non-output units from an underlying base network.   
        ![](images/001.png)
        - cf.) There are multiple ways to remove a unit
          - We can effectively remove a unit from a network by **multiplying its output value by zero**.
          - For the [radial basis function](../../ch05/07/note.md#eg-gaussian-kernel-radial-basis-function-rbf) networks, take the difference between the unit's state and some reference value.

<br>

## Structure)
- Procedures)
  - Construct $`k`$ different datasets by sampling from the training set with replacement.
  - We will perform the [minibatch-based](../../ch05/09/note.md#59-stochastic-gradient-descent) learning algorithm for each $`i`$-th dataset  $`(i=1,2,\cdots,k)`$
    - For $`i`$-th dataset
      - Randomly sample a binary mask vector $`\mu`$ for each unit.
        - Desc.) $`\mu`$
          - The size of $`\mu`$ is equal to the number of units in the underlying base network.
          - If the $`j`$-th entry of $`\mu`$ is $`\begin{cases} 0\\1 \end{cases}`$, the $`j`$-th unit $`\begin{cases} \textrm{is removed} \\ \textrm{remains} \end{cases}`$.
            - e.g.)
              - $`x_1, x_2, h_1, h_2`$ : units
                - where
                  - $`x_i`$ : the input unit
                  - $`h_i`$ : the hidden unit
              - $`\mu = \begin{bmatrix} 1&0&0&1 \end{bmatrix} \Rightarrow`$ $`x_1, h_2`$ are included and $`x_2, h_1`$ are removed.
        - The mask for each unit must be **sampled independently** from all of the others.
          - The probability of sampling a mask value of one is a **hyperparameter** fixed before training begins.
            - Usually, 
              - $`0.5`$ for the hidden units 
              - $`0.8`$ for the input units.
      - Then we can define the cost of the model $`J(\theta, \mu)`$.
      - Optimization : Minimize $`\mathbb{E}_\mu J(\theta, \mu)`$
        - Why expectation?)
          - $`\mu`$ is randomly sampled with probabilities.
          - The expectation contains exponentially many terms but we can obtain an unbiased estimate of its gradient by sampling values of $`\mu`$.
        - Run forward propagation, backward-propagation, and the learning update.
  - To make a prediction, a bagged ensemble must accumulate votes from all of its members.
    - We refer to this process as [inference](#tech-inference) in this context.

- e.g.)    
  |Network|Graphic|Desc.|
  |:-:|:-|:-|
  |Underlying Base Network|<img src="images/002.png">|- Two input units $`x_1, x_2`$ <br> - Two output units $`h_1, h_2`$|
  |Dropout Network|<img src="images/003.png">|- $`\mu = \begin{bmatrix} \mu_i \end{bmatrix} \textrm{, where } \mu_i \in \{0,1\}, i=1,2,3,4`$|

<br>

## Analysis) Comparison with Bagging
- Differences)
  ||[Bagging](../11/note.md#concept-bagging-bootstrap-aggregating)|Dropout|
  |:-|:-|:-|
  |Dependencies between sub-models|- Independent|- Models [share parameters](../09/note.md#tech-2-parameter-sharing).|
  |Training|- Each model is trained to convergence on its respective training set|- Typically most models are not explicitly trained at all. <br>- Instead, a tiny fraction of the possible sub-networks are each trained for a single step. <br>- And the parameter sharing causes the remaining sub-networks to arrive at good settings of the parameters.|
- Other than the above differences, **dropout** follows the [bagging]((../11/note.md#concept-bagging-bootstrap-aggregating)) algorithm.

<br><br>

## Tech.) Inference
- Objective)
  - Output a probability distribution from the [dropout](#desc) model.
- Desc.)
  - In the case of dropout, each sub-model defined by mask vector $`\mu`$ defines a probability distribution $`p(y|x,\mu)`$
  - Thus, the arithmetic mean over all masks is given by
    - $`\displaystyle\sum_\mu p(\mu)p(y|x,\mu)`$
      - where $`p(\mu)`$ is the probability distribution that was used to sample $`\mu`$
- Problem)
  - It is intractable to evaluate except in cases where the structure of the model permits some form of simplification.
    - why?) There are exponential number of $`\mu`$s
  - So far, deep neural nets are not known to permit any tractable simplification.
- Sols.)
  - Approximate the inference with sampling, by averaging together the output from many masks. 
    - Even 10-20 masks are often sufficient to obtain good performance.
  - Using Geometric Mean by *Warde-Farley et al. (2014)*
    - Settings)
      - To guarantee that the result is a probability distribution, we impose the requirement that none of the sub-models assigns probability $`0`$ to any event, and we re-normalize the resulting distribution.
        - why?) The geometric mean of multiple probability distributions is not guaranteed to be a probability distribution.
      - The **unnormalized probability distribution** defined directly by the geometric mean is given by
        - $`\displaystyle \tilde{p}_{\textrm{ensemble}}(y|x) = \sqrt[^{2^d}]{\prod_\mu p(y|x,\mu)}`$
          - where $`d`$ is the number of units that may be dropped.
      - For simplicity, use a uniform distribution over $`\mu`$
        - cf.) Non-uniform distributions are also possible.
    - Procedures)
      - Get $`\tilde{p}_{\textrm{ensemble}}(y|x)`$ for each $`(y, \mu)`$
      - Re-normalize the ensemble to make predictions.
        - $`\displaystyle p_{\textrm{ensemble}}(y|x) = \frac{\tilde{p}_{\textrm{ensemble}}(y|x)}{\sum_{y'} \tilde{p}_{\textrm{ensemble}}(y'|x)}`$
          - Concept) **Weight Scaling Inference Rule**
            - Desc.)
              - We are trying to approximate $`p_{\textrm{ensemble}}`$ by evaluating $`p(y|x)`$ in the $`i`$-th model
                - where
                  - the model has all units
                  - the weights going out of unit $`i`$ is multiplied by the probability of including the unit $`i`$
              - The motivation for this approach is to capture the right expected value of the output from that unit.
              - This approach is called the **weight scaling inference rule**.
            - e.g.)
              - [Recall](#structure) that we usually assign $`0.5`$ for the inclusion probability of the input units.
              - Then the **weight scaling rule** usually amounts to dividing the weights by 2 at the end of training, and then using the model as usual.
              - Another way to achieve the same result is to multiply the states of the units by 2 during training. 
              - Either way, the goal is to make sure that the **expected total input to a unit at test time** is roughly the same as the **expected total input to that unit at train time**, even though **half the units at train time are missing on average**.
            - Props.)
              - For many classes of models that do not have nonlinear hidden units, the weight scaling inference rule is **exact**.
                - e.g.) A Softmax regression classifier with $`n`$ input variables represented by the vector $`v`$.
                  - $`P(\mathbf{y}=y|\mathbf{v}) = \textrm{softmax}\left(W^\top \mathbf{v} + b\right)_y`$
                  - Then the family of sub-models by element-wise multiplication of the input with a binary vector $`d`$ goes as
                    - $`P(\mathbf{y}=y|\mathbf{v};d) = \textrm{softmax}\left(W^\top (d\odot \mathbf{v}) + b\right)_y`$
                  - The ensemble predictor is defined by re-normalizing the geometric mean over all ensemble members’ predictions:
                    - $`\displaystyle P_{\textrm{ensemble}}(\mathbf{y}=y|v) = \frac{\tilde{P}_{\textrm{ensemble}}(\mathbf{y}=y|\mathbf{v})}{\sum_{y'} \tilde{P}_{\textrm{ensemble}}(\mathbf{y}=y'|\mathbf{v})}`$
                      - where $`\displaystyle\tilde{P}_{\textrm{ensemble}}(\mathbf{y}=y|\mathbf{v}) = \sqrt[^{2^n}]{\prod_{d\in\{0,1\}^n} P(\mathbf{y}=y|\mathbf{v};d)}`$



<br>

* [Back to Deep Learning MIT](../../main.md)