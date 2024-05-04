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
      1. Translation Invariance
         - In the earliest layers, our network should respond similarly to the same patch, regardless of where it appears in the image. 
      2. Locality
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

    









<br>

* [Back to Dive into Deep Learning](../../main.md)