* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 13.5 Temporal Difference Learning

### Concept) Temporal Difference Algorithm
- Def.)
  - An algorithm that learns by reducing discrepancies between estimates made by the agent at different times.
- Desc.)
  - [Q Learning](../03/note.md#133-q-learning) is a special case of a temporal difference algorithm.
    - Why?)
      - Its training rule reduces the difference between the estimated $\hat{Q}$ values of a state and its immediate successor.

#### Question)
Then, can we design an algorithm that reduces the discrepancies between the current state and more distant descendants or ancestors?
- Sol.) [TD(λ)](#concept-tdλ)

<br>

### Concept) TD(λ)
*Sutton (1988)*
- Def.)
  - The Training Value Calculated by $n$-step lookahead.
    - One-Step : $`\displaystyle Q^{(1)}(s_t, a_t) \equiv r_t + \gamma \max_a \hat{Q}(s_{t+1},a)`$
    - Two-Step : $`\displaystyle Q^{(2)}(s_t, a_t) \equiv r_t + \gamma r_{t+1} + \gamma^2 \max_a \hat{Q}(s_{t+2},a)`$
    - $n$-Step : $`\displaystyle Q^{(n)}(s_t, a_t) \equiv r_t + \gamma r_{t+1} + \cdots + \gamma^{n-1} r_{t+n-1} + \gamma^n \max_a \hat{Q}(s_{t+n},a)`$
  - The $`TD(\lambda)`$
    - For $`0 \le \lambda \le 1`$   
      $`\begin{array}{ll}
          Q^\lambda(s_t, a_t) &\equiv (1-\lambda) \left[ Q^{(1)}(s_t, a_t) + \lambda Q^{(2)}(s_t, a_t)  + \lambda^2 Q^{(3)}(s_t, a_t) + \cdots \right] \\
          & = r_t + \gamma \left[ (1-\lambda) \displaystyle\max_a \hat{Q}(s_t, a_t) + \lambda Q^\lambda(s_{t+1}, a_{t+1}) \right]
      \end{array}`$
- Prop.)
  - If $\lambda = 0$, $Q^\lambda(s_t, a_t) = Q^{(1)}(s_t, a_t)$
    - Meaning)
      - We will consider only one-step discrepancies in the $\hat{Q}$ estimates.
  - If $\lambda = 1$,  only the observed $r_{t+i}$ values are considered, with no contribution from the current $\hat{Q}$ estimate.
    - Meaning)
      - Considering the discrepancies between the current state and the MOST distant descendants.
      - If the agent is following the optimal policy $(\hat{Q}= Q)$, the training values given by $Q^\lambda$ will be identical for all values of $\lambda$ such that $0\le \lambda \le 1$.
        - i.e.) The faster algorithm with perfect accuracy!





<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)