* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 7.4 Sample Complexity for Infinite Hypothesis Spaces

#### Prop.) Drawback of the Finite Hypothesis Space
- Recall that we derived [general bound on the number of examples](../03/note.md#concept-general-bound-on-the-number-of-training-examples-for-successful-consistent-learner) using the size of the hypothesis space, $|H|$.
- However, this bound has two problems.
  1. The bound is too weak.
     - Recall that the bound on $\delta$ can be significantly greater than 1 for large $|H|$.
       - $\because|H|e^{-\epsilon m} \le \delta$
  2. $|H|$ cannot be applied to the infinite hypothesis space.
- Alternative Solution : [Vapnik-Chervonenkis Dimension](#742-the-vapnik-chervonenkis-dimension) below.


<br><br>

## 7.4.1 Shattering a Set of Instances
### Concept) Shattering a Set of Instances
- Why shattering?)
  - The [VC dimension](#742-the-vapnik-chervonenkis-dimension) measures the complexity of the hypothesis space $H$ by the number of distinct instances from $X$ that can be completely discriminated using $H$.
    - Recall that the **finite case** used the number of distinct hypotheses $|H|$.

#### Def.) Shattering a Set of Instances
- Let $S \subseteq X$ be a subset of instances.
- A set of instances $S$ is shattered by hypothesis space $H$ if and only if 
for every dichotomy of $S$ there exists some hypothesis in $H$ consistent with this 
dichotomy.

#### E.g.) Shattering a Set of Instances
- Settings)
  - three instances : $x_1, x_2, x_3$
    - Put $S = \lbrace x_1, x_2, x_3 \rbrace$
  - eight hypotheses : $h_1, h_2, \cdots, h_8$

![](images/001.png)

- Desc.)
  - There can be $2^{|S|}=2^3=8$ dichotomies for $S$.
    - $\emptyset, \lbrace x_1 \rbrace, \lbrace x_2 \rbrace, \cdots, \lbrace x_1, x_2, x_3 \rbrace$
  - Each hypothesis $h_1, h_2, \cdots, h_8$ corresponds with the above dichotomies.
    |$h$|dichotomy|Why?|
    |:-:|:-:|-|
    |$h_1$|$\emptyset$|$h_1(x)\ne c(x), \forall x \in S$|
    |$h_2$|$\lbrace x_1 \rbrace$|$`h_2(x) = \left\lbrace\begin{array}{ll} c(x) & x=x_1 \\ \neg c(x) & x=x_2, x_3\end{array}\right.`$|
    |$h_3$|$\lbrace x_2 \rbrace$|$`h_3(x) = \left\lbrace\begin{array}{ll} c(x) & x=x_2 \\ \neg c(x) & x=x_1, x_3\end{array}\right.`$|
    |$\vdots$|$\vdots$|$\vdots$|
    |$h_7$|$\lbrace x_1, x_3 \rbrace$|$`h_7(x) = \left\lbrace\begin{array}{ll} c(x) & x=x_1, x_3 \\ \neg c(x) & x=x_2\end{array}\right.`$|
    |$h_8$|$\lbrace x_1, x_2, x_3 \rbrace$|$h_8(x)= c(x), \forall x \in S$|



<br><br>

## 7.4.2 The Vapnik-Chervonenkis Dimension








<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)