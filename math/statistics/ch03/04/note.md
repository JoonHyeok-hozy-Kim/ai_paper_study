* [Back to Statistics Main](../../main.md)

# 3.4 Functions of Random Variables
#### Objective)
- The methods of finding the probability distribution of a function of a
random variable $X$.
  - e.g.)
    - Suppose the velocity $V$ of a gas molecule behaves as a gamma-distributed random variable.
    - Then what is the distribution of $E = mV^2$.
      - i.e.) This is a problem of finding the distribution of a function of a random variable $E = g(V)$.

<br><br>

## 3.4.1 Method of Distribution Functions
- Desc.)
  - If $X$ is a random variable with pdf $f_X(x)$ and if $Y$ is some function of $X$, then we can find the cdf $F_Y(y) = P(Y \le y)$ directly by integrating $f_X(x)$ over the region for which $\lbrace Y \le y\rbrace$.
- Procedure)   

![](images/001.png)


#### Examples)
- Continuous Case)
   - Let $X \sim N(0,1)$. Find the pdf of $X^2$.
      - Sol.)   

![](images/002.png)   
![](images/003.png)   

- Discrete Case)
   - Let $X \sim Poisson(\lambda)$. Find the cdf of $Y=aX+b$.
      - Sol.)    

![](images/004.png)   

<br><br>

## 3.4.2 The pdf of Y=g(X), Where g is Differentiable and Monotone Increasing or Decreasing
- Settings)
  - $Y=g(X)$ a random variable
    - where $X$ is a continuous random variable with pdf $f_X(x)$.
    - and $g$ is differentiable and the inverse function $g^{-1}$ of $g$ exists.
- Derivation)
  - Then, $X = g^{-1}(Y)$.
  - Let $f_X(x)$ the pdf of $X$.
  - Then $f_Y(y)$, the pdf of $Y$, is...
    - $f_Y(y) = f_X(g^{-1}(y))\cdot\frac{d}{dy}g^{-1}(y)$
- Example)
  - Let $X \sim N(0,1)$. Find the pdf of $Y=e^X$.
    - Sol.)   

![](images/005.png)

<br><br>

## 3.4.3 Probability Integral Transformation
![](images/006.png)
- Example)
  - Let $X \sim N(\mu,\sigma^2)$.
    - Sol.)
      - Then   

![](images/007.png)
![](images/008.png)

<br><br>

## 3.4.4 Functions of Several Random Variables: Method of Distribution Functions
- i.e.) $Y$ is a function of several random variables.
  - $Y=g(X_1, \cdots, X_n)$

#### Example : min/max function
1. $Y_1 = min(X_1, \cdots, X_n)$

![](images/009.png)

<br>

2. $Y_n = max(X_1, \cdots, X_n)$

![](images/010.png)

<br><br>

## 3.4.5 Transformation Method
- For functions of more than one variable

<br>

### Concept) Bivariate Distribution Case
- Let
  - $X,Y,U,V$ : random variables
  - $f(x, y)$ : the joint pdf of $(X,Y)$
  - $U = g_1(X,Y)$
  - $V = g_2(X,Y)$
  - The mapping from $(X,Y)$ to $(U,V)$ is one-to-one and onto.
- Then, $\exists h_1, h_2$ such that
  - $x=h_1^{-1}(u,v)$
  - $y=h_2^{-1}(u,v)$
- Define the Jacobian of the transformation $J$ by
  - $`J=\left\vert \begin{array}{cc} \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\ \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} \end{array} \right\vert`$
- Then the joint pdf of $U$ and $V$ is given by
  - $f(u,v) = f\left(h_1^{-1}(u,v), h_2^{-1}(u,v) \right) |J|$

#### e.g.)
![](images/011.png)
- Additionally, the marginal pdf will be...
  ![](images/012.png)

<br>

#### Tech.) Bivariate to One Variable Expression
Call the given expression of $X$ and $Y$ as $U$, and define $V = Y$.

- e.g.)   
  ![](images/013.png)   
  ![](images/014.png)   
  ![](images/015.png)   
  ![](images/016.png)   


### [Exercises](./exercises.md)

<br><br>

* [Back to Statistics Main](../../main.md)