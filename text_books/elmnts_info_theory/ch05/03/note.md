* [Back to Elements of Information Theory](../../main.md)

# 5.3 Optimal Codes

### Problem) Finding the Prefix Code with the Minimum Expected Length
- Objective)
  - Recall that the [Kraft Inequality](../02/note.md#theorem-521-kraft-inequality) provided a sufficient condition for the existence of a codeword set with the specified set of codeword lengths.
  - We now consider the problem of finding **the prefix code with the minimum expected length**.
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














<br>

* [Back to Elements of Information Theory](../../main.md)