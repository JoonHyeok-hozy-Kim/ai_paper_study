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
        & \frac{\partial J}{\partial l_i} = 0 \\
        \Leftrightarrow & \; p_i -\lambda D^{-l_i}\log_e D = 0 \\
    \end{aligned}`$














<br>

* [Back to Elements of Information Theory](../../main.md)