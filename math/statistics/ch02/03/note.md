* [Back to Statistics Main](../../main.md)

## 2.3 Counting Techniques and Calculation of Probabilities

#### Theorem 2.3.1) Multiplication Principle
If the experiments $A_1, A_2,...,A_m$ contain, respectively, $n_1, n_2,...,n_m$ outcomes, such that for each possible outcomes of $A_1$ there are $n_2$ possible outcomes for $A_2$, and so on, then there are a total of $(n_1 \times n_2 \times ... \times n_m)$ possible outcomes for the composite experiment $A_1, A_2,...,A_m$.

<br>

#### Calculating the Total Number of Ways for Random Sample Collection
Let $n$ be the number of objects and $k$ be the sample size.
<table>
<tr>
<td></td><td>Replacement</td><td>No Replacement</td>
</tr>
<tr>
<td>Objects Ordered</td><td> $n^k$ </td><td> ${}_n P_k$ </td>
</tr>
<tr>
<td>Objects Not Ordered</td><td> ${}_{n+k-1} C_k$ * </td><td> ${}_n C_k$ </td>
</tr>
</table>

\* ex) An urn contains 15 balls numbered 1 to 15. If four balls are drawn at random, with replacement and without
regard for order the number of possible samples is ${18!} \over {4!14!}$

<br>

#### Theorem 2.3.4) Number of Combinations of $n$ Objects Into $m$ Classes
The number of ways that $n$ objects can be grouped into $m$ classes with $n_i$ in the $i$-th class, is given by ${n!} \over {n_1!n_2! \dots n_m!}$, where $i=1,2,3, \dots m$ and $\Sigma_{i=1}^{m}n_i=n$.

<br>

### [Exercises 2.3](./exercises.md)

<br><br>

* [Back to Statistics Main](../../main.md)