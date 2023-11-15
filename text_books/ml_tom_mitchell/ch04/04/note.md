* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 4.4 Perceptrons

#### Concept) Perceptron
- Desc.)
  - Takes a vector of real-valued inputs
  - Calculates a linear combination of these inputs
  - Outputs a 1 if the result is greater than some threshold and -1 otherwise.
- Notation)
  - Inputs : $x_1, x_2, ..., x_n$
  - Outputs : $`o(x_1, x_2, ..., x_n) = \left\lbrace \begin{array}{cl} 1 & if \space w_0+w_1x_1+w_2x_2+\cdots+w_nx_n \gt 0 \\ -1 & otherwise \end{array} \right.`$
    - where each $w_i$ is a real-valued constant or weight
      - $w_i$ determines the contribution of input $x_i$
    - Put $\Sigma_{i=0}^n w_ix_i = w\cdot x \gt 0$.
    - Also, $o(x) = sgn(w\cdot x)$
      - where $`sgn(y)=\left\lbrace \begin{array}{cl} 1 & if \space y \gt 0 \\ -1 & otherwise \end{array} \right.`$

![](images/001.png)

#### Concept) Learning a perceptron
- Involves choosing values for the weights $w_0, \dots, w_n$.
- Thus, the candidate hypotheses' space $H$ is the set of all possible real-valued weight vectors.
  - i.e.) $H = \lbrace w | w \in \mathbb{R}^{n+1} \rbrace$

<br><br>

## 4.4.1 Representational Power of Perceptrons
#### Concept) Geometrical View of a Perceptron
<table>
<tr><td><img src="images/002.png"></td><td>We can view the perceptron as representing a hyperplane decision surface in the n-dimensional space of instances (i.e., points). <br><br> <img src="images/003.png">  </td></tr>
</table>

- Above cases are **linearly separable**.
- Some operations like XOR are not separable.   
  ![](images/004.png)





<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)