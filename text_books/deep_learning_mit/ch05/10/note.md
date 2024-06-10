* [Back to Deep Learning MIT](../../main.md)

# 5.10 Building a Machine Learning Algorithm
- Prop.)
  - Nearly all deep learning algorithms can be described as particular instances of a fairly simple recipe:
    - Combining
      1. Specification of a Dataset
      2. Cost function
         - e.g.) 
           - Negative Log-Likelihood
           - Whether to add a **regularization** term or not
             - e.g.) Weight Decay : $`\lambda||w||_2^2`$
      3. Optimization Procedure 
         - e.g.) 
           - Closed form optimization problem for linear models
           - Gradient Descent for others
      4. Model
    - We can **replace** any of these components mostly **independently** from the others.
    - Thus, we can obtain a very wide variety of algorithms.














<br>

* [Back to Deep Learning MIT](../../main.md)