* [Back to Dive into Deep Learning](../../main.md)

# 4.7. Environment and Distribution Shift

## 4.7.1 Types of Distribution Shift
- Assumption)
  - The training data was sampled from some distribution $p_S(\mathbf{x}, y)$
  - The test data consists of unlabeled examples drawn from $p_T(\mathbf{x}, y)$
- Types)
  - [Covariate Shift](#4711-covariate-shift)
  - [Label Shift](#4712-label-shift)
  - [Concept Shift](#4713-concept-shift)
---

<br><br>

### 4.7.1.1 Covariate Shift
- Assumption)
  - The distribution of inputs may change over time.
  - The labeling function does not change.
    - e.g.) the conditional distribution $P(y|\mathbf{x})$
- Prop.)
  - The problem arises due to a shift in the distribution of the covariates (features).
- e.g.)
  1. The training set consists of photos, while the test set contains only cartoons.
     - Training on a dataset with substantially different characteristics from the test set can spell trouble absent a coherent plan for how to adapt to the new domain.
  2. [Medical Diagnostics](#4721-medical-diagnostics) below.
- [Covariate Shift Correction](#4732-covariate-shift-correction)

<br><br>


### 4.7.1.2 Label Shift
- Assumption)
  - The label marginal $P(y)$ can change but the class-conditional distribution $P(\mathbf{x}|y)$ remains fixed across domains.
- Prop.)
  - Label shift is applicable to cases when we believe that $y$ causes $\mathbf{x}$.
- e.g.)
  - Consider the case that we want to predict diagnoses given their symptoms.
  - And the relative prevalence of diagnoses are changing over time.
- [Label Shift Correction](#4733-label-shift-correction)

<br><br>


### 4.7.1.3 Concept Shift
- Assumption)
  - The definitions of labels change.
- e.g.)
  - The distribution of names for soft drinks in the United States.
    - In this case, if we were to build a machine translation system, the distribution $P(y|\mathbf{x})$ might be different depending on our location.
- [Concept Shift Correction](#4734-concept-shift-correction)

<br><br>

## 4.7.2 Examples of Distribution Shift
### 4.7.2.1 Medical Diagnostics
- Situation)
  - You are to develop a **blood test for a disease** that predominantly affects older men and hoped to study it using blood samples that they had collected from patients.
  - You collect data from **healthy** and **sick** people and you train your algorithm.
  - It is more difficult to obtain blood samples from healthy men than from sick patients already in the system.
- Problem)
  - It would \be easy to distinguish between the healthy and sick cohorts with near-perfect accuracy. 
  - However, that is because the test subjects **differed in** age, hormone levels, physical activity, diet, alcohol consumption, and many more **factors unrelated to the disease**.
  - This was unlikely to be the case with real patients. 
  - Due to their sampling procedure, we could expect to encounter extreme [covariate shift](#4711-covariate-shift).

<br>

### 4.7.2.2 Detecting Tanks in the Forest
- Situation)
  - The US Army tried to detect tanks in the forest.
  - They took aerial photographs of the forest without tanks, then drove the tanks into the forest and took another set of pictures.
  - The classifier appeared to work perfectly.
- Problem)
  - Unfortunately, it had merely learned how to distinguish trees with shadows from trees without shadows—the first set of pictures was taken in the early morning, the second set at noon.

<br>

### 4.7.2.3 Nonstationary Distributions
- Desc.)
  - The distribution changes slowly (also known as nonstationary distribution) and the model is not updated adequately.
- e.g.)
  - We train a computational advertising model and then fail to update it frequently (e.g., we forget to incorporate that an obscure new device called an iPad was just launched).
  - We build a spam filter. It works well at detecting all spam that we have seen so far. But then the spammers wise up and craft new messages that look unlike anything we have seen before.
  - We build a product recommendation system. It works throughout the winter but then continues to recommend Santa hats long after Christmas.

<br><br>

## 4.7.3 Corrections of Distribution Shift
### 4.7.3.1 Empirical Risk and Risk
- Problem)
  - Recall our model training process.
  - We iterate over features and associated labels of training data $`\{(\mathbf{x}_1, y_1), \ldots, (\mathbf{x}_n, y_n)\}`$.
  - Then, we update the parameters of a model $`f`$ after every minibatch by minimizing the loss by $`\displaystyle\textrm{minimize}_f \frac{1}{n} \sum_{i=1}^n l(f(\mathbf{x}_i), y_i)`$
    - where $l$ is the loss function measuring how bad the prediction $f(\mathbf{x})$ is given the associated label $y_i$.
  - However, in practice we typically cannot obtain the **entire population of data**. 
  - Thus, empirical risk minimization, which is minimizing the [empirical risk](#concept-empirical-risk) in, is a practical strategy for machine learning, with the hope of approximately minimizing the [risk](#concept-risk).

#### Concept) Risk
- Def.)
  - The expectation of the loss over the entire population of data drawn from their true distribution $p(\mathbf{x},y)$.
    - i.e.) $`\displaystyle E_{p(\mathbf{x}, y)} [l(f(\mathbf{x}), y)] = \int\int l(f(\mathbf{x}), y) p(\mathbf{x}, y) \;d\mathbf{x}dy`$

#### Concept) Empirical Risk
- Def.)
  - An average loss over the training data for approximating the [risk](#concept-risk).

<br>

### 4.7.3.2 Covariate Shift Correction
- Desc.)
  - Suppose we have labeled data $(\mathbf{x}_i, y_i)$.
  - We want to estimate some dependency $P(y|\mathbf{x})$.
  - However, the observations $\mathbf{x}_i$ are drawn from some source distribution $q(\mathbf{x})$.
    - Not the target distribution $p(\mathbf{x})$ we are looking for.
  - Still, the dependency assumption means that the conditional distribution does not change.
    - Thus, $p(y|\mathbf{x})=q(y|\mathbf{x})$
  - Thus, if $p\ne q$, we can correct this as follows.
    - $`\begin{aligned} \int\int l(f(\mathbf{x}), y) p(y \mid \mathbf{x})p(\mathbf{x}) \;d\mathbf{x}dy = \int\int l(f(\mathbf{x}), y) q(y \mid \mathbf{x})q(\mathbf{x})\frac{p(\mathbf{x})}{q(\mathbf{x})} \;d\mathbf{x}dy\end{aligned}`$
      - i.e.)
        - Reweigh each data example by the **ratio** of the probability that it would have been drawn from the correct distribution to that from the wrong one.
        - Ratio : $\displaystyle\beta_i \stackrel{\textrm{def}}{=} \frac{p(\mathbf{x}_i)}{q(\mathbf{x}_i)}$
  - Then, with the weight $\beta_i$, we can train our model using weighted empirical risk minimization:
    - $`\displaystyle\mathop{\mathrm{minimize}}_f \frac{1}{n} \sum_{i=1}^n \beta_i l(f(\mathbf{x}_i), y_i)`$
  - But, we do not know $\beta_i$.
    - Many methods are available
      - e.g.)
        - some fancy operator-theoretic approaches that attempt to recalibrate the expectation operator directly using a minimum-norm or a maximum entropy principle.
      - Note that for any such approach, we need samples drawn from both distributions
        1. The **true** $p$
        2. The one used for generating the training set $q$ (trivially available)
      - Note that we only need features $\mathbf{x}\sim p(\mathbf{x})$.
        - We do not need to access labels $y\sim p(y)$.
    - Use logistic regression.
      - Why?)
        - If it is impossible to distinguish between the two distributions, $p$ and $q$, then it means that the associated instances are equally likely to come from either one of those two distributions.
          - On the other hand, any instances that can be well discriminated should be significantly overweighted or underweighted accordingly.
      - How?)
        - Assumption)
          - For simplicity, assume that we have an equal number of instances from both distributions $p(\mathbf{x})$ and $q(\mathbf{x})$ respectively.
          - Each data example in the target (e.g., test time) distribution had nonzero probability of occurring at training time.
            - cf.) If we find a point where $p(\mathbf{x})\gt 0, q(\mathbf{x})=0$, then $\beta \rightarrow \infty$
        - Settings)
          - $`z= \left\lbrace \begin{array}{ll} 1 & \textrm{if data is drawn from } p \\ -1 & \textrm{else} \end{array} \right.`$
            - $`\displaystyle P(z=1 \mid \mathbf{x}) = \frac{p(\mathbf{x})}{p(\mathbf{x})+q(\mathbf{x})} \textrm{ and hence } \frac{P(z=1 \mid \mathbf{x})}{P(z=-1 \mid \mathbf{x})} = \frac{p(\mathbf{x})}{q(\mathbf{x})}`$
          - Logistic Regression Approach : $`\displaystyle P(z=1 \mid \mathbf{x})=\frac{1}{1+\exp(-h(\mathbf{x}))}`$
            - Then, $`\displaystyle \beta_i = \frac{1/(1 + \exp(-h(\mathbf{x}_i)))}{\exp(-h(\mathbf{x}_i))/(1 + \exp(-h(\mathbf{x}_i)))} = \exp(h(\mathbf{x}_i))`$
        - Training)
          - Suppose we have 
            - $`\{(\mathbf{x}_1, y_1), \cdots, (\mathbf{x}_n, y_n)\}`$ : a training set
              - $`\mathbf{x}_i\sim q, \; 1\le i\le n`$ (i.e. drawn from the source distribution)
            - $`\{\mathbf{u}_1, \cdots, \mathbf{u}_m\}`$ : an unlabeled test set 
              - $`\mathbf{u}_i\sim p, \; 1\le i\le n`$ (i.e. drawn from the target distribution)
          - Procedure)
            1. Create a binary-classification training set:   
              $`\{(\mathbf{x}_1, -1), \ldots, (\mathbf{x}_n, -1), (\mathbf{u}_1, 1), \ldots, (\mathbf{u}_m, 1)\}`$ 
            2. Train a binary classifier using logistic regression to get the function $`h`$.
            3. Weigh training data using $`\beta_i = \exp(h(\mathbf{x}_i))`$ or better $`\beta_i = \min(\exp(h(\mathbf{x}_i)), c)`$ for some constant $`c`$.
            4. Use weights $`\beta_i`$ for training on $`\{(\mathbf{x}_1, y_1), \ldots, (\mathbf{x}_n, y_n)\}`$ in $`\displaystyle\mathop{\mathrm{minimize}}_f \frac{1}{n} \sum_{i=1}^n \beta_i l(f(\mathbf{x}_i), y_i)`$
    
<br><br>

### 4.7.3.3 Label Shift Correction
- Assumptions)
  - Task : A classification task with $k$ categories
  - $q$ : the source distribution
  - $p$ : the target distribution
  - The distribution of labels shifts over time : $q(y) \ne p(y)$
  - The class-conditional distribution stays the same : $`q(\mathbf{x}|y) = p(\mathbf{x}|y)`$
- Problem)
  - The source distribution $q(y)$ is wrong!
- Sol.)
  - We can modify the identity that we derived from the [Covariate Shift Correction](#4732-covariate-shift-correction) above.
    - $`\begin{aligned} \int\int l(f(\mathbf{x}), y) p(\mathbf{x} \mid y)p(y) \;d\mathbf{x}dy = \int\int l(f(\mathbf{x}), y) q(\mathbf{x} \mid y)q(y)\frac{p(y)}{q(y)} \;d\mathbf{x}dy\end{aligned}`$
      - The new ratio : $\displaystyle\beta_i \stackrel{\textrm{def}}{=} \frac{p(y_i)}{q(y_i)}$
  - Now, in order to estimate $\beta_i$, we need to estimate $p(y)$ and $q(y)$.
    1. Estimating $q(y)$
       - Because we observe the labels on the source data, it is easy to estimate the distribution $q(y)$.
    2. Estimating $p(y)$
       - Concept) Confusion Matrix, $\mathbf{C}$
         - Def.)
           - $`\mathbf{C}=\left[ c_{ij} \right] \in \mathbb{R}^{k\times k}`$
             - where
               - $k$ : the number of label categories
               - $c_{ij}$ : the fraction of total predictions on the validation set where the true label was $j$ and our model predicted $i$
         - Prop.)
           - We cannot calculate $\mathbf{C}$ on the target data directly.
             - why?)
               - We cannot see the labels for the examples that we see in the population, unless we implement a complex real-time annotation pipeline.
           - Instead, average all of our model’s predictions at test time together.
           - Yield the mean model outputs $`\mu(\hat{\mathbf{y}}) = \left[ \mu(\hat{y_1}) \; \cdots \; \mu(\hat{y_k}) \right]\in \mathbb{R}^k`$
             - where $\mu(\hat{y_i})$ is the fraction of the total predictions on the test set that our model predicted $i$
       - With the following additional assumptions...
         1. Our classifier was reasonably accurate in the first place
         2. The target data contains only categories that we have seen before.
         3. The label shift assumption holds in the first place.
       - We can estimate the test set label distribution by solving the following linear system.
         - $\mathbf{C} p(\mathbf{y}) = \mu(\hat{\mathbf{y}})$
           - How?)
             - An estimate $`\displaystyle\mu(\hat{y_i}) = \sum_{j=1}^k{c_{ij}p(y_j)}`$ holds for all $i$
               - where $`p(\mathbf{y}) = \left[ p(y_1) \; \cdots \; p(y_k) \right] \in \mathbb{R}^k`$
         - Hence, we can finally get $p(\mathbf{y}) = \mathbf{C}^{-1}\mu(\hat{\mathbf{y}})$
           - cf.) $\mathbf{C}$ is invertible if our classifier is sufficiently accurate.
       - Therefore, estimate $p(\mathbf{y}) = \mathbf{C}^{-1}\mu(\hat{\mathbf{y}})$.
  - With the estimated $\displaystyle\beta_i \stackrel{\textrm{def}}{=} \frac{p(y_i)}{q(y_i)}$, solve the weighted empirical risk minimization problem.
    - $`\displaystyle\mathop{\mathrm{minimize}}_f \frac{1}{n} \sum_{i=1}^n \beta_i l(f(\mathbf{x}_i), y_i)`$




<br><br>

### 4.7.3.4 Concept Shift Correction
- Assumption)
  - [Concept shifts](#4713-concept-shift) take place gradually.
    - e.g.) Real world cases...
      - In computational advertising, new products are launched, old products become less popular. This means that the distribution over ads and their popularity changes gradually and any click-through rate predictor needs to change gradually with it.
      - Traffic camera lenses degrade gradually due to environmental wear, affecting image quality progressively.
      - News content changes gradually (i.e., most of the news remains unchanged but new stories appear).
- Sol.)
  - We can use the same approach that we used for training networks to make them adapt to the change in the data.
    - i.e.) Use the existing network weights and simply perform a few update steps with the new data rather than training from scratch.


<br><br>


## 4.7.4 A Taxonomy of Learning Problems
### 4.7.4.1 Batch Learning
- Training data will be given in a format $`\{(\mathbf{x}_1, y_1), \cdots, (\mathbf{x}_n, y_n)\}`$
- We train a model $f(\mathbf{x})$.
- Then, we deploy this model to score new data $(\mathbf{x},y)$ drawn from the same distribution.
- This is the default assumption for any of the problems that we discuss here. 

<br>

### 4.7.4.2 Online Learning
- Only one sample is provided each time.
  - i.e.) Batches with the sizes of $1$.
- Procedure)
  - At a time period $t$, we have 
    - $f_t$ : our model at $t$.
    - $`(\mathbf{x}_t, y_t)`$ : a sample given
  - Estimate $f_t(\mathbf{x}_t)$.
  - Get loss $`l(y_t, f_t(\mathbf{x}_t))`$.
  - Minimize the loss and update our model into $f_{t+1}$

<br>

### 4.7.4.3 Bandits
- In a **bandit problem** we only have a finite number of arms that we can pull.
  - i.e.) We can take a finite number of actions.
  - cf.) In most learning problems we have a continuously parametrized function $f$ where we want to learn parameters.
- Since the problem is simpler, it guarantees stronger theoretical optimality.
- Bandit problem is often (confusingly) treated as if it were a distinct learning setting.

<br>

### 4.7.4.4 Control
- In many cases the environment remembers what we did.
- This is due to algorithms form a model of the environment in which they act so as to make their decisions appear less random.
  - e.g.) PID (proportional-integral-derivative) controller algorithms
- Recently, control theory (e.g., PID variants) has also been used to automatically tune hyperparameters to achieve better disentangling and reconstruction quality, and improve the diversity of generated text and the reconstruction quality of generated images.
  - *ControlVAE: controllable variational autoencoder* (Shao et al., 2020)


<br>

### 4.7.4.5 Reinforcement Learning
- Environments trying to cooperate with the users.
  - e.g.) Chess, Go, Backgammon, and StarCraft

<br>

### 4.7.4.6 Considering the Environment
- A strategy that might have worked throughout in the case of a stationary environment, might not work throughout in an environment that can adapt.
  - e.g.) An arbitrage opportunity discovered by a trader is likely to disappear once it is exploited.
- In such case, the speed and manner at which the environment changes determines to a large extent the type of algorithms that we can bring to bear.
  - e.g.) If we know that things may only change slowly, we can force any estimate to change only slowly, too.

<br><br>

## 4.7.5 Fairness, Accountability, and Transparency in Machine Learning





<br>

* [Back to Dive into Deep Learning](../../main.md)