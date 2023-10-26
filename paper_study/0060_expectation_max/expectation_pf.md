# Combination and Conditional Expectations Multinomials

Let $X_1, X_2, X_3$ have a multinomial distribution with class probabilities $(p_1, p_2, p_3)$.   
Then, $P(X_1=x_1, X_2=x_2, X_3=x_3) = \frac{(x_1+x_2+x_3)!}{x_1!x_2!x_3}p_1^{x_1}p_2^{x_2}p_3^{x_3}$

<br>

Let $Y=X_1+X_2$.   
Then, the probability $P(Y,X_3)$ can be determined as follows:
* $`\begin{array}{lcl} P(X_1+X_2=y, X_3=x_3) & = & \Sigma_{i=0}^y P(X_1=i, X_2=y-i, X_3=x_3) \\ & = & \frac{(y+x_3)!}{y!x_3!} p_3^{x_3} \Sigma_{i=0}^y \frac{y!}{i!(y-i)!} p_1^i p_2^{y-i} \\ & = & \frac{(y+x_3)!}{y!x_3!} {(p_1+p_2)}^y p_3^{x_3} \space (\because the \space binomial \space theorem) \end{array}`$