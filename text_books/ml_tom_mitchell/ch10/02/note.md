* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 10.2 Sequential Covering Algorithms

### Concept) First-Order Rule
- e.g.) A set of two first-order rules
  - $`\begin{array}{ll}
    \textrm{IF } Parent(x,y) & \textrm{ THEN } Ancestor(x,y) \\
    \textrm{IF } Parent(x,z) \wedge Ancestor(z,y) & \textrm{ THEN } Ancestor(x,y) \\
    \end{array}`$
    - Desc.)
      - Two rules are jointly describing the target concept $Ancestor$.
      - They are illustrating a recursive function structure.
- cf.)
  - First-order rules are much more expressive than propositional rules.

<br><br>

### Concept) Sequential Covering Algorithms
- Def.)
  - A family of algorithms that learn rule sets based on the following strategy.
    - Iteratively invoke the following two processes until no training example remains.
      1. **Learn-one-rule**.
         - How?)
           - Input : A set of positive/negative training examples
           - Output : A single rule that covers many of the positive examples and few of the negative examples.
             - High accuracy is required.
               - i.e.) Predictions should be CORRECT!
             - Low coverage is fine.
               - i.e.) The rule need NOT make predictions for every training examples.
      2. Remove the data it covers.
         - How?)
           - By the previous **Learn-one-rule** process, we obtained a rule.
           - Now, remove any positive examples covered by the previous rule.
    - The final set of rules are sorted by the accuracy.
- Prop.)
  - It reduces the problem of learning a disjunctive set of rules to a sequence of simpler problems, each requiring that a single conjunctive rule be learned.
  - It is not guaranteed to find the smallest or best set of rules that cover the training examples.
    - Why?) It performs a greedy search, formulating a sequence of rules without backtracking.
- Algorithm
  - ```sequential_covering(target_attribute, attributes, examples, threshold)```
    - ```learned_rules``` $\leftarrow$ ```{}```
    - ```rule``` $\leftarrow$ ```learn_one_rule(target_attribute, attributes, examples)```
    - ```while performance(rule, examples)``` > ```threshold do...```
      - ```learned_rules``` $\leftarrow$ ```learned_rules``` + ```rule```
      - ```examples``` $\leftarrow$ ```examples``` - ```{examples correctly classified by rule}```
      - ```rule``` $\leftarrow$ ```learn_one_rule(target_attribute, attributes, examples)```
    - Sort ```learned_rules``` by ```performance(rule, examples)``` for each ```rule```
    - Return ```learned_rules```

<br><br>

## 10.2.1 General to Specific Beam Search
### Concept) General to Specific Search
- Desc.)
  - Organize the hypothesis space search in the same general fashion as the [ID3 algorithm](../../ch03/04/note.md#concept-the-id3-algorithm).
  - Follow **only** the most promising branch in the tree at each step.
    - **Differ from ID3** which grew a subtree that covers all possible values of the selected attribute.
    - What is the most promising branch?)
      - A rule with the best performance.
      - The performance measure may vary by the implementation
        - e.g.)
          - One with the lowest [entropy](../../ch03/04/note.md#concept-entropy). 
            - Or the highest [information gain](../../ch03/04/note.md#concept-information-gain)
            - Used in ID3.
  - e.g.)   
    ![](images/001.png)
- Prop.)
  - Greedy DFS approach!
    - There is a danger that a suboptimal choice will be made at any step.
      - Sol.) [Beam Search](#concept-general-to-specific-beam-search) below

<br><br>

### Concept) General to Specific Beam Search
- Desc.)
  - A search in which the algorithm maintains a list of **the k best candidates** at each step, rather than a single best candidate.
  - How?)
    - On each search step, descendants (specializations) are generated for each of these k best candidates.
    - The resulting set is again reduced to the k most promising members.
- e.g.)
  - An algorithm used in [the CN2 program](#eg-the-cn2-program) below.

<br>

#### E.g.) The CN2 Program
*Clark and Niblett 1989*
- Desc.)
  - The CN2 Program used the an [General to Specific Beam Search](#concept-general-to-specific-beam-search) approach.
- Algorithm)
  - ```entropy(examples, target_attribute)```
    - Return the entropy w.r.t. target_attribute
  - ```performance(h, examples, target_attribute)```
    - ```h_examples``` $\leftarrow$ the subset of ```examples``` that match ```h```
    - Return ```entropy(h_examples)```
  - ```learn_one_rule(target_attribute, attributes, examples, k)```
    - ```best_hypothesis``` $\leftarrow \emptyset$
    - ```candidate_hypotheses``` $\leftarrow$ ```{best_hypothesis}```
    - ```while``` ```candidate_hypotheses``` is not empty ```do```
      1. Generate the next more specific ```candidate_hypothesis```.
         - ```all_constraints``` $\leftarrow$ the set of all constraints of the form $a=v$ 
           - where $a$ is a member of ```attributes```
           - and $v$ is a value of a that occurs in the current set of ```examples```
         - ```new_candidate_hypotheses``` $\leftarrow \emptyset$
         - ```for``` ```h``` in  ```candidate_hypothesis``` ```do```
           - ```for``` ```c``` in  ```all_constraints``` ```do```
             - Create a specialization of ```h``` by adding the constraint ```c``` and add to ```new_candidate_hypotheses```.
         - Remove from ```new_candidate_hypotheses``` any hypotheses that are duplicates, inconsistent, or not maximally specific.
      2. Update ```best_hypothesis```.
         - ```for``` ```h``` in ```new_candidate_hypotheses``` ```do```
           - ```if``` ```performance(h, examples, target_attribute)``` > ```performance(best_hypothesis, examples, target_attribute)```
             - ```best_hypothesis``` $\leftarrow$ ```h```
      3. Update ```candidate_hypotheses```.
         - ```candidate_hypotheses``` $\leftarrow$ the ```k``` best members of ```new_candidate_hypotheses``` sorted by ```performance()```
    - Return a rule of the form
      - "IF ```best_hypothesis``` THEN ```prediction```"
        - where ```prediction``` is the most frequent value of ```target_attribute``` among those ```examples``` that match ```best_hypothesis```.
- Remarks)
  - Each hypothesis considered in the main loop of the algorithm is a **conjunction** of attribute-value constraints.
    - Each of these conjunctive hypotheses...
      1. corresponds to a candidate set of preconditions for the rule to be learned 
      2. is evaluated by the entropy of the examples it covers.
  - The postcondition for the output rule is chosen only in the final step of the algorithm, after its precondition (represented by the variable ```best_hypothesis```) has been determined.
    - The algorithm constructs the rule postcondition to predict the value of the target attribute that is **most common** among the examples covered by the rule precondition.
  - Despite the use of beam search to reduce the risk, the greedy search may still produce suboptimal rules.

<br><br>

## 10.2.2 Variations
1. The program learn only rules that cover positive examples and to include a "default" that assigns a negative classification to instances not covered by any rule.
   - Desc.)
     - This approach might be desirable if the fraction of positive examples in the entire population is small.
       - Then, the rule set will be more compact and intelligible to humans if it identifies only classes of positive examples, with the default classification of all other examples as negative.
       - e.g.) Learning a target concept such as "pregnant women who are likely to have twins."
       - cf.) Corresponds to the Negation-As-Failure strategy of PROLOG
         - where any expression that cannot be proven to be true is by default assumed to be false.
   - How to implement?)
     - The ```learn_one_rule()``` algorithm can be modified to accept an additional input argument specifying the target value of interest. 
     - The general-to-specific beam search is conducted just as before, changing only the ```performance()``` subroutine that evaluates hypotheses.
       - The definition of ```performance()``` as negative entropy is no longer appropriate in this new setting
         - why?) It assigns a maximal score to hypotheses that cover exclusively negative examples, as well as those that cover exclusively positive examples.
       - Using a measure that evaluates the fraction of positive examples covered by the hypothesis would be more appropriate in this case. 
2. AQ, *Michalski (1969), Michalski et al. (1986)*
   - Desc.)
     - Like CN2, AQ learns a disjunctive set of rules that together cover the target function.
     - However, AQ differs in several ways...
       1. the covering algorithm of AQ differs from [the Sequential Covering Algorithms](#concept-sequential-covering-algorithms) because it explicitly seeks rules that cover a particular target value, learning a disjunctive set of rules for each target value in turn. 
       2. AQ's algorithm for learning a single rule differs from ```learn_one_rule()```. 
          - While it conducts a general-to-specific beam search for each rule, it uses a single positive example to focus this search. 
          - In particular, it considers only those attributes satisfied by the positive example as it searches for progressively more specific hypotheses. 
          - Each time it learns a new rule, it selects a new positive example from those that are not yet covered, to act as a seed to guide the search for this new disjunct. 



# ADD 10.3 TO 10.2!

<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)