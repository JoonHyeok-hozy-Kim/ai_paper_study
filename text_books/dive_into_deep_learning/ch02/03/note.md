* [Back to Dive into Deep Learning](../../main.md)

# 2.3 Linear Algebra
Using tools from linear algebra implemented for tensor.
- Thus, start with importing PyTorch
    ```python
    import torch
    ```

<br>

## 2.3.1 Scalars
- Basic Arithmetic Operations
    ```python
    x = torch.tensor(3.0)
    y = torch.tensor(2.0)
    x+y
    x*y
    x/y
    x**y
    ```

<br>

## 2.3.2 Vectors
- Declaration
    ```python
    x = torch.arange(3)
    x
    ```
    ![](images/001.png)
- Indexing Elements
  ```python
  x[2]
  ```
  ![](images/002.png)
- Size of a vector
  - Python built-in ```len```
    ```python    
    len(x)
    ```
    ![](images/003.png)
  - tensor's ```shape``` attribute.
    ```python    
    x.shape
    ```
    ![](images/004.png)

<br>

## 2.3.3 Matrices
- Declaration
  - Create a tensor and use ```reshape``` method.
    ```python
    A = torch.arange(6).reshape(3,2)
    A
    ```
    ![](images/005.png)
- Transpose
  ```python
  A.T
  ```
  ![](images/006.png)

<br>

## 2.3.4 Tensors
- Def.)
  - Tensors give us a generic way of describing extensions to n-th order arrays.
- Declaration
  - Create a tensor and use ```reshape``` method.
    ```python
    T = torch.arange(24).reshape(2,3,4)
    T
    ```
    ![](images/007.png)

<br>

## 2.3.5 Basic Properties of Tensor Arithmetic
1. Hadamard Product   
   ![](images/008.png)
   ```python
   A = torch.arange(6, dtype=torch.float32).reshape(2, 3)
   B = A.clone()
   A*B
   ```
    ![](images/009.png)

2. Scalar Product
   ```python
   a = 2
   X = torch.arange(24).reshape(2, 3, 4)
   a * X
   ```
   ![](images/010.png)

<br>

## 2.3.6 Reduction
- Sum of tensor elements
  ```python
  x = torch.arange(3, dtype=torch.float32)
  x.sum()
  ```
  ![](images/011.png)
   - Specifying an axis to sum up the elements.
     ```python
     A = torch.arange(6, dtype=torch.float32).reshape(2, 3)
     A
     A.sum(axis=0)  # Sum by columns
     A.sum(axis=1)  # Sum by rows
     A.sum(axis=[0,1]) # Sum all
     ```
     ![](images/012.png)
- Mean of a tensor
  ```python
  A.mean()
  A.sum() / A.numel()
  ```
  ![](images/013.png)
  - Specifying an axis to calculate the mean.
    ```python
    A.mean(axis=0)
    A.mean(axis=1)
    ```
    ![](images/014.png)

<br>

## 2.3.7 Non-Reduction Sum
- When to use?
  - Keep the number of axes unchanged when invoking the function for calculating the sum or mean.
- Summation
  ```python
  A = torch.arange(6, dtype=torch.float32).reshape(2, 3)
  A
  sum_A = A.sum(axis=1, keepdims=True)
  sum_A
  sum_A.shape
  ```
- Cumulative Sum





<br>

* [Back to Dive into Deep Learning](../../main.md)