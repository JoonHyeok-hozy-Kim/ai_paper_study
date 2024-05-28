* [Back to Elements of Information Theory](../../main.md)

# 2.8 Data-Processing Inequality

### Concept) Markov Chain
- Def.) $`X\rightarrow Y \rightarrow Z`$
  - Random variables $`X,Y,Z`$ are said to **form a Markov chain in that order**
    - if the conditional distribution of $`Z`$ 
      - depends only on $`Y`$ 
      - conditionally independent of $`X`$.
    - i.e.)
      - $`p(x,y,z) = p(x)p(y|x)p(z|y)`$
- Props.)
  - $`X\rightarrow Y\rightarrow Z`$ $`\Leftrightarrow`$ $`X`$ and $`Z`$ are conditionally independent given $`Y`$.
    - pf.)  
      1. $`X\rightarrow Y\rightarrow Z`$ $`\Rightarrow`$ $`X`$ and $`Z`$ are conditionally independent given $`Y`$.   
      $`\begin{aligned}
        p(x,z|y) &= \frac{p(x,y,z)}{p(y)} \\
        &= \frac{p(x,y) p(z|y)}{p(y)} \\
        &= p(x|y)p(z|y)
      \end{aligned}`$
      2. $`X\rightarrow Y\rightarrow Z`$ $`\Leftarrow`$ $`X`$ and $`Z`$ are conditionally independent given $`Y`$.      
      $`\begin{aligned}
        p(x,z|y) &= \frac{p(x,y,z)}{p(y)}
      \end{aligned}`$  
      $`\begin{aligned}
        p(x|y)p(z|y) &= \frac{p(x,y)p(z|y)}{p(y)} \\
        &= \frac{p(x)p(x,y)p(z|y)}{p(y)}
      \end{aligned}`$  
      $`\begin{aligned}
        p(x,z|y) = p(x|y)p(z|y) & \Rightarrow \frac{p(x,y,z)}{p(y)} = \frac{p(x)p(x,y)p(z|y)}{p(y)} \\
        & \Rightarrow p(x,y,z) = p(x)p(x,y)p(z|y)
      \end{aligned}`$
  - $`X\rightarrow Y\rightarrow Z`$ implies that $`X\leftarrow Y\leftarrow Z`$.
    - Thus, sometimes we write $`X\leftrightarrow Y\leftrightarrow Z`$.
  - If $`Z = f(Y)`$ then $`X\rightarrow Y\rightarrow Z`$.


<br><br>

### Concept) Data-Processing Inequality
If $`X\rightarrow Y \rightarrow Z`$ then $`I(X;Y) \ge I(X;Z)`$.    
- pf.)
  - By the [chain rule of the mutual information](../05/note.md#theorem-252-chain-rule-for-information)    
    $`\begin{aligned}
        I(X;Y,Z) &= I(X;Z) + I(X;Y|Z) \cdots (1) \\
        &= I(X;Y) + I(X;Z|Y) \cdots (2)
    \end{aligned}`$
  - Thus,   
    $`\begin{aligned}
        I(X;Z) + I(X;Y|Z) &= I(X;Y) + I(X;Z|Y) \\
        I(X;Z) + I(X;Y|Z) &= I(X;Y) & \because X\rightarrow Y \rightarrow Z \Rightarrow I(X;Z|Y) = 0 \\
    \end{aligned}`$
  - By the [Non-negativity of the Mutual Information](../06/note.md#corollary-non-negativity-of-conditional-mutual-information), $`I(X;Y|Z) \ge 0`$.
  - Thus,
    $`I(X;Y|Z) = I(X;Y) - I(X;Z) \ge 0`$.
  - Therefore, $`I(X;Y) \ge  I(X;Z)`$.
- cf.) Equality holds iff. $`I(X;Y|Z) = 0`$
  - i.e.) $`X\rightarrow Z\rightarrow Y`$ forms a Markov chain.

#### Corollary 1)
If $`Z = f(Y)`$, then $`I(X;Y) \ge I(X;g(Y))`$.
- Meaning)
  - Functions of the data $`Y`$ cannot increase the information about $`X`$.

#### Corollary 2)
If $`X\rightarrow Y \rightarrow Z`$ then $`I(X;Y) \ge I(X;Y|Z)`$.    
- pf.)
  - Recall that
    - $`I(X;Z) + I(X;Y|Z) = I(X;Y)`$
  - By the [Non-negativity of the Mutual Information](../06/note.md#corollary-non-negativity-of-conditional-mutual-information), $`I(X;Z) \ge 0`$.
  - Therefore, $`I(X;Y) \ge I(X;Y|Z)`$.    
- Meaning)
  - The dependence of $`X`$ and $`Y`$ is decreased (or remains unchanged) by the observation of the "downstream" random variable $`Z`$.
    - cf.) If $`X,Y,Z`$ do not form the [Markov chain](#concept-markov-chain), $`I(X;Y|Z) \gt I(X;Y)`$ is possible.
      - e.g.)
        - Let
          - $`X,Y`$ are independent binary random variables 
            - Then, $`I(X;Y) = 0`$.
          - $`Z = X+Y`$
        - By the definition of the [Conditional Mutual Information](../05/note.md#concept-conditional-mutual-information),
          - $`I(X;Y|Z) = H(X|Z) - H(X|Y,Z)`$
        - By the [corollary](../02/note.md#corollary) of the [chain rule of entropy](02/note.md#theorem-221-chain-rule)
          - $`H(X|Y,Z) = H(X,Y|Z) - H(Y|Z) = - H(Y|Z)`$.
        - Thus, $`I(X;Y|Z) = H(X|Z) + H(Y|Z)`$
          - where
            - $`H(X|Z) = P(Z=1)H(X|Z=1) = \frac{1}{2}`$
            - $`H(Y|Z) = P(Z=1)H(Y|Z=1) = \frac{1}{2}`$
        - Therefore, $`I(X;Y|Z) = H(X|Z) + H(Y|Z) = 1 > 0 = I(X;Y)`$




<br>

* [Back to Elements of Information Theory](../../main.md)