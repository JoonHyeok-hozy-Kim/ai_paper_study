* [Back to Deep Learning MIT](../../main.md)

# 6.0 Deep Feedforward Networks

### Concept) Deep Feedforward Network (Multilayer Perceptron, MLP)
- Goal)
  - Approximate some function $`f^\ast`$.
    - How?)
      - Put $`y = f(x;\theta)`$.
      - Learn the value of parameters $`\theta`$ that result in the best function approximation.
- Props.)
  - Information flows ...
    1. through the function being evaluated from $`x`$
    2. through the intermediate computations used to define $`f`$
    3. finally to the output $`y`$.
  - There are **no feedback connections** in which outputs of the model are fed back into itself.
    - cf.) Recurrent Neural Network has such.
- Structure)
  - The model is associated with a **directed acyclic graph** describing how the functions are composed together.
    - e.g.) Functions $`f^{(1)}, f^{(2)}, f^{(3)} \textrm{ such that } f(x)=f^{(3)}(f^{(2)}(f^{(1)}(x)))`$
      - $`i`$-th function denotes the $`i`$-th **layer** of the network.
      - Each $`f^{(i)}`$ is a vector-to-vector function.
      - Each **layer** consists of many **units** that act in parallel, each representing a vector-to-scalar function.
  - The **depth** of a model is given by the length of its chain.
  - The **output layer** is the final layer of a feedforward network.
    - It must produce a value that is close to $`y`$ at each point $`x`$.
  - The **training data (example)**
    - provides us with noisy, approximate examples of $`f^\ast(x)`$ evaluated at different training points.
    - does not say what each individual layer should do.
      - Instead, the learning algorithm must decide how to use these layers to best implement an approximation of $`f^\ast`$
      - Because the training data does not show the desired output for each of these layers, these layers are called **hidden layers**.
  - The **width** of a model is determined by the dimensionality of its hidden layers.

<br>

### Analysis) Comparison with Linear Models
- Linear Models)
  - Advantage)
    - Fits efficiently and reliably, either in closed form or with convex optimization.
  - Drawback)
    - The model capacity is limited to **linear** functions.
      - Thus, the model cannot understand the **interaction** between any two input variables.
- Applying linear model to a transformed input $`\phi(x)`$, where $`\phi`$ is a nonlinear transformation.
  - How?)
    1. Use a very generic $`\phi`$.
       - e.g.) Infinite Dimensional $`\phi`$ : [RBF Kernel](../../ch05/07/note.md#eg-gaussian-kernel-radial-basis-function-rbf)
       - Pro) 
         - Enough capacity to fit the training set
       - Cons)
         - Generalization to the test set often remains poor.
         - Very generic feature mappings are usually based only on the principle of [local smoothness](../../ch05/11/note.md#concept-smoothness-prior-local-constancy-prior) and do not encode enough prior information to solve advanced problems.
    2. Manually engineer $`\phi`$.
       - Desc.)
         - This approach requires decades of human effort for each separate task, with practitioners specializing in different domains such as speech recognition or computer vision, and with **little transfer between domains**.
    3. Learn $`\phi`$ as deep learning does.
       - Model)
         - $`y = f(x;\theta,w) = \phi(x;\theta)^\top w`$
           - where
             - $`\theta`$ : parameters used to learn $`\phi`$ from a broad class of functions
             - $`w`$ : parameters that map from $`\phi(x)`$ to the desired output.
       - Prop.)
         - $`\phi`$ defines the hidden layer.
         - This approach gives up the benefit of convexity of the training problem.
           - If we wish, this approach can capture the benefit of the first approach by being highly generic.
         - Human practitioners can encode their knowledge to help generalization by designing families $`\phi(x;\theta)`$ that they expect will perform well.





<br>

* [Back to Deep Learning MIT](../../main.md)