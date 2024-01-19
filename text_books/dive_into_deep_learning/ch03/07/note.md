* [Back to Dive into Deep Learning](../../main.md)

# 3.7 Weight Decay

### Concept) Limits of the Previously Covered Regularization Techniques
1. Collecting more training data
   - Costly, time consuming, or entirely out of our control, making it impossible in the short run.
2. Tweaking the degree of the fitted polynomial
   - Simply tossing aside features can be too blunt an instrument
   - The number of terms with degree $d$ blows up rapidly as $d$ grows larger.
     - e.g.)
       - Suppose $k$ variable are given.
       - Then the number of monomials of degree $d$ is $`{}_{k-1++d} C_{k-1}`$
         - where monomials are the natural extensions of polynomials to multivariate data.
           - e.g.) monomials of degree 3 : $`x_1x_2^2, \;x_4^3, \;x_5x_6x_7`$

<br><br>

## 3.7.2 Norms and Weight Decay
### Concept) Weight Decay
- Intuition)
  - We want to restrict the values that the parameters can take.
  - Before that we want to define the value of the parameters.
  - The value of the parameters may be defined as the distance of the from zero.
  - Among all functions $\mathcal{f}$, the function $\mathcal{f}=0$ is the simplest form.
  - Thus, we may measure the distance of its parameters from zero.
  - There is no single right answer. 
    - In fact, entire branches of mathematics, including parts of functional analysis and the theory of Banach spaces, are devoted to addressing such issues.
- Simpler Approach)
  - Consider the norm of the weight vector : $||\mathbf{w}||^2$










<br>

* [Back to Dive into Deep Learning](../../main.md)