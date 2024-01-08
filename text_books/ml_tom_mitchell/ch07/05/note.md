* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 7.5 The Mistake Bound Model of Learning

### Concept) The Mistake Bound Model
- Desc.)
  - The learner is evaluated by the total number of mistakes it makes before it converges to the correct hypothesis.
  - How to evaluate the performance?
    - Goal)
      - $h(x)=c(x), \forall x$
    - Procedure)
      1. The learner receives a sequence of training examples.
      2. Upon receiving each example $x$, the learner must predict the target value $c(x)$, before it is shown the correct target value by the trainer. 
  - The **total number of mistakes** can be even more important than the **total number of training examples**.

<br>

## 7.5.1 Mistake Bound for the Find-S Algorithm
### Model) The Find-S Algorithm
- [Review Ch.2](../../ch02/04/note.md#concept-find-s-algorithm)
- Settings)
  - $H$ : the hypothesis space consisting of conjunctions of up to $n$ boolean literals $l_1, l_2, \cdots, l_n$ and their negations (e.g. $\neg l_1$)
- Procedure)
  1. Initialize $h$ to the most specific hypothesis : $(l_1 \wedge \neg l_1) \wedge(l_2 \wedge \neg l_2) \wedge\cdots\wedge (l_n \wedge \neg l_n)$
  2. For each positive training instances $x$,
     1. Remove from $h$ any literal that is not satisfied by $x$.
        - i.e.) Generalization
  3. Output $h$

<br>

### Analysis) Bound on the Total Number of Mistakes of the Find-S Algorithm
- Goal)
  - Get the bound on the total number of mistakes that FIND-S will make before exactly learning the target concept $c$.
- Result)
  - At most $n+1$
    - where $n$ is the number of literals.
- Why?)
  - Consider that the initial $h$ had $2n$ terms total.
    - $(l_1 \wedge \neg l_1) \wedge(l_2 \wedge \neg l_2) \wedge\cdots\wedge (l_n \wedge \neg l_n)$
  - Receiving the first positive example, the mistake is inevitable.
    - Find-S will eliminate $n$ terms from the initial hypothesis.
      - $l_i$ or $\neg l_i$ for $i$-th term, $i=1,2,\cdots,n$
  - In the remaining positive training examples, there are at most $n$ literals that can be updated.
    - Worst Case : $n$ mistakes afterwards.
      - $n$ literals are all updated in $n$ subsequent examples.
      - This will be the case when $c(x)=1, \forall x$.
    - Best Case : No mistake afterwards.
      - No literal is updated.
      - This will be the case when $c(x)=1, \exists! x$.
  - Therefore, the upper bound is $n+1$.
- e.g.)
  - Suppose $n=4$.
  - Initial $h$ : $(l_1 \wedge \neg l_1) \wedge(l_2 \wedge \neg l_2) \wedge(l_3 \wedge \neg l_3) \wedge(l_4 \wedge \neg l_4)$
  - Positive Examples)
    - Worst Case)
      |No.|Example|$h$ after update|
      |:-:|:-:|:-:|
      |Init|-|$(l_1 \wedge \neg l_1) \wedge(l_2 \wedge \neg l_2) \wedge(l_3 \wedge \neg l_3) \wedge(l_4 \wedge \neg l_4)$|
      |1|$l_1 \wedge \neg l_2 \wedge l_3 \wedge l_4$|$l_1 \wedge \neg l_2 \wedge l_3 \wedge l_4$|
      |2|$l_1 \wedge \neg l_2 \wedge \neg l_3 \wedge l_4$|$l_1 \wedge \neg l_2 \wedge l_4$|
      |3|$\neg l_1 \wedge \neg l_2 \wedge \neg l_3 \wedge l_4$|$\neg l_2 \wedge l_4$|
      |4|$\neg l_1 \wedge l_2 \wedge \neg l_3 \wedge l_4$|$l_4$|
      |5|$\neg l_1 \wedge l_2 \wedge \neg l_3 \wedge \neg l_4$|$\emptyset$|


<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)