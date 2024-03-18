* [Back to Dive into Deep Learning](../../main.md)

# 5.3 Forward Propagation, Backward Propagation, and Computational Graphs

## 5.3.1. Forward Propagation
### Concept) Forward Propagation
- Def.)
  - Forward propagation (or forward pass) refers to the calculation and storage of intermediate variables (including outputs) for a neural network **in order from the input layer to the output layer**. 
- Derivation)
  - Assumptions)
    - $`\mathbf{x} \in \mathbb{R}^d`$ : an input example
    - Hidden layer does not include a bias term.
  - Output)
    - $\mathbf{o}= \mathbf{W}^{(2)} \mathbf{h}$
      - where
        - $`\mathbf{W}^{(2)} \in \mathbb{R}^{q \times h}`$ : the weight parameter of the output layer
        - $\mathbf{h}= \phi (\mathbf{z})$
          - where
            - $`\phi : \mathbb{R}^h \rightarrow \mathbb{R}^h`$ : the hidden activation function
            - $\mathbf{z}= \mathbf{W}^{(1)} \mathbf{x}$
              - where $`\mathbf{W}^{(1)} \in \mathbb{R}^{h \times d}`$ : the weight parameter of the hidden layer
#### Objective Function)
- $J = L + s$
  - where
    - $L = l(\mathbf{o}, y)$ : the loss function
    - $\displaystyle s = \frac{\lambda}{2} \left(\|\mathbf{W}^{(1)}\|_\textrm{F}^2 + \|\mathbf{W}^{(2)}\|_\textrm{F}^2\right)$ : the regularization term
      - cf.) The Frobenius norm of the matrix is simply the $`\ell_2`$ norm applied after flattening the matrix into a vector.

<br>

#### Computational Graph of Forward Propagation
![](images/001.png)

<br><br>

## 5.3.2 Backpropagation
- Desc.)
  - Backpropagation refers to the method of calculating the gradient of neural network parameters.
  - In short, the method traverses the network in **reverse order**, from the output to the input layer, according to the **chain rule** from calculus.
  - The algorithm stores any **intermediate variables** (partial derivatives) required while calculating the gradient with respect to some parameters.
- Concept) Chain Rule
  - Assume that we have functions
    - $`\mathsf{Y}=f(\mathsf{X})`$
    - $`\mathsf{Z}=g(\mathsf{Y})`$
      - where $`\mathsf{X}, \mathsf{Y}, \mathsf{Z}`$ are tensors of arbitrary shapes.
  - By using the chain rule, we can compute the derivative of $\mathsf{Z}$ w.r.t. $\mathsf{X}$ via
    - $`\displaystyle\frac{\partial \mathsf{Z}}{\partial \mathsf{X}} = \textrm{prod}\left(\frac{\partial \mathsf{Z}}{\partial \mathsf{Y}}, \frac{\partial \mathsf{Y}}{\partial \mathsf{X}}\right)`$
      - where $`\textrm{prod}`$ is an operator that multiplies its arguments after the necessary operations, such as transposition and swapping input positions.
        - e.g.) matrix-matrix multiplication
          - For higher dimensional tensors, we use the appropriate counterpart.
- Optimizing the Objective Function)  
  - Recall our [objective function](#objective-function), $J = L+s$.
  - Then the objective of backpropagation is to calculate the gradients $`\displaystyle\frac{\partial J}{\partial \mathbf{W}^{(1)}}`$ and $`\displaystyle\frac{\partial J}{\partial \mathbf{W}^{(2)}}`$.
    1. $`\displaystyle\frac{\partial J}{\partial \mathbf{W}^{(2)}} = \displaystyle\frac{\partial L}{\partial \mathbf{o}} \mathbf{h}^\top + \lambda \mathbf{W}^{(2)}`$
       - Why?)   
            $`\left\lbrace\begin{array}{lll}
            (1)\;\displaystyle\frac{\partial L}{\partial \mathbf{W}^{(2)}} 
            &= \textrm{prod}\left(\displaystyle\frac{\partial L}{\partial \mathbf{o}}, \frac{\partial \mathbf{o}}{\partial \mathbf{W}^{(2)}}\right) & \because L = l(\mathbf{o}, y) \\
            &= \displaystyle\frac{\partial \mathsf{L}}{\partial \mathbf{o}} \mathbf{h}^\top & \because \mathbf{o}= \mathbf{W}^{(2)} \mathbf{h} \\
           (2)\;\displaystyle\frac{\partial s}{\partial \mathbf{W}^{(2)}} 
            &= \lambda \mathbf{W}^{(2)} & \because s=\frac{\lambda}{2} \left(\|\mathbf{W}^{(1)}\|_\textrm{F}^2 + \|\mathbf{W}^{(2)}\|_\textrm{F}^2\right)\\
           \end{array}\right.`$
    2. $`\displaystyle\frac{\partial J}{\partial \mathbf{W}^{(1)}} = \displaystyle\frac{\partial L}{\partial \mathbf{z}} \mathbf{x}^\top + \lambda \mathbf{W}^{(1)}`$
       - Why?)    
           $`\left\lbrace\begin{array}{lll}
              (1) \; \displaystyle\frac{\partial L}{\partial \mathbf{W}^{(1)}}
              &= \displaystyle\frac{\partial L}{\partial \mathbf{z}} \frac{\partial \mathbf{z}}{\partial \mathbf{W}^{(1)}} = \displaystyle\frac{\partial L}{\partial \mathbf{z}} \mathbf{x}^\top & \because \mathbf{z}= \mathbf{W}^{(1)} \mathbf{x} \\
              &= \displaystyle \left(\frac{\partial L}{\partial \mathbf{h}} \displaystyle\frac{\partial \mathbf{h}}{\partial \mathbf{z}}\right)\mathbf{x}^\top = \left(\frac{\partial L}{\partial \mathbf{h}} \phi'(\mathbf{z})\right)\mathbf{x}^\top & \because \mathbf{h}= \phi (\mathbf{z}) \\
              &= \displaystyle \left(\left(\frac{\partial L}{\partial \mathbf{o}}\frac{\partial \mathbf{o}}{\partial \mathbf{h}} \right) \phi'(\mathbf{z}) \right) \mathbf{x}^\top = \displaystyle \left(\left(\frac{\partial L}{\partial \mathbf{o}} {\mathbf{W}^{(2)}}^\top \right) \phi'(\mathbf{z}) \right) \mathbf{x}^\top & \because \mathbf{o}= \mathbf{W}^{(2)} \mathbf{h} \\
              (2) \; \displaystyle\frac{\partial s}{\partial \mathbf{W}^{(1)}} &= \lambda \mathbf{W}^{(1)} & \because s=\frac{\lambda}{2} \left(\|\mathbf{W}^{(1)}\|_\textrm{F}^2 + \|\mathbf{W}^{(2)}\|_\textrm{F}^2\right)
             \end{array}\right.`$

<br><br>

## 5.3.3 Training Neural Networks
- Desc.)
  - Forward and backward propagation depend on each other when training a neural network.
    - For **forward propagation**, we traverse the computational graph in the direction of dependencies and compute all the variables on its path. 
    - These are then used for **backpropagation** where the compute order on the graph is reversed.
  - Procedure)
    - Initialize the model parameters : $\mathbf{W}^{(1)}$, $\mathbf{W}^{(2)}$
    - Alternate **forward propagation** with **backpropagation**
      - i.e.) Update model parameters using gradients given by **backpropagation**
        - cf.) **Backpropagation** reuses the stored intermediate values from forward propagation to avoid duplicate calculations.
  - Consequence)
    - We need to retain the intermediate values until backpropagation is complete.
    - Training requires significantly more memory than plain prediction.
      - Thus, training deeper networks using larger batch sizes more easily leads to out-of-memory errors.


<br>

* [Back to Dive into Deep Learning](../../main.md)