* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 7.3 Sample Complexity for Finite Hypothesis Spaces

### Def.) Sample complexity
The growth in the number of required training examples with problem size
- e.g.)
  - [PAC-learnability](../02/note.md#concept-pac-learnability) is largely determined by the number of training examples required by the learner

<br>

### Def.) Consistent Learner
A learner is **consistent** if it outputs hypotheses that perfectly fit the training data, whenever possible.
- Every consistent learner outputs a hypothesis belonging to the [version space](../../ch02/05/note.md#concept-version-space), regardless of the instance space $X$, hypothesis space $H$, or training data $D$.
  - Recall $VS_{H,D}=\lbrace h\in H|h(x)=c(x),\space\forall\langle x,c(x)\rangle \in D\rbrace$

<br>

### Concept) Exhausted Version Space
- Def.)
  - Let
    - $H$ : a hypothesis space
    - $c$ : a target concept
    - $D$ : an instance distribution
  - The version space $VS_{H,D}$ is said to be $\epsilon$-exhausted w.r.t. $c$ and $D$, if $\forall h \in VS_{H,D}$ has errors less than $\epsilon$ w.r.t. $c$ and $D$.
    - i.e.) $error_D(h) \lt \epsilon, \space \forall h \in VS_{H,D}$
- Prop.)
  - The version space is $\epsilon$-exhausted when all the hypotheses consistent with the observed training examples (i.e., those with zero training error) happen to have true error less than $\epsilon$.
    - What the **learner** knows is that these hypotheses fit the training data equally well.
      - i.e.) They all have zero training error.
    - Only an **observer** who knew the identity of the target concept $c$, could determine with certainty whether the version space is $\epsilon$-exhausted.
    - Still, with [a theorem below](#theorem-exhausting-the-version-space), we can bound the probability that the version space will be $\epsilon$-exhausted after a given number of training examples, even without knowing the identity of the target concept or the distribution from which training examples.

![](images/001.png)

<br>

### Theorem) Exhausting the Version Space
$\epsilon$-exhausting version space.   
If the hypothesis space $H$ is finite, and $D$ is a sequence of $m \ge 1$ independent randomly drawn examples of some target concept $c$, then for any $0 \le \epsilon \le 1$, the **probability** that the version space $VS_{H,D}$ is not $\epsilon$-exhausted w.r.t. $c$ is less than or equal to $|H|e^{-\epsilon m}$.
- pf.)
  - Let $H_1, H_2 \subset H$ such that
    - $H_1 \cup H_2 = H$ and $H_1 \cap H_2 = \emptyset$
    - $error_D(h_1) \gt \epsilon, \space \forall h_1 \in H_1$ : all the hypotheses with **true error greater** than $\epsilon$ w.r.t. $c$
    - $error_D(h_2) \lt \epsilon, \space \forall h_2 \in H_2$ : all the hypotheses with **true error less** than $\epsilon$ w.r.t. $c$
  - Then, we **fail** to $\epsilon$-exhaust the version space $VS_{H,D}$ iff. $\exists h_1 \in H_1$ consistent with $m$ independently drawn examples.
    - Why?)
      - Recall [the def. of the exhausted version space](#concept-exhausted-version-space).
        - i.e.) $VS_{H,D}$ contains all the consistent hypotheses.
      - If $h_1$ is consistent, then $h_1 \in VS_{H,D}$
      - But, $error_D(h_1) \gt \epsilon$.
      - Therefore, $VS_{H,D}$ is NOT $\epsilon$-exhausted.
  - Consider that the probability that $h_1 \in H_1$ would be consistent with one randomly drawn example is at most $(1-\epsilon)$. 
  - Thus, the probability that $h_1$ will be consistent with $m$ independently drawn examples is at most $(1-\epsilon)^m$.
  - Also, there will be $|H_1|$ number of hypotheses in $H_1$ where $|H_1| \le |H|$.
  - Hence, the probability that at least one of these will be consistent with all $m$ training examples is at most $|H|(1-\epsilon)^m$.
  - Consider that if $0 \le \epsilon \le 1$ then $(1-\epsilon) \le e^{-\epsilon}$.
  - Therefore, $|H|(1-\epsilon)^m \le |H|e^{-\epsilon m}$
- Meaning)
  - We derived an upper bound of the probability that the version space is not $\epsilon$-exhausted, based on the number of training examples $m$, the allowed error $\epsilon$, and the size of $H$.
  - This bounds the probability that $m$ training examples will fail to eliminate all "bad" hypotheses (i.e., hypotheses with true error greater than $\epsilon$), for any consistent learner using hypothesis space $H$. 

<br>

### Concept) General Bound on the Number of Training Examples for Successful Consistent Learner
- A general bound on the number of training examples sufficient **for any consistent learner** to successfully learn any target concept in $H$, for any desired values of $\delta$ and $\epsilon$.
  - $m \ge \frac{1}{\epsilon}\left(\ln{|H|}+\ln{\frac{1}{\delta}}\right)$
- Derivation)
  - With the [theorem above](#theorem-exhausting-the-version-space), we derived $|H|e^{-\epsilon m}$, which is the upper bound of the probability that the version space is not $\epsilon$-exhausted, based on the number of training examples $m$, the allowed error $\epsilon$, and the size of $H$.
  - We can use $|H|e^{-\epsilon m}$ for $\delta$ from [PAC Learnability](../02/note.md#723-pac-learnability).
    - Recall that $\delta$ was an arbitrary upper bound for the probability of failure.
    - We may set $|H|e^{-\epsilon m} \le \delta$.
  - $|H|e^{-\epsilon m} \le \delta \space \Rightarrow \space m \ge \frac{1}{\epsilon}\left(\ln{|H|}+\ln{\frac{1}{\delta}}\right)$
- Meaning)
  - $m$ training examples are sufficient to assure that any consistent hypothesis will be probably (with probability $(1-\delta)$ ) approximately (within error $\epsilon$ ) correct.
    - cf.) "Consistency" $\Leftrightarrow$ "Zero training error in $H$"
- Prop.)
  - $m$ grows...
     - linearly in $\frac{1}{\epsilon}$
     - logarithmically in $\frac{1}{\delta}$
     - logarithmically in the size of the hypothesis space $H$.
  - $m$ can be a substantial overestimate.
    - why?)
      - Recall that $m$ grows logarithmically with $|H|$.
      - Thus, if the size of hypothesis space is large, $m$ will be large as well.
      - Consider the case that **the version space is comparatively small**.
        - Then, the $m$ bound we derived will overestimate the sufficient bound for the number of training examples.
  - If $H$ does not contain the target concept $c$, then a zero-error hypothesis (the consistency of $H$) cannot always be found.
    - Alternative Sol)
      - Loosen the zero-error hypothesis condition.
      - [Agnostic Learner](#concept-agnostic-learner) : Find the hypothesis with **minimum** training error

<br><br>

## 7.3.1 Agnostic Learning and Inconsistent Hypothesis
### Concept) Agnostic Learner
- Ideation)
  - Recall that [the general bound for training examples](#concept-general-bound-on-the-number-of-training-examples-for-successful-consistent-learner) above, $m$, holds when every hypothesis in $H$ has zero training error.
    - i.e.) [Consistent Learner](#def-consistent-learner) is required.
  - However, if $H$ does not contain the target concept $c$, then a zero-error hypothesis (the consistency of $H$) cannot always be found.
  - Let's loosen the zero-error hypothesis condition.
    - Find the hypothesis with **minimum** training error
- Def.) Agnostic Learner
  - A learner that makes no assumption that the target concept is representable by $H$ and that simply finds the hypothesis with minimum training error, is often called an agnostic learner
    - It makes no prior commitment about whether or not $C \subseteq H$.

<br>

#### Concept) Hoeffding Bounds
- Desc.)
  - Hoeffding Bounds characterize the **deviation** between the **true probability** of some event and its **observed frequency** over $m$ independent trials.
  - The bounds apply to experiments involving $m$ distinct **Bernoulli** trials.
- Statement)
  - Let $X_1, \cdots, X_n$ be independent random variables such that $a_i \le X_i \le b_i$ almost surely.
  - Consider the sum of these random variables, $S_n = \Sigma_{i=1}^n X_i$
  - Then Hoeffding's theorem states that, for all $t \gt 0$,   
    $`\displaystyle{P} \left(S_{n}-\mathrm{E} \left[S_{n}\right]\geq t\right) \leq \exp \left(-{\frac {2t^{2}}{\sum_{i=1}^{n}(b_{i}-a_{i})^{2}}}\right)`$

<br>

### Concept) Inconsistent Hypothesis
- Goal)
  - Derive the sufficient amount of training examples when the hypothesis space is **inconsistent**.
    - i.e.) $\exists h \in H, h(x) \ne c(x)$ : non-zero training error!
- Settings)
  - $D$ :  the particular set of training examples available to the learner
    - $error_D(h)$ : the training error of hypothesis $h$
  - $\mathcal{D}$ : s the probability distribution over the entire set of instances $X$
    - $error_{\mathcal{D}}(h)$ : the true error over the entire probability distribution $\mathcal{D}$.
  - $h_{best}$ : the hypothesis from $H$ having lowest training error over the training examples
- Problem)
  - Get $m$ such that $error_{\mathcal{D}}(h) \ge \epsilon + error_D(h)$.
- Sol.)
  - Applying the [Hoeffding Bounds](#concept-hoeffding-bounds-chernoff-bounds), $Pr\left[error_{\mathcal{D}(h)} \gt error_D(h)+\epsilon\right] \le e^{\frac{-2\epsilon^2}{m}}$
    - why?)
      - Recall the inequality, $`{Pr} \left(S_{n}-\mathrm {E} \left[S_{n}\right]\geq t\right) \leq \exp \left(-{\frac {2t^{2}}{\sum _{i=1}^{n}(b_{i}-a_{i})^{2}}}\right)`$
      - Then 
        - LHS : $Pr\left[error_{\mathcal{D}(h)} \gt error_D(h)+\epsilon\right]$
          - $S_n=error_{\mathcal{D}(h)}$ : the true error on the entire set
          - $E[S_n]=error_D(h)$ : the training error of an arbitrarily chosen single hypothesis $h$
          - $t=\epsilon \gt 0$ 
        - RHS : $e^{\frac{-2\epsilon^2}{m}}$
          - $${\color{red}(\textrm{Verification Required!})}$$
            - The book says it's $e^{-2m\epsilon^2}$ instead of $e^{\frac{-2\epsilon^2}{m}}$
            - But, considering the direction of the inequality operator, $e^{-2m\epsilon^2}$ seems more reasonable, setting the lower bound for $m$.
            - If we use $e^{-2m\epsilon^2}$, we may derive $m \le \textrm{(...)}$, which is the upper bound for $m$, non-sense!
          - Consider that our problem is whether a hypothesis is correctly classifying training examples.
            - Since each examples are independently drawn from $\mathcal{D}$ over $X$, we can see this as the Bernoulli distribution.
            - Thus, put $`\left\lbrace\begin{aligned}a_i=0, & \textrm{ Success} \\ b_i=1, & \textrm{ Failure} \end{aligned}\right.`$
          - Recall that we draw $m$ independent training examples.
            - Thus, $m=n$
            - Hence, $`\sum _{i=1}^{n}(b_{i}-a_{i})^{2} = \sum _{i=1}^{m}(b_{i}-a_{i})^{2}=\sum _{i=1}^{m}(1-0)^{2}=m`$ 
              - i.e.) the **frequency** that the hypothesis misclassified a randomly drawn instance.
          - Therefore, $`\exp \left(-{\frac {2t^{2}}{\sum _{i=1}^{n}(b_{i}-a_{i})^{2}}}\right) = e^{\frac{-2\epsilon^2}{m}}`$
      - Thus, the inequality goes as 
        - $Pr\left[error_{\mathcal{D}(h)} \gt error_D(h)+\epsilon\right] \le e^{\frac{-2\epsilon^2}{m}}$
          - i.e.) A **bound** on the **probability** that an arbitrarily chosen single hypothesis has a very misleading training error.
  - Then, $Pr\left[\left(\exists h \in H\right) \left(error_{\mathcal{D}(h)} \gt error_D(h)+\epsilon\right)\right] \le |H|e^{\frac{-2\epsilon^2}{m}}$
    - why?)
      - Consider that there are $|H|$ hypotheses in $H$.
        - To assure that $h_{best}$, the best hypothesis is found by $L$, has an error bounded as above, we must consider the probability that any one of the $|H|$ hypotheses could have a large error.
  - Putting $\delta$ denote this probability, $\delta=Pr\left[\left(\exists h \in H\right) \left(error_{\mathcal{D}(h)} \gt error_D(h)+\epsilon\right)\right]$
  - Then   
    $`\begin{aligned} & \delta \le |H|e^{\frac{-2\epsilon^2}{m}} \\ \Rightarrow & \ln{\delta} \le \ln{|H|} -\frac{2\epsilon^2}{m} \\ \Rightarrow & \frac{2\epsilon^2}{m} \le \ln{|H|} + \ln{\frac{1}{\delta}} \\ \Rightarrow & \frac{m}{2\epsilon^2} \ge \frac{1}{\ln{|H|} + \ln{\frac{1}{\delta}}} \\ \Rightarrow & m \ge \frac{2\epsilon^2}{\ln{|H|} + \ln{\frac{1}{\delta}}} \end{aligned}`$

<br><br>

## 7.3.2 Conjunctions of Boolean Literals Are PAC-Learnable
#### Def.) Boolean Literal
A boolean literal is any boolean variable, or its negation. 
- e.g.)
  - $Old$
  - $\neg Old$

<br>

#### Concept.) Conjunction of Boolean Literals
- e.g.)
  - $\neg Old \wedge Tall$

<br>

### Theorem) PAC-Learnability of Boolean Conjunctions
The class $C$ of conjunctions of boolean literals is [PAC-learnable](../02/note.md#props-pac-learnability) by the FIND-S algorithm using $H = C$.
- pf.)
  1. The sample complexity for this concept class is polynomial in $n$ (the number of variables), $\frac{1}{\delta}$, and $\frac{1}{\epsilon}$, and independent of the size of the concept class, $size(c)$.
     - Consider any consistent learner $L$ using a hypothesis space $H$ identical to $C$.
       - i.e.) $H = C$.
     - Here, $m \ge \frac{1}{\epsilon}\left(n\ln{3}+\ln{\frac{1}{\delta}}\right)$
       - why?)
         - Recall [the General Bound on the Number of Training Examples for Successful Consistent Learner](#concept-general-bound-on-the-number-of-training-examples-for-successful-consistent-learner) : $m \ge \frac{1}{\epsilon}\left(\ln{|H|}+\ln{\frac{1}{\delta}}\right)$ 
         - $\epsilon$ and $\delta$ are the hyperparameters that we set.
         - $|H| = 3^n$, where $n$ is the number of boolean variables.
           - $\because$ For each variable, there are three possibilities
              1. True
              2. False (negation)
              3. Ignore the variable.
         - By assumption, $|H| = size(c)$.
           - Thus, the sample complexity $m$ is independent of $size(c)$.
       - e.g.)
         - Suppose a consistent learner attempts to learn a target concept 
           - described by conjunctions of up to 10 boolean literals. $(n=10)$
           - and we desire a 95% probability that it will learn a hypothesis with error less than 0.1. $(\delta = 0.05, \epsilon = 0.1)$
         - Then, $m \ge \frac{1}{0.1}\left(10\ln{3}+\ln{\frac{1}{0.05}}\right)$
  2.  To incrementally process each training example, the FIND-S algorithm requires effort linear in $n$ and independent of $\frac{1}{\delta}$, $\frac{1}{\epsilon}$, and $size(c)$.
      - Requirement 
        - Efficiency : Total computation is polynomial
          - no more than **polynomial computation per training example** 
          - no more than a **polynomial number of training examples**
        - Capable of learning conjunctions of boolean literals
      - The [The Find-S Algorithm](../../ch02/04/note.md#24-find-s-finding-a-maximally-specific-hypothesis) PAC-learns the concept class of conjunctions of $n$ boolean literals with negations.
        - Why?) 
          - Recall that Find-S
            - incrementally computes the most specific hypothesis consistent with the training examples. 
            - computes the intersection of the literals shared by the current hypothesis and the new training example, for each new positive training example, using time linear in $n$.

<br><br>

## 7.3.3 PAC-Learnability of Other Concept Classes
### 7.3.3.1 Unbiased Learners
- Unbiased Learners have **exponential** sample complexity under PAC Model.
  - Thus, NOT [PAC-learnable](../02/note.md#props-pac-learnability) (linear complexity required.)
  - Why?)
    - Consider the unbiased concept class $C$ that contains every teachable concept relative to $X$.
    - Then, $|C|=2^{|X|}$.
      - $\because C$ is unbiased $\Rightarrow \space C$ is the power set of $X$.
    - For the simplicity, assume that instances in $X$ are defined by $n$ boolean variables.
      - Then $|X|=2^n$.
    - Thus, $|C|=2^{|X|}=2^{2^n}$
    - Since the concept class $C$ is unbiased, the learner should use an unbiased hypothesis space, i.e., $H=C$.
    - Hence, $|H|=|C|=2^{2^n}$
    - Therefore, $m \ge \frac{1}{\epsilon}\left(2^n\ln{2}+\ln{\frac{1}{\delta}}\right)$ : Exponential Sample Complexity!


<br><br>

### 7.3.3.2 k-Term DNF and k-CNF Concepts
#### Concept) k-Term Disjunctive Normal Form (k-Term DNF)
- Def.) $k$-Term DNF Expressions
  - $T_1 \vee T_2 \vee \cdots \vee T_k$
    - where $T_i$ is a conjunction of $n$ boolean attributes and their negations.
- Prop.)
  - $k$-Term DNF has **polynomial** sample complexity.
    - why?)
      - Assuming $H=C$, $|H| = 3^{nk}$.
        - Why?)
          - There are $k$ terms($T_1, \cdots, T_k$), each of which may take on $3^{n}$ possible values
        - cf.) $3^{nk}$ is an overestimate of $|H|$.
          - why?)
            - It excludes the cases that $T_i = T_j$ and $T_i \subset T_j$.
      - Still, we can use this upper bound of $H$ to obtain the upper bound on the sample complexity.
        - $m \ge \frac{1}{\epsilon}\left(nk\ln{3}+\ln{\frac{1}{\delta}}\right)$
      - Therefore, the sample complexity of $k$-Term DNF is **polynomial** in $\frac{1}{\delta}$, $\frac{1}{\epsilon}$, $n$, and $k$.
  - $k$-Term DNF is NOT PAC-Learnable.
    - The computational complexity is not polynomial, because this learning problem can be shown to be equivalent to other problems that are known to be unsolvable in polynomial time (unless $RP = NP$).

<br>

#### Concept) k-Conjunctive Normal Form (k-CNF)
- Def.) $k$-CNF Expressions
  - $T_1 \wedge T_2 \wedge \cdots \wedge T_j$
    - where $T_i$ is a disjunction of up to $k$ boolean attributes and their negations.
- Prop.)
  - $k$-CNF subsumes $k$-Term DNF.
    - i.e.) Any $k$-Term DNF expression can be rewritten as a $k$-CNF expression.
      - But not vice versa.
  - $k$-CNF is PAC Learnable.
    - i.e.) polynomial sample complexity and polynomial time complexity.
  - $k$-term DNF is PAC learnable by an efficient algorithm using $H = k\textrm{-CNF}$.
    - Refer to Kearns and Vazirani (1994)


<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)