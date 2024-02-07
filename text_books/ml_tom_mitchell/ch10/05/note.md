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
      - ```if target_predicate(e) is True```:
        - Add ```e``` to ```pos```
      - ```else```
        - Add ```e``` to ```neg```
    - ```while pos do```
      - *Learn a New Rule*
      - ```new_rule``` $\leftarrow$ the rule that predicts ```target_predicate``` with no preconditions
      - ```new_rule_neg``` $\leftarrow$ ```neg```
      - ```while new_rule_neg do```
        - *Add a new literal to specialize* ```new_rule```.
          - ```candidate_literals``` $\leftarrow$ generate candidates for ```new_rule``` based on ```predicates```
          - ```best_literal``` $`\displaystyle\leftarrow \; {\arg\max}_{L\in candidate\_ literals}foil \_ gain(L, new\_ rule)`$ 
          - Add ```best_literal``` to preconditions of ```new_rule```
          - ```new_rule_neg``` $\leftarrow$ subset of ```new_rule_neg``` that satisfies ```new_rule``` preconditions
      - Add ```new_rule``` to ```learned_rules```
      - Pop $`\{\textrm{members of } pos \textrm{ covered by } new\_ rule\}`$ from ```pos```
    - Return ```learned_rules```.
- Desc.)
  - Each iteration through ```FOIL```'s outer loop adds a new rule to its disjunctive hypothesis, ```learned_rules```
- Props.)
  - It employs an approach very similar to [the Sequential Covering](../02/note.md#concept-sequential-covering-algorithms) and [Learn-one-rule](../02/note.md#concept-learn-one-rule) algorithms.




<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)