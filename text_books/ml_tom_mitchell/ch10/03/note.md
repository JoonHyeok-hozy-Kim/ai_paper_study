* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 10.3 Learning Rule Sets : Summary

### Analysis) Sequential-Covering Algorithm vs Decision Tree Learning Algorithms (ID3)
#### Review)
  - [Sequential Covering Algorithms](../02/note.md#concept-sequential-covering-algorithms)
    - Learn one rule at a time by...
      1. Removing the covered examples 
      2. Repeating the process on the remaining examples.
    - e.g.) [CN2](../02/note.md#eg-the-cn2-program)
  - [Decision Tree Algorithms](../../ch03/04/note.md#34-the-basic-decision-tree-learning-algorithm)
    - Learn the entire set of disjuncts simultaneously as part of the single search for an acceptable decision tree.
    - We may call them the **simultaneous covering algorithms**.
    - e.g.) [ID3](../../ch03/04/note.md#concept-the-id3-algorithm).

#### Comparison)
1. Choice made at the most primitive steps
    - At each search step...
      - **ID3** chooses among alternative **attributes** by comparing the **partitions** of the data they generate.
      - **CN2** chooses among alternative **attribute-value** pairs, by comparing the **subsets** of data they cover.
2. The number of distinct choices made by the two algorithms in order to learn the same set of rules.
    - The **Sequential Covering Algorithms** make a larger number of independent choices than the **Decision Tree Algorithms**.
    - To learn a set of $n$ rules, each containing $k$ attribute-value tests in their preconditions...
      - **Sequential Covering Algorithms** performs $n \cdot k$ primitive search steps
        - why?) It makes an independent decision to select each precondition of each rule. 
      - **Decision Tree Algorithms** will make many fewer independent choices
        - why?) Each choice of a decision node in the decision tree corresponds to choosing the precondition for the multiple rules associated with that node.
          - i.e.) If the decision node tests an attribute that has $m$ possible values, the choice of the decision node corresponds to choosing a precondition for each of the $m$ corresponding rules.
          - cf.) Refer to the ID3 case below.
    - e.g.) **CN2 vs ID3**
      - Both algorithms are to be used to learn a target concept defined over instances represented by conjunctions of $n$ boolean attributes. 
      - If **ID3** learns a balanced decision tree of depth $d$, it will contain $2^d - 1$ distinct decision nodes, and therefore will have made $2^d - 1$ distinct choices while constructing its output hypothesis.

#### Which one should we prefer?)
- Size of Data)
  - If data is plentiful, choose the **Sequential Covering Algorithm**. 
    - Why?) It may support the larger number of independent decisions required by the algorithm.
      - For the attributes $a,b,c$ with $n_a, n_b, n_c$ values respectively...
        - $"a=a_1"$ vs $\cdots$ vs $"a=a_{n_a}"$ vs $"b=b_1"$ vs $\cdots$ vs $"b=b_{n_b}"$ vs $"c=c_1"$ vs $\cdots$ vs $"c=c_{n_c}"$
  - If data is scarce, choose the **Decision Tree Algorithms**.
    - Why?) The "sharing" of decisions regarding preconditions of different rules may be more effective.
      - For the attributes $a,b,c$ with $n_a, n_b, n_c$ values respectively...
        - $a \textrm{ vs } b \textrm{ vs } c$
- Do different rules test the same attributes?
  - If yes, choose the **Decision Tree Algorithms**.
  - If no, choose the **Sequential Covering Algorithm**. 


<br><br>

### Analysis) Generate-Then-Test vs Example-Driven
- Concept) Generate-Then-Test
  - Desc.)
    - Successor hypotheses are generated based only on the syntax of the hypothesis representation. 
    - The training data is considered only after these candidate hypotheses are generated and is used to choose among the candidates based on their performance over the entire collection of training examples.
  - e.g.) 
    - **Sequential Covering Algorithm**'s learn-one-rule is a **generate-then-test** search through the syntactically legal hypotheses.
  - Advantage)
    - Robust to the noisy data.
      - Why?) Each choice in the search is based on the hypothesis performance over many examples, so that the impact of noisy data is minimized.
- Concept) Example-Driven
  - Desc.)
    - The generation or revision of hypotheses is driven by the analysis of an individual training example.
    - The result is a revised hypothesis designed to correct performance for this single example. 
  - e.g.)
    - [Find-S](../../ch02/04/note.md#24-find-s-finding-a-maximally-specific-hypothesis)
    - [Candidate-Elimination](../../ch02/05/note.md#254-candidate-elimination-learning-algorithm)
    - [AQ](../02/note.md#1022-variations)
    - [CIGOL]() <- To be added!


<br><br>

### Analysis) Whether and how rules are post-pruned?
- Recall that the **Decision Tree Algorithms** utilize [the post-pruning](../../ch03/07/note.md#concept-two-groups-of-approaches-to-avoid-overfitting) technique to avoid the [overfitting](../../ch03/07/note.md#371-avoiding-overfitting-the-data) issue.
- The **Learn-one rule** can also post-prune each rule after it is learned from the training data.
  - How?)
    - Preconditions can be removed from the rule whenever this leads to improved performance over a set of pruning examples distinct from the training examples.


<br><br>

### Analysis) Various Definitions of Rule Performance
#### Concept) Relative Frequency
- Def.)
  - Let 
    - $n$ denote the number of examples the rule matches
    - $n_c$ denote the number of examples that are classified correctly.
  - Then the relative frequency of rule performance is $\frac{n_c}{n}$.
- Usage)
  - [AQ](../02/note.md#1022-variations)

<br>

#### Concept) m-Estimate of Accuracy
- Def.)
  - Let 
    - $n$ denote the number of examples the rule matches
    - $n_c$ denote the number of examples that are classified correctly.
    - $p$ be the prior probability that a randomly drawn example from the entire data set will have the classification assigned by the rule
      - e.g.) e.g., If 12 out of 100 examples have the value predicted by the rule, then $p = 0.12$.
    - $m$ be the weight, or equivalent number of examples for weighting this prior $p$
  - Then the $m$-Estimate of Accuracy is $\frac{n_c+mp}{n+m}$.
- Usage)
  - It is often preferred when data is scarce and the rule must be evaluated based on few examples.
  - *Cestnik and Bratko (1991)*
  - Recall that [the naive Bayes classifier](../../ch06/09/note.md#concept-naive-bayes-classifier) used it [to estimate the probabilities](../../ch06/09/note.md#6911-estimating-probabilities).
- Props.)
  - This accuracy estimate is biased toward the default accuracy expected of the rule.
  - If $m$ increase, a larger number of examples is needed to override the prior assumed accuracy $p$.

<br>

#### Concept) m-Estimate of Accuracy
- Def.)
  - $\displaystyle -\textrm{Entropy}(S)=\sum_{i=1}^c{p_i\log_2{p_i}}$


<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)