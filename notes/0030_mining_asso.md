* [Back to Main](../README.md)
---

# Mining Association Rules between Sets of Items in Large Databases
### Rakesh Agrawal, Tomasz Imielinski, and Arun Swami
* [Read Paper](/papers/230926%20mining_asso.pdf)

---

## 1. Introduction
#### Purpose of this paper
1. Introduce the problem of “mining” a large collection of basket data type transactions for [association rules](#eg-association-rule) between sets of items with some minimum specified confidence 
2. Present an efficient algorithm for this purpose.

<br>

#### e.g.) Association Rule
* cf.) [Formal Definition](#concept-association-rule)
* Statement
  * 90% of transactions that purchase bread and butter also purchase milk.
* The **antecedent** of this rule consists of bread and butter
* The **consequent** consists of milk alone. 
* **Confidence** of the rule : The number 90%

<br>

#### Practical Usage Examples
|Query|Usage|
|-----|-----|
|Find all rules that have “Diet Coke” as consequent.|These rules may help plan what the store should do to boost the sale of Diet Coke|
|Find all rules that have “bagels” in the antecedent.|These rules may help determine what products may be impacted if the store discontinues selling bagels|
|Find all rules that have “sausage” in the antecedent and “mustard” in the consequent.|This query can be phrased alternatively as a request for the additional items that have to be sold together with sausage in order to make it highly likely that mustard will also be sold.|
|Find all the rules relating items located on shelves A and B in the store.|These rules may help shelf planning by determining if the sale of items on shelf A is related to the sale of items on shelf B.|
|Find the “best” $k$ rules that have “bagels” in the consequent.|Here, “best” can be formulated in terms of the confidence factors of the rules, or in terms of their support, i.e., the fraction of transactions satisfying the rule.|


<br><br>


## 2. Formal Model
* Setting)
  * $I =\{I_1, I_2, ..., I_m\}$ : a set of binary attributes called items
    * $m$ : the number of items
  * $T$ : a database of transaction
    * $t\in R^m$ : a transaction represented as a binary vector
      * $`t[k]=\left\lbrace\begin{array}{cl}1&if\space bought\space the\space item\space I_k\\0&otherwise\end{array}\right.`$
      * e.g.) 
        * $t = [0\space 1\space 0\space ...\space 1]$
  * $X\subset I$ : a set of items in $I$
  * $t$ satisfies $X$ : For all items $I_k$ in $X$, $t[k]=1$.

<br>

#### Concept) Association Rule
Def.) $X\Rightarrow I_j$
  * Let $I_j$ an item not included in $X$.
  * Then the **association rule** can be denoted as $X\Rightarrow I_j$

<br>

#### Concept) Confidence Factor c
  * The rule of $X\Rightarrow I_j$ can be satisfied in $T$ with the confidence factor $0 \le c \le 1$
  * If and only if at least $c$% of transactions in $T$ that satisfy $X$ also satisfy $I_j$.

<br>

#### Concept) Syntactic Constraints
Restrictions on items that can appear in a rule.
* e.g.) We may be interested only in rules that have a specific item $I_x$ appearing in the consequent, or rules that have a specific item $I_y$ appearing in the antecedent.
* Combinations of the above constraints
are also possible.

<br>

#### Concept) Support Constraints
The number of transactions in $T$ that support a rule.
* Def.) The **support** for a rule 
  * The fraction of transactions in $T$ that satisfy the union of items in the consequent and antecedent of the rule.
* Note) support $\ne$ [confidence](#concept-confidence-factor-c)
  * **confidence** is a measure of the rule’s strength
  * **support** corresponds to statistical significance
    * cf.) We are usually interested only in rules with **support** above some minimum threshold for business reasons.


### 2.1 Problem Decomposition
The problem of rule mining can
be decomposed into two subproblems:
1. Generate all **large itemsets**. 
   * Terms)
     * **large itemsets** : combinations of items that have fractional transaction support above **minsupports**
       * **minsupport** : a certain threshold for support
     * **small itemsets** : all other combinations that do not meet the threshold
   * cf.) [Syntactic constraints](#concept-syntactic-constraints) further constrain the admissible combinations.
     * i.e.) We can focus on a certain consequent $I_x$ and antecedent $I_y$.
2. For a large itemset $Y=I_1I_2\dots I_k\space (k\ge2)$, generate all rules that use items from the set $\{I_1, I_2, \dots , I_k\}$.
   * The antecedents of these rules : $X$
     * $X\subset Y$
     * $X$ has $k-1$ items.
   * The consequents of these rules : $Y-X$
   * A rule : $X\Rightarrow I_j\space |\space c\space$, where $X=I_1I_2\dots I_{j-1}I_{j+1}\dots I_k$
     * How to generate?)
       1. Take the support of $Y$ and divide it by the support of $X$.
       2. If the ratio is greater than $c$ then the rule is satisfied with the confidence factor $c$; otherwise it is not.
     * Props.)
       * If the itemset $Y$ is large, then every subset of $Y$ will also be large.
       * All rules derived from $Y$ must satisfy the support constraint because $Y$ satisfies the support constraint and $Y$ is the union of items in the consequent and antecedent of every such rule.


<br><br>


## 3. Discovering Large Itemsets




---
* [Back to Main](../README.md)