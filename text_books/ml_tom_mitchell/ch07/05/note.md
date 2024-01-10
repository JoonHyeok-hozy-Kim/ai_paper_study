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
      |2|$l_1 \wedge \neg l_2 \wedge \mathbf{\neg l_3} \wedge l_4$|$l_1 \wedge \neg l_2 \wedge l_4$|
      |3|$\mathbf{\neg l_1} \wedge \neg l_2 \wedge \neg l_3 \wedge l_4$|$\neg l_2 \wedge l_4$|
      |4|$\neg l_1 \wedge \mathbf{l_2} \wedge \neg l_3 \wedge l_4$|$l_4$|
      |5|$\neg l_1 \wedge l_2 \wedge \neg l_3 \wedge \mathbf{\neg l_4}$|$\emptyset$|

<br><br>

## 7.5.2 Mistake Bound for the Halving Algorithm
- Ideation)
  - Recall the [version space](../../ch02/05/note.md#concept-version-space).
    - i.e.) the subset of $H$ that is consistent with the training examples in $D$.
  - Consider an approach that an algorithm learns by maintaining the version space.
    - e.g.)
      - [List-Then-Eliminate](../../ch02/05/note.md#concept-list-then-elimination-algorithm)
      - [Candidate-Elimination](../../ch02/05/note.md#254-candidate-elimination-learning-algorithm)
  - How do we get the mistake bound for such algorithms?
    - Use voting method!
- Procedure)
  - For each instance $x$, halve the hypotheses in $H$ depending on their predictions.
    - Positive vs Negative
  - Take the majority side, i.e. output the majority's prediction.
    - If the prediction is wrong, discard the majority and take the minority side.
      - MISTAKE!
    - If the prediction is right, discard the minority.
      - NO MISTAKE!
- Analysis)
  - The worst case mistake bound is $\lfloor \log_2 |H| \rfloor$.
    - i.e.) Every majority predictions were wrong!
  - Idealistically, if all the majorities' predictions were right, the mistake count is 0.


<br><br>

## 7.5.3 Optimal Mistake Bounds
- Settings)
  - $A$ : a learning algorithm
  - $c$ : a target concept
  - $M_A(c)$ : the maximum over all possible sequences of training examples of the number of mistakes made by $A$ to **exactly** learn $c$.
  - $C$ : a concept class
    - Assume the hypothesis class $H=C$.
  - For any nonempty concept class $C$, let $M_A(C)\equiv \max_{c\in C} M_A(c)$.
    - cf.)
      - $M_{\textrm{Find-S}}(C) = n+1$
      - $M_{\textrm{Halving}}(C) \le \log_2 |H|$
- Def.)
  - Let $C$ be an arbitrary nonempty concept class. The optimal mistake bound for $C$, denoted $Opt(C)$, is the minimum over all possible learning algorithms $A$ of $M_A(C)$.
    - $Opt(C)\equiv \min_{A \in \lbrace \textrm{Learning Algorithms}\rbrace} M_A(C)$
- Desc.)
  - $Opt(C)$ is the number of mistakes made for the hardest target concept in $C$, using the hardest training sequence, by the best algorithm.
- Prop.)
  - Littlestone (1997)
    - $VC(C) \le Opt(C) \le M_{\textrm{Halving}}(C) \le \log_2 |C|, \forall C$
      - where $VC(C)$ is the [VC dimension](../04/note.md#def-the-vapnik-chervonenkis-dimension) of $C$.
  - $\exists C, VC(C) = Opt(C) = M_{\textrm{Halving}}(C) = \log_2 |C|$
    - e.g.)
      - The powerset $C_P$ of any finite set of instances $X$.
        - $VC(C_P)=|X|=\log_2|C_P|$






<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)