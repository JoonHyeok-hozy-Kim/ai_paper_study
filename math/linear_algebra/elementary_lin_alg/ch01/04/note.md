* [Back to Linear Algebra Main](../../../main.md)

# 1.4 Gaussian Elimination

#### Defs.) Pivot Position and Pivot Column
Suppose $R$ is the reduced row echelon form of a matrix $A$.
* Pivot Positions of $A$
  * The positions that contain the leading entries of the nonzero rows of $R$
* Pivot Columns
  * A column of $A$ that contains some pivot positions of $A$.
* Example   

![](./images/04_01_01.png)
![](./images/04_01_02.png)   


<br>

#### Tech.) Gaussian Elimination Algorithm
* Goal)
  * Locate the pivot positions so we can compute the reduced row echelon form
* Assumptions)
  * The target matrix is nonzero
* Algorithm
  1. Determine the leftmost nonzero column.
  2. In the pivot column, choose any nonzero entry in a row that is not above the pivot row, and perform the appropriate row interchange to bring this entry into the pivot position.
  3. Add an appropriate multiple of the row containing the pivot position to each lower row in order to change each entry below the pivot position into 0.
  4. Ignore the row containing the pivot position and all rows above it. If there is a nonzero row that is not ignored, repeat steps 1–4 on the submatrix that remains.
  5. If the leading entry of the row is not 1, perform the appropriate scaling operation to make it 1. Then add an appropriate multiple of this row to every preceding row to change each entry above the pivot position into 0.
  6. If step 5 was performed on the first row, stop. Otherwise, repeat step 5 on the preceding row.
* Example   
  * System of Linear Equation   
    ![](./images/04_01_03.png)
  * Augmented Matrix   
    ![](./images/04_01_04.png)
  * Gaussian Elimination   
    ![](./images/04_01_05.png)
    ![](./images/04_01_06.png)
    ![](./images/04_01_07.png)
  * Result   
    ![](./images/04_01_08.png)


<br>

#### Def.) Rank and Nullity of a Matrix
Let $A$ a $m \times n$ matrix.
* Rank of $A$ : $rank(A)$
  * the number of nonzero rows in the reduced row echelon form of $A$
* Nullity of $A$
  * $n - rank(A)$

<br>

#### Props.)
* The rank of a matrix equals the number of pivot columns in the matrix
* the nullity of a matrix equals the number of nonpivot columns in the matrix
* In a matrix in reduced row echelon form with rank $k$, the standard vectors $e_1, e_2, ... , e_k$ must appear.   

![](./images/04_01_09.png)   

* If a $n \times n$ matrix has rank $n$, then its reduced row echelon form is $I_n$.   

![](./images/04_01_10.png)   

<br>

#### Props.)
Let $Ax=b$ a consistent system of linear equations
* $rank(A) =$ (the number of basic variables in a general solution of the system)
* (nullity of A) = (the number of free variables in a general solution of the system)
* A consistent system of linear equations has a **unique solution** if and only if the nullity of its coefficient matrix equals 0.
* A consistent system of linear equations has **infinitely many solutions** if and only if the nullity of its
coefficient matrix is positive.

<br>

#### Theorem 1.5) Test for Consistency
The following conditions are equivalent
1. The matrix equation $Ax=b$ is consistent.
2. The vector $b$ is a linear combination of the columns of A.
3. The reduced row echelon form of the augmented matrix $[A \space b]$ has no row of the form $[0 \space 0 \space \dots d]$, where $d \ne 0$.
* Proof)
  * **1** is equivalent to **2**
     * Let $A$ be a $m \times n$ matrix and $b \in R^m$. 
     * By definition, $`\exists v = \left[ \begin{array}{c} v_1 \\ v_2 \\ \vdots \\ v_n \end{array} \right] \in R^n`$ such that $Av = b$ if and only if $\Sigma_{i=1}^{n}{v_ia_i} = b$.
     * Thus, $Ax=b$ is consistent if and only if $b$ is a linear combination of the columns of $A$.
     * $\therefore$ **1** is equivalent to **2**.
  * **1** is equivalent to **3**
     * Let $[R \space c]$ be the reduced row echelon form of the augmented matrix $[A \space b]$.
     * Suppose not.
     * Then, the system of linear equations corresponding to $Rx=c$ contains the equation $0x_1 + 0x_2 + \dots 0x_n = d$, where $d \ne 0$.
     * Thus, the equation has no solution and $Rx=c$ is inconsistent. $\dots \otimes$



### [Exercises 1.4](./exercises.md)


* [Back to Linear Algebra Main](../../../main.md)