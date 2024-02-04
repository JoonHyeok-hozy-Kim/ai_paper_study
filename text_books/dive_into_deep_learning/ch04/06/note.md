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






<br>

* [Back to Dive into Deep Learning](../../main.md)