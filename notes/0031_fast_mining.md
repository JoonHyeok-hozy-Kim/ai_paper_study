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
  
* Association Rule : $X\Rightarrow Y$
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
       * For every such subset $a$, output a rule of the form $a\Rightarrow (l-a)$ if the ratio of support($l$) to support($a$) is at least [minconf](#the-problem-of-mining-association-rules).

<br><br>

## 2. Discovering Large Itemsets
#### Preivious Algorithms for Discovering Large Itemsets
* Algorithms
  * AIS
  * SETM
* Props.)
  * Make multiple passes over the data
    * First Pass
      * Count the support of individual items.
      * Determine which of them are [large (having minium support)](#11-problem-decomposition-and-paper-organization) .
    * Subsequent Passes
      * Start with a seed of itemsets found to be large in the previous pass.
      * Generate candidate itemset, a potentially large itemset, from that seed.
      * Count the actual support for these candidate itemsets during the pass over the data
      * Determine which candidate itemsets are actually large.
        * If a large one exists, it becomes the seed for the next pass
    * Continue until no new large itemset is found.

<br>

#### Preview) [Apriori](#21-algorithm-apriori) and [AprioriTid](#22-algorithm-aprioritid) Algorithm
* Prop.)
  * Candidate itemsets are counted in a pass and in a way that those candidates are generated.
  * **(AprioryTid only)** An encoding of the candidate itemsets used in the previous pass is employed for counting the support of candidate itemsets after the first pass.
* Analysis)
  * Distinctive Feature from from [AIS and SETM](#preivious-algorithms-for-discovering-large-itemsets)
    * Generating and counting the itemsets are operated separately.
    * Thus, unnecessarily generates and counts too many candidate itemsets.
      * Why) 
        * Perform recursive algorithm for every itemset that it generates
        * Most of them turn out to be small, not large.
  * Intuition)
    * Any subset of a large itemset must be large.
  * Implementation)
    * Generate itemsets with $k$ items by joining itemsets with $k-1$ items.
    * Delete those that contain any subset that is not large.
  * Advantage)
    * Much smaller number of candidate itemsets are generated.

<br>

#### Assumptions & Notations
* Items in each transaction are kept sorted in the lexicographic order.
* The database $D$ is kept normalized and each database record is a **<TID, item>** pair.
  * **TID** : The identifier of the corresponding transaction
* size : the number of items in an itemset
* $k$-itemset : an itemset of size $k$
* $c[1] \cdot c[2] \cdot ... \cdot c[k]$ : items sorted lexicographically in a $k$-itemset.
  * $c[1] \lt c[2] \lt ... \lt c[k]$ : Due to the lexicographic sorting
* $m$-extension of $X$:
  * $c=X\cdot Y$ and $Y$ is an $m$-itemset
* A count field to store the support for an itemset   
  * Initialized to zero when the itemset is first created.   

![](../images/003_fast_mining/02_01_01.png)
* $\bar{C_k}$ will be used for [AprioriTid](#22-algorithm-aprioritid)

<br><br>

### 2.1 Algorithm Apriori
#### Algorithm
```
L[1] = {large 1-itemsets};       -- first pass

for (k=2; L[k-2]!=∅; k++) do     -- subsequent k-passes
  begin
    Ck = apriori-gen(L[k-1]);    -- New candidates
    for t in D do
      begin
        Ct = subset(Ck, t);      -- Candidates contained in t
        for c in Ct do
          c.count++;
      end
    L[k] = {c in Ck | c.count >= minsupport}
  end

result = union(L[k])
```
* Description
  * The first pass of the algorithm counts item occurrences to determine the large 1-itemsets.
  * Subsequent passes consists of two phases
    * Let the pass be $k$-th pass.
    * Then,
      1. Use [the apriori-gen function]() to generate candidate itemsets $C_k$ using large itemsets $L_{k-1}$ found in the $(k-1)$-th pass.
         * Use [the subset function]() to efficiently determine the candidates for $C_k$
      2. Scan the database and count the support of candidates in $C_k$.
    
<br>

#### 2.1.1 Apriori Candidate Generation
* Apriori-gen Function
  * Input
    * $L_{k-1}$ : the set of all large $(k-1)$-itemsets
  * Output
    * A superset of the set of all large $k$-itemsets.
  * Steps
    1. **Join Step** : Join $L_{k-1}$ with $L_{k-1}$.
       ```
       INSERT INTO Ck
       SELECT p.item_1_, p.item_2_, ..., p.item_k-1_, q.item_k-1_
       FROM   L_k-1_  p
             ,L_k-1_  q
       WHERE p.item_1_ = q.item_1_
       AND   ...
       AND   p.item_k-2_ = q.item_k-2_
       AND   p.item_k-1_ < q.item_k-1     -- guarantees that no duplicate is generated!
       ```
    2. **Prune Step** : Delete all itemsets $c \in C_k$ such that some $(k-1)$-subset of $c$ is not in $L_{k-1}$.
       ```
       for c in Ck do   -- c : candidate itemsets
        for s in c do   -- s : (k-1)-subsets of c
          if (s not in L_k-1_) then
            DELETE c from Ck;
       ```
  * Examples
    * Let $L_3$ be {{1 2 3}, {1 2 4}, {1 3 4}, {1 3 5}, {2 3 4}}.
    * Then, $apriori \_ gen(L_3) = \{ \{ 1 2 3 4 \} \}$
      * why?)
        * After the join step, $C_4$ will be {{1 2 3 4}, {1 3 4 5}}.
        * The prune step will delete {1 3 4 5}.
          * why?) {1 4 5} $\notin L_3$.
        * Thus, {1 2 3 4} will be returned.
  * Proof
    * $C_k \supe L_k$
      * Any subset of a large itemset must also have minimum support.
      * Then we did the join and prune step.
        * Join : Extend $L_{k-1}$ with items in $L_{k-1}$
        * Prune : Delete all itemsets which $(k-1)$-subset is not in $L_{k-1}$
      * Thus, $L_k$ is left with the superset of the itemsets in $L_k$
  * Analysis
    * Comparison with AIS and SETM
      * Apriori is way efficient.
      * Example
        * Suppose AIS and SETM are at $L_3$ state and about to extend to $L_4$
        * Then, they will extend {1 2 3} to {1 2 3 4} and {1 2 3 5} first and then calculate the support.
        * They will repeat this for {1 2 4}, {1 3 4}, {1 3 5}, {2 3 4} again.
          * Redundant!




<br><br>

### 2.2 Algorithm AprioriTid



---
* [Back to Main](../README.md)