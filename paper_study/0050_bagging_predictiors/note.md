* [Back to Main](../../README.md)
---

# Bagging Predictors
### Leo Breiman
* [Read Paper](../paper_pdfs/231015%20bagging_predictors.pdf)

---
## 0. Abstract
* Objective
  * Generate an accurate predictor
* How?
  * Generate multiple predictors using the bagging predictors method.
    * Make bootstrap replicates of the learning set
    * Use these learning sets

<br><br>

## Intoduction
### The Model
#### Settings
* $L$ : a learning set
  * Consists of data $\lbrace (y_n,x_n), n=1,\dots , N\rbrace$
    * where $y$ is either a class label or a numerical response.
* $\varphi (x, L)$ : a predictor
  * We want to generate a predictor using the data $x$ and the learning set $L$.
* $\lbrace L_k \rbrace$ : a sequence of learning sets
  * Each $L_k$ consists of $N$ independent observations from the same underlying distributions as $L$.

<br>

#### Our mission
Use $\lbrace L_K \rbrace$ to get a better predictor than the single learning set predictor $\varphi (x, L)$.

* Predictor notation depending on the data type
  * $y$ can be either a numerical or a class value
    * Case 1 : $y$ is numerical
      * Use the average of the predictors from $\lbrace L_K \rbrace$ 
      * $\varphi_A(x) = E_L{\varphi (x,L)}$
        * $A$ : aggregation
        * $E_L$ : expectation over $L$
    * Case 2 : $y$ is a class value $j \in \{ 1, \dots , J \}$
      * Use voting.
      * $\varphi_A(x) = argmax_jN_j$ : $j$ for which $N_j$ is maximum
        * $N_j = nr \{ k; \varphi (x, L_k)=j \}$
<br>

#### Data Type : Numerical vs. Classification
$y$ can be either a numerical or a class value.
* Case1) $y$ is numerical
  * 


---

* [Back to Main](../../README.md)