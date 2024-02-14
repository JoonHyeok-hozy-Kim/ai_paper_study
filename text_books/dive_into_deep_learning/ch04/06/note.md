* [Back to Dive into Deep Learning](../../main.md)

# 4.6 Generalization in Classification

## 4.6.1 The Test Set
- Settings)
  - $f$ : a classifier trained with some training data.
  - $\mathcal{D}=(\mathbf{x}^{(i)}, y^{(i)})$ : a fresh dataset not used for training $f$
- Type of Errors)
  - The Empirical Error
    - $`\displaystyle\epsilon_{\mathcal{D}}(f)=\frac{1}{n}\sum_{i=1}^n{1 (f(\mathbf{x}^{(i)}) \ne y^{(i)})}`$ 
      - where $1 (f(\mathbf{x}^{(i)}) \ne y^{(i)})$ denotes that the classifier made an error. $0$ for the correct classification.
      - Desc.) The fraction of instances for which the prediction $f(\mathbf{x}^{(i)})$ disagrees with the true label $y^{(i)}$.
  - The Population Error
    - $`\displaystyle\epsilon(f)=E_{(\mathbf{x}, y)\sim P}{1(f(\mathbf{x})\ne y)}=\int\int{1(f(\mathbf{x})\ne y)p(\mathbf{x},y)}d\mathbf{x}dy`$
      - where $P(X,Y)$ is a probability distribution characterized by $p(\mathbf{x},y)$
      - Desc.) The expected fraction of examples in the underlying population for which our classifier disagrees with the true label.
- Analysis)
  - $\epsilon(f)$ cannot be observed directly.
  - Assuming that $\mathcal{D}$ is statistically representative of the underlying population, we can view $\epsilon_{\mathcal{D}}(f)$ as a statistical estimator of the population error $\epsilon(f)$.
    - i.e.) The sample average or the mean estimation, $\bar{\epsilon(f)}$
  - Suppose we have $a_1, \cdots, a_n$ : $n$ random samples with mean $\mu$ and std.dev. $\sigma$.
    - By the Central Limit Theorem, it is guaranteed that $n \rightarrow\infty \Rightarrow \hat{\mu} \rightarrow \mu$ with std.dev $(\sigma / \sqrt{n})$.
    - Thus, $\epsilon_{\mathcal{D}}(f)$ approaches $\epsilon(f)$ with the rate of $\mathcal{O}(1/\sqrt{n})$.
      - i.e.) To estimate our test error twice as precisely, we must collect four times as large a test set.
      - We can call this the asymptotic rate at which our test error $\epsilon_{\mathcal{D}}(f)$ converges to the true error $\epsilon(f)$.
  - The asymptotic standard deviation of $\epsilon_{\mathcal{D}}(f)$ cannot be greater than $\sqrt{0.25/n}$.
    - why?)
      - Recall that we used the random variable $1(f(\mathbf{x})\ne y)$.
      - This is a Bernoulli random variable.
      - Thus, its variance goes $\sigma^2 = \epsilon(f)(1-\epsilon(f))$.
      - Consider that $\epsilon(f)(1-\epsilon(f)) \le 0.25, \forall 0\le\epsilon(f)\le 1$.
      - Hence, $n \rightarrow\infty \Rightarrow \hat{\mu} \rightarrow \mu$ with std.dev $(\sigma / \sqrt{n})$ 
        - where $(\sigma / \sqrt{n}) \le \sqrt{0.25/n}$
    - Usage) Finite sample case confidence interval estimation
      - If we want our test error $\epsilon_{\mathcal{D}}(f)$ to approximate the population error $\epsilon(f)$ with...
        - One standard deviation corresponds to an interval of $\pm 0.01$, then we should collect through $2500$ samples.
        - Two standard deviation or the $`95\%`$ confidence interval, then we need $10,000$ samples.

<br>

### Concept) Hoeffding Bound
- $P(\epsilon_\mathcal{D}(f) - \epsilon(f) \geq t) < \exp\left( - 2n t^2 \right)$
  - where $t$ is the distance between $\epsilon_\mathcal{D}(f)$ and $\epsilon(f)$.
- Desc.)
  - The relationship between $\epsilon_{\mathcal{D}}(f)$ and $\epsilon$ evolves as the sample size goes to infinity.
- e.g.)
  - Getting the smallest size of the data with 95% confidence that $t$ does not exceeds 0.01.
    - Then, $n \approx 15,000$.
- Refer to [Tom Mitchell](../../../ml_tom_mitchell/ch07/03/note.md#concept-hoeffding-bounds) for the further reading.

<br><br>

## 4.6.2. Test Set Reuse
### Concept) Adaptive Overfitting
- Desc.)
  - Once information from the test set has leaked to the modeler, it can never be a true test set again in the strictest sense.
  - Consider the case that we are testing the $k$ classifier models $f_1, f_2, \cdots, f_k$.
    - Can we reuse the test set for $f_2$ that we have already used for $f_1$?
    - No.
- [Reference](https://d2l.ai/chapter_references/zreferences.html#id353)


<br>

* [Back to Dive into Deep Learning](../../main.md)