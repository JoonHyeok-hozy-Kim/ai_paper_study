* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 3.5 Hypothesis Space Search in Decision Tree Learning

## Capabilities and limitations of ID3
#### Capabilities)
- ID3 avoids one of the major risks of methods that search incomplete hypothesis spaces.
  - e.g.) Risks...
    - the hypothesis space might not contain the target function.
  - cf.) methods that search incomplete hypothesis spaces
    - e.g.) methods that consider only conjunctive hypotheses
  - why?)
    - ID3's hypothesis space of all decision trees is a complete space of finite discrete-valued functions, relative to the available attributes.
      - i.e.) Every finite discrete-valued function can be represented by some decision tree
- ID3 is robust to training example errors and noises.
  - why?)
    - ID3 uses **all training examples** at each step in the search to make **statistically based decisions** regarding how to refine its current hypothesis.
      - cf.) Find-S and Candidate-Elimination make decisions incrementally based on individual training examples.
  - ID3 can be easily extended to handle noisy training data by modifying its **termination criterion** to accept hypotheses that imperfectly fit the training data.

<br>

#### Limitations)
- ID3 may not explicitly represent all consistent hypotheses.
  - why?)
    - ID3 maintains only a single current hypothesis as it searches through the space of decision trees.
      - cf.) Candidate-Elimination maintained the set of all consistent hypotheses.
  - Thus, ID3 cannot
    1. determine how many alternative decision trees are consistent with the available training data.
    2. pose new instance queries that optimally resolve among these competing hypotheses. 
- ID3 may converge to locally optimal solutions that are not globally optimal.
  - why?)
    - ID3 performs no backtracking in its search.
    - Once it,selects an attribute to test at a particular level in the tree, it never backtracks to reconsider this choice.
  - Sol.) [Post-Pruning the Decision Tree]()





<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)