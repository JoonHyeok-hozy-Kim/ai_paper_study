* [Back to Elements of Information Theory](../../main.md)

# 2.7 Log Sum Inequality and its Applications

### Theorem 2.7.1) Log Sum Inequality
- For non-negative numbers $`a_1, a_2, \cdots, a_n`$ and $`b_1, b_2, \cdots, b_n`$,
  - $`\displaystyle\sum_{i=1}^n a_i \log\frac{a_i}{b_i} \ge \left(\sum_{i=1}^n a_i \right) \log\frac{\sum_{i=1}^n a_i}{\sum_{i=1}^n b_i}`$
    - with equality iff. $`\exists c\in\mathbb{R} \textrm{ such that } \frac{a_i}{b_i}=c`$
    - cf.) Convention
      - $`0\log0 = 0`$
      - $`a\log\frac{a}{0}=\infty \textrm{ if } a\gt0`$
      - $`0\log\frac{0}{0}=0`$
- pf.)
  - Assume without loss of generality that $`a_i \gt 0`$ and $`b_i \gt 0`$.
  - Consider that $`f(t) = t\log{t}`$ is strictly convex for all positive $`t\gt 0`$.
    - why?)
      - $`f''(t) = \frac{1}{t}\log e \gt 0`$
  - Also, by the [Jensen's Inequality](../06/note.md#theorem-262-jensens-inequality),
    - for $`\alpha_i \ge 0, \sum_i \alpha_i = 1`$
      - $`\displaystyle\sum \alpha_i f(t_i) \ge f\left(\sum\alpha_i t_i \right)`$
  - Putting $`\displaystyle\alpha_i = \frac{b_i}{\sum_{j=1}^n b_j}`$ and $`\displaystyle t_i = \frac{a_i}{b_i}`$
    - LHS   
      $`\begin{aligned}
        \sum \alpha_i f(t_i) &= \sum \left(\frac{b_i}{\sum b_j}\right) \left(\frac{a_i}{b_i}\right) \left(\log\frac{a_i}{b_i}\right) \\
        &= \sum \frac{a_i}{\sum b_j} \log\frac{a_i}{b_i}
      \end{aligned}`$
    - RHS   
      $`\begin{aligned}
        f\left(\sum\alpha_i t_i \right) &= \left(\sum\alpha_i t_i\right) \log\left(\sum\alpha_i t_i\right) \\
        &= \left(\sum\frac{a_i}{\sum b_j}\right) \log\left(\sum \frac{a_i}{\sum b_j} \right) \\
        &= \frac{\sum a_i}{\sum b_j} \log\left(\frac{\sum a_i}{\sum b_j} \right)
      \end{aligned}`$
  - Dividing both sides with $`\sum b_j \gt 0`$, we get
    - $`\displaystyle \sum a_i\log\frac{a_i}{b_i} \ge \left(\sum a_i\right) \log\left(\frac{\sum a_i}{\sum b_j} \right)`$

<br><br>

### Theorem 2.7.2) Convexity of Relative Entropy
$`D(p||q)`$ is convex in the pair $`(p,q)`$.    
- i.e.)
  - If $`(p_1, q_1)`$ and $`(p_2, q_2)`$ are two pairs of probability mass functions,
    - then $`D(\lambda p_1 + (1-\lambda)p_2 || \lambda q_1 + (1-\lambda)q_2) \le \lambda D(p_1||q_1) + (1-\lambda) D(p_2 || q_2)`$ 
      - $`\forall 0\le\lambda\le1`$
- pf.)   
  $`\begin{aligned}
        D(\lambda p_1 + (1-\lambda)p_2 || \lambda q_1 + (1-\lambda)q_2) &= \left( \lambda p_1(x) + (1-\lambda) p_2(x) \right) \log\frac{\lambda p_1(x) + (1-\lambda) p_2(x)}{\lambda q_1(x) + (1-\lambda) q_2(x)} \\
        &\le \lambda p_1(x)\log\frac{\lambda p_1(x)}{\lambda q_1(x)} + (1-\lambda) p_2(x)\log\frac{(1-\lambda) p_2(x)}{(1-\lambda) q_2(x)} & \because \textrm{Log Sum Inequality} \\
        &= \lambda p_1(x)\log\frac{p_1(x)}{q_1(x)} + (1-\lambda) p_2(x)\log\frac{p_2(x)}{q_2(x)} \\
        &= \lambda D(p_1(x) || q_1(x)) + (1-\lambda) D(p_2(x) || q_2(x)) \\
    \end{aligned}`$
  - cf.) Recall the [Log Sum Inequality](#theorem-271-log-sum-inequality)
    - Put $`\begin{cases}
        a_i = \lambda p_1(x) + (1-\lambda) p_2(x) \\
        b_i = \lambda q_1(x) + (1-\lambda) q_2(x) \\
    \end{cases}`$

<br><br>

### Theorem 2.7.3) Concavity of Entropy
$`H(p)`$ is a concave function of $`p`$.
- pf.)
  - Recall [Theorem 2.6.4](../06/note.md#theorem-264) that
    - $`H(p) = \log|\mathcal{X}| - D(p||u)`$
      - where $`u`$ is the uniform distribution on $`|\mathcal{X}|`$ outcomes.
  - $`\log|\mathcal{X}|`$ is a constant.
  - $`D(p||u)`$ is convex.
  - Therefore, $`H(p)`$ is a concave.
- Alternative pf.)
  - Let
    - $`X_1`$ : a random variable with distribution $`p_1`$ taking on values in a set $`A`$.
    - $`X_2`$ : a random variable with distribution $`p_2`$ taking on values in a set $`A`$.
    - $`\theta = \begin{cases}
        1 & \textrm{with probability } \lambda \\
        2 & \textrm{with probability } 1-\lambda \\
    \end{cases}`$
    - $`Z = X_\theta`$.
  - Then the distribution of $`Z`$ is $`\lambda p_1 + (1-\lambda) p_2`$.
  - Also, $`H(Z) \ge H(Z|\theta)`$.
    - which is equivalent to $`H(\lambda p_1 + (1-\lambda) p_2) \ge \lambda H(p_1) + (1-\lambda) H(p_2)`$.
      - i.e.) $`H`$ is concave.

<br><br>

### Theorem 2.7.4) Convexity / Concavity of Mutual Information
Let $`(X,Y) \sim p(x,y) = p(x)p(y|x)`$.   
The mutual information $`I(X;Y)`$ is   
1. a concave function of $`p(x)`$ for fixed $`p(y|x)`$
2. a convex function of $`p(y|x)`$ for fixed $`p(x)`$.

- pf)
  - Recall that $`I(X;Y) = H(Y) - H(Y|X) = H(Y) - \sum_x p(x) H(Y|X=x)`$
  - If $`p(y|x)`$ is fixed...
    - $`\displaystyle p(y) = \frac{p(y|x)p(x)}{p(x|y)}`$ is a linear function of $`p(x)`$.
    - [Recall](#theorem-273-concavity-of-entropy) that $`H(Y)`$ is a concave function of $`p(y)`$.
    - Thus, $`H(Y)`$ is a concave function of $`p(x)`$.
    - Also, $`\sum_x p(x) H(Y|X=x)`$ is linear to $`p(x)`$.
    - Therefore, $`I(X;Y)`$ is a concave function of $`p(x)`$ for fixed $`p(y|x)`$.
  - If $`p(x)`$ is fixed... 
    - Consider two different conditional distributions : $`p_1(y|x)`$, $`p_2(y|x)`$
      - Then the corresponding joint distributions are
        - $`p_1(x,y) = p(x)p_1(y|x)`$
        - $`p_2(x,y) = p(x)p_2(y|x)`$
      - And their respective marginals are 
        - $`p(x), p_1(y)`$
        - $`p(x), p_2(y)`$
    - Consider another conditional distribution
      - $`p_\lambda(y|x) = \lambda p_1(y|x) + (1-\lambda) p_2(y|x)`$ for $`0 \le \lambda \le 1`$.
      - The corresponding joint distribution goes
        - $`p_\lambda(x,y) = \lambda p_1(x,y) + (1-\lambda)p_2(x,y)`$
      - And the distribution of $`Y`$ goes
        - $`p_\lambda(y) = \lambda p_1(y) + (1-\lambda) p_2(y)`$.
      - Thus, if we put $`q_\lambda(x,y) = p(x)p_\lambda(y)`$,
        - $`q_\lambda(x,y) = \lambda q_1(x,y) + (1-\lambda)q_2(x,y)`$.
      - Since the [mutual information is the relative entropy between the joint distribution and the product of marginals](../03/note.md#concept-mutual-information),
        - $`I(X;Y) = D(p_\lambda(x,y) || q_\lambda(x,y))`$.
      - Recall that the relative entropy $`D(p||q)`$ is a convex function of $`(p,q)`$.
        - Thus, the mutual information is a convex function of the conditional distribution.



<br>

* [Back to Elements of Information Theory](../../main.md)