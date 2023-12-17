* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 6.10 An Example: Learning to Classify Text
- A general algorithm for learning to classify text, based 
on the [naive Bayes classifier](../09/note.md#69-naive-bayes-classifier)

<br>

#### Setting)
- $X$ : an instance space consisting of all possible text documents.
  - Here, the text documents denote all possible strings of words and punctuation of all possible lengths.
- $V$ : the training set
  - We are given training examples of some unknown target function $f(x)$.
  - Each training example will be $\langle x_j, v_j \rangle$
    - where 
      - $x \in X$ 
      - $v_j$ is the target value.

#### Objective)
  - Learn from these training examples to predict the target value for subsequent text documents.
    - e.g.)
      - classifying documents as interesting or uninteresting to a particular person, using the target values *like* and *dislike* to indicate these two classes.

<br>

#### Assumptions)
  1. The word probabilities for one text position are independent of the words that occur in other positions, given a document classification.
     - cf.) Very unrealistic.
       - why?) E.g., the probability of observing the word "learning" in some position may be greater if the preceding word is "machine." 
     - Still, for the simplicity of the model, we use this assumption.
     - Even thought the assumption is unrealistic, the model's performance is good!
  2. The probability of encountering a specific word is independent of the specific word position being considered.
     - This allows us to further assume that the attributes are independent and identically distributed, given the target classification.

<br>

#### The Model)
- Idea)
  - Given a text document, define an attribute for each **(1)word position** in the document and define the value of that attribute to be the **(2)English word** found in that position.
    - Then a text document can be denoted as the following.
      - $a_1=w_1, a_2=w_2, \cdots, a_n=w_n$
        - where
          - $n$ : the number of word positions in a given text document.
          - $a_i$ : the $i$-th **(1)word position** in the text document
          - $w_i$ : the $i$-th **(2)English word** in the text document
  - Then our target will be $P(v_j|a_1=w_1, a_2=w_2, \cdots, a_n=w_n)$
  - We can apply naive Bayesian classifier for this problem.
    - i.e.) $P(v_j|a_1=w_1, a_2=w_2, \cdots, a_n=w_n) = P(v_j) P(a_1=w_1, a_2=w_2, \cdots, a_n=w_n|v_j)$
- Naive Bayesian Classifier)
  - $`\begin{array}{lll} v_{NB} &= argmax_{v_j \in V} P(v_j) P(a_1=w_1, a_2=w_2, \cdots, a_n=w_n|v_j) & \\&= argmax_{v_j \in V} P(v_j)\prod_{i=1}^n P(a_i=w_i|v_j) & \because Assumption \space 1  \\&= argmax_{v_j \in V} P(v_j) \prod_{k} P(w_k|v_j) & \because Assumption \space 2 \\&= argmax_{v_j \in V} P(v_j) \prod_{k} \frac{n_k+1}{n+|Vocabulary|} & \because \textrm{m-estimate} \end{array}`$
    - Why?
      1. $P(a_1=w_1, a_2=w_2, \cdots, a_n=w_n|v_j) = \prod_{i=1}^n P(a_i=w_i|v_j)$ ?
         - Recall our [Assumption](#assumptions) 1.
         - Then, two distinct word positions $a_{i_1}$ and $a_{i_2}$ are independent of each other, given a classification $v_j$.
           - i.e.), $P(a_{i_1}, a_{i_2}|v_j) = P(a_{i_1}|v_j)P(a_{i_2}|v_j)$
         - Thus, without the loss of generality, $P(a_1, a_2, \cdots, a_n|v_j) = \prod_{i=1}^n P(a_i|v_j)$
      2. $\prod_{i=1}^n P(a_i=w_i|v_j) = \prod_{k} P(w_k|v_j)$ ?
         - Recall our [Assumption](#assumptions) 2.
         - Thus, $P(a_{i_1}=w_k|v_j) = P(a_{i_2}=w_k|v_j), \forall i_1,i_2,k,j$
           - where $w_k$ is the $k$-th word in the word dictionary.
         - Therefore, we estimate the entire set of probabilities $P(a_{i_1} = w_k |v_j), P(a_{i_2} = w_k |v_j) \cdots P(a_{i_q} = w_k |v_j)$ by the single position-independent probability $P(w_k|v_j)$, which we will use regardless of the word position.
      3. $P(w_k|v_j) = \frac{n_k+1}{n+|Vocabulary|}$ ?
         - Recall the [m-estimate](../09/note.md#6911-estimating-probabilities) such that $\frac{n_c+mp}{n+m}$.
         - We can apply this by...
           - $n$ : the number of word positions in the text document.
           - $n_c = n_k$
             - where $n_k$ is the number of times the word $w_k$ is found among the $n$ word positions in the text document. 
           - $m = |Vocabulary|$
             - where $|Vocabulary|$ is the total number of distinct words found within the training data.
           - $mp = |Vocabulary|\times\frac{1}{|Vocabulary|}= 1$
             - Since $|Vocabulary|$ is the number of distinct words, assuming the uniform prior, $p = \frac{1}{|Vocabulary|}$.


#### Algorithm Implementation)
  - ```LearnNaiveBayesText(examples, V)```
    - Desc.)
      - ```examples``` is a set of text documents along with their target values. 
      - ```V``` is the set of all possible target values. 
      - This function learns the probability terms $P(w_k|v_j)$, describing the probability that a randomly drawn word from a document in class $v_j$ will be the English word $w_k$. It also learns the class prior probabilities $P(v_j)$.
    - Procedures)
      1. Collect all words, punctuation, and other tokens that occur in ```examples```.
         - ```vocabulary``` $\leftarrow$ the set of all distinct words and other tokens occurring in any text document from ```examples```
      2. Calculate the required $P(v_j)$ and $P(w_k|v_j)$ probability terms.
         - For each target value $v_j \in V$ do
           - $docs_j\leftarrow$ the subset of documents from ```examples``` for which the target value is $v_j$
           - $P(v_j) \leftarrow \frac{|dosc_j|}{|examples|}$ 
           - $Text_j\leftarrow$ a single document created by concatenating all members of $docs_j$
           - ```n``` $\leftarrow$ total number of distinct word positions in $Text_j$
           - For each word $w_k$ in ```vocabulary``` do
             - $n_k \leftarrow$ number of times word $w_k$ occurs in $Text_j$
             - $P(w_k|v_j) \leftarrow \frac{n_k+1}{n+|Vocabulary|}$ 
  - ```ClassifyNaiveBayesText(doc)```
    - Desc.)
      - Return the estimated target value for the document ```doc```. 
      - $a_i$ denotes the word found in the $i$-th position within ```doc```.
    - Procedures)
      - ```positions``` $\leftarrow$ all word positions in ```doc``` that contain tokens found in ```vocabulary```
      - Return $v_{NB}$
        - where $v_{NB} = argmax_{v_j \in V} P(v_j) \prod_{i \in positions} P(a_i|v_j)$



<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)