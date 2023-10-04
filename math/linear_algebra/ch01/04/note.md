* [Back to Linear Algebra Main](../../main.md)

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



### [Exercises 1.4](./exercises.md)


* [Back to Linear Algebra Main](../../main.md)