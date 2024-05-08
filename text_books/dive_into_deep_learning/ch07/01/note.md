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
      1. [Translation Invariance](#7121-translation-invariance)
         - In the earliest layers, our network should respond similarly to the same patch, regardless of where it appears in the image. 
      2. [Locality](#7122-locality)
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
        - For any location $`(i,j)`$, the value of $`\left[\mathbf{H}\right]_{i,j}`$ is computed by summing over pixels in $`x\in\mathbf{X}`$ centered around $`(i,j)`$ and weighted by $`\left[\mathsf{V}\right]_{i,j,a,b}`$.
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
      - $`u\in \mathbb{R}$ : a constant assumed to be the value of $\mathbf{U}`$.
      - $`\left[\mathbf{V}\right]_{a,b} = \left[\mathsf{V}\right]_{i,j,a,b}`$
- Why doing this?)
  - Recall that even [a single layer model for a one-mega-pixel image](#712-constraining-the-mlp) have huge size.
  - By emancipating $\mathsf{V}$ and $\mathbf{U}$ from $(i,j)$, we can drastically reduce the number of parameters.
    - How?)
      - The model with $`\left[\mathsf{V}\right]_{i,j,a,b}`$ hidden layer required $10^{12}$ parameters.
        - why?)
          - $`i,j,a,b \in (0, 1000)`$
          - Thus, $`(1000)^4 = 10^{12}`$
      - The model with $`\left[\mathbf{V}\right]_{a,b}`$ hidden layer required $4\times 10^{6}$ parameters.
        - where $a,b \in (-1000,1000)$
          - i.e.) $`2000 \times 2000 = 4\times 10^6`$

<br>

### 7.1.2.2 Locality
- Desc.)
  - Refer to [the Description above](#711-invariance).
  - We will investigate the local range of the location $(i,j)$ to get relevant information to assess $\left[\mathbf{H}\right]_{i,j}$.
- How?)
  - Set $`\left[\mathbf{V}\right]_{a,b} = \begin{cases}
    \left[\mathbf{V}\right]_{a,b} & |a| \le \Delta, |b| \le \Delta \\
    0 & |a| \gt \Delta, |b| \gt \Delta
  \end{cases}`$
  - Then $`\displaystyle\left[\mathbf{H}\right]_{a,b} = u + \sum_{a=-\Delta}^\Delta \sum_{b=-\Delta}^\Delta \left[\mathbf{V}\right]_{a,b} \left[\mathbf{X}\right]_{i+a,j+b}`$
- Why doing this?)
  - We can reduce the number of parameters even more!
    - e.g.) One-Mega-Pixel Input Case
      - Recall that we reduced $10^{12}$ to $4\times 10^{6}$ with the [translation invariance](#7121-translation-invariance).
      - By focusing on the locality we can reduce it to $4 \times \Delta^2$.
        - Why?)
          - Recall that One-Mega-Pixel was $1000 \times 1000 = 10^6$.
          - By narrowing the range of $a$ and $b$ from $1000$ to $\Delta$ respectively, we get the new number of $\Delta^2$.
            - i.e.) $`\displaystyle \sum_a\sum_b \rightarrow \sum_{a=-\Delta}^\Delta \sum_{b=-\Delta}^\Delta`$
      - Typically, $\Delta \lt 10$.
  - We call this the [convolutional layer](#concept-convolutional-layer).

<br>

#### Concept) Convolutional Layer
- Desc.)
  - A layer that the number of parameters are reduced with [translation invariance](#7121-translation-invariance) and [locality](#7122-locality).
    - $`\displaystyle\left[\mathbf{H}\right]_{a,b} = u + \sum_{a=-\Delta}^\Delta \sum_{b=-\Delta}^\Delta \left[\mathbf{V}\right]_{a,b} \left[\mathbf{X}\right]_{i+a,j+b}`$
  - Convolutional neural networks (CNNs) are a special family of neural networks that contain convolutional layers.
  - In the deep learning research community, $\mathbf{V}$ is referred to as a **convolution kernel**, a **filter**, or simply the layer’s **weights** that are learnable parameters.
- Prop.)
  - Pros)
    - Drastically reduces the size of a model
    - It does NOT alter the dimensionality of either the inputs or the hidden representations.
  - Cons)
    - When determining the value of each hidden activation...
      1. The features are [translation invariant](#7121-translation-invariance).
      2. The layer can only incorporate [local](#7122-locality) information.
  - All learning depends on imposing **inductive bias**.
    - When that bias agrees with reality, we get sample-efficient models that generalize well to unseen data.
    - If those biases do not agree with reality, our models might struggle even to fit our training data.



<br>

* [Back to Dive into Deep Learning](../../main.md)