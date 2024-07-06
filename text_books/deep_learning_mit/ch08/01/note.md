* [Back to Deep Learning MIT](../../main.md)

# 8.1 How Learning Differs from Pure Optimization

### Concept) Indirectness of Machine Learning Optimization
- In the pure optimization problems, the goal is to optimize the cost function $`J`$.
- However, in machine learning, the goal is to optimize the performance measure $`P`$.
  - The problem is that $`P`$ is defined w.r.t. the **test set**.
  - Thus, we should optimize $`P`$ indirectly by reducing a different [cost function](#concept-cost-function-in-machine-learning) $`J(\theta)`$.
    - But optimizing $`J(\theta)`$ does NOT guarantee the optimization of $`P`$.

<br>

### Concept) Cost Function in Machine Learning
- Def.)
  - $`J(\theta) \equiv \mathbb{E}_{(x,y)\sim\hat{p}_{\textrm{data}}} L(f(x;\theta), y)`$ : the cost function over the training set
    - where
      - $`\hat{p}_{\textrm{data}}`$ : the training set
      - $`L`$ : the per-example loss function
      - $`f(x;\theta)`$ : the predicted output when the input is $`x`$
      - $`y`$ : the target output in the supervised learning
  - $`J^\ast (\theta) \equiv \mathbb{E}_{(x,y)\sim p_{\textrm{data}}} L(f(x;\theta), y)`$ : the cost function over the data generating distribution
    - where
      - $`p_{\textrm{data}}`$ : the data generating distribution

<br><br>

## 8.1.1 Empirical Risk Minimization






<br>

* [Back to Deep Learning MIT](../../main.md)