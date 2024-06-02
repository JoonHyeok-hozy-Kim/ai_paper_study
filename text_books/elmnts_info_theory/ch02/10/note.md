* [Back to Elements of Information Theory](../../main.md)

# 2.10 Fano's Inequality

### Theorem 2.10.1) Fano's Inequality
- Ideation)
  - Suppose that we **know** a random variable $`Y`$ and we wish to guess the value of a **correlated random variable** $`X`$.
  - We know that $`H(X|Y)= 0`$ iff. $`X`$ is a function of $`Y`$.
  - Hence, we can estimate $`X`$ from $`Y`$ with zero probability of error iff. $`H(X|Y)= 0`$.
  - Extending this argument, we expect to be able to estimate $`X`$ with a low probability of error $`(P_e)`$ only if the conditional entropy $`H(X|Y)`$ is small.
- Theorem)
  - Let
    - $`X, Y`$ : random variables
      - where 
        - $`X`$ has a distribution of $`p(x)`$
        - $`Y`$ is observable and related to $`X`$ by $`p(x|y)`$.
    - $`g(Y) = \hat{X}`$ :
      - where
        - $`\hat{X}`$ : an estimate of $`X`$ and takes on values in $`\hat{\mathcal{X}}`$
        - $`g`$ : a function that we calculate $`\hat{X}`$ from $`Y`$.
    - $`P_e \equiv \textrm{Pr}\{\hat{X}\ne X\}`$ : the probability of error
  - Then
    - For any estimator $`\hat{X}`$ such that $`X\rightarrow Y \rightarrow \hat{X}`$ with $`P_e`$
      - we have $`H(P_e) + P_e\log{|\mathcal{X}|} \ge H(X|\hat{X}) \ge H(X|Y)`$.
  - This inequality can be weakened to
    - $`1+P_e\log{|\mathcal{X}|} \ge H(X|Y)`$
    - $`\displaystyle P_e \ge \frac{H(X|Y) - 1}{\log |\mathcal{X}|}`$
- pf.)
  - Define an error random variable
    - $`E = \begin{cases}
        1 & \textrm{if } \hat{X} \ne X \\
        0 & \textrm{if } \hat{X} = X \\
    \end{cases}`$
  - Then, by the [chain rule](../05/note.md#theorem-251-chain-rule-for-entropy) we can get the following two respectively.  
    1. $`H(E, X | \hat{X}) = H(X | \hat{X}) + \underbrace{H(E | X, \hat{X})}_{= 0}`$ 
       - Why?)
         - Consider that $`E`$ is a function of $`X`$ and $`\hat{X}`$.
           - Then, given $`X`$ and $`\hat{X}`$, there is no uncertainty in $`E`$.
           - Thus, $`H(E | X, \hat{X}) = 0`$
    2. $`H(E, X | \hat{X}) = \underbrace{H(E|\hat{X})}_{\le H(E) = H(P_e)} + \underbrace{H(X|E,\hat{X})}_{\le P_e \log{|\mathcal{X}|}}`$
       - Why?)
         - Consider that [conditioning reduces entropy](../06/note.md#theorem-265-conditioning-reduces-entropy).
           - Thus, $`H(E|\hat{X}) \le H(E)`$
         - Also, $`E`$ is a binary random variable.
           - By [definition](../01/note.md#ex211), $`H(E) = H(P_e)`$
         - Finally,   
           $`\begin{aligned}
            H(X|E,\hat{X}) &= \textrm{Pr}(E=0) \cdot H(X|\hat{X}, E=0) + \textrm{Pr}(E=1) \cdot H(X|\hat{X}, E=1) \\
            &\le (1-P_e) \cdot 0 + P_e \cdot \log{|\mathcal{X}|} & \because H(X) \le \log{|\mathcal{X}|} \\
            &= P_e \log{|\mathcal{X}|} \\
           \end{aligned}`$
           - where $`|\mathcal{X}|`$ is the number of possible outcomes.
             - For the pf. of $`H(X) \le \log{|\mathcal{X}|}`$, refer to [Theorem 2.6.4](../06/note.md#theorem-264).
  - Combining the above two we can get   
      $`\begin{aligned}
      & H(X | \hat{X}) = H(E|\hat{X}) + H(X|E,\hat{X}) \le H(P_e) + P_e \log{|\mathcal{X}|} \\
      \Rightarrow & H(P_e) + P_e \log{|\mathcal{X}|} \ge H(X | \hat{X}) \\
    \end{aligned}`$
  - Recall the [data-processing inequality](../08/note.md#concept-data-processing-inequality).
    - Since $`\hat{X}`$ such that $`X\rightarrow Y \rightarrow \hat{X}`$ is a [Markov chain](../08/note.md#concept-markov-chain), we get
      - $`I(X;\hat{X}) \le I(X;Y)`$.
  - Finally,
    - Consider that
      - $`I(X;\hat{X}) = H(X) - H(X|\hat{X})`$
      - $`I(X;Y) = H(X) - H(X|Y)`$
    - Thus,   
      $`\begin{aligned}
        I(X;\hat{X}) \le I(X;Y) &\Leftrightarrow H(X) - H(X|\hat{X}) \le H(X) - H(X|Y) \\
        &\Leftrightarrow H(X|\hat{X}) \ge H(X|Y)
      \end{aligned}`$
    - Therefore,   
      $`H(P_e) + P_e \log{|\mathcal{X}|} \ge H(X | \hat{X}) \ge H(X|Y)`$
- Prop.)
  - $`P_e = 0 \Rightarrow H(X|Y) = 0`$
    - Why?)
      - Recall that $`H(P_e) + P_e\log{|\mathcal{X}|} \ge H(X|\hat{X}) \ge H(X|Y)`$.
      - Thus, $`P_e = 0 \Rightarrow H(P_e) + P_e\log{|\mathcal{X}|} = 0 \ge H(X|Y) = 0`$

<br>

#### Corollary 1 of Theorem 2.10.1)
For any two random variables $`X, Y`$, let $`p = \textrm{Pr}(X\ne Y)`$.   
Then $`H(p) + p\log|\mathcal{X}| \ge H(X|Y)`$
- pf.)
  - Put $`\hat{X} = Y`$ in [Fano's inequality](#theorem-2101-fanos-inequality).

<br>

#### Corollary 2 of Theorem 2.10.1) Slightly Stronger Inequality
Let $`P_e = \textrm{Pr}(X\ne\hat{X})`$ and $`\hat{X}:\mathcal{Y}\rightarrow\mathcal{X}`$.   
Then $`H(P_e) + P_e\log(|\mathcal{X}| - 1) \ge H(X|Y)`$.
- pf.)
  - Recall that we defined $`E = \begin{cases}
        1 & \textrm{if } \hat{X} \ne X \\
        0 & \textrm{if } \hat{X} = X \\
    \end{cases}`$.
  - Since $`\hat{X}:\mathcal{Y}\rightarrow\mathcal{X}`$, 
    - if $`E=1`$, then the range of possible $`X`$ outcome is $`|\mathcal{X}|-1`$.
  - Thus, upon proving [Fano's inequality](#theorem-2101-fanos-inequality), below part will be modified.   
     $`\begin{aligned}
      H(X|E,\hat{X}) &= \textrm{Pr}(E=0)\cdot H(X|\hat{X},E=0) + \textrm{Pr}(E=1)\cdot H(X|\hat{X},E=1) \\
      &\le (1-P_e)\cdot 0 + P_e\log(|\mathcal{X}|-1)
    \end{aligned}`$

<br>

#### Remark) No Knowledge Case
- Ideation)
  - Suppose that there is no knowledge of $`Y`$.   
  - Thus, $`X`$ must be guessed without any information
- Theorem)
  - Let $`X \in \{1,2,\cdots, m\}`$
    - where
      - $`p_i`$ is the probability that $`X=i`$
      - $`p_1 \ge p_2 \ge \cdots \ge p_m`$
  - Then the best guess of $`X`$ is $`\hat{X} = 1`$, which has the highest probability of $`p_1`$.
  - The resulting probability of error is $`P_e = 1-p_1`$.
  - Thus, [Fano's inequality](#theorem-2101-fanos-inequality) goes
    - $`H(P_e) + P_e \log(m-1) \ge H(X)`$.
  - Also, the probability mass function below achieves this bound with equality.
    - $`\displaystyle (p_1, p_2, \cdots, p_m) = \left( 1-P_e, \frac{P_e}{m-1}, \cdots, \frac{P_e}{m-1} \right)`$
  - Therefore, [Fano's inequality](#theorem-2101-fanos-inequality) is sharp.

<br><br>

### Lemma 2.10.1) Inequality Relating Probability Error and Entropy
If $`X`$ and $`X'`$ are i.i.d. with entropy $`H(X)`$,   
Then $`\textrm{Pr}(X=X') \ge 2^{-H(X)}`$
- pf.)
  - Put $`p(x)`$ such that $`X, X' \stackrel{i.i.d}{\sim} p(x)`$
  - Then,   
    $`\begin{aligned}
      \textrm{Pr}(X=X') &= \sum_x p^2(x) = \sum_x p(x) 2^{\log p(x)} \\
      &\ge 2^{\sum p(x)\log{p(x)}} = 2^{-H(X)}
    \end{aligned}`$.
    - Why?)
      - Put $`f(X) = 2^X`$.
      - Then $`f`$ is a convex function.
      - Thus, by [Jensen's Inequality](../06/note.md#theorem-262-jensens-inequality), $`Ef(X) \ge f(EX)`$.
      - Hence, $`p(x) 2^{\log p(x)} \ge 2^{p(x) \log p(x)}`$.
      - Therefore, $`\sum p(x) 2^{\log p(x)} \ge 2^{\sum p(x) \log p(x)}`$

<br>

#### Corollary 1 of Lemma 2.10.1) 
Let $`\begin{cases} X \sim p(x) \\ X' \sim r(x) \end{cases}`$ be independent random variables such that $`x,x'\in\mathcal{X}`$.   
Then $`\begin{cases}
  \textrm{Pr}(X=X') \ge 2^{-H(p) - D(p||r)} \\
  \textrm{Pr}(X=X') \ge 2^{-H(r) - D(r||p)} \\
\end{cases}`$.
- pf)    
  $`\begin{aligned}
    2^{-H(p) - D(p||r)} &= 2^{\sum p(x)\log p(x) + \sum p(x)\log\frac{r(x)}{p(x)}} \\
    &= 2^{\sum p(x)\log r(x)} \\
    &\le \sum p(x) 2^{\log r(x)} & \because \textrm{Jensen's Inequality} \\
    &= \sum p(x)r(x) \\
    &= \textrm{Pr}(X=X') & \because X, X' \textrm{ are iid.}
  \end{aligned}`$





<br>

* [Back to Elements of Information Theory](../../main.md)