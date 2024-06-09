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
      - where $`\textrm{Var}[z]`$ is diagonal.
        - pf.)
          - Using the [Singular Value Decomposition (SVD)](../../ch02/08/note.md#concept-singular-value-decomposition-svd) we may get
            - $`X = U\Sigma W^\top`$
              - where
                - $`U`$ : An orthogonal matrix which columns are the **left singular vectors** of $`X`$
                  - The **left singular vectors** of $`X`$ are the eigenvectors of $`X^\top X`$
                - $`\Sigma`$ : A diagonal matrix which diagonal values are the **singular values** of $`X`$
                  - The non-zero **singular values** of $`X`$ are the square roots of the eigenvalues of $`XX^\top`$ and $`X^\top X`$
                - $`W`$ : A orthogonal matrix which columns are the **right singular vectors** of $`X`$
                  - The **right singular vectors** of $`X`$ are the eigenvectors of $`XX^\top`$








<br>

* [Back to Deep Learning MIT](../../main.md)