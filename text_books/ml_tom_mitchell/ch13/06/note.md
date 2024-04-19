* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 13.6 Generalizing from Examples & Relationship to Dynamic Programming

### Prop.) Limits of Q Learning and Solutions
- $\hat{Q}$ : an explicit lookup table
  - Recall that [Q Learning](../03/note.md#133-q-learning) used an explicit lookup table $\hat{Q}$.
    - i.e.) a distinct table entry for every distinct input value
      - This kind of learning is called the rote learning.
  - However, rote learning has a drawback that it cannot estimate the $Q$ value for unseen state-action pairs by generalizing from those that have been seen.
    - why?)
      - We should define every state and action pair as the column and the row pair to create a table.
      - But in reality there can be infinite number of states and actions that cannot be predefined!
  - Sol.) Incorporate Other Function Approximation Algorithms
    - e.g.) [Backpropagation](../../ch04/05/note.md#452-the-backpropagation-algorithm)
      - How?)
        - Substitute a neural network for the lookup table and using each $\hat{Q}(s,a)$ update as a training example.
          - e.g.)
            1. Encode the state $s$ and the action $a$ as network inputs and train the network to output the target values of $\hat{Q}$ given by the training rules that we covered.
               - [Deterministic Case (13.3)](../03/note.md#concept-the-algorithm-for-learning-q) : $`\displaystyle \hat{Q}(s,a) \leftarrow r + \gamma \max_{a'} \hat{Q}(s',a')`$
               - [Non-Deterministic Case (13.4)](../04/note.md#algorithm) : $`\displaystyle\hat{Q}_n(s,a) \leftarrow (1-\alpha_n) \hat{Q}_{n-1}(s,a) + \alpha_n \left[ r + \gamma \max_{a'} \hat{Q}_{n-1}(s',a') \right]`$
            2. Train a separate **network for each action**, using the state as **input** and $\hat{Q}$ as **output**.
               - which has sometimes been found to be more successful in practice
            3. Train one network with the state as input, but with one $\hat{Q}$ output for each action.

<br><br>

### Concept) Offline System
- Desc.)
  - Consider the MDP with perfect knowledge of the functions $\delta(s,a)$ and $r(s,a)$.
  - In this case, the problem has primarily addressed the question of how to compute the optimal policy using the **least computational effort**, assuming the environment could be perfectly simulated and no direct interaction was required.
  - This kind of system that learns solely by simulating actions within an internal model are called **offline systems**.

<br>

### Concept) Online System
- Desc.)
  - Consider the MDP that the agent does not have knowledge of $\delta(s,a)$ and $r(s,a)$.
  - In this case our primary concern is usually **the number of real-world actions that the agent must perform to converge to an acceptable policy**, rather than the number of computational cycles it must expend.
    - More practical case!
  - Likewise, systems that learn by moving about the real environment and observing the results are typically called **online systems**.



<br><br>

### Concept) Bellman's Equation and Dynamic Programming
- Def.)
  - $`(\forall s \in S) \; V^\ast(s) = E\left[ r(s,\pi(s)) + \gamma V^\ast\left( \delta(s, \pi(s)) \right) \right]`$
- Prop.)
  - Bellman (1957) showed that the optimal policy $\pi^\ast$ satisfies the above equation and that any policy $\pi$ satisfying this equation is an optimal policy.
  - This formed the foundation for many dynamic programming approaches to solving MDPs.
- Relationship with the Reinforcement Learning)
  - The equation is similar to our definition of [the optimal policy in the reinforcement learning](../02/note.md#the-optimal-policy).
    - $\pi^\ast\equiv{\arg\max}_{\pi} V^\pi(s), \forall s$
    - $`\displaystyle \pi^\ast (s) = \arg\max_a\left[ r(s,a) + \gamma V^\ast\left( \delta(s,a) \right) \right]`$
  - Thus, the early work of reinforcement learning, which consisted mainly the [offline systems](#concept-offline-system), tried to utilize the DP methods as solutions.
    - Refer to *Barto et al. (1995)*.

<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)