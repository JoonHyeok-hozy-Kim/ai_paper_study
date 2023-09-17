* [Back to Main](../README.md)
---

# Fast Algorithm for Mining Association Rules
### Rakesh Agrawal and Ramakrishnan Srikant
* [Read Paper](../papers/230916%20fast_mining.pdf)

---

## 1. Introduction
#### The Problem of Mining Association Rules over Basket Data
* Setting)
  * $I =\{i_1, i_2, ..., i_m\}$ : a set of literals, or items
  * $T$ : a transaction
  * $D$ : a set of transactions
    * where each transaction $T$ is a set of items s.t. $T \subseteq I$
  * $TID$ : a unique identifier of a transaction
  * $X \subseteq T$ : a transaction $T$ contains $X$, where $X$ is a set of items in $I$    
  
* Association Rule ": $X\Rightarrow Y$
  * Condition : $X\subset I$, $Y\subset I$, and $X\cap Y = \emptyset$
  * **Association Rule with Confidence**
    * Notation
      * $X\Rightarrow Y$ with confidence $c$
    * Meaning
      * $c$% of transaction set in $D$ that contain $X$ also contain $Y$
  * **Association Rule with Support**
    * Notation
      * $X\Rightarrow Y$ has support $s$
    * Meaning
      * $s$% of transactions in $D$ contain $X\cup Y$

<br>

#### The Problem of Mining Association Rules
* Goal)
  * Generate all association rules that have support and confidence greater than the user-specified *minimum support (minsup)* and *minimum confidence (minconf)* respectively.
* Prop.)
  * The problem in neutral with respect to the representation of $D$.
    * $D$ can be either a data file, a relational table, or the result of a relational expression.

<br>

### 1.1 Problem Decomposition and Paper Organization
* Subproblems of the problem of discovering all association rules
  1. Find all sets of items that have transaction *support* above minimum support.
     * the *support* for an item set
       * the number of transactions that contain the item set.
     * *large item set*
       * an item set with minimum support
     * *small item set*
       * ~ *large item set*
  2. Use the large item sets to generate the desired rules.
     * Algorithm
       * For every large item set $l$, find all non-empty subsets of $l$.
       * For every such subset $a$, output a rule of the form $a\Rightarrow (l-a)$ if the ratio of support($l$) to support($a$) is at least [minconf]().





---
* [Back to Main](../README.md)