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
|4.2|[Entropy Rates](ch04/02/note.md)|- $`\displaystyle H(\mathcal{X}) = \lim_{n\rightarrow\infty} H(X_1, X_2,\cdots, X_n)`$ <br> - $`\displaystyle H'(\mathcal{X}) = \lim_{n\rightarrow\infty} H(X_n\|X_1, X_2,\cdots, X_{n-1})`$|



<br><br>

[Back to AI Main](../../README.md)