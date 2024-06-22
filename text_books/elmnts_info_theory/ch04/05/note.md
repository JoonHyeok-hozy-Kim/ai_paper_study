* [Back to Elements of Information Theory](../../main.md)

# 4.5 Functions of Markov Chains

### Theorem) Upper and Lower Bound of the Function of the Markov Process
- Theorem)
  - Let
    - $`X_1, X_2, \cdots, X_n`$ form a stationary Markov chain
    - $`Y_i = \phi(X_i)`$ : A function of the Markov process
  - Then   
    $`\begin{aligned}
        &H(Y_n | Y_{n-1}, \cdots, Y_1, X_1) \le H(\mathcal{Y}) \le H(Y_n | Y_{n-1}, \cdots, Y_1)  & \cdots (A) \\
        &\lim_{n\rightarrow\infty} H(Y_n | Y_{n-1}, \cdots, Y_1, X_1) = H(\mathcal{Y}) = \lim_{n\rightarrow\infty} H(Y_n | Y_{n-1} \cdots, Y_1) & \cdots (B) \\
    \end{aligned}`$
- pf.)
  - By [Lemma 4.5.1](#lemma-451-lower-bound), we get the lower bounds as    
    $`\begin{cases}
        H(Y_n | Y_{n-1}, \cdots, Y_1, X_1) \le H(\mathcal{Y}) \\
        \displaystyle\lim_{k\rightarrow\infty} H(Y_{n+k+1} | Y_{n+k},\cdots,Y_1) = H(\mathcal{Y}) \\
    \end{cases}`$
  - By [Theorem 4.2.2](../02/note.md#theorem-422), $`H(Y_n|Y_{n-1},\cdots, Y_1)`$ converges monotonically to $`H(\mathcal{Y})`$.
  - Since [conditioning reduces entropy](../../ch02/06/note.md#theorem-265-conditioning-reduces-entropy),
    - $`H(Y_n | Y_{n-1}, \cdots, Y_1, X_1) \le H(Y_n | Y_{n-1}, \cdots, Y_1)`$.
  - Thus, $`H(Y_n | Y_{n-1}, \cdots, Y_1, X_1) \le H(\mathcal{Y}) \le H(Y_n | Y_{n-1}, \cdots, Y_1) \; \cdots (A)`$
  - By [Lemma 4.5.2](#lemma-452-decreasing-interval-between-the-upper-and-the-lower-bounds),   
    $`\displaystyle \lim_{n\rightarrow\infty} \left\{ H(Y_n | Y_{n-1}, \cdots, Y_1) - H(Y_n | Y_{n-1}, \cdots, Y_1, X_1) \right\} = 0`$.
  - $`\displaystyle \therefore \lim_{n\rightarrow\infty} H(Y_n | Y_{n-1}, \cdots, Y_1, X_1) = H(\mathcal{Y}) = \lim_{n\rightarrow\infty} H(Y_n | Y_{n-1} \cdots, Y_1)  \cdots (B)`$

<br>

#### Lemma 4.5.1) Lower Bound
- Lemma)
  - $`H(Y_n | Y_{n-1}, \cdots, Y_2, X_1) \le H(\mathcal{Y})`$
- pf.)
  - For $`k=1,2,\cdots`$   
    $`\begin{aligned}
        H(Y_n | Y_{n-1}, \cdots, Y_2, X_1) 
        &= H(Y_n | Y_{n-1}, \cdots, Y_2, Y_1, X_1) & \because Y_1 = \phi(X_1) \\
        &= H(Y_n | Y_{n-1}, \cdots, Y_2, Y_1, X_1, X_0, \cdots, X_{-k}) & \because \textrm{Markovity of } X \\
        &= H(Y_n | Y_{n-1}, \cdots, Y_1, Y_0, \cdots, Y_{-k}, X_1, X_0, \cdots, X_{-k}) & \because Y_i = \phi(X_i) \\
        &\le H(Y_n | Y_{n-1}, \cdots, Y_1, Y_0, \cdots, Y_{-k}) & \because \textrm{Conditioning reduces entropy.} \\
        &= H(Y_{n+k+1} | Y_{n+k},\cdots,Y_1) & \because \textrm{Stationarity.}
    \end{aligned}`$
  - Since the above inequality is true for all $`k`$, it is true in the limit as well.
  - Thus,    
    $`\begin{aligned}
        H(Y_n | Y_{n-1}, \cdots, Y_1, X_1) &\le \lim_{k\rightarrow\infty} H(Y_{n+k+1} | Y_{n+k},\cdots,Y_1) \\
        &= H(\mathcal{Y})
    \end{aligned}`$

#### Lemma 4.5.2) Decreasing Interval between the Upper and the Lower Bounds
- Lemma)
  - $`H(Y_n | Y_{n-1}, \cdots, Y_1) - H(Y_n | Y_{n-1}, \cdots, Y_1, X_1) \rightarrow 0`$
- pf.)
  - By the [property of the mutual information](../../ch02/04/note.md#243),
    - $`H(Y_n | Y_{n-1}, \cdots, Y_1) - H(Y_n | Y_{n-1}, \cdots, Y_1, X_1) = I(X_1;Y_n | Y_{n-1}, \cdots, Y_1)`$
  - By [another property](../../ch02/04/note.md#244) of the mutual information,   
    $`\begin{aligned}
        I(X_1;Y_n | Y_{n-1}, \cdots, Y_1) 
        &= H(X_1) - H(X_1| (Y_n | Y_{n-1}, \cdots, Y_1)) \\
        &\le H(X_1)
    \end{aligned}`$
  - Considering that $`I(X_1;Y_n | Y_{n-1}, \cdots, Y_1)`$ increases with $`n`$,
    - $`\displaystyle \lim_{n\rightarrow\infty} I(X_1;Y_n | Y_{n-1}, \cdots, Y_1) \le H(X_1)`$
  - By the [chain rule](../../ch02/05/note.md#theorem-252-chain-rule-for-information),   
    $`\begin{aligned}
        H(X) &\ge \lim_{n\rightarrow\infty} I(X_1;Y_1,Y_2,\cdots,Y_n) \\
        &= \lim_{n\rightarrow\infty} \sum_{i=1}^n I(X_1;Y_i|Y_{i-1}, \cdots, Y_1) \\
    \end{aligned}`$
  - Thus,    
    $`\begin{aligned}
        \lim_{n\rightarrow\infty} I(X_1;Y_n|Y_{n-1}, \cdots, Y_1) 
        &= \lim_{n\rightarrow\infty} \left\{ H(Y_n | Y_{n-1}, \cdots, Y_1) - H(Y_n | Y_{n-1}, \cdots, Y_1, X_1) \right\} \\
        &= 0
    \end{aligned}`$.
  - $`\displaystyle \therefore H(Y_n | Y_{n-1}, \cdots, Y_1) - H(Y_n | Y_{n-1}, \cdots, Y_1, X_1) \rightarrow 0`$










<br>

* [Back to Elements of Information Theory](../../main.md)