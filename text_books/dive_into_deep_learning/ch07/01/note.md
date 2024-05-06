* [Back to Dive into Deep Learning](../../main.md)

# 7.1 From Fully Connected Layers to Convolutions

#### Concept) Tabular Data
- Desc.)
  - The data consist of rows corresponding to examples and columns corresponding to features.
  - When learning the data, the patterns we seek could involve interactions among the features.
    - But we do not assume any structure a **priori** concerning how the features interact.
      - For high-dimensional perceptual data, such **structureless networks** can grow unwieldy.
        - e.g.) 1 Mega-pixel image

<br>

## 7.1.1 Invariance
- Desc.)
  - CNNs systematize the idea of spatial invariance, exploiting it to learn useful representations with fewer parameters.
    - Desiderata)
      1. **Translation Invariance**
         - In the earliest layers, our network should respond similarly to the same patch, regardless of where it appears in the image. 
      2. **Locality**
         - The earliest layers of the network should focus on local regions, without regard for the contents of the image in distant regions. 
         - Eventually, these local representations can be aggregated to make predictions at the whole image level.
      3. As we proceed, deeper layers should be able to capture longer-range features of the image, in a way similar to higher level vision in nature.

<br>

## 7.1.2 Constraining the MLP
- Settings)
  - A MLP
    - $`\begin{aligned}
        \displaystyle\left[\mathbf{H}\right]_{i,j} & = \left[\mathbf{U}\right]_{i,j} + \sum_k\sum_l \left[\mathsf{W}\right]_{i,j,k,l} \left[\mathbf{X}\right]_{k,l} \\
         &= \left[\mathbf{U}\right]_{i,j} + \sum_a\sum_b \left[\mathsf{V}\right]_{i,j,a,b} \left[\mathbf{X}\right]_{i+a,j+b}
      \end{aligned}`$
      - where
        - $\mathbf{X}$ : the input of two-dimensional images
          - $\left[\mathbf{X}\right]_{i,j}$ : the pixel at location $(i,j)$ in $\mathbf{X}$
        - $\mathbf{H}$ : the immediate hidden representations of $\mathbf{X}$
          - $\mathbf{X}$ and $\mathbf{H}$ are similarly represented as matrices (two-dimensional tensors).
            - Interpretation)
              - Imagine that the hidden representations also possess spatial structure.
          - $\left[\mathbf{H}\right]_{i,j}$ : the pixel at location $(i,j)$ in $\mathbf{H}$
        - $\mathbf{U}$ : A matrix containing biases
        - $`\mathsf{W, V}`$ : fourth-order weight parameter tensors
          - $`\left[\mathsf{V}_{i,j,a,b}\right] = \left[\mathsf{W}_{i,j,i+a,j+b}\right]`$ 
          - $`\left\lbrace\begin{aligned}
             k=i+a \\ l=j+b 
          \end{aligned}\right.`$
            - The indices $a$ and $b$ run over both positive and negative offsets, covering the entire image.
      - Meaning)
        - For any location $(i,j)$, the value of $\left[\mathbf{H}\right]_{i,j}$ is computed by summing over pixels in $x\in\mathbf{X}$ centered around $(i,j)$ and weighted by $\left[\mathsf{V}\right]_{i,j,a,b}$.
      - Prop.)
        - The size of the model is huge!
          - Why?)
            - Suppose the input data is the one-mega-pixel image $(1000 \times 1000 = 1000000)$.
            - Recall that the hidden layer must have the same size as the input.
            - Even for a single layer model, the hidden representation should have the size of $1000 \times 1000$.
            - Thus, the model requires $10^{12}$ parameters.
              - Far beyond the size we can handle.
          - Sol.)
            - [Translation Invariance](#7121-translation-invariance)


<br><br>

### 7.1.2.1 Translation Invariance
- Desc.)
  - Refer to [the Definition above](#711-invariance).
- Implementation)
  - How can we apply this to our model?)
    - Make our parameters $\mathsf{V}$ and $\mathbf{U}$ independent on $(i,j)$.
  - $`\displaystyle \left[\mathbf{H}\right]_{i,j} = u + \sum_a\sum_b \left[\mathbf{V}\right]_{a,b} \left[\mathbf{X}\right]_{i+a,j+b}`$
    - where
      - $u\in \mathbb{R}$ : a constant assumed to be the value of $\mathbf{U}$.
      - $\left[\mathbf{V}\right]_{a,b} = \left[\mathsf{V}\right]_{i,j,a,b}$
- Why doing this?)
  - Recall that even [a single layer model for a one-mega-pixel image](#712-constraining-the-mlp) have huge size.
  - By emancipating $\mathsf{V}$ and $\mathbf{U}$ from $(i,j)$, we can drastically reduce the number of parameters.
    - How?)
      - The model with $`\left[\mathsf{V}\right]_{i,j,a,b}`$ hidden layer required $10^{12}$ parameters.
      - The model with $`\left[\mathbf{V}\right]_{a,b}`$ hidden layer required $4\times 10^{6}$ parameters.
        - where $a,b \in (-1000,1000)$

<br>

### 7.1.2.2 Locality



<br>

* [Back to Dive into Deep Learning](../../main.md)