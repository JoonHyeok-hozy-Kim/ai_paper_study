* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 10.5 Learning Sets of First-Order Rules: FOIL

### Concept) FOIL
*Quinlan 1990*
- Algorithm)
  - ```FOIL(target_predicate, predicates, examples)```
    - ```pos = {}```
    - ```neg = {}```
    - ```learned_rules = {}```
    - ```for e in examples```
      - ```if target_predicate(e) is True:```
        - Add ```e``` to ```pos```
      - ```else:```
        - Add ```e``` to ```neg```
    - ```while pos do```
      - *Learn a New Rule*
      - ```new_rule``` $\leftarrow$ the rule that predicts ```target_predicate``` with no preconditions
      - ```new_rule_neg``` $\leftarrow$ ```neg```
      - ```while new_rule_neg do```
        - *Add a new literal to specialize* ```new_rule```.
        - ```candidate_literals``` $\leftarrow$ generate candidates for ```new_rule``` based on ```predicates```
        - ```best_literal``` $`\displaystyle\leftarrow \; {\arg\max}_{L\in candidate\_ literals}`$ ```foil_gain(L, new_rule)```
        - Add ```best_literal``` to preconditions of ```new_rule```
        - ```new_rule_neg``` $\leftarrow$ subset of ```new_rule_neg``` that satisfies ```new_rule``` preconditions
      - Add ```new_rule``` to ```learned_rules```
      - Pop $`\{\textrm{members of } pos \textrm{ covered by } new\_ rule\}`$ from ```pos```
    - Return ```learned_rules```.
- Desc.)
  - ```FOIL```'s outer loop adds a new rule to its disjunctive hypothesis, ```learned_rules```.
    - Each ```new_rule``` generalizes the current disjunctive hypothesis by adding a new disjunct.
      - i.e.) It increases the number of instances that are classified as positive.
      - cf.) It can be seen as a specific-to-general search through the space of hypothesis.
  - ```FOIL```'s inner loop performs a finer-grained search to determine the exact definition of each new rule.
    - [How FOIL generates candidates](#1051-generating-candidate-specializations-in-foil)
    - [```foil_gain``` : How FOIL choose the best literal](#1052-guiding-the-search-in-foil)
    - It searches a second hypothesis space, consisting of conjunctions of literals to find a conjunction that will form the preconditions for the new rule.
      - Recall $(L_1\wedge\cdots\wedge L_n)$ in [the Horn clause](../04/note.md#1041-first-order-horn-clause).
      - It conducts a general-to-specific, hill-climbing search.
- Props.)
  - It employs an approach very similar to [the Sequential Covering](../02/note.md#concept-sequential-covering-algorithms) and [Learn-one-rule](../02/note.md#concept-learn-one-rule) algorithms.

#### Analysis) FOIL vs Sequential Covering and Learn-One-Rule
- Similarities
  - FOIL employs an approach very similar to [the Sequential Covering](../02/note.md#concept-sequential-covering-algorithms) and [Learn-one-rule](../02/note.md#concept-learn-one-rule) algorithms.
    - The hypotheses learned by FOIL are sets of first-order rules, where each rule is similar to a [Horn clause](../04/note.md#1041-first-order-horn-clause) with two exceptions.
      - Exceptions)
        1. The rules learned by FOIL are more restricted than general Horn clauses, because the literals are not permitted to contain [function symbols](../04/note.md#1042-terminology).
        2. FOIL rules are more expressive than Horn clauses, because the literals appearing in the body of the rule may be negated.
  - FOIL's outer loop corresponds to a variant of [the Sequential-Covering algorithm](../02/note.md#concept-sequential-covering-algorithms).
    - Why?)
      - It learns new rules one at a time, removing the positive examples covered by the latest rule before attempting to learn the next rule.
      - But, FOIL seeks only rules that predict when the target literal is $True$
        - whereas [the Sequential-Covering algorithm](../02/note.md#concept-sequential-covering-algorithms) seeks both rules that predict when it is $True$ or $False$.
  - FOIL's inner loop corresponds to a variant of [the Learn-one-rule algorithm](../02/note.md#concept-learn-one-rule).
- Differences
  - In its general-to-specific search to each new rule, FOIL employs different detailed steps to generate candidate specializations of the rule.
  - FOIL employs a performance measure ```foil_gain()``` which differs from [the entropy measure used for Learn-one-rule's general-to-specific beam search](../02/note.md#concept-general-to-specific-beam-search).

<br><br>

## 10.5.1 Generating Candidate Specializations in FOIL
- Settings)
  - Suppose we want to learn the following rule.
    - $P(x_1, \cdots, x_k) \leftarrow L_1 \cdots L_n$
      - where 
        - $L_1 \cdots L_n$ are literals forming the current rule preconditions.
        - $P(x_1, \cdots, x_k)$ is the literal that forms the rule head or prepositions ($\textrm{IF}$).
- Generation)
  - [FOIL](#concept-foil) generates candidate specializations of this rule by considering new literals $L_{n+1}$ that fit one of the following forms.
    1. $Q(v_1, \cdots, v_r)$
       - where 
         - $Q$ is any predicate name occurring in ```predicates```
         - $v_i$ are either new variables or variables already present in the rule.
           - At least one of the $v_i$ in the created literal must already exist as a variable in the rule.
    2. $Equal(x_j, x_k)$
       - where $x_j, x_k$ are variables already present in the rule
    3. The negation of either of the above forms of literals. 
- e.g.)
  - Objective)
    - Learning rules to predict the target literal $GrandDaughter(x,y) \leftarrow$
  - Procedure)
    1. [FOIL](#concept-foil) specialize the initial rule of $GrandDaughter(x,y) \leftarrow$ by generating the following literals as candidate additions to the rule preconditions :
       - $Equal ( x , y ) , Female(x), Female(y), Father(x, y), Father(y, x), Father(x, z), Father(z, x), Father(y, z), Father(z, y)$
         - cf.) $z$ is a new variable where $x,y$ already exists within the rule.
       - And the negations of the above.
         - e.g.) $\neg Equal ( x , y ) ,\neg Female(x), \cdots$
    2. FOIL greedily selects a candidate.
       - Suppose $Father(y,z)$ is chosen.
       - Then a more specific rule is derived : $GrandDaughter(x,y) \leftarrow Father(y,z)$
    3. Again FOIL generates candidates that specialize the current rule $GrandDaughter(x,y) \leftarrow Father(y,z)$.
       - Candidates include...
         - All of the literals from the previous step : $Equal ( x , y ) , Female(x), Female(y),  \cdots$
         - Additional literals and their negations : $Female(z), Equal(z, x), Equal(z, y), Father(z, w), Father(w, z), \neg Female(z), \neg Equal(z, x), \cdots, \neg Father(w, z)$
           - cf.) $w$ is a new variable different from $x,y,z$.
    4. FOIL greedily select literals throughout the following iterations.
       - Suppose, $Father(z, x)$ and $Female(y)$ are chosen in the next two iterations.
       - Then we have $GrandDaughter(x,y) \leftarrow Father(y,z) \wedge Father(z, x) \wedge Female(y)$
    5. Above iteration will terminate when there is no positive example left.

<br><br>

## 10.5.2 Guiding the Search in FOIL
### Concept) FOIL Gain
- Desc.)
  - **FOIL Gain** is the evaluation function used by FOIL to estimate the utility of adding a new literal is based on **the numbers of positive and negative bindings** covered before and after adding the new literal.
    - Recall that FOIL repeatedly [generates candidates for the best specialization literal](#1051-generating-candidate-specializations-in-foil) by adding new literals to the existing rule.
    - After generating the candidates, it evaluates them using the ```foil_gain``` function.
- Notation)
  - Concept) Binding
    - Def.)
      - Assigning constants to variables in a rule
    - How?)
      - Suppose we have a rule $GrandDaughter(x,y) \leftarrow$ and four constants $Victor, Sharon, Bob, \textrm{ and } Tom$
      - Then, the rule has two variables $x$ and $y$, and they can be bound with four constants each.
        - i.e.) 16 possible cases
    - Notation)
      - $`\{x/Victor, y/Sharon\}`$
        - $x,y$ are bound with $Victor, Sharon$ respectively.
- Def.)
  - Let
    - $R$ : a rule
    - $L$ : a candidate literal that might be added to the body of $R$
    - $R'$ : the rule created by adding literal $L$ to rule $R$
    - $p_0$ : the number of positive bindings of rule $R$
    - $n_0$ : the number of negative bindings of $R$
    - $p_1$ : the number of positive bindings of rule $R'$
    - $n_1$ : the number of negative bindings of $R'$
    - $t$ : the number of positive bindings of rule $R$ that are still covered after adding literal $L$ to $R$
  - Then 
    - $`Foil\_Gain(L, R) \equiv t\left(\log_2{\frac{p_1}{p_1+n_1}}-\log_2{\frac{p_0}{p_0+n_0}}\right)`$
- Prop.)
  - $`Foil\_Gain(L, R)`$ can be seen as the reduction due to $L$ in the total number of bits needed to encode the classification of all positive bindings of $R$. 
    - Why?)
      - $`(A) \; -\log_2{\frac{p_0}{p_0+n_0}}`$ is the minimum number of bits needed to encode the classification of an arbitrary positive binding among the bindings covered by rule $R$.
        - Refer to [Entropy and Surprisal (Shannon, 1948)](../../../dive_into_deep_learning/ch04/01/note.md#4131-entropy) for more description.
      - $`(B) \; -\log_2{\frac{p_1}{p_1+n_1}}`$ is the minimum number of bits needed to encode the classification of an arbitrary positive binding among the bindings covered by rule $R'$.
      - Hence, $`(B)-(A) \; \left(\log_2{\frac{p_0}{p_0+n_0}}-\log_2{\frac{p_1}{p_1+n_1}}\right)`$ is the amount of bits reduced by adding $L$ to $R$.

<br><br>

## 10.5.3 Learning Recursive Rule Sets
### Concept) Recursive Rules
- Def.)
  - Rules that use the same predicate in the body and the head of the rule.
- Why does this happens?)
  - Our FOIL may add the ```target_predicate``` to ```predicates```.
  - Then, FOIL will consider it as well when generating candidate literals.
- e.g.)   
  $`\begin{array}{ll}
    \textrm{IF } Parent(x,y) && \textrm{ THEN } Ancestor(x,y) \\ \textrm{IF } Parent(x,z) \wedge Ancestor(z,y) && \textrm{ THEN } Ancestor(x,y)
  \end{array}`$
- Problem)
  - Learning rule sets may produce infinite recursion.
    - Still, whether this particular rule would be learned or not depends on whether these particular literals outscore competing candidates during FOIL'S greedy search for increasingly specific rules. 
- Sol.)
  - *Cameron-Jones and Quinlan (1993)* discuss several examples in which FOIL has successfully discovered recursive rule sets.


<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)