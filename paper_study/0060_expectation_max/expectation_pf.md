# Combination and Conditional Expectations Multinomials

## Prop. 1) 

For $0 \lt i \lt n$,  
$P(X_1+X_2 = y) = (p_1+p_2)^y$
* Why?)   
  $`\begin{array}{lcl} P(X_1+X_2 = y) & = & P(X_1=i, X_2=y-i) \\ &=& \Sigma_{x_1=0}^y \frac{(i+(y-i))!}{i!(y-i)!} p_1^i p_2^{y-i} \\&=& \Sigma_{x_1=0}^y \frac{y!}{i!(y-i)!} p_1^i p_2^{y-i} \\&=& (p_1+p_2)^y \end{array}`$

<br>

## Tech.) Computing the Binomial Class probability
#### Derivation)
* Let $X_1, X_2, X_3$ have a multinomial distribution with class probabilities $(p_1, p_2, p_3)$.   
* Then, $P(X_1=x_1, X_2=x_2, X_3=x_3) = \frac{(x_1+x_2+x_3)!}{x_1!x_2!x_3}p_1^{x_1}p_2^{x_2}p_3^{x_3}$
* Let $Y=X_1+X_2$.   
* Then, the probability $P(Y,X_3)$ can be determined as follows:   
  $`\begin{array}{lcl} P(X_1+X_2=y, X_3=x_3) & = & \Sigma_{i=0}^y P(X_1=i, X_2=y-i, X_3=x_3) \\ & = & \frac{(y+x_3)!}{y!x_3!} p_3^{x_3} \Sigma_{i=0}^y \frac{y!}{i!(y-i)!} p_1^i p_2^{y-i} \\ & = & \frac{(y+x_3)!}{y!x_3!} {(p_1+p_2)}^y p_3^{x_3} \space (\because the \space binomial \space theorem) \end{array}`$    
* Thus, $(X_1+X_2, X_3)$ is binomial with class probabilities $(p_1+p_2, p_3)$.   
  * This can be generalized to multinomials!

#### Result 1)
* $P(X_1+X_2=y, X_3=x_3) = \frac{(y+x_3)!}{y!x_3!} {(p_1+p_2)}^y p_3^{x_3}$

<br><br>

## Tech.) Computing the Conditional Expectation
#### Goal)
* Compute the conditional expectation $E[X_1 | Y=y]$.
#### Derivation)
* First, determine the conditional probability, $P(X_1=x_1 | Y=y) = P(X_1=x_1 | X_1+X_2=y)$.   
  * why?)
    * $E[X_1 | Y=y] = \Sigma_{x_1=0}^{y} x_1 P(X_1=x_1 | Y=y)$
    * We need $P(X_1=x_1 | Y=y)$
* By definition,   
  $`\begin{array}{lcl} P(X_1=x_1 | Y=y) & = & \frac{P(X_1=x_1, Y=y)}{P(Y=y)} \space (\because P(A|B)=\frac{P(A \cap B)}{P(B)}) \\ &=& \frac{P(X_1=x_1, X_2=y-x_1)}{P(Y=y)} \end{array}`$   
* Let's separate this into the denominator and the nominator
  * Denominator : $P(X_1=x_1, Y=y) = (X_1=x_1, X_2=y-x_1)$ 
    * binomial out of $n$ trials
    * Thus, $P(X_1=x_1, X_2=y-x_1) = \frac{(x_1+(y-x_1))!}{x_1!(y-x_1)!} p_1^{x_1} p_2^{y-x_1} = \frac{y!}{x_1!(y-x_1)!} p_1^{x_1} p_2^{y-x_1}$
  * Nominator : $P(Y=y)$ 
    * trinomial out of $n$ trials
    * $P(Y=y) = P(X_1+X_2=y)$ 