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

* [Back to Machine Learning Tom Mitchell Main](../../main.md)