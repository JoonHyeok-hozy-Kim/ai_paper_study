* [Back to Statistics Main](../../main.md)

## 2.2 Random Events and Probability

#### Terms)
* Experiment
  * Any process whose outcome is not known in advance but is random
* Trial
  * Each repetition of *experiments*, assuming that the *experiment* can be repeated any number of times under identical conditions.
* Random Experiment
  * An experiment that satisfies the following three conditions.
    1. The set of all possible outcomes are known in advance in each trial.
    2. In any particular trial, it is not known which particular outcome will happen.
    3. The experiment can be repeated under identical conditions.

#### Defs.)
* Sample Space
  * the set consisting of all possible outcomes and is called the sure event in the experiment
  * also referred to as a **Probability Space**
* Sample Point (outcome) $S$
  * An event $A$ is a subset of outcomes in $S$, i.e., $A\subset S$. 
  * We say that an event $A$ occurs if the outcome of the experiment is in $A$.
* Impossible Event $\emptyset$
  * The null subset $\emptyset$ of $S$
* $A \cup B$
  * The event consists of all outcomes that are in $A$ or in $B$ or in both.
* $A \cap B$
  * The event consists of all outcomes that are both in $A$ and $B$.
* $A^c$ (the complement of $A$ in $S$)
  * The event consists of all outcomes not in $A$, but in $S$.
* $A \cap B = \emptyset$ 
  * Mutually exclusive or disjoint

<br>

#### Def.) Probability
* Informal Definition
  * The probability of an event is a measure (number) of the chance with which we can expect the event to occur. 
  * We assign a number between 0 and 1 inclusive to the probability of an event. 
  * A probability of 1 means that we are 100% sure of the occurrence of an event, and a probability of 0 means that we are 100% sure of the nonoccurrence of the event. 
  * The probability of any event $A$ in the sample space $S$ is denoted by $P(A)$.
* Classical Definition
  * If there are $n$ equally likely possibilities, of which one must occur, and $m$ of these are regarded as favorable to an event, or as “success,” then the probability of the event or a “success” is given by $m/n$.
  * Drawback
    * Not applicable in situations where the various possibilities cannot be regarded as equally likely
    * Alternative : Frequency interpretation of probability
* Frequency Definition of Probability
  * The probability of an outcome (event) is the proportion of times the outcome (event) would occur in a long run of repeated experiments.
  * Drawback
    * Not complete
    * The condition of repetition under identical circumstances is impossible
* Axiomatic Definition of Probability : $P(.)$
  * Let $S$ be a sample space of an experiment. Probability $P(.)$ is a real-valued function that assigns to each event $A$ in the sample space $S$ a number $P(A)$, called the probability of $A$, with the following conditions satisfied:
    1. It is nonnegative, $P(A) \ge 0$.
    2. It is unity for a certain event
        * i.e., $P(S) = 1$.
    3. It is additive over the union of an infinite number of pairwise disjoint events
        * i.e., if $A_1, A_2,...$ form a sequence of pairwise mutually exclusive events(i.e., $A_i \cap A_j = \emptyset$ for $i \ne j$) in $S$, then $`P({\bigcup}^{\infty}_{i=1}{A_i})={\sum}^{\infty}_{i=1}{P(A_i)}`$
  * Props. derived
    * $P(\emptyset)=0$
    * $0 \le P(A) \le 1, \forall A$

<br>

#### Props.) Basic Properties of Probability
For events $A$, $B$, and $S$ such that $A, B \subset S$
* $P(A^c)=1-P(A)$
* If $A \subset B$, then $P(A) \le P(B)$
* $P(A) \cup P(B) = P(A) + P(B) - P(A \cap B)$
  * in particular, if $P(A \cap B) = \emptyset$, then $P(A) \cup P(B) = P(A) + P(B)$

<br><br>

### [Exercises 2.2](./exercises.md)

<br><br>

* [Back to Statistics Main](../../main.md)