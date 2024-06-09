* [Back to Deep Learning MIT](../../main.md)

# 5.8 Unsupervised Learning Algorithms

### Concept) Unsupervised Learning Algorithm
- Desc.)
  - Informally, unsupervised learning refers to most attempts to extract information from a distribution that do not require human labor to annotate examples.
  - Learning Task)
    - Find the “best” representation of the data.
      - i.e.) A representation that 
        1. preserves as much information about $`x`$ as possible 
        2. obeying some penalty or constraint aimed at keeping the representation **simpler** or more **accessible** than $`x`$ itself
    - What is simplicity?
      1. Low Dimensional Representation
         - Compressing as much information about $`x`$ as possible in a smaller representation
      2. Sparse Representation
         - Embedding the dataset into a representation whose entries are mostly zeroes for most inputs
         - This results in an overall structure of the representation that tends to distribute data along the axes of the **representation space**
      3. Independent Representation
         - Disentangling the sources of variation underlying the data distribution such that the dimensions of the representation are **statistically independent**

<br><br>

## 5.8.1 Principal Component Analysis (PCA)
- Desc.)
  - PCA provides a means of compressing data.
  - It is an **unsupervised** learning algorithm that learns a **representation** of data.
    - How?)
      - Learn a representation that has **lower dimensionality** than the original input.
      - Learn a representation whose elements have **no linear correlation** with each other
        - i.e.) 
          - Statistically Independent
          - Removing the nonlinear relationships between variables.
- Model)
  - Settings and Assumptions)
    - $`x`$ : the input
      - $`\mathbb{E}[x] = 0`$
    - $`X`$ : the $`m\times n`$ design matrix
    - $`\displaystyle\textrm{Var}[x] = \frac{1}{m-1}X^\top X`$ : the unbiased sample covariance matrix associated with $`X`$
  - The Representation) 
    - $`z = x^\top W`$
      - where $`W`$ is an orthogonal matrix which columns are the **right singular vectors** of $`X`$
        - The **right singular vectors** of $`X`$ are the eigenvectors of $`XX^\top`$
  - Derivation)
    - Recall that the [target of PCA](../../ch02/12/note.md#objective) was to...
      1. Find a **encoding function** that best reduces the dimension and can be decoded with the linear transformation.
         - Encoding Function : $`c = f(x)`$
      2. Find a **decoding function** which is a linear transformation function that maximizes the variance.
         - Decoding Function : $`x = Dc`$ where $`D`$ is a matrix.
    - We figured out that 
      - The [optimal encoding](../../ch02/12/note.md#derivation-1-what-is-the-optimal-encoding-result-c) was $`c = D^\top x`$.
      - The [optimal decoding](../../ch02/12/note.md#derivation-2-what-is-the-optimal-linear-transformation-d) $`D^\ast`$ was given by the eigenvector of $`X^\top X`$ corresponding to the largest eigenvalue.
    - Thus, we want to get $`X^\top X`$.
    - Using the [Singular Value Decomposition (SVD)](../../ch02/08/note.md#concept-singular-value-decomposition-svd), any matrix $`X`$ can be denoted as 
      - $`X = U\Sigma W^\top`$
        - where
          - $`U`$ : An orthogonal matrix which columns are the **left singular vectors** of $`X`$
            - The **left singular vectors** of $`X`$ are the eigenvectors of $`X^\top X`$
          - $`\Sigma`$ : A diagonal matrix which diagonal values are the **singular values** of $`X`$
            - The non-zero **singular values** of $`X`$ are the square roots of the eigenvalues of $`XX^\top`$ and $`X^\top X`$
          - $`W`$ is an orthogonal matrix which columns are the **right singular vectors** of $`X`$
            - The **right singular vectors** of $`X`$ are the eigenvectors of $`XX^\top`$
    - Then   
      $`\begin{aligned}
          X^\top X &= \left(U\Sigma W^\top\right)^\top U\Sigma W^\top \\
          &= W\Sigma^\top U^\top U\Sigma W^\top \\
          &= W\Sigma^2 W^\top & \because U \textrm{ is orthogonal and } \Sigma \textrm{ is diagonal}
      \end{aligned}`$
    - Therefore, we can use the eigenvectors of $`W\Sigma^2 W^\top`$ as our **principal components**.
  - Meaning)
    - PCA projects the data $`x`$ to $`z`$, via the linear transformation $`W`$.
- Prop.)
  - $`\textrm{Var}[z]`$ is diagonal.
    - pf.)
      - By definition, $`\displaystyle\textrm{Var}[x] = \frac{1}{m-1}X^\top X`$.
      - Then $`\displaystyle\textrm{Var}[x] = \frac{1}{m-1} W\Sigma^2 W^\top \;(\because X^\top X = W\Sigma^2 W^\top)`$.
      - Hence,   
        $`\begin{aligned}
            \textrm{Var}[x] &= \frac{1}{m-1} Z^\top Z \\
            &= \frac{1}{m-1} {(XW)}^\top XW \\
            &= \frac{1}{m-1} W^\top X^\top XW \\
            &= \frac{1}{m-1} W^\top W\Sigma^2 W^\top W & \because X^\top X = W\Sigma^2 W^\top \\
            &= \frac{1}{m-1} \Sigma^2 & \because W \textrm{ is orthogonal. } \\
        \end{aligned}`$
  - Meaning)
    - The resulting representation of PCA, $`z`$, has a diagonal covariance matrix.
      - Thus, individual elements of $`z`$ are mutually uncorrelated.
        - i.e.) Disentangling the unknown factors of variation underlying the data by rotating the axes (linear transformation!).

<br><br>

## 5.8.2 k-means Clustering
- Desc.)
  - Divide the training set into $`k`$ different clusters of examples that are near each other.
  - Or, it can be interpreted as providing a $`k`$-dimensional one-hot code vector $`h`$ representing an input $`x`$.
    - e.g.)
      - If $`x`$ belongs to cluster $`i`$, then $`h_i = 1`$ and all other entries of the representation $`h`$ is zero.
- Algorithm)
  - Initialize $`k`$ different centroids $`\{\mu^{(1)}, \cdots, \mu^{(k)}\}`$ to different values.
  - Alternate between two different steps until convergence.
    - Step 1)
      - Assign each training example to cluster $`i`$, where $`i`$ is the index of the nearest centroid $`\mu^{(i)}`$.
    - Step 2)
      - Update each centroid $`\mu^{(i)}`$ to the mean of all training examples $`x^{(j)}`$
- Prop.)
  - There is no single criterion that measures how well a clustering of the data corresponds to the real world.
    - e.g.) red vehicles, red trucks, gray vehicles, and gray trucks
      - Depending on the number of $`k`$
        - **Reds** vs **Grays**
        - **Vehicles** vs **Trucks**
        - **Red Vehicle** vs **Red Trucks** vs **Gray Vehicle** vs **Gray Trucks**
      - The algorithm never knows which clustering corresponds to the properties of the real world.



<br>

* [Back to Deep Learning MIT](../../main.md)