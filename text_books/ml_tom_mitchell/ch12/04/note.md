* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 12.4 Using Prior Knowledge to Alter the Search Objective
- Objective)
  - Incorporate prior knowledge into the error criterion minimized by gradient descent, so that the network must fit a combined function of the training data and domain theory.
  - We will consider prior knowledge in the form of known derivatives of the target function.
    - e.g.) Handwritten character recognition problem
      - Prior Knowledge : "The identity of the character is independent of small translations and rotations of the image."
      - We can specify certain derivatives of the target function in order to express the above prior knowledge.

<br>

## Concept) The TangentProp Algorithm
*Simard et al. 1992*
#### Desc.)
- The TangentProp Algorithm accommodates **domain knowledge expressed as derivatives of the target function** w.r.t. transformations of its inputs.

<br>

### Simple Model Ex.)
- Settings)
  - $f$ : the target function
  - $X$ : the instance space
    - Each instance $x_i$ is described by a single real value.
    - Each training example is in the form $`\displaystyle \left\langle x_i, \; f(x_i), \; \left.\frac{\partial f(x)}{\partial x}\right|_{x_i} \right\rangle`$
      - where $`\displaystyle \left.\frac{\partial f(x)}{\partial x}\right|_{x_i}`$ denotes the derivative of the target function $f$ w.r.t. $x$ evaluated at the point $x=x_i$.

#### Analysis) Comparison with Backpropagation
- The impact of including the training **derivatives** is to override the usual syntactic inductive bias of Backpropagation that favors a smooth interpolation between points, replacing it by explicit input information about required derivatives.   

![](images/001.png)

- Compared to $g$, the resulting hypothesis $h$ shown in the rightmost plot of the figure provides a much more accurate estimate of the true target function $f$.










<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)