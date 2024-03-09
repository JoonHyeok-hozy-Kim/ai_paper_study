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

#### Concept) Approximate Inductive Bias of PROLOG-EBG
- Review)
  - The [inductive bias](../../ch02/07/note.md#def-inductive-bias) of a learning algorithm is a set of assertions that, together with the training examples, deductively entail subsequent predictions made by the learner.
- Desc.)
  - Inductive Bias of PROLOG-EBG
    1. The domain theory $B$
       - Recall that PROLOG-EBG chooses a hypothesis $h$ where 
         - $`(\forall\langle x_i, f(x_i)\rangle\in D) \; (h\wedge x_i)\vdash f(x_i)`$
         - $`D\wedge B \vdash h`$
    2. Sequential Covering Algorithm & The Greedy Method
       - Recall that $h$ has many alternative sets of Horn clauses entailed by the domain theory.
       - PROLOG-EBG has the bias of choosing $h$ among these alternatives.
         1. [Sequential Covering Algorithm](../../ch10/02/note.md#concept-sequential-covering-algorithms)
         2. The Greedy Method by [choosing the one with the weakest preimage](../02/note.md#11212-analyze-the-explanation).
            - i.e.) The most general clause
            - In fact, the greedy algorithm of PROLOG-EBG is only a heuristic **approximation** to the exhaustive search algorithm.
              - Therefore, we can approximately characterize the bias as the **Approximate Inductive Bias of PROLOG-EBG**
  - Approximate Inductive Bias of PROLOG-EBG
    - The domain theory $B$, plus a preference for small sets of maximally general Horn clauses

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

## 11.3.1 Comparison with the Inductive Learning Methods
### 11.3.1.1 Discovering New Features
Comparison with the the inductive derivation of new features in the hidden layer of **neural networks**
- PROLOG-EBG
  - It can formulate **new features** that are not explicit in the description of the training examples, but that are needed to describe the general rule underlying the training example.
    - e.g.) Previous [SafeToStack example](../02/note.md#eg-the-above-safetostack-problem-continues)
  - Source of Information
    - Analysis of single examples using the domain theory
- [Neural Network](../../main.md#4-artificial-neural-networks-anns)
  - Recall that hidden layers could formulate a classifier after training.
  - Source of Information
    - Statistical regularities over many examples

<br>

### 11.3.1.2 Deductive Learning
Comparison with the background knowledge of the ILP
- PROLOG-EBG
  - PROLOG-EBG uses its domain theory $B$ to **reduce** the set of acceptable hypotheses.
    - Why?)
      - It produces $h$ that follows deductively from the domain theory $B$.
        - i.e.) $`\begin{array}{c}
          (\forall\langle x_i, f(x_i)\rangle\in D) (h\wedge x_i)\vdash f(x_i) \\
          D\wedge B\vdash h          
        \end{array}`$
      - The output hypothesis $h$ is further **constrained** so that it must follow from the domain theory and the data.
        - i.e.) Reducing the ambiguity faced by the learner
      - PROLOG-EBG assumes the domain theory $B$ entails the classifications of the instances in the training data.
        - i.e.) $`(\forall\langle x_i, f(x_i)\rangle\in D) (B\wedge x_i)\vdash f(x_i)`$
  - Thus, PROLOG-EBG has a **deductive** learning process.
- [Inductive Logic Program (ILP)](../../ch10/04/note.md#concept-inductive-logic-program-ilp)
  - ILP uses the background knowledge $B'$ to **enlarge** the set of hypotheses to be considered.
    - i.e.) $`(\forall\langle x_i, f(x_i)\rangle\in D) (B'\wedge h\wedge x_i)\vdash f(x_i)`$
  - Thus, ILP is an **inductive** system.

<br><br>

## 11.3.4 Knowledge Level Learning
### Concept) Knowledge Level Learning
- Def.)
  - A Learning method that its learned hypothesis entails predictions that go beyond those entailed by the domain theory.
- Ideation)
  1. Can PROLOG-EBG ever learn a hypothesis that goes beyond the knowledge that is already implicit in the domain theory?
      - No.
        - why?)
          - Recall that $B\vdash h$.
          - Thus, classification entailed by $h$ is also entailed by $B$.
  2. Are analytical or deductive learning methods inherently limited to go beyond $B$?
     - No.
       - Counter Ex.) 
         1. Case when $B\nvdash h$ but $D\wedge B \vdash h$
            - Recall the [deductive learning property of PROLOG-EBG](#11312-deductive-learning) above.
              - e.g.)
                - $B$ contains the assertion that "If $x$ satisfies the target concept, then so will $g(x)$."
                  - Taken alone, this assertion does not entail the classification of any instances.
                  - However, once we observe a positive example, it allows generalizing deductively to other unseen instances.
                  - e.g.)
                    - Suppose $B$ includes the following assertion.   
                      $`\begin{array}{ll}
                       (\forall x) & \textrm{IF } (PlayTennis=Yes) \leftarrow (Humidity=x) \\
                       & \textrm{THEN } (PlayTennis=Yes) \leftarrow (Humidity \le x)
                      \end{array}`$
                    - The domain theory does not entail any conclusions regarding which instances are positive or negative instances of $PlayTennis$.
                    - Then suppose the learner observes a positive example for $(Humidity = 0.3)$ from $D$.
                    - Then $B\wedge D \vdash h$ such that $`(PlayTennis=Yes) \leftarrow (Humidity \le 0.3)`$
                    - Here,  $B\nvdash h$ but $D\wedge B \vdash h$!
            - Prop.)
              - In knowledge-level learning the deductive closure of $B$ is a proper subset of the deductive closure of $B + h$.
                - cf.) Deductive Closure
                  - The set of all predictions entailed by a set of assertions $Y$ is often called the deductive closure of $Y$. 
         2. Determination, *Russell 1989*
            - Concept) Determination
              - Determinations assert that some attribute of the instance is fully **determined** by certain other attributes, **without** specifying the exact nature of the **dependence**.
            - e.g.)
              - Suppose learning the target concept ""people who speak Portuguese."
              - $B$ : "The **language** spoken by a person is determined by their **nationality**."
              - $D$ : "Joe, a 23-year-old left-handed Brazilian, speaks Portuguese" 
                - A positive example
              - Then the learner may generalize with $h$ such that "all Brazilians speak Portuguese."  
                   




<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)