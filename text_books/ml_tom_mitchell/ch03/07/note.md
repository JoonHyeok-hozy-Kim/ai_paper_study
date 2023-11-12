* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 3.7 Issue in Decision Tree Learning
- Issues
  - Determining how deeply to grow the decision tree
  - Handling continuous attributes
  - Choosing an appropriate attribute selection measure
  - Handling training data with missing attribute values
  - Handling attributes with differing costs
  - Improving computational efficiency 

<br>

## 3.7.1 Avoiding Overfitting the Data
#### Def.) Overfit
Given a hypothesis space $H$, a hypothesis $h \in H$ is said to **overfit** the training data if there exists some alternative hypothesis $h' \in H$, such that $h$ has smaller error than $h'$ over the **training examples**, but $h'$ has a smaller error than $h$ over the **entire distribution** of instances.
- e.g.)   
  ![](images/001.png)
  - As the size of the tree increase, the model becomes more complex.
  - And its accuracy over the training data increases.
  - But the accuracy over the test data decreases.
    - It implies that the model's accuracy over the entire population decreases.
    
#### Concept) Possible Reasons for the Overfitting
1. Random Errors and Noise in the training example
2. Coincidental Regularities
   - i.e.) Some attribute happens to partition the examples very well, despite being unrelated to the actual target function.
     - Then, small numbers of examples are associated with leaf nodes.
     - And the model is overfit to the coincidental attribute.

#### Concept) Two Groups of Approaches to Avoid Overfitting
- Groups)
  1. Approaches that stop growing the tree earlier.
     - Thus, it prevents the algorithm to perfectly classify the training data.
  2. Approaches that allow the tree to overfit the data, and then post-prune the tree
- Comparison)
  - Pruning is more successful in practice.
- Props.)
  - The correct tree size must be determined.
    - Why?)
      - For 1, to stop growing.
      - For 2, to stop pruning
    - The solutions are depicted as [below](#tech-how-to-get-the-correct-tree-size).

<br>

#### Tech) How to Get the Correct Tree Size
1. Training and Validation Approach
   - Use a separate set of examples distinct from the training examples to evaluate the utility of post-pruning nodes from the tree.
   - Methodologies)
     - [Reduced-Error Pruning](#3711-reduced-error-pruning)
     - [Rule Post-Pruning](#3712-rule-post-pruning)
2. Use all the available data for training, but apply a **statistical test** to estimate whether expanding (or pruning) a praticular node is likely to produce an improvement beyond the training set.
   - e.g.) Quinlan(1986)
     - Use $\chi^2$ test to estimate whether further expanding a node improve the performance over the entire data set.
3. Use an explicit measure of the complexity for encoding the training examples and the decision tree.

<br>

### 3.7.1.1 Reduced-Error Pruning
- How?)
  - Choose a node.
  - Remove the subtree rooted at that node and make it a leaf node.
  - Assign the node the most common classification of the training examples.
  - If the tree performs no worse than the original over the **validation set**, keep the subtrees pruned.
    - Else, restore the subtrees.
- Effect)
  - Any leaf node added due to [coincidental regularities](#concept-possible-reasons-for-the-overfitting) will be pruned.
    - why?)
      - It is unlikely that the same coincidence repeats in the validation set.
  - In general, pruning prevents the overfitting problem
    ![](images/002.png)
- Prop.)
  - Effective when a large amount of data is available
    - Which is a serious drawback!
    - Data tends to be limited!
    - Alternative Sol.)
      - Involving partitioning the available data several different times in multiple ways. Then average the results.

<br>

### 3.7.1.2 Rule Post-Pruning
- How?)
  1. Infer the decision tree from the training set, growing the tree until the training data is fit 
     - Allow overfitting to occur.
  2. Convert the learned tree into an equivalent set of rules by creating one rule for each path from the root node to a leaf node.
     - Each leaf node has its own rule.
       - We call this **the rule antecedent (or the precondition)**
       - The classification at the leaf node is called **the rule consequent (or postcondition)**
       - e.g.)
         |Tree|Rule|
         |:--:|:--:|
         |![](images/003.png)|![](images/004.png)|
  3. Prune (generalize) each rule by removing any preconditions that result in improving its estimated accuracy.
  4. Sort the pruned rules by their estimated accuracy, and consider them in this sequence when classifying subsequent instances.



<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)