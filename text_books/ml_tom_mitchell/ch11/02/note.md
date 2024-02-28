* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 11.2 Learning with Perfect Domain Theories : PROLOG-EBG

### Concept) Domain Theory
- Props.)
  - Correctness
    - A domain theory is said to be correct if each of its assertions is a **truthful** statement about the world.
  - Completeness
    - A domain theory is said to be complete with respect to a given target concept and instance space, if the domain theory **covers every positive example** in the instance space.
      - i.e.) Every instance that satisfies the target concept can be proven by the domain theory to satisfy it.
      - cf.) Completeness does **NOT** require that the domain theory be able to prove that **negative examples** do not satisfy the target concept.
      - cf.) **PROLOG Convention**
        - Unprovable assertions are assumed to be false.
          - With the **PROLOG Convention**, the definition of completeness includes full coverage of both positive and negative examples by the domain theory.
- Questions)
  1. Is it reasonable to assume that such perfect domain theories are **available** to the learner?
     - There are **limited cases** in which it is feasible to provide a perfect domain theory.
       - e.g.) [Previous Chess Game Example](../01/note.md#eg-chess)
         - We can provide all the legal moves of chess as a domain theory.
     - In many other cases it is unreasonable to assume that a perfect domain theory is available.
       - e.g.) [Previous SafeToStack Problem](../01/note.md#eg-analytical-learning-problem--safetostack)
         - It is difficult to write a perfectly correct and complete theory even for simple actions such as the ```SafeToStack``` problem.
     - Thus, it is more realistic to assume that plausible explanations based on **imperfect domain theories** must be used, rather than exact proofs based on perfect knowledge.
       - This will be covered in [Chapter 12](../../main.md#12-combining-inductive-and-analytical-learning).
  2. If the learner had a perfect domain theory, why would it need to learn?
     - It is difficult to describe a target concept, compared to providing just the perfect domain theory from which the learner can learn the target concept.
       - e.g.) Again the [Previous Chess Game example](../01/note.md#eg-chess).
         - It is easy to write down the legal moves of chess that constitute this domain theory.
         - However, it is extremely difficult to write down the optimal chess-playing strategy.
         - Thus, we should rely on the learner to formulate a useful description of the target concept by examining and generalizing from specific training examples.

<br><br>

### Concept) PROLOG-EBG
*Kedar-Cabelli and McCarty, 1987*
- Desc.)
  - A sequential covering algorithm
    - i.e.) It operates by learning a single Horn clause rule, removing the positive training examples covered by this rule, then iterating this process on the remaining positive examples until no further positive examples remain uncovered.
  - When given a **complete** and **correct** domain theory, PROLOG-EBG is guaranteed to output a hypothesis (set of rules) that is itself correct and that covers the observed positive training examples.
  - For any set of training examples, the hypothesis output by PROLOG-EBG constitutes a set of **logically sufficient** conditions for the target concept, **according to the domain theory**.
  - PROLOG-EBG isa refinement of the EBG algorithm introduced by Mitchell et al. (1986) and is similar to the EGGS algorithm described by DeJong and Mooney (1986).
- Procedure)
  - For each new positive training example that is not covered by a learned Horn clause, it forms a new Horn clause by the following procedure. ([Detailed step-by-step illustration below](#1121-an-illustrative-trace).)
    1. [Explain](#11211-explain-the-training-example) the new positive training example
    2. [Analyze](#11212-analyze-the-explanation) this explanation to determine an appropriate generalization
    3. [Refine](#11213-refine-the-current-hypothesis) the current hypothesis by adding a new Horn clause rule to cover this positive example, as well as other similar instances.
- Algorithm) 
  - ```PROLOG_EBG(target_concept, training_examples, domain_theory):```
    - ```learned_rules``` $\leftarrow$ ```{}```
    - ```pos``` $\leftarrow$ the positive examples from ```training_examples```
    - ```for positive_example in pos```
      - ```if positive_example in learned_rules:```
        - ```continue```
      1. [Explanation](#11211-explain-the-training-example)
         - ```explanation``` $\leftarrow$ an explanation (proof) in terms of the ```domain_theory``` that ```positive_example``` satisfies the ```target_concept```
      2. [Analysis](#11212-analyze-the-explanation)
         - ```sufficient_conditions``` $\leftarrow$ the most **general** set of features of ```positive_example``` sufficient to satisfy the ```target_concept``` according to the ```explanation```
      3. [Refinement](#11213-refine-the-current-hypothesis)
         - ```new_horn_clause``` $\leftarrow$ "```target_concept``` $\leftarrow$ ```sufficient_conditions```"
         - ```learned_rules.add(new_horn_clause)```
    - ```return learned_rules```

<br><br>

## 11.2.1 An Illustrative Trace
### 11.2.1.1 Explain the Training Example
- Objective)
  - Construct an explanation in terms of the domain theory, showing how this positive example satisfies the target concept.
    - Concept) Explanation Satisfying the Target Concept
      - If the domain theory is [correct and complete](#concept-domain-theory), this explanation constitutes a **proof** that the training example satisfies the target concept.
  - When dealing with **imperfect** prior knowledge, the notion of explanation must be extended to allow for **plausible, approximate arguments** rather than perfect proofs. 
- e.g.) [SafeToStack](../01/note.md#eg-analytical-learning-problem--safetostack) Problem   
  ![](images/001.png)
- Prop.)
  - In the case of PROLOG-EBG, the explanation is generated using a backward chaining search as performed by PROLOG. 
    - PROLOG-EBG, like PROLOG, halts once it finds the first valid proof.



<br>

### 11.2.1.2 Analyze the Explanation

<br>
 
### 11.2.1.3 Refine the Current Hypothesis

<br>










<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)