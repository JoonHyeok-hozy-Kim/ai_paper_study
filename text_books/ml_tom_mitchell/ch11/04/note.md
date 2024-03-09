* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 11.4 Explanation-Based Learning of Search Control Knowledge
Applying [Explanation-Based Learning](../01/note.md#concept-explanation-based-learning-ebl) to speeding up search problems.

<br>

### Concept) Applying EBL to Searching Problems
- Desc.)
  - Recall that the requirement of the [Explanation-Based Learning](../01/note.md#concept-explanation-based-learning-ebl) was that the domain knowledge should be [correct and complete](../02/note.md#concept-domain-theory).
  - Complex search problems easily satisfy this requirement.
  - EBL can be used to speed-up such complex search problems.
- e.g.)
  - Scheduling and optimization problems
    - Task) Find some move toward the goal state
      - In such problems the definitions of the **legal search operators**, together with the definition of the **search objective**, provide a complete and correct domain theory for learning search control knowledge.
    - Problem Structure)
      - $S$ : the set of possible search states
      - $O$ : a set of legal search operators that transform one search state into another
      - $G$ : a predicate defined over $S$ that indicates which states are goal states
      - Problem)
        - Find a sequence of operators from $O$ that will transform an arbitrary initial state $s_i$ to some final state $s_f$.
          - where $s_i, s_f \in S$
      - Sol.)
        - Formulate the problem by separating the target concept of each $o\in O$.
          - i.e.) Learn the target concept "the set of states for which $o$ leads toward a goal state."
        - Then the exact choice of which target concepts to learn depends on the internal structure of problem solver that must use this learned knowledge.
          - e.g.) Means-Ends Planning System
            - It works by establishing and solving **subgoals**.
            - Learn "the set of planning states in which subgoals of type $A$ should be solved **before** subgoals of type $B$." 
              - e.g.) [PRODIGY](#eg-prodigy), [SOAR](#eg-soar)
- Limitations)
  - Many or most heuristic search programs still use [numerical evaluation functions similar to the one described in Chapter 1](../../ch01/02/note.md#123-choosing-a-representation-for-the-target-function), rather than rules acquired by explanation-based learning.
    - why?)
      - In many cases the number of control rules that must be learned is very **large**.
        - As the system learns more and more control rules to improve its search, **it must pay a larger and larger cost** at each step to match this set of rules against the current search state.
        - Efficient algorithms for matching rules can **alleviate** this problem, but **not eliminate** it completely.
          - cf.) Empirically estimating the computational cost and benefit of each rule, *Minton 1988*
            - Desc.)
              - Learn rules only when the estimated benefits outweigh the estimated costs.
              - Delete rules later found to have negative utility
      - In many cases it is intractable even to construct the explanations for the desired target concept.
        - e.g.) 
          - In chess we might wish to learn a target concept such as "states for which operator $A$ leads toward the optimal solution." 
          - Unfortunately, to prove or explain why A leads toward the optimal solution **requires explaining that every alternative operator leads to a less optimal outcome**. 
          - This typically requires effort **exponential** in the search depth.
        - Sol.)
          - Lazy or Incremental Explanation, *Chien (1993) and Tadepalli (1990)*
            - Desc.)
              - Heuristics are used to produce partial and approximate, but tractable, explanations.
              - Rules are extracted from these **imperfect explanations** as though the explanations were perfect.
              - Of course these learned rules may be **incorrect** due to the **incomplete explanations**.
              - The system accommodates this by **monitoring the performance of the rule** on subsequent cases.
              - If the rule subsequently makes an error, then the original explanation is incrementally elaborated to cover the new case, and a more refined rule is extracted from this incrementally improved explanation.



### E.g.) PRODIGY
 *Carbonell et al. 1990*
- Desc.)
  - PRODIGY is a domain-independent planning system that accepts the definition of a problem domain in terms of the state space $S$ and operators $O$.
  - It then solves problems of the form "find a **sequence** of operators that leads from initial state $s_i$ to a state that satisfies goal predicate $G$."
  - Thus, during its search for problem solutions PRODIGY repeatedly faces questions such as "Which subgoal should be solved next?'and "Which operator should be considered for solving this subgoal?' 
- e.g.)
  - A simple block-stack problem    
    - Objective)
      - Stack the blocks so that they spell the word "universal."
    - Target Concept)   
      $`\begin{array}{ll}
        \textrm{IF } & \textrm{One subgoal is to solve } On(x,y) \wedge \textrm{One subgoal is to   solve } On(y,z)\\
        \textrm{THEN } & \textrm{Solve the subgoal } On(y,z) \textrm{ before } On(x,y) \\
      \end{array}`$
    - Sol.)
      - PRODIGY would decompose this problem into several subgoals to be achieved.
        - e.g.) $On(U,N), On(N,I), On(I,V), \cdots, On(S,E)$.
      - Then it may encounter a conflict as follows.
        - It must undo the solution to the $On(U, N)$ subgoal in order to achieve the other subgoal $On(N, I)$.
      - PRODIGY explains to itself the reason for this conflict and creating a rule such as the one above.
        - The net effect is that PRODIGY uses domain-independent knowledge about possible subgoal conflicts, together with domain-specific knowledge of specific operators , to learn useful domain-specific planning rules such as the one illustrated above.

<br><br>


### E.g.) SOAR
*Laird et al. 1986; Newel1 1990*
- Desc.)
  - SOAR supports a broad variety of problem-solving strategies that subsumes [PRODIGY](#eg-prodigy)'S means-ends planning strategy.
  - Like PRODIGY, SOAR learns by **explaining** situations in which its current search strategy leads to **inefficiencies**. 
    - When it encounters a search choice for which it does not have a definite answer (e.g., which operator to apply next) SOAR reflects on this search impasse, using weak methods such as generate-and-test to determine the correct course of action. 
    - The reasoning used to resolve this impasse can be interpreted as an explanation for how to resolve similar impasses in the future. 
  - SOAR uses a variant of explanation-based learning called **chunking** to extract the general conditions under which the same explanation applies.


<br><br>




<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)