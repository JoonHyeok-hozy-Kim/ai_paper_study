* [Back to Elements of Information Theory](../../main.md)

# 2.8 Data-Processing Inequality

### Concept) Markov Chain
- Def.) $`X\rightarrow Y \rightarrow Z`$
  - Random variables $`X,Y,Z`$ are said to form a Markov chain in that order
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








<br>

* [Back to Elements of Information Theory](../../main.md)