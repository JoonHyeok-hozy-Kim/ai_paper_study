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


### 4.7.1.2 Label Shift
- Assumption)
  - The label marginal $P(y)$ can change but the class-conditional distribution $P(\mathbf{x}|y)$ remains fixed across domains.
- Prop.)
  - Label shift is applicable to cases when we believe that $y$ causes $\mathbf{x}$.
- e.g.)
  - Consider the case that we want to predict diagnoses given their symptoms.
  - And the relative prevalence of diagnoses are changing over time.
- [Label Shift Correction](#4733-label-shift-correction)


### 4.7.1.3 Concept Shift
- Assumption)
  - The definitions of labels change.
- e.g.)
  - The distribution of names for soft drinks in the United States.
    - In this case, if we were to build a machine translation system, the distribution $P(y|\mathbf{x})$ might be different depending on our location.
- [Concept Shift Correction](#4734-concept-shift-correction)

<br><Br>

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
- Assumptions)
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

<br>

### 4.7.3.3 Label Shift Correction

<br>

### 4.7.3.4 Concept Shift Correction





<br>

* [Back to Dive into Deep Learning](../../main.md)