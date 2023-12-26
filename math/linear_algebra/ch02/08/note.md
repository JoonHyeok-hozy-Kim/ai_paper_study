* [Back to Linear Algebra Main](../../main.md)

# 2.8 Composition and Invertibility of Linear Transformation

## 2.8.1 Onto and One-To-One
#### Concept) The Range of a Linear Transformation
The range of a linear transformation equals the span of the columns of its standard matrix.
- e.g.)
  - Consider a linear transformation $T:\mathbb{R}^3\rightarrow\mathbb{R}^2$ such that $`T\left(\left[\begin{array}{c}x_1\\x_2\\x_3\end{array}\right]\right)=\left[\begin{array}{c}3x_1-4x_2\\2x_1+x_3\end{array}\right]`$.
  - Then the standard matrix of $T$ is $`A=\left[\begin{array}{ccc}T(e_1)&T(e_2)&T(e_3)\end{array}\right]=\left[\begin{array}{ccc}3&-4&0\\2&0&1\end{array}\right]`$.
  - Now $w$ is in the range of $T$ iff. $w=T(v), \exists v \in \mathbb{R}^3$.
  - Putting $v=v_1e_1+v_2e_2+v_3e_3$, 
    - $w=T(v)=T(v_1e_1+v_2e_2+v_3e_3)=v_1T(e_1)+v_2T(e_2)+v_3T(e_3)$.
  - Thus, $w$ is the span of the columns of $A$, which is the standard matrix of $T$.


<br><br>

#### Def.) Onto Function
A function $f : \mathbb{R}^n \rightarrow \mathbb{R}^m$ is said to be **onto** if its range is all of $\mathbb{R}^m$, that is, if every vector in $\mathbb{R}^m$ is an image.

<br>

#### Theorem 2.10)
![](images/001.png)

<br>

#### Def.) One-To-One Function
A function $f : \mathbb{R}^n \rightarrow \mathbb{R}^m$ is said to be **one-to-one** if every pair of distinct vectors in $\mathbb{R}^n$ has distinct images. That is, if $u, v \in \mathbb{R}^n$ and $u \ne v$, then
$f(u)$ and $f(v)$ are distinct vectors in $\mathbb{R}^m$.
![](images/002.png)

<br>

#### Def.) Null Space
Let $T:\mathbb{R}^n\rightarrow\mathbb{R}^m$ be linear.   
The **null space** of $T$ is a set of all $v \in \mathbb{R}^n$ such that $T(v)=0$.

<br>

#### Prop.) One-To-One and Null Space
A linear transformation is one-to-one if and only if its null space contains only $0$.
- why?)
  1. Suppose $T$ is one-to-one.
     - Considering that $T(0)=0$, $T(w) \ne T(0) = 0, w \ne 0$.
     - Thus, $0$ is the only element in its null space.
  2. Suppose $T$'s null space contains only $0$.
     - Then if $w \ne 0$, $T(w) \ne 0 = T(0)$.

<br>

#### Theorem 2.11)
![](images/003.png)



<br><br>

## 2.8.2 Composition of Linear Transformations



<br>

### [Exercises 2.8](./exercises.md)





* [Back to Linear Algebra Main](../../main.md)