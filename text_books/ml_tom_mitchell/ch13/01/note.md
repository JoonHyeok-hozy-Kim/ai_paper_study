* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 13.1 Introduction

#### Key Quetsion)
How can an **autonomous agent** that senses and acts in its **environment** **learn** to choose optimal actions to achieve its goals?
- Each time the agent performs an action in its environment, a trainer may provide a 
**reward** or **penalty** to indicate the desirability of the resulting state.

<br>

#### Model)
- Settings)
  - An Agent
    - It has 
      - a set of sensors to observe the **state** of its environment
        - e.g.) a camera or a sonar
      - a set of **actions** it can perform to alter this state
        - e.g.) "move forward" or "turn"
  - Task)
    - Learn a control strategy, or **policy**, for choosing actions that achieve its goals.
      - e.g.) "Docking onto its battery charger whenever its battery level is low"
- Assumptions)
  - The goals of the agent can be defined by a **reward** function that assigns a numerical value to each distinct action the agent may take from each distinct state.
    - Maximize cumulative reward!
- Structure)
  - $\pi : S \rightarrow A$ : the target function
    - where 
      - $S$ : a set of states
        - $s\in S$
      - $A$ : a set of actions
        - $a\in A$
    - Distinctive Props.)
      - Delayed Reward
        - Task : Learn $\pi$ s.t. $a=\pi(s)$
          - cf.) In reinforcement learning the training example is NOT provided in form $\langle s, \pi(s)\rangle$.
            - Instead, the trainer provides only a sequence of immediate reward values as the agent executes its sequence of actions.
            - Therefore, the agent faces the problem of **temporal credit assignment**: determining which of the actions in its sequence are to be credited with producing the eventual rewards.
      - Exploration
        - The agent influences the distribution of training examples by the action sequence it chooses.
        - The learner faces a tradeoff in choosing whether to favor...
          1. **exploration** of unknown states and actions 
             - to gather new information
          2. **exploitation** of states and actions that it has already learned will yield high reward 
             - to maximize its cumulative reward
      - Partially Observable States
        - In many practical situations sensors provide only partial information.
        - In such cases, it may be necessary for the agent to consider its previous observations together with its current sensor data when choosing actions, and the best policy may be one that chooses actions specifically to improve the observability of the environment.
      - Life-Long Learning
        - Unlike isolated function approximation tasks, robot learning often requires that the robot learn several related tasks within the same environment, using the same sensors.
        - This setting raises the possibility of using previously obtained experience or knowledge to **reduce sample complexity** when learning new tasks.








<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)