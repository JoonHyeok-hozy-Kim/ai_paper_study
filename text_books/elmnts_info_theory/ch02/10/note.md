* [Back to Elements of Information Theory](../../main.md)

# 2.10 Fano's Inequality

### Theorem 2.10.1) Fano's Inequality
- Ideation)
  - Suppose that we **know** a random variable $`Y`$ and we wish to guess the value of a **correlated random variable** $`X`$.
  - We know that $`H(X|Y)= 0`$ iff. $`X`$ is a function of $`Y`$.
  - Hence, we can estimate $`X`$ from $`Y`$ with zero probability of error iff. $`H(X|Y)= 0`$.
  - Extending this argument, we expect to be able to estimate $`X`$ with a  low probability of error only if the conditional entropy $`H(X|Y)`$ is small.
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
    - $`\displaystyle P_e \ge \frac{H(X|Y) - 1}{\log |\mathcal{X}|`}`$
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
           - Thus, $`H(E) = H(P_e)`$
         - Finally,   
           $`\begin{aligned}
            H(X|E,\hat{X}) &= \textrm{Pr}(E=0) \cdot H(X|\hat{X}, E=0) + \textrm{Pr}(E=1) \cdot H(X|\hat{X}, E=1) \\
            &\le (1-P_e) \cdot 0 + P_e \cdot \log{|\mathcal{X}|} \\
            &= P_e \log{|\mathcal{X}|} \\
           \end{aligned}`$
           - where $`|\mathcal{X}|`$ is the number of possible outcomes.
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

* [Back to Elements of Information Theory](../../main.md)