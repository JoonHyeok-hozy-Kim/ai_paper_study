* [Back to Elements of Information Theory](../../main.md)

# 5.6 Huffman Codes

### Concept) Huffman Code
- Desc.)
  - An [optimal (shortest expected length) prefix code](../03/note.md#53-optimal-codes) for a given distribution can be constructed by a simple algorithm discovered by Huffman.
  - In [section 5.8](../08/note.md), we will prove that any other code for the same alphabet cannot have a lower expected length than the code constructed by the algorithm.

<br><br>

#### Example 5.6.1) Binary Code
- Settings)
  - $`X`$ : a random variable taking values in the set $`\mathcal{X} = \{1,2,3,4,5\}`$ with probabilities as below.   
    |$`\mathcal{x}`$|$`p(\mathcal{x})`$|
    |:-:|:-:|
    |1|0.25|
    |2|0.25|
    |3|0.2|
    |4|0.15|
    |5|0.15|


- Getting the code.
  - How?)
    - Combine the two least likely symbols into one symbol until we are finally left with only one symbol.
    - Assign codewords to the symbols.
  - e.g.)    
    ![](images/001.png)
    1. 4 and 5 are the least likely symbols with the probabilities 0.15 respectively.
       - Assign the longest symbols to 4 and 5 with equal lengths. : 00X
         - Why equal lengths?) 
           - Otherwise, we can delete a bit from the longer codeword and still have a prefix code but with a shorter expected length.
       - Combine the symbols 4 and 5 into a single source symbol 00X, with a probability assignment 0.30.   
         |Symbol|Codeword c|p(c)|
         |:-:|:-:|:-:|
         |(4, 5)|00X|0.30|
         |1|-|0.25|
         |2|-|0.25|
         |3|-|0.2|
    2. 2 and 3 are the least likely symbols.
       - Assign the next longest symbols to 2 and 3 with equal lengths : 1X.
       - Combine the symbols 2 and 3 into a single symbol 1X, with a probability assignment 0.45.   
         |Symbol|Codeword c|p(c)|
         |:-:|:-:|:-:|
         |(2, 3)|1X|0.45|
         |(4, 5)|00X|0.30|
         |1|-|0.25|
    3. 1 and (4,5) are the least likely symbols.
       - Assign the next longest symbols to 1 and (4,5) with equal lengths : 0X
       - Combine the symbols 1 and (4,5) into a single symbol 0X, with a probability assignment 0.55.   
         |Symbol|Codeword c|p(c)|
         |:-:|:-:|:-:|
         |(1, (4, 5))|0X|0.55|
         |(2, 3)|1X|0.45|
    4. (1,4,5) and (2,3) are the final two symbols.
       - Assign the next longest symbols to (1,4,5) and (2,3) with equal lengths : X
       - Combine the symbols (1,4,5) and (2,3) into a single symbol X, with a probability assignment 1.00.   
         |Symbol|Codeword c|p(c)|
         |:-:|:-:|:-:|
         |((2, 3), (1, (4, 5)))|X|1.00|

<br><br>

#### Example 5.6.2) Ternary Code
- Settings)
  - Same $`X`$ as [Example 5.6.1](#example-561-binary-code).


- Getting the optimal codes.   
  ![](images/002.png)
  1. 3,4,5 are the least likely three symbols.
     - Assign the longest symbol to 3,4,5 and combine the probabilities.   
       |Symbol|Codeword c|p(c)|
       |:-:|:-:|:-:|
       |(3, 4, 5)|0X|0.5|
       |1|-|0.25|
       |2|-|0.25|
  2. (3,4,5), 1, 2 are the least likely three symbols.
     - Assign the longest symbol to (3,4,5), 1, 2 and combine the probabilities.   
       |Symbol|Codeword c|p(c)|
       |:-:|:-:|:-:|
       |((3, 4, 5), 1, 2)|X|1.00|

<br><br>

### Concept) Dummy Symbol
- Why needed?)
  - If $`D \ge 3`$, we may not have a sufficient number of symbols to combine by $`D`$ amount at a time.
  - In such case, add dummy symbols to the end of the set of symbols.
- How?)
  - At each stage of reduction, the number of symbols is reduced by $`D-1`$.
  - Thus, the total number of symbols must be $`1+k(D-1)`$
    - where $`k`$ is the number of merges.

#### Example 5.6.3) Dummy Symbol Example
- Ternary coding with a random variable $`X`$ taking symbols from $`\mathcal{X} = \{1,2,3,4,5,6\}`$ with probabilities $`\{0.25, 0.25, 0.2, 0.1, 0.1, 0.1, 0.1\}`$ respectively.

![](images/003.png)



<br>

* [Back to Elements of Information Theory](../../main.md)