* [Back to Dive into Deep Learning](../../main.md)

# 4.6 Generalization in Classification

## 4.6.1 The Test Set
- Settings)
  - $f$ : a classifier trained with some training data.
  - $\mathcal{D}=(\mathbf{x}^{(i)}, y^{(i)})$ : a fresh dataset not used for training $f$
- Type of Errors)
  - The Empirical Error
    - $`\displaystyle\epsilon_{\mathcal{D}}(f)=\frac{1}{n}\sum_{i=1}^n{1 (f(\mathbf{x}^{(i)}) \ne y^{(i)})}`$ 
      - Desc.) The fraction of instances for which the prediction $f(\mathbf{x}^{(i)})$ disagrees with the true label $y^{(i)}$.
  - The Population Error
    - $`\displaystyle\epsilon(f)=E_{(\mathbf{x}, y)\sim P}{1(f(\mathbf{x})\ne y)}=\int\int{1(f(\mathbf{x})\ne y)p(\mathbf{x},y)}d\mathbf{x}dy`$
      - where $P(X,Y)$ is a probability distribution characterized by $p(\mathbf{x},y)$
      - Desc.) The expected fraction of examples in the underlying population for which our classifier disagrees with the true label.














<br>

* [Back to Dive into Deep Learning](../../main.md)