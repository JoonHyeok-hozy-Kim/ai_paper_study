* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 11.1 Introduction

#### Limits of the Inductive Learning Methods
- Review)
  - Inductive Learning Methods
    - Desc.)
      - Methods that generalize from observed training examples by identifying features that empirically distinguish positive from negative training examples.
    - e.g.)
      - [Decision Tree Learning](../../main.md#3-decision-tree-learning)
      - [Neural Network Learning](../../main.md#4-artificial-neural-networks-anns)
      - [Inductive Logic Programming](../../ch10/04/note.md#concept-inductive-logic-program-ilp)
      - [Genetic Algorithms](../../main.md#9-genetic-algorithms)
- Limit)
  - Inductive Learning Methods perform poorly when insufficient data is available.
    - There are [fundamental bounds on the accuracy](../../ch07/03/note.md#concept-general-bound-on-the-number-of-training-examples-for-successful-consistent-learner) that can be achieved when learning inductively from a given number of training examples.
- Alternative)
  - Develop learning algorithms that accept **explicit prior knowledge as an input**, in addition to the input training data.
    - e.g.)
      - [Explanation-Based Learning](#concept-explanation-based-learning-ebl) below

<br><br>

### Concept) Explanation-Based Learning (EBL)
- Desc.)
  - It uses prior knowledge to **explain** each training example in order to infer which example features are relevant to the target function and which are irrelevant.
  - These **explanations** enable it to generalize more accurately than inductive systems that rely on the data alone.
- Prop.) 
  - Background Knowledge Usage Comparison with the [ILP](../../ch10/04/note.md#concept-inductive-logic-program-ilp)
    - **ILP** used prior background knowledge to **increase** the complexity of the hypothesis space to be searched.
      - How?)
        - By infer features that augment the input descriptions of instances
    - **EBL** uses prior knowledge to **reduce** the complexity of the hypothesis space to be searched, thereby reducing sample complexity and improving generalization accuracy of the learner. 
- e.g.) Chess
  - Consider a chess program.
  - We want it to learn to recognize the target concept : "chessboard positions in which black will lose its queen within two moves"
    - e.g.)   
      <img src="images/001.png" width="300px"></img>
  - Learning such concept is complex in the inductive learning's perspective.
    - why?)
      - The chessboard is fairly complex.
      - The particular patterns that capture this concept are fairly subtle.
      - We would have to provide thousands of training examples similar to the one above to expect an inductively learned hypothesis to generalize correctly to new situations.
  - But we humans learn such target concepts from just a handful of training examples.
    - How humans can **generalize** so successfully from just few examples?
      - People rely heavily on **explaining** the training example in terms of their **prior knowledge** about the legal moves of chess.
        - e.g.)
          - "Because white's knight is attacking both the king and queen, black must move out of check, thereby allowing the knight to capture the queen."
      - i.e.)
        - Humans provide the information needed to **rationally** generalize from the details of the training example to a correct general hypothesis.
          - Explanations **relevant** to the target concepts are mentioned.
          - Ones **irrelevant** to the target concepts are NOT mentioned.
  - Then what is the prior knowledge?
    - It is simply knowledge about the legal rules of chess: 
      - Which moves are legal for the knight and other pieces. 
      - Players must alternate moves in the game.
      - To win the game, one player must capture his opponent's king.
    - Given just this prior knowledge it is possible in **principle** to calculate the optimal chess move for any board position.
      - However, in **practice** this calculation can be frustratingly complex and despite the fact that we humans ourselves possess this complete, perfect knowledge of chess, we remain unable to play the game optimally.
      - As a result, much of human learning in chess involves a long process of uncovering the consequences of our prior knowledge, guided by specific training examples encountered as we play the game.

<br><br>

## 11.1.1 Inductive and Analytical Learning Problems
### Analysis) Inductive Learning Problem vs Analytical Learning Problem
- Differences in Formulations of the Learning Problem
  |IO|[Inductive Learning Program](../../ch10/04/note.md#concept-inductive-logic-program-ilp)|[Analytical Learning Program (EBL)](#concept-explanation-based-learning-ebl)|
  |:-:|-|-|
  |Input|- $H$ : a hypothesis space <br> - $`D=\{\langle x_1, f(x_1)\rangle, \cdots, \langle x_n, f(x_n)\rangle\}`$ : training examples|- $H$ : a hypothesis space <br> - $`D=\{\langle x_1, f(x_1)\rangle, \cdots, \langle x_n, f(x_n)\rangle\}`$ : training examples <br> - $B$ : a domain theory consisting of background knowledge that can be used to explain observed training examples.|
  |Output|- $h\in H$ consistent with $D$|- $h\in H$ consistent with both $D$ and $B$|
- Prop.)
  - $H$ is defined to consist of sets of [Horn clauses](../../ch10/04/note.md#prop-horn-clause-representation).
  - If $B$ does not entail the negation of $h$ $`(\textrm{i.e. } B \nvdash \neg h)`$, then $h$ is consistent with $B$.
    - Effect)
      - If the domain theory $B$ is correct, then it increases the accuracy of the output hypothesis.



<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)