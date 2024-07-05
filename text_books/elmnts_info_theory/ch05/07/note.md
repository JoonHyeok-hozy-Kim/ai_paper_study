* [Back to Elements of Information Theory](../../main.md)

# 5.7 Some Comments on Huffman Codes

### Prop.1) Equivalence of Source Coding and 20 Questions
- Consider an object determined by the **20 questions**.
  - Any question depends only on the answers to the questions before it. 
  - Since the sequence of answers uniquely determines the object, each object has a different sequence of answers,
    - e.g.) If we represent the yes–no answers by 0’s and 1’s, we have a binary code for the set of objects. 
  - The average length of this code is the average number of questions for the questioning scheme.
- Consider an Object determined by a **source code**.
  - From a binary code for the set of objects, we can find a sequence of questions that correspond to the code, with the average number of questions equal to the expected codeword length of the code.
    - e.g.) Is the first bit equal to 1 in the source code?
- [We will prove](../08/note.md) that Huffman code is the optimal code.
  - Assuming that, the optimal series of questions is that determined by the Huffman code.
  - Thus, the expected number of questions in this optimal scheme satisfies
    - $`H(X) \le EQ \lt H(X) + 1`$

<br>

### Prop.2) Huffman coding for weighted codewords
- Recall that Huffman's algorithm minimizes $`\sum p_i l_i`$ where $`\sum p_i = 1`$.
- However, the algorithm can be applied to any set of numbers $`p_i \ge 0`$.
  - In this case, the Huffman code minimizes the sum of weighted code lengths $`\sum w_i l_i`$, not the average code lengths.

#### Example 5.7.1)
- Consider the case with    
  |Symbol|Weight|
  |:-:|:-:|
  |1|5|
  |2|5|
  |3|4|
  |4|4|
  - Desc.)
    - Instead of the probability $`p_i`$, the weight $`w_i`$ is given.
    - And $`\sum w_i > 1`$

- Applying the Huffman's algorithm we get the following.   
 ![](images/001.png)
  - Then the result shows the minimum weighted sum of 36.

<br><br>

### Prop.3) Slice Code (Alphabetic Code)
- Recall the [relation between the Huffman code and the 20 questions](#prop1-equivalence-of-source-coding-and-20-questions).
  - Huffman code was equivalent to asking question as below.
    - Settings)
      - $`\mathcal{X} = \{1,2,3,\cdots,m\}`$ : the symbols
    - Question)
      - "Is $`X\in A, \exists A \subseteq \mathcal{X}`$?"`$
        - e.g.) "Is $`X=3 \vee X=4`$?"
- To setup a slice question, We want to give more restrictions.
  - For $`\mathcal{X} = \{1,2,3,\cdots,m\}`$
    - the elements of $`\mathcal{X}`$ are ordered so that $`p_1\ge p_2\ge \cdots \ge p_m`$.
  - Questions are restricted to
    - "Is $`X \gt a, \exists a \le m`$?"
      - i.e.) **Slicing** the elements into sets of the forms $`\{x:x\gt a\}`$ and $`\{x:x\lt a\}`$. 
- Using the slice questions and the following condition we can derive another optimal code of slice code.
  - Additional Condition) By [Lemma 5.8.1](../08/note.md#Lemma581)
    - The codeword lengths are taken as $`l_1 \le l_2 \le \cdots \le l_m`$
- Slice code is different from the Huffman code.
  - In Slice code, each bit of the code splits the tree into sets of the form $`\{x:x\gt a\}`$ and $`\{x:x\lt a\}`$.

#### Example 5.7.2)
|Symbol|Slice Code|
|:-:|:-:|
|1|00|
|2|01|
|3|10|
|4|110|
|5|111|


<br><br>

### Prop.4) Shannon code
- Recall the codeword length of $`\displaystyle \left\lceil \log\frac{1}{p_i} \right\rceil`$.
  - cf) [Theorem 5.4.1](../04/note.md#theorem-541-bounds-on-the-optimal-code-length)
- Codeword with this property is called the Shannon coding.
- Shannon code may be much worse than the optimal code for some particular symbol.
  - e.g.)
    - Consider two symbols.   
      |Symbol|Probability|
      |:-:|:-:|
      |1|0.9999|
      |2|0.0001|
    - Then using codeword lengths of $`\displaystyle \left\lceil \log\frac{1}{p_i} \right\rceil`$ gives codeword lengths of 1 bit and 14 bits.
      - Why?)   
        $`\begin{cases}
            \log\frac{1}{0.9999} \approx 0.000144276718044 & \Rightarrow \left\lceil \log\frac{1}{0.9999} \right\rceil = 1 \\
            \log\frac{1}{0.0001} \approx 13.28771237954945 & \Rightarrow \left\lceil \log\frac{1}{0.0001} \right\rceil = 14 \\
        \end{cases}`$
        - Refer to [this script](ShannonCode.py) for the calculation.
    - On the other hand, the optimal codeword length is obviously 1bit for both symbol : 0 and 1.
- The optimal code is not always less than the Shannon code.
  - i.e.) Individual symbol of Shannon code can be less than the optimal code.
  - e.g.)
    - Consider a random variable $`X`$ with distribution $`\left(\frac{1}{3}, \frac{1}{3}, \frac{1}{4}, \frac{1}{12}\right)`$
    - Then the Huffman coding procedure results in codeword lengths of $`(2,2,2,2)`$ or $`(1,2,3,3)`$ depending on where one puts the merged probabilities.
    - Both of them achieve the same expected codeword length.   
      $`\begin{cases}
        2\times\frac{1}{3}+ 2\times\frac{1}{3}+ 2\times\frac{1}{4}+ 2\times\frac{1}{12} = \frac{8+8+6+2}{12} = 2 \\
        1\times\frac{1}{3}+ 2\times\frac{1}{3}+ 3\times\frac{1}{4}+ 3\times\frac{1}{12} = \frac{4+8+9+3}{12} = 2 \\
      \end{cases}`$
    - The third symbol of the Huffman codes $`(1,2,3,3)`$ is $`3`$.
    - However, if we used the Shannon coding, the third symbol would have the length of $`\left\lceil \log\frac{1}{1/4} \right\rceil = 2`$
- Although either the Shannon code or the Huffman code can be shorter for individual symbols, **the Huffman code is shorter on average**.


<br><br>

### Prop.5) Fano code
- How to code)
  - Order the probabilities in decreasing order.
  - Find $`k`$ s.t. $`\displaystyle \left| \sum_{i=1}^k p_i - \sum_{i=k+1}^m p_i \right|`$ is minimized.
  - This point divides the source symbols into two sets of almost equal probability.
  - Assign 
    - 0 for the first bit of the upper set
    - 1 for the first bit of the lower set
  - Repeat the above process for each subset.
- Props.)
  - Sub-optimal code where $`L(C) \le H(X) + 2`$



<br>

* [Back to Elements of Information Theory](../../main.md)