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

### [Exercises](./exercises.md)

<br><br>

* [Back to Statistics Main](../../main.md)