* [Back to Deep Learning MIT](../../main.md)

# 4.3 Gradient-Based Optimization

## 4.3.1 Optimization
#### Concept) Optimization
- Optimization refers to the task of either minimizing or maximizing some function $`f(x)`$ by altering $`x`$.
#### Concept) Objective Function (Criterion)
- The function we want to optimize.
#### Concept) Cost Function (Loss Function, Error Function)
- Specific name for the objective function in case of minimizing.

#### Notation) Asterisk (*)
- Meaning)
  - The value that minimizes or maximizes a function.
- e.g.)
  - $`\displaystyle x^\ast = \arg\min_x f(x)`$

<br>

## 4.3.2 Gradient Descent
### Concept) Derivative
- Def.)
  - Let
    - $`y=f(x)`$
      - where $`x,y\in \mathbb{R}`$
  - The derivative of $`f(x)`$ is $`f'(x) = \frac{dy}{dx}`$
- Prop.)
  - The derivative gives the slope of $`f(x)`$ at the point $`x`$.
    - i.e.) $`f(x+\epsilon) \approx f(x) + \epsilon f'(x)`$

#### Concept) Critical Point (Stationary Point)
- Def.)
  - Point $`x`$ where $`f'(x)=0`$.
- Prop.)
  - The derivative at the critical point provides no information about which direction to move.
  - It is either a local minimum, a local maximum, or a saddle point.

<br>

### Concept) Gradient
- Def.)
  - $`f:\mathbb{R}^n\rightarrow\mathbb{R}`$
  - The **gradient** $`\nabla_x f(x)`$ is the vector containing all of the partial derivatives
    - where **partial derivatives** $`\frac{\partial}{\partial x_i} f(x)`$ measures how $`f`$ changes as only the variable $`x_i`$ increases at point $`x`$.
    - i.e.) $`\nabla_x f(x) = \left[\begin{array}{c}
      \frac{\partial}{\partial x_1} f(x) \\ \vdots \\ \frac{\partial}{\partial x_n} f(x)
    \end{array}\right]`$
    - In this case, the [critical point](#concept-critical-point-stationary-point) is when $`\nabla_x f(x) = 0, \textrm{ i.e. } \frac{\partial}{\partial x_i} f(x) = 0, \forall i`$
- Props.)
  - In the multivariate function case, the [critical point](#concept-critical-point-stationary-point) is $`x`$ such that $`\nabla_x f(x) = 0, \textrm{ i.e. } \frac{\partial}{\partial x_i} f(x) = 0, \forall i`$

<br>

### Concept) Directional Derivative
- Def.)
  - $`\frac{\partial}{\partial\alpha} f(x+\alpha u)`$
    - where 
      - $`u`$ : a unit vector.
      - $`\alpha \in \mathbb{R}`$
- Meaning)
  - The slope of $`f`$ in direction $`u`$.
- Usage)
  - When $`\alpha = 0`$, 
    - $`\frac{\partial}{\partial\alpha} f(x+\alpha u) = u^\top \nabla_x f(x)`$
  - Thus, we can seek a critical point by minimizing $`u^\top \nabla_x f(x)`$
    - i.e.) Find $`x \textrm{ such that } u^\top \nabla_x f(x) = 0`$.

<br>

### Concept) Gradient Descent (Method of Steepest Descent)
- Desc.)
  - A technique that reduce $`f(x)`$ by moving $`x`$ in small steps with **opposite sign** of the [derivative](#concept-derivative).
- How?)
  - Settings)
    - $`f:\mathbb{R}^n\rightarrow\mathbb{R}`$
    - $`\nabla_x f(x)`$ : the [gradient](#concept-gradient)
    - $`\frac{\partial}{\partial\alpha} f(x+\alpha u)`$ : the [directional derivative](#concept-directional-derivative)
  - Ideation)
    - Recall that we want to find a [critical point](#concept-critical-point-stationary-point) by minimizing the derivative.
    - Also, we found that the [directional derivative](#concept-directional-derivative) $`\frac{\partial}{\partial\alpha} f(x+\alpha u)`$ was the slope of $`f`$ in direction $`u`$.
    - Thus, we will find the [critical point](#concept-critical-point-stationary-point) by solving the following problem.
      - $`\displaystyle\min_{u, u^\top u=1} u^\top \nabla_x f(x)`$
      - $`\displaystyle\min_{u, u^\top u=1} ||u||_2 \; ||\nabla_x f(x)||_2 \; \cos\theta`$
        - where $`\theta`$ is the angle between $`u`$ and the gradient.
        - Why?)
          - Recall the property of the dot product.
            - $`u \cdot v = |u||v|\cos\theta`$
      - $`\therefore \textrm{Solve } \displaystyle\min_{u} \cos\theta`$
        - Why?)
          - $`||u||_2=1`$
          - The gradient does not depend on $`u`$.
  - Optimization)
    - $`\displaystyle\min_{u} \cos\theta`$
      - where $`\theta`$ is the angle between $`u`$ and the gradient.
  - Repetition)
    - After the optimization, a new point is proposed as $`x' = x - \epsilon\nabla_x f(x)`$.
      - where $`\epsilon`$ is the learning rate.
        - cf.) How to set $`\epsilon`$?
          - e.g.)
            - Line Search
              - Evaluate $`f(x - \epsilon\nabla_x f(x))`$ for several values of $`\epsilon`$ and choose the one that results in the smallest objective function value.
    - Repeat the process until, $`\nabla_x f(x)=0`$ is accomplished.

<br><br>

## 4.3.3 Jacobian and Hessian Matrices
### Concept) Jacobian Matrix
- Def.)
  - For $`f:\mathbb{R}^m\rightarrow\mathbb{R}^n`$
  - the Jacobian Matrix $`J\in\mathbb{R}^{m\times n}`$ is defined as
    - $`J_{i,j} = \frac{\partial}{\partial x_j} f(x)_i`$

<br>

### Concept) Second Derivative
- Def.)
  - For $`f:\mathbb{R}^n\rightarrow\mathbb{R}`$
  - the second derivative can be defined as
    - $`\frac{\partial^2}{\partial x_i \partial x_j} f`$
- Prop.)
  - The second derivative tells us **how the first derivative will change** as we vary the input.
  - We can think of the second derivative as measuring **curvature**.
    - e.g.) Quadratic Function
      - If such a function has a **second derivative** of zero, then there is no curvature.
      - If the **gradient** is $`1`$, then we can make a step of size $`\epsilon`$ along the negative gradient, and the cost function will decrease by $`\epsilon`$.
        - If the **second derivative is negative**, the function curves downward, so the cost function will actually decrease by more than $`\epsilon`$.
        - If the **second derivative is positive**, the function curves upward, so the cost function can decrease by less than $`\epsilon`$.


<br>

### Concept) Hessian Matrix
- Def.)
  - $`H(f)(x)_{i,j} = \frac{\partial^2}{\partial x_i \partial x_j} f(x)`$
- Desc.)
  - For a function with multiple input dimensions, there are many [second derivatives](#concept-second-derivative).
  - The Hessian matrix consists them.
- Prop.)
  - The Hessian matrix is symmetrical.
    - Why?)
      - Second partial derivatives are commutative.
          - $`\frac{\partial^2}{\partial x_i \partial x_j} f(x) = \frac{\partial^2}{\partial x_j \partial x_i} f(x) `$
  - The Hessian is the [Jacobian](#concept-jacobian-matrix) of the [gradient](#concept-gradient).
    - Why?)
      - $`\nabla_x f(x) = \left[\begin{array}{c} \frac{\partial}{\partial x_1} f(x) \\ \vdots \\ \frac{\partial}{\partial x_n} f(x) \end{array}\right]`$ : the gradient
      - Thus, the Jacobian of the gradient goes $`\left[\begin{array}{ccc}
        \frac{\partial^2}{\partial x_1 \partial x_1} f(x) & \cdots &  \frac{\partial^2}{\partial x_n \partial x_1} f(x) \\
        \frac{\partial^2}{\partial x_1 \partial x_2} f(x) & \cdots &  \frac{\partial^2}{\partial x_n \partial x_2} f(x) \\
        \vdots & \ddots & \vdots \\
        \frac{\partial^2}{\partial x_1 \partial x_n} f(x) & \cdots &  \frac{\partial^2}{\partial x_n \partial x_n} f(x) \\
      \end{array}\right] \equiv H(f)(x)_{i,j}`$
        - Recall that second partial derivatives are **commutative**.
  - The Hessian matrix can be decomposed into a set of real eigenvalues and an orthogonal basis of eigenvectors.

<br>

### Concept) Directional Second Derivative
- Def.)
  - The second derivative in a specific direction.
  - It can be represented by $`d^\top H d`$.
    - where
      - $`d`$ : a unit vector
      - $`H`$ : the Hessian matrix
    - Why?)
      - Suppose $`d = \begin{bmatrix} 1 \\ 0 \\ \vdots \\ 0 \end{bmatrix}`$.
      - Then, $`d^\top H d = \left(\frac{\partial}{\partial x_1}\right)^2f(x)`$
- Props.)
  - If $`d`$ is the [eigenvector](../../ch02/07/note.md#concept-eigenvector-and-eigenvalue) of $`H`$, the second derivative in that direction is given by the corresponding eigenvalue.
    - Why?)
      - By the definition of the eigenvector, $`d^\top Hd = d^\top (\lambda d) = \lambda d^\top d = \lambda \; (\because ||d||_2 = 1)`$.
  - If $`d`$ is not an eigenvector, the directional second derivative is a **weighted average of all of the eigenvalues** with weights between 0 and 1.
    - cf.) 
      - Eigenvectors with smaller angle with $`d`$ receives more weight.
      - The maximum(minimum) eigenvalue determines the maximum(minimum) second derivative.
  - The (directional) second derivative tells us how well we can expect a [gradient descent](#concept-gradient-descent-method-of-steepest-descent) step to perform.
    - Suppose we applied the [gradient descent method](#concept-gradient-descent-method-of-steepest-descent) at $`x = x^{(0)}`$ with the learning rate $`\epsilon`$.
      - Then the new $x$ can be denoted as $`x^{(0)} - \epsilon g`$.
        - where $`g`$ is the gradient.
    - Then we can use the **Second Order Taylor Series Approximation** to approximate the value of $`f`$ at the new point.
      - Concept) The Second Order Taylor Series Approximation
        - $`f(x) \approx f(x^{(0)}) + (x - x^{(0)})^\top g + \frac{1}{2}(x - x^{(0)})^\top H(x - x^{(0)})`$
          - where
            - $`g`$ : the gradient
            - $`H`$ : the Hessian
      - Thus, $`f(x^{(0)} - \epsilon g) \approx f(x^{(0)}) - \epsilon g^\top g + \frac{1}{2}\epsilon^2 g^\top H g`$
        - Interpretation)
          - $`f(x^{(0)})`$ : the original value of the function
          - $`-\epsilon g^\top g`$ : the expected improvement due to the slope of the function
            - Why negative?)
              - Recall that we had to move $`x`$ in small steps with [opposite sign of the derivative](#concept-gradient-descent-method-of-steepest-descent).
          - $`\frac{1}{2}\epsilon^2 g^\top H g`$ : the correction we must apply to account for the curvature of the function
            - If this term is too large, the gradient descent step can actually move **uphill**
              - which means that the algorithm is **NOT minimizing** the loss.
            - cf.) Getting the appropriate $`\epsilon`$ value.
              - $`\displaystyle\epsilon^\ast = \frac{g^\top g}{g^\top H g}`$ : the optimal step size that decreases the Taylor series approximation.
                - Worst Case) 
                  - $`g`$ aligns with the eigenvector of $`H`$ corresponding to the maximal eigenvalue $`\lambda_{\max}`$
                    - Then $`\displaystyle\epsilon^\ast = \frac{1}{\lambda_{\max}}`$
                      - Why?)
                        - $`g^\top g = 1 \; (\because g \textrm{ is an unit vector.})`$
                        - $`g^\top H g = g^\top (\lambda_{\max})g = \lambda_{\max} g^\top g = \lambda_{\max}`$


<br>

* [Back to Deep Learning MIT](../../main.md)