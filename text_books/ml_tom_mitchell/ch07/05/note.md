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


<br><br>

## 7.5.4 Weighted-Majority Algorithm
### Concept) Weighted-Majority Algorithm
- Desc.)
  - A generalization of [the Halving algorithm](#752-mistake-bound-for-the-halving-algorithm)
  - It makes predictions by taking a **weighted vote** among a pool of prediction algorithms and learns by altering the weight associated with each prediction algorithm.
- Prop.)
  - It is able to accommodate **inconsistent** training data.
    - How?)
      - It **reduces the weight** of a hypothesis that is found to be inconsistent.
        - NOT eliminating it.
  - We can bound the number of mistakes made by Weighted-Majority in terms of the number of mistakes committed by the best of the pool of prediction algorithms.
- Def.)
  - Settings)
    - $a_i$ be the $i$-th prediction algorithm in the pool $A$ of algorithms.
    - $w_i$ be  the weight associated with $a_i$.
    - $0 \lt\beta \lt 1$
  - Procedure)
    1. For all $i$, initialize $w_i \leftarrow 1$.
    2. For each training example $\langle x, c(x) \rangle$...
       1. Initialize $q_0 \leftarrow 0$ and $q_1 \leftarrow 0$.
          - cf.) $q_0$ is the vote count of the false and $q_1$ is the vote count of the true.
       2. For each prediction algorithm $a_i$...
          1. If $a_i(x) = 0$ then $q_0, \leftarrow q_0+w_i$
             - Else, $q_1, \leftarrow q_1+w_i$
       3. If $q_1 \gt q_0$, then predict $c(x)=1$.
          - Else if $q_1 \lt q_0$, then predict $c(x)=0$.
          - Else, predict 0 or 1 at random for $c(x)$.
       4. For each prediction algorithm $a_i \in A$ do...
          1. If $a_i(x) \ne c(x)$, then $w_i \leftarrow \beta w_i$

<br>

#### Theorem) Relative mistake bound for Weighted-Majority
- Theorem)
  - Let 
    - $D$ be any sequence of training examples
    - $A$ be any set of $n$ prediction algorithms
    - $k$ be the minimum number of mistakes made by any algorithm in $A$ for the training sequence $D$. 
  - Then the number of mistakes over $D$ made by the Weighted-Majority algorithm using $\beta = \frac{1}{2}$ is at most
    - $${\color{red}(\textrm{Verification Required!})}$$
    - The book says, $2.4(k+\log_2 n)$
    - In my opinion, it's $(k+\log_2 n)$
- Proof)
  - Let $a_j \in A$ be an algorithm with the optimal number $k$ of mistakes.
  - Then the final weight will be $w_j=\left(\frac{1}{2}\right)^k$.
    - $\because$ We multiply $\beta=\frac{1}{2}$ when an algorithm makes mistake.
  - Put $W=\Sigma_{i=1}^n w_i$, the sum of all the weights associated with all $n$ algorithms in $A$.
    - Initially, $W=n \space (\because w_i=1, \forall a_i\in A)$.
  - $${\color{red}(\textrm{Verification Required!})}$$
  - The book says, $\left(\frac{3}{4}W\right)$
    - Then for each mistake made by the Weighted-Majority algorithm, $W$ reduces to at most $\frac{3}{4}W$.
  - In my opinion, it's $\left(\frac{1}{2}W\right)$
    - Then for each mistake made by the Weighted-Majority algorithm, $W$ reduces to at most $\frac{1}{2}W$.
      - Why?) Consider the edge cases.
        1. The **minimum** number of the majority, which is $\frac{1}{2}W$, makes mistake.
           - Then the majority is multiplied by $\beta=\frac{1}{2}$.
             - $W$ will be decreased into $\frac{3}{4}W$.
        2. The **maximum** number of the majority, which is $W$, makes mistake.
           - Then the majority is multiplied by $\beta=\frac{1}{2}$.
             - $W$ will be decreased into $\frac{1}{2}W$.
        3. The **minimum** number of the majority, which is $\frac{1}{2}W$, is correct.
           - Then the minority of $\frac{1}{2}W$ is multiplied by $\beta=\frac{1}{2}$.
             - $W$ will be decreased into $\frac{3}{4}W$.
        4. The **maximum** number of the majority, which is $W$, is correct.
           - Then the minority of $0$ is multiplied by $\beta=\frac{1}{2}$.
           - Then, the $W$ will NOT decreased.
      - i.e.) $\frac{1}{2}W_0 \le W_1 \le W_0$
    - Thus, the final total weight $W$ is at most $n\left(\frac{1}{2}\right)^M$
      - where $M$ is the total number of mistakes committed by Weighted-Majority for the training sequence $D$.
    - Hence, $\left(\frac{1}{2}\right)^k \le n\left(\frac{1}{2}\right)^M \Rightarrow -k \le\log_2{n}-M \Rightarrow M\le k+\log_2{n}$
- General Formula, *Littlestone and Warmuth (1991)*
  - For $0 \le \beta \lt 1$, the bound is $\frac{k\log_2{\frac{1}{\beta}}+log_2{n}}{\log_2{\frac{2}{1+\beta}}}$


<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)