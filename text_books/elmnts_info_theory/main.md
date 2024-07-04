[Back to AI Main](../../README.md)

<br>

# Elements of Information Theory (2006)
*THOMAS M. COVER, JOY A. THOMAS*


## 2. Entropy, Relative Entropy, and Mutual Information
|No.|Chapter|Keywords|
|:-:|:------|:-------|
|2.1|[Entropy](ch02/01/note.md)|- $`H(p)`$|
|2.2|[Joint Entropy and Conditional Entropy](ch02/02/note.md)|- Chain Rule : $`H(X,Y) = H(X) + H(Y\|X)`$|
|2.3|[Relative Entropy and Mutual Information](ch02/03/note.md)|- Relative Entropy (Kullback–Leibler Distance) : $`D(p\|\|q)`$ <br> - Mutual Information : $`I(X;Y)`$|
|2.4|[Relationship between Entropy and Mutual Information](ch02/04/note.md)|- Self Information|
|2.5|[Chain Rules for Entropy, Relative Entropy, and Mutual Information](ch02/05/note.md)|- Chain Rule for Entropy : $`\displaystyle H(X_1, X_2, \cdots, X_n) = \sum_{i=1}^n H(X_i\|X_1, \cdots, X_{i-1})`$ <br>- Conditional Mutual Information <br> - Chain Rule for Information <br> $`\displaystyle I(X_1, X_2, \cdots, X_n; Y) = \sum_{i=1}^n I(X_i; Y\|X_1, X_2, \cdots, X_{i-1})`$ <br> - Chain Rule for Relative Entropy <br> $`D(p(x,y) \|\| q(x,y)) = D(p(x) \|\| q(x)) + D(p(y\|x) \|\| q(y\|x))`$|
|2.6|[Jensen's Inequality and Its Consequences](ch02/06/note.md)|- Convexity / Concavity <br> - Jensen's Inequality : $`Ef(X) \ge f(EX)`$ <br> - Information Inequality : $`D(p\|\|q)\ge0`$ <br> - Non-negativity of $`\begin{cases} \textrm{Mutual Information : } & I(X;Y)=D(p(x,y)\|\|p(x)q(y)) \ge 0 \\ \textrm{Conditional Relative Entropy : } & D(p(y\|x)\|\|q(y\|x)) \ge 0 \\ \textrm{Conditional Mutual Information : } & I(X;Y\|Z) \ge 0 \\ \end{cases}`$ <br> - Conditioning reduces entropy. : $`H(X\|Y) \le H(X)`$ <br> - Independence Bound on Entropy : $`\displaystyle H(X_1, \cdots, X_n) \le \sum_{i=1}^n H(X_i)`$|
|2.7|[Log Sum Inequality and its Applications](ch02/07/note.md)|- Log Sum Inequality <br> - Convexity of Relative Entropy <br> - Concavity of Entropy <br> - Convexity / Concavity of Mutual Information|
|2.8|[Data-Processing Inequality](ch02/08/note.md)|- Markov Chain : $`X\rightarrow Y \rightarrow Z`$ <br> - Data-Processing Inequality|
|2.9|[Sufficient Statistics](ch02/09/note.md)|- Minimal Sufficient Statistic|
|2.10|[Fano's Inequality](ch02/10/note.md)|- |

<br>

## 3. Asymptotic Equipartition Property
|No.|Chapter|Keywords|
|:-:|:------|:-------|
|3.1|[Asymptotic Equipartition Property Theorem](ch03/01/note.md)|- Convergence of Random Variable<br>- Asymptotic Equipartition Property Theorem (AEP) <br>$`\displaystyle -\frac{1}{n}\log{p(X_1, X_2, \cdots, X_n)} \rightarrow H(X)`$  <br> - Typical Set : $`A_\epsilon^{(n)}`$|
|3.2|[Consequences of the AEP : Data Compression](ch03/02/note.md)|- $`\displaystyle E\left[ \frac{l(X^n)}{n} \right] \le H(X) + \epsilon`$ for sufficiently large $`n`$|
|3.3|[High-Probability Sets and the Typical Set](ch03/03/note.md)|- High-Probability Set $`B_\delta^{(n)}`$ <br> - Equal to the First Order in the Exponent : $`\doteq`$ <br> - $`\left\| B_\delta^{(n)} \right\| \doteq \left\|A_\epsilon^{(n)} \right\| \doteq 2^{nH}`$|

<br>

## 4. Entropy Rates of a Stochastic Process
|No.|Chapter|Keywords|
|:-:|:------|:-------|
|4.1|[Markov Chains](ch04/01/note.md)|- Markov Chain (Markov Process) <br> - Time Invariant Markov Chain : State, Probability Transition Matrix <br> - Irreducible / Aperiodic Markov Chain <br> - Stationary Distribution|
|4.2|[Entropy Rate](ch04/02/note.md)|- $`\displaystyle H(\mathcal{X}) = \lim_{n\rightarrow\infty} \frac{H(X_1, X_2,\cdots, X_n)}{n}`$ <br> - $`\displaystyle H'(\mathcal{X}) = \lim_{n\rightarrow\infty} H(X_n\|X_1, X_2,\cdots, X_{n-1})`$ <br> - Cesaro mean|
|4.3|[Example: Entropy Rate of a Random Walk on a Weighted Graph](ch04/03/note.md)|- |
|4.4|[Second Law of Thermodynamics](ch04/04/note.md)|- |
|4.5|[Functions of Markov Chains](ch04/05/note.md)|- Deterministic Function of Markov Chain <br> $`\begin{aligned} \textrm{For } &Y_i = \phi(X_i) \\ (1) &H(Y_n \| Y_{n-1}, \cdots, Y_1, X_1) \le H(\mathcal{Y}) \le H(Y_n \| Y_{n-1}, \cdots, Y_1) \\ (2)&\lim_{n\rightarrow\infty} H(Y_n \| Y_{n-1}, \cdots, Y_1, X_1) = H(\mathcal{Y}) = \lim_{n\rightarrow\infty} H(Y_n \| Y_{n-1} \cdots, Y_1) \\ \end{aligned}`$ <br> - Hidden Markov Model (HMM)|

<br>

## 5. Data Compression
|No.|Chapter|Keywords|
|:-:|:------|:-------|
|5.1|[Examples of Codes](ch05/01/note.md)|- Source Code : $`C`$ <br> - Expected Length : $`L(C) = El(X)`$ <br> - Non-Singularity <br> - Extension of a Code : $`C^\ast`$ <br> - Unique Decodability <br> - Prefix Code (Instantaneous Code)|
|5.2|[Kraft Inequality](ch05/02/note.md)|- $`\displaystyle \sum_i D^{-l_i} \le 1`$ <br>- $`\displaystyle \sum_{i=1}^\infty = D^{-l_i} \le 1`$|
|5.3|[Optimal Codes](ch05/03/note.md)|- $`L \ge H_D(X)`$ <br> - $`D`$-adic Probability Distribution|
|5.4|[Bounds on the Optimal Code Length](ch05/04/note.md)|- $`H_D(X) \le L^\ast \lt H_D(X) + 1`$ <br> - $`\displaystyle \frac{H(X_1, X_2, \cdots, X_n)}{n} \le L_n^\ast \lt \frac{H(X_1, X_2, \cdots, X_n)}{n} +\frac{1}{n}`$ <br> - If the stochastic process is stationary, $`L_n^\ast \rightarrow H(\mathcal{X})`$ : entropy rate <br> - $`H(p) + D(p\|\|q) \le E_p l(X) \lt H(p) + D(p\|\|q) + 1`$|
|5.5|[Kraft Inequality for Uniquely Decodable Codes](ch05/05/note.md)|- |
|5.6|[Huffman Codes](ch05/06/note.md)|- Examples) Binary Code, Ternary Code, Dummy Code|
|5.7|[Some Comments on Huffman Codes](ch05/07/note.md)|- Equivalence of Source Coding and 20 Questions <br> - Huffman coding for weighted codewords <br> - Slice Code (Alphabetic Code) <br> - Shannon code <br> - Fano code|



<br><br>

[Back to AI Main](../../README.md)