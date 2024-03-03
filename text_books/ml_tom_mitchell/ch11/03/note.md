* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 11.3 Remarks on Explanation-Based Learning

#### Props.) PROLOG-EBG
- Unlike inductive methods, PROLOG-EBG produces justified general hypotheses by **using prior knowledge** to analyze individual examples. 
- The explanation of how the example satisfies the target concept determines **which example attributes are relevant**: those mentioned by the explanation. 
- The further analysis of the explanation, regressing the target concept to determine its weakest preimage with respect to the explanation, allows deriving more general constraints on the values of the relevant features. 
- Each learned Horn clause corresponds to a sufficient condition for satisfying the target concept. The set of learned Horn clauses covers the positive training examples encountered by the learner, as well as other instances that share the same explanations. 
- The **generality** of the learned Horn clauses will **depend on** the formulation of the **domain theory** and on the **sequence** in which training examples are considered. 
- PROLOG-EBG implicitly **assumes that the domain theory is correct and complete**. If the domain theory is incorrect or incomplete, the resulting learned concept may also be incorrect.
- Refer to its property as an [Experience-Based Learning](#props-experience-based-learning) method.

<br>

#### Props.) Experience-Based Learning
- EBL as **theory-guided generalization of examples**. 
  - EBL uses its given domain theory to **generalize** rationally from examples, distinguishing the relevant example attributes from the irrelevant, thereby allowing it to avoid the bounds on sample complexity that apply to purely inductive learning. 
  - This is the perspective implicit in the above description of the [PROLOG-EBG](../02/note.md#concept-prolog-ebg) algorithm. 
- EBL as **example-guided reformulation of theories**. 
  - The [PROLOG-EBG](../02/note.md#concept-prolog-ebg) algorithm can be viewed as a method for **reformulating** the domain theory into a more operational form. 
    - In particular, the original domain theory is reformulated by creating rules that...
      1. follow deductively from the domain theory 
      2. classify the observed training examples in a single inference step. 
  - Thus, the learned rules can be seen as a reformulation of the domain theory **into a set of special-case rules** capable of classifying instances of the target concept in a single inference step.
- EBL as "just" **restating what the learner already "knows."**
  - In one sense, the learner in our [SafeToStack example](../02/note.md#eg-explanation-for-safetostack-problem) begins with full knowledge of the ```SafeToStack``` concept. 
    - That is, if its initial domain theory is sufficient to explain any observed training examples, then it is also sufficient to predict their classification in advance. 
    - In what sense, then, does this qualify as learning? 
      - One answer is that in many tasks the **difference between** what one **knows in principle** and what one can **efficiently compute in practice** may be great.
        - In such cases this kind of "knowledge reformulation" can be an important form of learning. 
        - e.g.) 
          - In playing chess, the rules of the game constitute a perfect domain theory, sufficient in principle to play perfect chess. Despite this fact, people still require considerable experience to learn how to play chess well. This is precisely a situation in which a complete, perfect domain theory is already known to the (human) learner, and further learning is "simply" a matter of reformulating this knowledge into a form in which it can be used more effectively to select appropriate moves. 
          - A beginning course in Newtonian physics exhibits the same property-the basic laws of physics are easily stated, but students nevertheless spend a large part of a semester working out the consequences so they have this knowledge in more operational form and need not derive every problem solution from first principles come the final exam. 
  - [PROLOG-EBG](../02/note.md#concept-prolog-ebg) performs this type of reformulation of knowledge-its learned rules map directly from observable instance features to the classification relative to the target concept, in a way that is consistent with the underlying domain theory. 
  - Whereas it may **require many inference steps and considerable search to classify an arbitrary instance using the original domain theory, the learned rules classify the observed instances in a single inference step**.


<br>

## 11.3.1 Discovering New Features







<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)