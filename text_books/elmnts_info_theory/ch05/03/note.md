* [Back to Elements of Information Theory](../../main.md)

# 5.3 Optimal Codes

### Problem) Finding the Prefix Code with the Minimum Expected Length
- Objective)
  - Recall that the [Kraft Inequality](../02/note.md#theorem-521-kraft-inequality) provided a sufficient condition for the existence of a codeword set with the specified set of codeword lengths.
  - We now consider the problem of finding **the prefix code with the minimum expected length**.
    - Or, finding the [D-adic distribution](#concept-d-adic-probability-distribution) closest to the distribution of $`X`$.
- Problem)
  - Finding the set of lengths $`l_1, l_2, \cdots, l_m`$ satisfying...
    - the [Kraft Inequality](../02/note.md#theorem-521-kraft-inequality)
    - its expected length $`L = \sum p_i l_i`$ is less than the expected length of any other prefix code.
  - i.e.)   
    $`\displaystyle \arg\min_{l_1, l_2, \cdots, l_m} L = \sum_i p_i l_i`$
    - where $`\sum D^{-l_i} \le 1`$
- Sol.)
  - We can set up a Lagrangian as
    - $`J = \sum p_i l_i + \lambda \left( \sum D^{-l_i} - 1 \right)`$
  - Then,   
    $`\begin{aligned}
        (1) \; & \frac{\partial J}{\partial l_i} = 0 \\
        \Leftrightarrow & \; p_i -\lambda D^{-l_i}\log_e D = 0 \\
        \Rightarrow & \; D^{-l_i} = \frac{p_i}{\lambda \log_e D} & \cdots (A) \\
        \Rightarrow & \sum D^{-l_i} =  \sum \frac{p_i}{\lambda \log_e D} = \frac{1}{\lambda \log_e D} \\
        \\
        (2) \; & \frac{\partial J}{\partial \lambda} = 0 \\
        \Leftrightarrow & \sum D^{-l_i} - 1 = 0 \\
        \Rightarrow & \sum D^{-l_i} = 1 \\
        \Leftrightarrow & \frac{1}{\lambda \log_e D} = 1 \\
        \Rightarrow & \lambda = \frac{1}{\log_e D} & \cdots (B) \\
    \end{aligned}`$
  - Plugging (B) into (A), we get
    - $`p_i = D^{-l_i}`$.
  - Therefore,   
    $`\begin{aligned}
        & l_i^\ast = -\log_D p_i \\
        \Rightarrow & L^\ast = \sum p_i l_i^\ast = -\sum p_i \log_D p_i = H_D(X)
    \end{aligned}`$
- Result)
  - The optimal codeword length is equal to the entropy $`H_D(X)`$.
- Limit)
  - The codeword length should be integer, while $`H_D(X)`$ may not be the one.
  - Instead, we provide a lower bound as [Theorem 5.3.1](#theorem-531-lower-bound-for-the-expected-length-of-instantaneous-codeword)

<br>

### Theorem 5.3.1) Lower Bound for the Expected Length of Instantaneous Codeword
- Theorem)
  - The expected length $`L`$ of any instantaneous $`D`$-ary code for a random variable $`X`$ is greater than or equal to the entropy $`H_D(X)`$.
    - i.e.) $`L \ge H_D(X)`$
      - with equality iff. $`D^{-l_i} = p_i`$
- pf.)
  - By definition,   
    $`\begin{aligned}
      L - H_D(X) &= \sum p_i l_i - \sum p_i \log_D \frac{1}{p_i} \\
      &= - \sum p_i \log_D D^{-l_i} + \sum p_i \log_D p_i
    \end{aligned}`$
  - Putting $`\displaystyle r_i = \frac{D^{-l_i}}{\sum_j D^{-l_j}} \textrm{ and } c = \sum D^{-l_i}`$, we obtain   
    $`\begin{aligned}
       -\sum p_i \log_D D^{-l_i} &= \sum p_i \log_D \frac{1}{D^{-l_i}} \\ 
      &= \sum p_i \log_D \frac{\sum_j D^{-l_j}}{D^{-l_i}} - \sum p_i \log_D \left(\sum_j D^{-l_j}\right) \\
      &= \sum p_i \log_D \frac{1}{r_i} + \log_D \frac{1}{c} & \because \sum p_i = 1 \\
    \end{aligned}`$
  - Thus,   
    $`\begin{aligned}
      L - H_D(X) &= \sum p_i \log_D \frac{1}{r_i} + \log_D \frac{1}{c} + \sum p_i \log_D p_i \\
      &= \sum p_i \log_D \frac{p_i}{r_i} + \log_D \frac{1}{c} \\
      &= D(p||r)  + \log_D \frac{1}{c} \\
      &\ge 0 & \because D(p||r) \ge 0 \textrm{ and } c \le 1
    \end{aligned}`$
    - cf.) 
      - $`D(q||r) \ge 0`$
        - Refer to the [Information inequality](../../ch02/06/note.md#theorem-263-information-inequality).
      - $`c = \sum D^{-l_i} \le 1`$
        - Refer to the [Kraft inequality](../02/note.md#theorem-521-kraft-inequality)

<br><br>

### Concept) D-adic Probability Distribution
- Def.)
  - A probability distribution is called $`D`$-adic if each of the probabilities is equal to $`D^{-n}`$ for some $`n`$.
- Prop.)
  - The equality in [Theorem 5.3.1](#theorem-531-lower-bound-for-the-expected-length-of-instantaneous-codeword) holds iff. the distribution of $`X`$ is $`D`$-adic.
  - The [above problem](#problem-finding-the-prefix-code-with-the-minimum-expected-length) is identical to finding the $`D`$-adic distribution that is closest to the distribution of $`X`$.
    - How?)
      - Construct the code by choosing the first available node as in the proof of the Kraft inequality.
      - We then have an optimal code for $`X`$.
        - Which is not easy.

<br>

* [Back to Elements of Information Theory](../../main.md)