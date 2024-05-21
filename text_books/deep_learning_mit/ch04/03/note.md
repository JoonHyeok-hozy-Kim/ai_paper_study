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

### Concept) Gradient Descent (Method of Steepest Descent)
- Desc.)
  - A technique that reduce $`f(x)`$ by moving $`x`$ in small steps with **opposite sign** of the [derivative](#concept-derivative).
- How?)
  - Settings)
    - $`f:\mathbb{R}^n\rightarrow\mathbb{R}`$
    - The **gradient** $`\nabla_x f(x)`$ is the vector containing all of the partial derivatives
      - where **partial derivatives** $`\frac{\partial}{\partial x_i} f(x)`$ measures how $`f`$ changes as only the variable $`x_i`$ increases at point $`x`$.
      - i.e.) $`\nabla_x f(x) = \left[\begin{array}{c}
        \frac{\partial}{\partial x_1} f(x) \\ \vdots \\ \frac{\partial}{\partial x_n} f(x)
      \end{array}\right]`$
      - In this case, the [critical point](#concept-critical-point-stationary-point) is when $`\nabla_x f(x) = 0, \textrm{ i.e. } \frac{\partial}{\partial x_i} f(x) = 0, \forall i`$
    - $`\frac{\partial}{\partial\alpha} f(x+\alpha u)`$ : the directional derivative
      - where 
        - $`u`$ : a unit vector.
        - $`\alpha \in \mathbb{R}`$
      - Meaning)
        - The slope of $`f`$ in direction $`u`$.
      - Usage)
        - When $`\alpha = 0`$, 
          - $`\frac{\partial}{\partial\alpha} f(x+\alpha u) = u^\top \nabla_x f(x)`$
        - Thus, we will seek a critical point by minimizing $`u^\top \nabla_x f(x)`$
  - Derivation)
    - Recall that we want to find a [critical point](#concept-critical-point-stationary-point) by minimizing the derivative.
    - Also, we found that the directional derivative $`\frac{\partial}{\partial\alpha} f(x+\alpha u)`$ was the slope of $`f`$ in direction $`u`$.
    - Thus, we will find the [critical point](#concept-critical-point-stationary-point) by solving the following problem.
      - $`\displaystyle\min_{u, u^\top u=1} u^\top \nabla_x f(x)`$
      - $`\displaystyle\min_{u, u^\top u=1} ||u||_2 \; ||\nabla_x f(x)||_2 \; \cos\theta`$
        - where $`\theta`$ is the angle between $`u`$ and the gradient.
        - Why?)
          - Recall the property of the dot product.
            - $`u \cdot v = |u||v|\cos\theta`$
      - $`\displaystyle\min_{u} \cos\theta`$
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

* [Back to Deep Learning MIT](../../main.md)