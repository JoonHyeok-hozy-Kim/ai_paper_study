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
    * where $A$ denotes the aggregation

<br>

$y$ can be either a numerical or a class value
* Case 1) $y$ is numerical
  * Use the average of the predictors from $\lbrace L_k \rbrace$ 
  * $\varphi_A(x) = E_L{\varphi (x,L)}$
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
    * Still, bagging works well for unstable procedures.
      * This will be covered in Section 2.


<br><br>

## 2. Bagging Classification Trees
### 2.1 Results for Moderate Sized Data Sets
#### Data used   
![](images/020101.png)

#### Procedures
  1. Dataset is divided into a test set $T$ and a learning set $L$.
     * Real Data : $T$ 10% vs $L$ 90%
     * Simulated Data : $T$ 1500/1800 vs $L$ 300/1800
  2. A classification tree is constructed from $L$ using 10-fold cross-validation.
     * $e_S(L, T)$ : the misclassification rate of running $T$ down this tree.
  3. A bootstrap sample $L_B$ is selected from $L$ and a tree grown using $L_B$
     * $L$ is used as test set to select the best pruned subtree.
       * Repeated 50 times giving tree classifiers : $\phi_1(x), \dots , \phi_{50}(x)$
  4. Class Determination : Calculate the bagging's accuracy.
     * If $(j_n, x_n) \in T$, then the estimated class of $x_n$ is that class having the plurality in $\phi_1(x), \dots , \phi_{50}(x)$.
     * If there is a tie, the estimated class is the one with the lowest class label.
     * $e_B(L, T)$ : the bagging misclassification rate
       * the proportion of times the estimated class differs from the true class.
  5. Repeat ramdomly dividing the data into $L$ and $T$ for 100 times.
     * $\overline{e_S}, \overline{e_B}$ : the averages over the 100 iterations.

#### Result
|Misclassification Rate (%)|Standard Errors of Misclassification|
|:-:|:-:|
|![](images/020102.png)|![](images/020103.png)|
* Analysis
  * Bagging reduces the excess error by about two-thirds
    * $\overline{e_S} \rightarrow \overline{e_B}$
  * Special Case : diabetes data
    * The excess error did not dicrease.
    * Author's expectation
      * Bagging is pushing close to the minimal attainable error rate. 

<br>

### 2.2 Statlog Comparisons for Larger Data Sets
#### The Statlog Project [Michie et al., 1994] 
* Compared 22 classification methods over a wide variety of data sets. 
  * For most of these data sets, error rates were estimated using a single cross-validation. 
    * Without knowing the random subdivisions used in these cross-validations, the variability in the resulting error estimates makes comparisons chancey.
  * Still, four data sets in the project were large enough.
    * Enough to divide them into training and test sets.
    ![](images/020201.png)
* Bagging Application
  * Data division
    * a tree grown on the randomly chosen 90%. 
    * a random 10% of the training set was set aside 
      * Used to select the best pruned subtree. 
  * In bagging, 50 bootstrap replicates of the training set were generated and a large tree grown on each one. 
  * The original training set is used to select the best pruned subtree. 
  * Result   
    ![](images/020202.png)
    * Bagged Trees' rank among the 22 classifiers in the Statlog Project
      * 2nd in accuracy on the DNA dataset
      * 1st in accuracy on the shuttle dataset
      * 2nd in accuracy on the satellite dataset
      * 1st in accuracy on the letters dataset
      * Average Rank : 1.8
        * Way above other classifiers in the project   
          ![](images/020203.png)
---

* [Back to Main](../../README.md)