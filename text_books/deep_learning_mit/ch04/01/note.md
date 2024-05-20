* [Back to Deep Learning MIT](../../main.md)

# 4.1 Overflow and Underflow
#### Question) Why matters?
- Digital computers are composed of finite bits of bit patterns.
- Thus, there is a substantial difficulty in performing continuous math on them.
- Computers utilize approximation, which incurs the rounding problem : underflow and overflow.

<br>

### Concept) Underflow
- Desc.)
  - Underflow occurs when numbers near zero are rounded to zero.
  - The problem is that many functions behave qualitatively differently when their argument is zero.
    - e.g.)
      - Zero division error : $`\frac{1}{0} \rightarrow \infty`$
      - $`\log 0 \rightarrow -\infty`$

<br>

### Concept) Overflow
- Desc.)
  - Overflow occurs when numbers with large magnitude are approximated as $`\infty \textrm{ or } -\infty`$.


<br>

### Solutions)
#### Softmax Function
- Def.)
  - $`\displaystyle \textrm{softmax}(x)_i = \frac{\exp{(x_i)}}{\sum_{j=1}^n \exp{(x_j)}}$
- Edge Cases)
  - Consider the case that $`x_i = c \in \mathbb{R}, \forall i`$
    - $`c \rightarrow -\infty`$
      - Then $`\exp{(c)}`$ underflows.
      - Thus, the denominator, $`\sum_{j=1}^n \exp{(x_j)}`$ will become $`0`$.
      - Therefore, the final result is undefined. 
    - $`c \rightarrow \infty`$
      - Then $`\exp{(c)}`$ overflows.
      - Thus, the denominator, $`\sum_{j=1}^n \exp{(x_j)}`$ will become $`\infty`$.
      - Therefore, the final result is undefined.
- Solution)
  - Use $`\displaystyle\textrm{softmax}(z) = x - \max_i{x_i}`$ instead.





<br>

* [Back to Deep Learning MIT](../../main.md)