* [Back to Elements of Information Theory](../../main.md)

# 5.8 Optimality of Huffman Codes

### Lemma 5.8.1)
- Theorem)
  - Without loss of generality, assume that the probability masses are ordered.
    - i.e.) $`p_1 \ge p_2 \ge \cdots \ge p_m`$
  - For any distribution, there exists an [optimal](../03/note.md#concept-optimal-code) [instantaneous code](../01/note.md#concept-prefix-code-instantaneous-code) that satisfies the following properties.
    - Prop.1)  The lengths are ordered inversely with the probabilities.
      - i.e.) $`p_j \gt p_k \Rightarrow l_j \le l_k`$
    - Prop.2) The two longest codewords have the same length.
    - Prop.3)  Two of the longest codewords differ only in the last bit and correspond to the two least likely symbols.
- pf.)
  - Consider an optimal code $`C_m`$.
  - Prop.1) $`p_j \gt p_k \Rightarrow l_j \le l_k`$.
    - (Swapping) 
      - Let $`C_m'`$ be the swapped code of $`C_m'`$ 
        - i.e.) The codewords $`j`$ and $`k`$ of $`C_m`$ are interchanged.
      - Then   
        $`\begin{aligned}
            L(C_m') - L(C_m) &= \sum p_i l_i' - \sum p_i l_i \\
            &= p_j l_k + p_k l_j - p_j l_j - p_k l_k & \because \textrm{Only }j,k\textrm{ are swapped in } C_m' \\
            &= (p_j - p_k)(l_k - l_j)
        \end{aligned}`$
      - By the assumption $`p_j - p_k \gt 0`$.
      - Also since $`C_m`$ is optimal, $`L(C_m') - L(C_m) \ge 0`$
      - Thus, $`l_k - l_j \ge 0 \Leftrightarrow l_k \ge l_j`$
  - Prop.2) *The two longest codewords are of the same length.*
    - (Trimming)
      - Suppose not.
        - i.e.) The two longest codewords are not of the same length.
      - Then, one can delete the last bit of the longer one, preserving the [prefix property](../01/note.md#concept-prefix-code-instantaneous-code) and achieving lower expected codeword length. $`\cdots \textrm{Contradiction!}`$
  - Prop.3) *The two longest codewords differ only in the last bit and correspond to the two least likely symbols.*
    - cf.) Not all optimal codes satisfy this property, but by rearranging, we can find an optimal code that does.
      - If there is a maximal-length codeword without a sibling, we can delete the last bit of the codeword and still satisfy the [prefix property](../01/note.md#concept-prefix-code-instantaneous-code).
      - This reduces the average codeword length and contradicts the [optimality](../03/note.md#concept-optimal-code) of the code.
      - Hence, every maximal-length codeword in any optimal code has a sibling.
      - Now we can exchange the longest codewords so that the two lowest-probability source symbols are associated with two siblings on the tree. 
      - This does not change the expected length, $`\sum p_i l_i`$. 
      - Thus, the codewords for the two lowest-probability source symbols have maximal length and agree in all but the last bit.

<br>

### Concept) Canonical Code
- Def.)
  - An optimal code that satisfies the properties of [Lemma 5.8.1](#lemma-581).

<br>

### Concept) Huffman Reduction
- Def.)
  - For
    - $`\mathbf{p} = \underbrace{(p_1, p_2, \cdots, p_m)}_m`$ : a probability mass function for an alphabet of size $`m`$
      - such that $`p_1 \ge p_2 \ge \cdots \ge p_m`$.
  - the **Huffman reduction** is defined as
    - $`\mathbf{p}' = \underbrace{(p_1, p_2, \cdots, p_{m-2}, p_{m-1} + p_m)}_{m-1}`$ : the probability mass function over an alphabet of size $`m-1`$

<br>

### Theorem 5.8.1) 
- Theorem)
  - Huffman coding is optimal.
    - i.e.) 
      - For a Huffman code $`C^\ast`$, $`L(C^\ast) \le L(C')`$
        - where $`C'`$ is any uniquely decodable code.
- pf.)
  - Let
    - $`\mathbf{p}`$ : a probability mass function for an alphabet of size $`m`$
      - where $`\mathbf{p} = \underbrace{(p_1, p_2, \cdots, p_m)}_m`$
    - $`\mathbf{p}'`$ : the [Huffman reduced](#concept-huffman-reduction) probability mass function for an alphabet of size $`m-1`$ 
      - where $`\mathbf{p}' = \underbrace{(p_1, p_2, \cdots, p_{m-2}, p_{m-1} + p_m)}_{m-1}`$
    - $`C^\ast_m (p)`$ : the [canonical](#concept-canonical-code) optimal code for $`\mathbf{p}`$
      |Probability|Codeword|Length|
      |:-:|:-:|:-:|
      |$`p_1`$|$`w_1`$|$`l_1`$|
      |$`p_2`$|$`w_2`$|$`l_2`$|
      |$`\vdots`$|$`\vdots`$|$`\vdots`$|
      |$`p_{m-2}`$|$`w_{m-2}`$|$`l_{m-2}`$|
      |$`p_{m-1} `$|$`w_{m-1}`$|$`l_{m-1}`$|
      |$`p_m`$|$`w_{m}`$|$`l_{m}`$|
    - $`C^\ast_{m-1}(\mathbf{p}')`$ : an optimal code for $`\mathbf{p}'`$   
      |Probability|Codeword|Length|
      |:-:|:-:|:-:|
      |$`p_1`$|$`w_1'`$|$`l_1'`$|
      |$`p_2`$|$`w_2'`$|$`l_2'`$|
      |$`\vdots`$|$`\vdots`$|$`\vdots`$|
      |$`p_{m-2}`$|$`w_{m-2}'`$|$`l_{m-2}'`$|
      |$`p_{m-1} + p_m`$|$`w_{m-1}'`$|$`l_{m-1}'`$|
  - We want to show that the optimal code for $`\mathbf{p}`$ can be obtained by extending the optimal code for $`\mathbf{p}'`$.
    - Procedure)
      - a) Expand $`C^\ast_{m-1}(\mathbf{p}')`$ to construct a code for $`\mathbf{p}`$.
      - b) Condense $`C^\ast_m (p)`$ to construct a code for the [Huffman reduction](#concept-huffman-reduction) $`\mathbf{p}'`$.
      - c) Compare the average codeword lengths for the two codes.
    - a) Expand $`C^\ast_{m-1}(\mathbf{p}')`$, to construct a code for $`\mathbf{p}`$.
      - Extend $`w_{m-1}`$ by adding $`\begin{cases} 0 \\ 1 \end{cases}`$ to form a codeword for symbol $`\begin{cases} m-1 \\ m \end{cases}`$.
      - Denoting the new code as $`C_m(\mathbf{p})`$, it may look like...
        |Probability|Codeword|Length|Desc.|
        |:-:|:-:|:-:|:-:|
        |$`p_1`$|$`w_1'`$|$`l_1'`$||
        |$`p_2`$|$`w_2'`$|$`l_2'`$||
        |$`\vdots`$|$`\vdots`$|$`\vdots`$||
        |$`p_{m-2}`$|$`w_{m-2}'`$|$`l_{m-2}'`$||
        |$`p_{m-1} `$|$`w_{m-1}'0`$|$`l_{m-1}'+1`$|0 added to $`w_{m-1}'`$|
        |$`p_m`$|$`w_{m-1}'1`$|$`l_{m-1}'+1`$|1 added to $`w_{m-1}'`$|
      - Then the average length of $`C_m(\mathbf{p})`$ goes   
        $`\begin{aligned}
          L(\mathbf{p}) &= \sum_{i=1}^{m-2} p_i l_i' + p_{m-1}(l_{m-1}'+1) + p_m(l_{m-1}'+1) \\
          &= \sum_{i=1}^{m-2} p_i l_i' + (p_{m-1} + p_m)l_{m-1}' + (p_{m-1} + p_m) \\
          &= L^\ast(\mathbf{p}') + (p_{m-1} + p_m)
        \end{aligned}`$
        - where $`L^\ast(\mathbf{p}')`$ is the average length of $`C^\ast_{m-1}(\mathbf{p}')`$
      - Thus,   
        $`L(\mathbf{p}) - L^\ast(\mathbf{p}') = p_{m-1} + p_m \; \cdots (A)`$
    - b) Condense $`C^\ast_m (p)`$ to construct a code for the [Huffman reduction](#concept-huffman-reduction) $`\mathbf{p}'`$.
      - Similarly, condense $`C^\ast_m (p)`$ by dropping the last digits of $`w_{m-1}`$ and $`w_m`$.
        - They will be identical after the drop, so merge the probabilities $`p_{m-1}`$ and $`p_m`$.
      - Denoting the new code as $`C_{m-1}(\mathbf{p}')`$, it may look like
        |Probability|Codeword|Length|Desc.|
        |:-:|:-:|:-:|:-:|
        |$`p_1`$|$`w_1`$|$`l_1`$||
        |$`p_2`$|$`w_2`$|$`l_2`$||
        |$`\vdots`$|$`\vdots`$|$`\vdots`$||
        |$`p_{m-2}`$|$`w_{m-2}`$|$`l_{m-2}`$||
        |$`p_{m-1} + p_m`$|$`\hat{w_{m-1}}`$|$`l_{m-1}-1`$|Last digit dropped and probabilities summed.|
      - Then the average length of $`C_m(\mathbf{p}')`$ goes     
        $`\begin{aligned}
          L(\mathbf{p}') &= \sum_{i=1}^{m-2} p_i l_i + (p_{m-1} + p_m) (l_{m-1}-1) \\
          &= \sum_{i=1}^{m-2} p_i l_i + p_{m-1} l_{m-1} + p_m l_{m-1} - (p_{m-1} + p_m) \\
          &= \sum_{i=1}^{m-2} p_i l_i + p_{m-1} l_{m-1} + p_m l_{m} - (p_{m-1} + p_m) & \because l_{m-1} = l_m \\
          &= L^\ast(\mathbf{p}) - (p_{m-1} + p_m)
        \end{aligned}`$
        - where $`L^\ast(\mathbf{p})`$ is the average length of $`C^\ast_m (p)`$
      - Thus,   
        $`L^\ast(\mathbf{p}) - L(\mathbf{p}') = p_{m-1} + p_m \; \cdots (B)`$
    - c) Compare the average codeword lengths for the two codes.
      - From $`(A) \textrm{ and } (B)`$ we get
        - $`p_{m-1} + p_m = L(\mathbf{p}) - L^\ast(\mathbf{p}') = L^\ast(\mathbf{p}) - L(\mathbf{p}')`$
      - Thus,   
        - $`(L(\mathbf{p}') - L^\ast(\mathbf{p}')) + (L(\mathbf{p}) - L^\ast(\mathbf{p})) = 0 \; \cdots (C)`$
      - Since $`L^\ast(\mathbf{p}')`$ and $`L^\ast(\mathbf{p})`$ are optimal codes by assumption,
        - we have $`\begin{cases} L(\mathbf{p}') - L^\ast(\mathbf{p}') \ge 0 \\ L(\mathbf{p}) - L^\ast(\mathbf{p}) \ge 0 \\ \end{cases} \; \cdots (D)`$
      - By $`(C) \textrm{ and } (D), \begin{cases} L(\mathbf{p}') = L^\ast(\mathbf{p}') \\ L(\mathbf{p}) = L^\ast(\mathbf{p}) \\ \end{cases}`$
        - i.e.)
          - The extension of the optimal code for $`\mathbf{p}'`$ is optimal for $`\mathbf{p}`$
          - The condensation of the optimal code for $`\mathbf{p}`$ is optimal for $`\mathbf{p}'`$.
  - Consequently, if we start with an optimal code for $`\mathbf{p}'`$ with $`m − 1`$ symbols and construct a code for $`m`$ symbols by extending the codeword corresponding to $`p_{m−1} + p_m`$, the new code is also optimal.
  - Therefore, starting with a code for two elements, in which case the optimal code is obvious, we can by induction extend this result to prove the theorem.
  - Without the loss of generality, we can prove for the $`D`$-ary alphabet case.



<br>

* [Back to Elements of Information Theory](../../main.md)