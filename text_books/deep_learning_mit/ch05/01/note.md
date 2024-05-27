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





<br>

* [Back to Deep Learning MIT](../../main.md)