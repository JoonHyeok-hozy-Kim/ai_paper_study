* [Back to Dive into Deep Learning](../../main.md)

# 4.1 Softmax Regression

## 4.1.1 Classification
#### Problem Setting) Image Classification
- Input : $2\times2$ grey scale image
  - Represent each pixel with $x_1, x_2, x_3, x_4$
- Output : Three categories of “cat”, “chicken”, and “dog”.
  - Using [the one-hot encoding](#concept-one-hot-encoding) below, we may represent as $`y \in \{(1, 0, 0), (0, 1, 0), (0, 0, 1)\}`$

#### Concept) One-Hot Encoding
- Desc.)
  - A vector with as many components as we have categories.
  - The component corresponding to a particular instance’s category is set to 1 and all other components are set to 0.

<br>

### 4.1.1.1 Linear Model
- Model)
  - Recall that we had 
    - 4 features : $x_1, x_2, x_3, x_4$
    - 3 classes of output : $`y \in \{(1, 0, 0), (0, 1, 0), (0, 0, 1)\}`$
      - Denote them as $o_1, o_2, o_3$
  - Thus, the linear model goes...
    - $`\begin{aligned}   o_1 &= x_1 w_{11} + x_2 w_{12} + x_3 w_{13} + x_4 w_{14} + b_1,\\   o_2 &= x_1 w_{21} + x_2 w_{22} + x_3 w_{23} + x_4 w_{24} + b_2,\\ o_3 &= x_1 w_{31} + x_2 w_{32} + x_3 w_{33} + x_4 w_{34} + b_3.   \end{aligned}`$
      - Simply put,
        - $`\mathbf{o} = \mathbf{W} \mathbf{x} + \mathbf{b}`$


- Desc.)
  - Fully connected Layer   
    ![](images/001.png)
- Problems)
  - $\displaystyle \sum_{i=1,2,3}o_i\ne 1$
    - i.e.) There is no guarantee that the outputs $`o_i`$ sum up to $`1`$ in the way we expect probabilities to behave.
  - $\exists o_i \notin [0,1]$
    - There is no guarantee that the outputs $`o_i`$ are even nonnegative, even if their outputs sum up to $`1`$, or that they do not exceed $`1`$.
- **Alternative Sol.)**
  - [Softmax Regression](#4112-softmax-model)

<br>

### 4.1.1.2 Softmax Model
#### Concept) Softmax Function
- Def.)
  - $\hat{\mathbf{y}} = \mathrm{softmax}(\mathbf{o}) \quad \textrm{where}\quad \hat{y}_i = \frac{\exp(o_i)}{\sum_j \exp(o_j)}$
- Prop.)
  - The softmax operation preserves the ordering among its arguments.
    - Thus, $\displaystyle{\arg\max}_j \hat y_j = {\arg\max}_j o_j$



<br>

* [Back to Dive into Deep Learning](../../main.md)