* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 3.6 Inductive Bias in Decision Tree Learning
- Recall the concept of [inductive bias](../../ch02/07/note.md#27-inductive-bias).
  - i.e.) the policy by which an algorithm generalizes from observed training examples to classify unseen instances

### Concept) ID3's Inductive Bias
- ID3 has a complex bias.
  - why?)
     - ID3's attribute selection heuristic has subtle interactions. (i.e. complex!)
       1. Select in favor of shorter trees over longer ones.
       2. Select trees that place the attributes with highest information gain closest to the root.
- Let's get closer to the bias with the approximations.
  1. **Approximate Inductive Bias of ID3**
     - Shorter trees are preferred over larger trees.
     - cf.) BFS-ID3
       - Understanding ID3 with the BFS
       - How?
         - BFS-ID3 begins with the empty tree.
         - It searches breadth first through progressively more complex trees.
           - First considering all trees of depth 1
           - Then, all trees of depth2...
         - It returns the smallest consistent tree when it finds a decision tree consistent with the training data
       - Still, ID3 has a more complex bias
  2. **A Closer Approximation to the Inductive Bias of ID3**
     - Shorter trees are preferred over longer trees.
     - Trees that place high information gain attributes close to the root are preferred over those that do not.

<br>

## 3.6.1 Restriction Bias and Preference Bias
### Analysis) Comparison Between ID3 and Candidate-Elimination
| - |ID3|Candidate-Elimination|
|:-:|:--|:--------------------|
|Hypothesis Space|Searches a *complete* hypothesis space|Searches an *incomplete* hypothesis space|
|Searching|Searches *incompletely* from simple to complex hypotheses|Searches *completely* finding every hypothesis consistent with the training data.|
|Inductive Bias|Its inductive bias follows *search strategy*.|Its inductive bias follows from the definition of its *search space*.|
|Additional Bias|Its hypothesis space introduces no additional bias.|Its search strategy introduces no additional bias.|

<br>

#### Concept) Preference Bias (Search Bias)
- Def.)
  - An inductive bias that prefers certain hypotheses over others
- e.g.)
  - ID3

<br>

#### Concept) Restriction Bias (Language Bias)
- Def.)
  - An inductive bias that restricts the category of the set of hypotheses considered.
- e.g.)
  - Candidate-Elimination

<br>

#### Prop.) Preference Bias is more desirable than Restriction Bias
- why?)
  - Preference Bias allows the learner to work within a complete hypothesis space that is assured to contain the unknown target function.
  - Restriction Bias has the possibility of excluding the unknown target function.

<br><br>

## 3.6.2 Why Prefer Short Hypotheses?
- Possible reasons
  1. There are fewer short hypotheses than long ones.
     - e.g.)
       - 20 training examples are given.
       - Suppose a tree with five nodes, and a tree with 500 nodes fit the data.
       - The former will be scarce while the cases like the latter will be abundant.
     - Rebuff)
       1. What if the small sets of hypotheses has short descriptions?
          - e.g.) 17 nodes with 11 non-leaf nodes.
       2. The size of a hypothesis is determined by the particular representation used internally by the learner.
          - i.e.)
            - If two learners use different internal representations respectively, they could arrive at different hypotheses.


<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)