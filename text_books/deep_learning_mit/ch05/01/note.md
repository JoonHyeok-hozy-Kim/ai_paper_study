* [Back to Deep Learning MIT](../../main.md)

# 5.1 Learning Algorithms

### Concept) Machine Learning
- Def.)
  - An algorithm that is able to learn from data.
  - A computer program is said to learn from [experience](#513-the-experience) $`E`$ w.r.t. some class of [task](#511-the-task)s $`T`$ and [performance measure](#512-the-performance-measure) $`P`$, 
    - if its performance at [task](#511-the-task)s in $`T`$, as [measured](#512-the-performance-measure) by $`P`$, improves with [experience](#513-the-experience) $`E`$.

<br>

## 5.1.1 The Task
- Desc.)
  - Machine learning **tasks** are usually described in terms of how the machine learning system should process an **example**.
    - where an **example** is a collection of **features** that have been quantitatively measured from some object or event that we want the machine learning system to process.
      - $`x\in\mathbb{R}^n`$ : an example
        - where each entry $`x_i`$ denotes a feature.
- Types)
  - Classification
    - The computer program is asked to specify which of $`k`$ categories some input belongs to.
    - To solve this task, the learning algorithm is usually asked to produce a function $`f:\mathbb{R}^n\rightarrow\lbrace1,\cdots, k\rbrace`$.
  - Classification with missing inputs
    - A Classification task not guaranteed that every measurement in its input vector will always be provided.
    - Sol.)
      - Define a single function $`f:\mathbb{R}^n\rightarrow\lbrace1,\cdots, k\rbrace`$.
      - When some of the inputs may be missing, rather than providing a single classification function, the learning algorithm must learn **a set of functions**.
        - where each function corresponds to classifying $`x`$ with a different subset of its inputs missing.
          - e.g.) Define such a large set of functions with a probability distribution
            - Learn a probability distribution over all of the relevant variables.
            - Solve the classification task by marginalizing out the missing variables.
              - cf.) With $`n`$ input variables, we can now obtain all $`2^n`$ different classification functions needed for each possible set of missing inputs, but we only need to learn a single function describing the joint probability distribution.
  - Regression
    - The computer program is asked to predict a **numerical value** given some input.
    - Sol.)
      - Define a function $`f:\mathbb{R}^n\rightarrow\mathbb{R}`$.
  - Transcription
    - The machine learning system is asked to observe a relatively unstructured representation of some kind of data and transcribe it into discrete, textual form.
    - e.g.)
      - OCR
  - Machine Translation
    - The input already consists of a sequence of symbols in some language, and the computer program must **convert** this into a sequence of symbols in another language.
  - Structured Output
    - Structured output tasks involve any task where the output is a vector (or other data structure containing multiple values) with important relationships between the different elements.
      - e.g.)
        - Parsing
          - Mapping a natural language sentence into a tree that describes its grammatical structure and tagging nodes of the trees as being verbs, nouns, or adverbs, and so on.
  - Anomaly Detection
    - The computer program sifts through a set of events or objects, and flags some of them as being unusual or atypical.
  - Synthesis and sampling
    - The machine learning algorithm is asked to generate new examples that are similar to those in the training data.
  - Imputation of missing values
    - The machine learning algorithm is given a new example $`x\in\mathbb{R}^n`$ but with some entries $`x_i`$ of $`x`$ missing.
  - Denoising
    - The machine learning algorithm is given in input a corrupted example $`\tilde{x}\in\mathbb{R}^n`$ obtained by an unknown corruption process from a clean example $`x\in\mathbb{R}^n`$
    - The learner must predict the clean example $`x`$ from its corrupted version $`\tilde{x}`$.
      - Or more generally predict the conditional probability distribution $`p(x|\tilde{x})`$.
  - Density estimation (probability mass function estimation)
    - The machine learning algorithm is asked to learn a function $`p_{\textrm{model}} : \mathbb{R^n}\rightarrow\mathbb{R}`$
      - where $`p_{\textrm{model}}(x)`$ can be interpreted as a probability density(mass) function on the space that the examples were drawn from.


<br>

## 5.1.2 The Performance Measure
- Desc.)
  - In order to evaluate the abilities of a machine learning algorithm, we must design a quantitative measure of its performance.
  - Usually this performance measure $`P`$ is specific to the task $`T`$ being carried out by the system.
- e.g.)
  - Accuracy
    - The **proportion of** examples for which the model produces the **correct output**.
  - Error Rate
    - The proportion of examples for which the model produces an incorrect output.
    - Also known as $`0-1`$ loss.
      - i.e.) $`0`$ if correct, $`1`$ otherwise. 



<br>

## 5.1.3 The Experience
- Concepts)
  - The **experience** $`E`$ can categorize the ML into [supervised](#concept-supervised-learning-algorithms) and [unsupervised](#concept-unsupervised-learning-algorithms) learning.
  - A **dataset** is a collection of many examples.

<br>

### Concept) Unsupervised Learning Algorithms
- Desc.)
  - **Unsupervised learning algorithms** experience a dataset containing many features, then learn useful properties of the structure of this dataset.
- How?)
  - Examples of random vector $`x`$ are provided.
  - The algorithm should implicitly or explicitly learn the probability distribution $`p(x)`$.
- e.g.)
  - Deep Learning
    - We want to learn the **probability distribution** that generated the dataset.
      - explicit way : density estimation
      - implicit way : synthesis, denoising
  - Clustering


<br>

### Concept) Supervised Learning Algorithms
- Desc.)
  - **Supervised learning** algorithms experience a dataset containing features, but each example is also **associated with a label or target**.
- How?)
  - Examples of a random vector $`x`$ and an associated value or a vector $`y`$ are provided.
  - The algorithm should estimate $`p(y|x)`$ to predict $`y`$ from $`x`$.


<br>

### Concept) Combination of Unsupervised and Supervised Learning
- Many machine learning technologies can be used to perform both tasks.
- e.g.)
  - [Joint Probability Decomposition](../../../elmnts_info_theory/ch02/05/note.md#prop-general-multiplication-law-of-conditional-probabilities).
    - Consider that $`\displaystyle p(x) = \prod_{i=1}^n p(x_i|x_1, \cdots, x_{i-1})`$.
    - The LHS $`p(x)`$ is the joint probability, which is the target of the [unsupervised learning](#concept-unsupervised-learning-algorithms).
    - Meanwhile, the RHS is the product of conditional probabilities, which is the target of the [supervised learning](#concept-supervised-learning-algorithms).
    - Thus, this decomposition means that we can solve the unsupervised problem of modeling $`p(x)`$ by splitting it into $`n`$ supervised learning problems.
  - Bayes Rule
    - Recall that $`\displaystyle p(y|x) = \frac{p(x,y)}{\sum_{y'} p(x,y')}`$
    - With the unsupervised learning, we can learn $`p(x,y)`$.
    - Using this result, we can derive $`p(y|x)`$, which is the supervised learning problem.

<br>

### Concept) Design Matrix
- Def.)
  - A design matrix is a matrix containing a different example in each row.
  - Each column denotes the features.
- e.g.)
  - 150 examples with four features : $`X\in \mathbb{R}^{150 \times 4}`$
    - $`X_{i,j}`$ : the $`j`$-th feature of the $`i`$-th example.

<br><br>

## 5.1.4 Example: Linear Regression
- Goal)
  - Build a system that
    - take a vector $`x\in\mathbb{R}^n`$ as input
    - predict the value of a scalar $`y\in\mathbb{R}`$ as output
- Settings)
  - $`\hat{y} = w^\top x`$ : a linear function model
    - where
      - $`w \in \mathbb{R}^n`$ : a vector of parameters
        - $`w_i`$ is the coefficient of the feature $`x_i`$
          - $`w_i \lt 0`$ : Decreasing the value of $`x_i`$ decreases $`\hat{y}`$.
          - $`w_i = 0`$ : $`x_i`$ has no impact on $`\hat{y}`$.
          - $`w_i \gt 0`$ : Increasing the value of $`x_i`$ increases $`\hat{y}`$.
  - $`X^{(\textrm{test})}`$ : a [design matrix](#concept-design-matrix) of test set.
    - $`y^{(\textrm{test})}`$ : the vector with associated values of $`X^{(\textrm{test})}`$
- Model)
  - Minimize the mean squared error (MSE).
    - $`\displaystyle\textrm{MSE} = \frac{1}{m} \sum_i (\hat{y} - y)^2_i`$
      - which optimization problem is identical to $`\displaystyle\textrm{MSE} = \frac{1}{m} ||\hat{y} - y||^2_2`$ : the Euclidean distance between the prediction and the target.
  - How?)
    - Train the model with the training set.
      - $`\displaystyle \min_w \textrm{MSE}_{(\textrm{train})} = \frac{1}{m} ||\hat{y}^{(\textrm{train})} - y^{(\textrm{train})}||^2_2`$
        - How?)
          - Get $`w`$ where its gradient is $`0`$.   
            $`\begin{array}{ll}
              \nabla_w \textrm{MSE}_{(\textrm{train})} = 0 \\
              \Rightarrow \nabla_w \frac{1}{m} ||\hat{y}^{(\textrm{train})} - y^{(\textrm{train})}||^2_2 = 0 \\
              \Rightarrow \nabla_w \frac{1}{m} ||X^{(\textrm{train})}w - y^{(\textrm{train})}||^2_2 = 0 \\
              \Rightarrow \nabla_w \left( X^{(\textrm{train})}w - y^{(\textrm{train})} \right)^\top \left( X^{(\textrm{train})}w - y^{(\textrm{train})} \right) = 0 \\
              \Rightarrow \nabla_w \left( w^\top {X^{(\textrm{train})}}^\top X^{(\textrm{train})}w -2w^\top {X^{(\textrm{train})}}^\top y^{(\textrm{train})} + {y^{(\textrm{train})}}^\top y^{(\textrm{train})} \right) = 0 \\
              \Rightarrow 2 {X^{(\textrm{train})}}^\top X^{(\textrm{train})}w -2{X^{(\textrm{train})}}^\top y^{(\textrm{train})} = 0 \\
              \Rightarrow w = {\left({X^{(\textrm{train})}}^\top X^{(\textrm{train})}\right)}^{-1} {X^{(\textrm{train})}}^\top y^{(\textrm{train})} \\
            \end{array}`$
        - One can add **bias** and by using an affine function.
          - $`\hat{y} = w^\top x + b`$
    - Test its performance with the test set.
      - $`\displaystyle\textrm{MSE}_{(\textrm{test})} = \frac{1}{m} ||\hat{y}^{(\textrm{test})} - y^{(\textrm{test})}||^2_2`$




<br>

* [Back to Deep Learning MIT](../../main.md)