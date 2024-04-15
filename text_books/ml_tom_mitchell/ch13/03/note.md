* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 13.3 Q-Learning

### Concept) The Q Function
- Def.)
  - $`Q(s,a) \equiv r(s,a) + \gamma V^\ast \left( \delta(s,a) \right)`$
- Application) 
  - Back to the $V^\ast$ [optimization problem](../02/note.md#the-optimal-policy).
    - We can rewrite the problem as $`\displaystyle\pi^\ast(s)=\arg\max_a Q(s,a)`$
      - Why doing this?)
        - Recall that the agent learned $V^\ast$ in the previous problem setting.
        - However, in order to learn $V^\ast$, the agent should know $r$ and $\delta$.
        - Instead, if we use $Q(s,a)$, we can select optimal actions without $r$ nor $\delta$
    - Then, the agent simply chooses $a$ for the current state $s$.
      - i.e.) The agent repeatedly chooses **local** values of $Q$ for corresponding states.
        - Ultimately, it may lead to the **global** optimum.


<br><br>

### Concept) The Algorithm for Learning Q
- Derivation)
  - Learning the $Q$ function **corresponds** to learning **the optimal policy**.
    - Recall that $`V^\ast`$ was the optimal policy.
  - Then we may assume the relationship between $Q$ and $V^\ast$ as
    - $`\displaystyle V^\ast(s)=\max_{a'} Q(s,a')`$
  - Thus, the $Q$ function can be rewritten as
    - $`\displaystyle Q(s,a) \equiv r(s,a) + \gamma V^\ast \left( \delta(s,a) \right)= r(s,a) + \gamma\max_{a'} Q(s,a')`$
- Settings)
  - $\hat{Q}$ : the learner's **estimate**, or hypothesis, of the actual $Q$ function
    - $\hat{Q}$ is represented by a large table with a separate entry for each state action pair, $`\langle s, a \rangle`$.
- Algorithm)
  - For each $`\langle s, a \rangle`$, initialize the table entry $\hat{Q}(s,a)$ to zero.
  - Observe the current state $s$
  - Do forever...
    - Select an action $a$ and execute it.
    - Receive an immediate reward $r$.
    - Observe a new state $s'$.
    - Update the table entry for $`\hat{Q}(s,a)`$ as follows:
      - $`\displaystyle \hat{Q}(s,a) \leftarrow r + \gamma \max_{a'} \hat{Q}(s',a')`$
- Prop.)
  - This is a recursive algorithm.

<br><br>

### E.g.) An Illustrative Example
<img src="images/001.png" width="600px">

- Settings)
  - $\gamma = 0.9$ : the discount rate
  - $\mathbf{R}$, a robot, is in a six-grid-world
    - $\mathbf{R}$ moves to one adjacent cell
    - The immediate reward $r=0$ for every move in the grid.
    - Suppose $\mathbf{R}$ is located at the upper-leftmost cell.
    - If it moves right, it gets an immediate reward of $0$ for the transition, i.e. $r=0$.
    - Then, it refine its estimate $\hat{Q}$ for $s=s_1$ and $a=a_{right}$.
      - i.e.) $`\hat{Q}(s_1, a_{right}) = 0 + 0.9 \cdot \max_{a'} \hat{Q}(s_2, a') = 0 + 0.9\cdot 100 = 90`$
- Prop.)
  - Each time the agent moves **forward** from an old state to a new one, $Q$ learning propagates $`\hat{Q}`$ **backward** from the new state to the old.
  - The immediate reward $r$ received by the agent for the transition is used to augment these propagated values of $Q$.
    - In this example $r=0$.

<br><br>

### Prop.) Convergence of Q
#### Lemma 1)
- $`\left(\forall s, a, n \right) \hat{Q}_{n+1}(s,a) \ge \hat{Q}_{n}(s,a)`$
  - Desc.)
    - $\hat{Q}$ values never decrease during learning.
      - why?) $`\displaystyle \hat{Q}=r+\gamma \max_{a'} Q(s,a')`$
    - It holds for any deterministic [MDP](../02/note.md#concept-markov-decision-process-mdp).

#### Lemma 2)
- $`\left(\forall s, a, n \right) 0 \le \hat{Q}_{n}(s,a) \le Q(s,a)`$
  - Desc.)
    - It also holds for any deterministic [MDP](../02/note.md#concept-markov-decision-process-mdp).




<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)