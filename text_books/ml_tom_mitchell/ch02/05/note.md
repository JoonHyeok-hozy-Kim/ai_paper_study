* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 2.5 Version Spaces and the Candidate-Elimination Algorithm

## Concept) Candidate-Elimination Algorithm
### Ideation)
* Recall that [Find-S Algorithm](../04/note.md#concept-find-s-algorithm) outputs **just one hypothesis** from $H$ that is consistent with the training examples.
* Is there a way to output **all hypothesis** consistent with the training examples?

<br>

### Representation)
#### Def.) Consistency
  * A hypothesis $h$ is consistent with a set of training examples $D$ if and only if $h(x) = c(x)$ for each example $\langle x, c(x) \rangle$ in $D$.
    * $Consistent(h, D) \equiv h(x)=c(x), \forall \langle x, c(x) \rangle$
      * where $c$ is the target concept.
    * i.e.) A hypothesis is consistent with the training examples if it correctly classifies these examples








<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)