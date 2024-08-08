* [Back to Deep Learning MIT](../../main.md)

# 8.5 Algorithms with Adaptive Learning Rates

## 8.5.1 AdaGrad

<br>

## 8.5.2 RMSProp

<br>

## 8.5.3 Adam
- Algorithm)
  - Inputs)
    - $`\epsilon`$ : the step size
    - $`\rho_1, \rho_2 \in [0,1)`$ : the exponential decay rates for moment estimates
    - $`\delta`$ : a small constant used for numerical stabilization
    - $`\theta`$ : the initial parameters
  - Procedure)
    - Initialize the first and second moment variables $`s=0, r=0`$.
    - Initialize time step $`t=0`$.
    - `while` stopping criterion not met `do`
      - Sample a minibatch of $`m`$ examples from the training set $`\{x^{(1)}, \cdots, x^{(m)}\}`$ with corresponding targets $`y^{(i)}`$.
      - Compute gradient : $`\displaystyle g \leftarrow \frac{1}{m}\nabla_\theta \sum_i L\left(f(x^{(i)};\theta), y^{(i)}\right)`$
      - $`t \leftarrow t+1`$
      - Update biased first moment estimate : $`s \leftarrow \rho_1 s + (1-\rho_1)g`$
      - Update biased second moment estimate : $`r \leftarrow \rho_2 r + (1-\rho_2)g\odot g`$
      - Correct bias in first moment : $`\displaystyle \hat{s} \leftarrow\frac{s}{1-\rho_1^t}`$
      - Correct bias in second moment : $`\displaystyle \hat{r} \leftarrow\frac{r}{1-\rho_2^t}`$
      - Compute update : $`\displaystyle \Delta\theta = -\epsilon \frac{\hat{s}}{\sqrt{\hat{r}}+\delta}`$
      - Apply update : $`\theta \leftarrow \theta + \Delta\theta`$
    - `end while`
- Ideation)
  - Consider the second-order Taylor series expansion to approximate $`J(\theta)`$ near som point $`\theta_0`$.
    - $`\displaystyle J(\theta) \approx J(\theta_0) + (\theta-\theta_0)^\top \nabla_\theta J(\theta_0) + \frac{1}{2} (\theta-\theta_0)^\top H(\theta-\theta_0)`$
      - where $`H`$ is the Hessian of $`J`$ w.r.t. $`\theta = \theta_0`$.
  - Solving for the critical point of this function, we obtain the Newton parameter update rule:
    - $`\theta^\ast = \theta_0 - H^{-1}\nabla_\theta J(\theta_0)`$

<br>

## 8.5.4 Choosing the Right Optimization Algorithm











<br>

* [Back to Deep Learning MIT](../../main.md)