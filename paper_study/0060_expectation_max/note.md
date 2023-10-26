* [Back to Main](../../README.md)

# The Expectation Maximization Algorithm
### T. K. Moon
* [Read Paper](../paper_pdfs/231023%20expectation_maximization.pdf)

---


## The Expectation-Maximization Algorithm (EM Algorithm)
#### Def.) EM Algorithm
An algorithm that consists of two steps that are repeated until the parameter estimates converge.
  1. Expectation Step
     * Make expectations for unknown underlying variables.
     * Use the current estimate of the parameters
     * Is conditioned upon observations
  2. Maximization Step
     * Provide new estimate of the parameters

<br>

#### Prop.) Problems in Parameter Estimation and the EM Algorithm
* There are some problems in parameter estimation such as...
  1. Estimating the mean of a noise
  2. Direct access to the data necessary to estimate the parameters is impossible
  3. Some of the data are missing  
* EM algorithm is ideally suited for these kinds of problems
  * why?)
    * It produces [maximum-likelihood(ML) estimates](maximum_likelihood.md) of parameters when there is a **many-to-one mapping** from an underlying distribution to the distribution governing the observation.
 

<br>

#### Ex.) Ector's Problem
* Situation
  * An image pattern-recognition problem
    * Classes
      * Light Object
      * Dark Round Object
      * Dark Square Object
* Modeling
  * Settings
    * $X_1$ : the random variable representing the number of round dark objects
    * $X_2$ : the random variable representing the number of square dark objects
    * $X_3$ : the random variable representing the number of light objects
    * $x = [x_1, x_2, x_3]^T$ : the column vector of values that random variables take for a sample image
  * The Probability Density Function : $f$
    * $P(X_1=x_1, X_2=x_2, X_3=x_3 | p) \\ = \left( \frac{n!}{x_1!x_2!x_3!} \right) \left( \frac{1}{4} \right)^{x_1} \left( \frac{1}{4} + \frac{p}{4} \right)^{x_2} \left( \frac{1}{2} - \frac{p}{4} \right)^{x_3} \\ = f(x_1, x_2, x_3|p)$
      * where $p$ is an unknown parameter
      * and $n=x_1+x_2+x_3$
* Problem
  * Suppose we are given a feature extractor that can distinguish between dark and light but cannot distinguish the shape.
    * Let $[y_1, y_2]^T = y$ be the number of dark and light objects.
    * Then $y_1 = x_1 + x_2$ and $y_2 = x_3$.
  * We now have observations that are denoted in $\lbrace y_1, y_2 \rbrace$
  * The problem is that we cannot distinguish between the $x_1$ and $x_2$.
  * In other words, we do not know the distribution of $f(x_1, x_2, x_3|p)$
* Solution : EM Algorithm
  * Settings
    * Put $Y_1$ and $Y_2$ the respective random variables.
    * Here is the **many-to-one mapping** between $\lbrace x_1, x_2 \rbrace$ and $y_1$.
      * e.g.) If $y_1=3$, we don't know whether $x_1=1,x_2=2$ or $x_1=2,x_2=1$.
    * Put observations into a new pdf : $g$
      * $`P(Y_1=y_1 | p) \\ = {}_nC_{y_1} \left( \frac{1}{4} + \frac{p}{4} \right)^{y_1} \left( \frac{1}{2} - \frac{p}{4} \right)^{n - y_1} \\ = g(y_1|p)`$
    * Using the EM Algorithm, we can compute the ML estimate of $p$ which is...
      * $p_{ML}=argmax_p \space g(Y_1=y_1|p)$
        * where $argmax$ means the value that maximizes the function
      * Simplify the above function using log.
        * $p_{ML}=argmax_p \space \log{g(Y_1=y_1|p)}$
    * Let $p^{[k]}$ be the estimate of $p$ after the $k$-th iteration.
  * Actual Steps
    1. Expectation Step
       * The expected value of $x_1$ given $y_1$ and the current($k$-th) estimate of the parameter
         * ${x_1}^{[k]} = E[x_1|y_1, p^{[k]}]$
    2. Maximization Step
       * d



---
* [Back to Main](../../README.md)