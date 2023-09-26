* [Back to Linear Algebra Main](../../main.md)

# 1.3 SYSTEMS OF LINEAR EQUATIONS

#### Def) Linear Equations
* $a_1x_1+a_2x_2+...+a_nx_n = b$
  * where $x_1, x_2, ..., x_n$ are variables
  * and $a_1, a_2, ..., a_n$, and $b$ are real numbers.
    * $a_1, a_2, ..., a_n$ : coefficients
    * $b$ : constant term

#### Def) System of Linear Equations
![](images/0301001.png)
![](images/0301002.png)

<br><br>

### 1.3.1 Systems of 2 Linear Equations in 2 variables
![](images/0301003.png)

#### Three possible situations
|Parallel (No sol.)|Intersect once (One sol.)|Coinside (Inf. sols.)|
|:-:|:-:|:-:|
|![](images/0301004.png)|![](images/0301005.png)|![](images/0301006.png)|
* Terminology)
  * Consistent
    * A system of linear equations have **one or more solutions**.
  * Inconsistent
    * A system of linear equations have **no solution**.

<br><br>

### 1.3.2 Elementary Row Operations
#### Def.) Equivalence
* Two systems of linear equations that have exactly the same solutions are
called equivalent.

<br>

#### Def.) Coefficient Matrix & Augmented Matrix
For a linear system $\left\{ \begin{array}{ccc} a_{11}x_1+a_{12}x_2+ & \dots & +a_{1n}x_n=b_1 \\ a_{21}x_1+a_{22}x_2+ & \dots & +a_{2n}x_n=b_2 \\ \vdots & \ddots & \vdots \\ a_{m1}x_1+a_{m2}x_2+ & \dots&+a_{mn}x_n=b_m\end{array}\right.$
* **Coefficient Matrix** is $\left[ \begin{array}{cccc} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{mn} \end{array}\right]$
* **Augmented Matrix** is $\left[ \begin{array}{ccccc} a_{11} & a_{12} & \dots & a_{1n} & b_1 \\ a_{21} & a_{22} & \dots & a_{2n} & b_2 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{mn} & b_m \end{array}\right]$


### [Exercises 1.3](./exercises.md)


* [Back to Linear Algebra Main](../../main.md)