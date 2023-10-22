* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 1.2 Designing a Learning System

## 1.2.1 Choosing the Training Experience
#### Concept) Key Attributes for Choosing Training Experience
1. Providing **direct or indirect feedback** regarding the choices made by the performance system.
   * Direct Feedback
     * Typically easier compared to the Indirect Feedback
   * Indirect Feedback
     * The learner faces the problem of Credit Assignment
       * i.e.) Determining the degree to which each move in the sequence deserves credit or blame for the final outcome
2. The degree to which the learner controls the sequence of training examples.
   * i.e.) Is there a teacher that helps the learner? If so, how supportive the teacher will help the learner?
3. How well the experience represents the **distribution** of examples over which the final system performance $P$ must be measured.
   * In general, learning is most reliable when the training examples follow a **distribution** similar to that of future test examples.
     * If the distributions of $E$ and $P$ are completely different, the test result will be very poor.
   * But in reality, we often learn from a distribution of examples that is somewhat different from those on which the final system will be evaluated.

<br>

#### Ex.) Checker Game Revisited
* Settings
  * Task $T$: playing checkers 
  * Performance measure $P$: percent of games won in the world tournament 
  * Training experience $E$: games played against itself 
* Attributes that should be determined
  1. the exact type of knowledge to be learned 
  2. a representation for this target knowledge 
  3. a learning mechanism


<br>

### 1.2.2 Choosing the Target Function
* What we should determine 
  1. What type of knowledge will be learned 
  2. How this will be used by the performance program

#### Ex.) Checker Game
* Definitions
  * Legal Moves : the moves that are allowed in the game
* Target Function
  * Ideal
    * $ChooseMove : B \rightarrow M$
      * where $B$ is the set of board states
      * and $M$ is the set of legal moves. 
    * Prop.
      * $ChooseMove$ is very difficult to learn given the indirect training experience.
  * Alternative
    * $V : B \rightarrow \mathbb{R}$
      * An evaluation function that assigns a numerical score to any given board state.
      * Make it assign higher scores to better board states.
      * How to assign the score.
        * Ex.1) For $b \in B$ : a board state
          * Methodology)
            * If $b$ is a final board state that is won, then $V(b)=100$.
            * If $b$ is a final board state that is lost, then $V(b)=-100$.
            * If $b$ is a final board state that is drawn, then $V(b)=0$.
            * If $b$ is not a final board state, then $V(b)=V(b')$ where $b'$ is the best final board state that can be achieved starting from $b$ and playing optimally until the end of the game.
          * Problem)
            * Inefficient!
              * Needs the specification of $V(b), \forall b \in B$
              * A.K.A. **nonoperational definition**
            * Instead, we need **operational description** of the ideal target function $V$.
              * i.e.) a description that can be used by the checkers-playing program to evaluate states and select moves within realistic time bounds
            * However, obtaining the **operational description** is very difficult.
              * Solution : Approximation
      * $\hat{V}$ : function approximation of $V$
        * The function that is actually learned by our program approximating to the ideal function $V$

<br><br>

### 1.2.3 Choosing a Representation for the Target Function
* What we should determine
  * A representation that the learning program will use to describe the function $\hat{V}$ that it will learn

<br>

#### Concept) Trade-Off when Choosing the Representation
* Trade-off between
  * Choosing a expressive representation which approximation is very close to the ideal target function $V$.
  * The increase of the amount of data required to choose the most expressive representation among the alternative hypotheses.

<br>

#### Ex.) Checker Game
* The Representation
  * $\hat{V}(b) = w_0 + w_1x_1 + w_2x_2 + w_3x_3 + w_4x_4 + w_5x_5 + w_6x_6$
    * where $x_1$ : the number of black pieces on the board
    * $x_2$ : the number of red pieces on the board
    * $x_3$ : the number of black kings on the board 
    * $x_4$ : the number of red kings on the board
    * $x_5$ : the number of black pieces threatened by red
    * $x_6$ : the number of red pieces threatened by black
    * $w_0, ..., w_6$ : weights
* Overall Program
  * Task $T$: playing checkers 
  * Performance measure $P$: percent of games won in the world tournament
  * Training experience $E$: games played against itself 
  * Target function: $V : B \rightarrow \mathbb{R}$
  * Target function representation
    * $\hat{V}(b) = w_0 + w_1x_1 + w_2x_2 + w_3x_3 + w_4x_4 + w_5x_5 + w_6x_6$

<br><br>

### 1.2.4 Choosing a Function Approximation Algorithm






<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)