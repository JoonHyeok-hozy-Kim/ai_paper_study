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
    * $N$ : the size of the data
* $\varphi (x, L)$ : a predictor
  * We want to generate a predictor using the data $x$ and the learning set $L$.
* $\lbrace L_k \rbrace$ : a sequence of learning sets
  * Each $L_k$ consists of $N$ independent observations from the same underlying distributions as $L$.

<br>

#### Our mission
Use $\lbrace L_k \rbrace$ to get a better predictor than the single learning set predictor $\varphi (x, L)$.
* Target Model
  * $\varphi_A(x)$

<br>

$y$ can be either a numerical or a class value
* Case 1) $y$ is numerical
  * Use the average of the predictors from $\lbrace L_k \rbrace$ 
  * $\varphi_A(x) = E_L{\varphi (x,L)}$
    * $A$ : aggregation
    * $E_L$ : expectation over $L$
* Case 2) $y$ is a class value $j \in \lbrace 1, \dots , J \rbrace$
  * Use voting.
  * $\varphi_A(x) = argmax_jN_j$ : $j$ for which $N_j$ is maximum
    * $N_j = nr \lbrace k; \varphi (x, L_k)=j \rbrace$

<br>

#### Bagging (**B**ootstrap **Agg**regat**ing**)
* Why needed?
  * Usually, we have a single leraning set $L$.   
  * But we need $\lbrace L_k \rbrace$ to derive $\varphi_A(x)$.
  * We can form a replicate data sets : $\lbrace L^{(B)} \rbrace$

<br>

$\lbrace L^{(B)} \rbrace$
* Def.)
  * Replicate data sets drawn from the bootstrap distribution approximating the distribution underlying $L$.
* Props.)
  * each consisting of $N$ cases
  * drawn at **random with replacement** from $L$
    * $(y_i, x_i)$ may appear repeated times or not at all
  * See Efron and Tibshirani, "An introduction to the Bootstrap" for the bootstrapping method. 
  * Stability of the procedure for constructing $\varphi$ improves the accuracy of bagging.
    * why?)
      * If changes in $L$ produces small changes in $\varphi$, then $\varphi_B$ will be close to $\varphi$.
    * Still, baggin works well for unstable procedures.
      * This will be covered in Section 2.


<br><br>

## 2. Bagging Classification Trees
### 2.1 Results for Moderate Sized Data Sets


---

* [Back to Main](../../README.md)