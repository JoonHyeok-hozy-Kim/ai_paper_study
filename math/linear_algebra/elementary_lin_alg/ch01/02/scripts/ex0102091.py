from library import *

A = [
    [2.1, 1.3, -0.1, 6.0,],
    [1.3, -9.9, 4.5, 6.2,],
    [4.4, -2.2, 5.7, 2.0,],
    [0.2, 9.8, 1.1, -8.5,],
]

B = [
    [4.4, 1.1, 3.0, 9.9,],
    [-1.2, 4.8, 2.4, 6.0,],
    [1.3, 2.4, -5.8, 2.8,],
    [6.0, -2.1, -5.3, 8.2,],
]

u = [1, -1, 2, 4]
v = [7, -1, 2, 5]

print('(a) Au = {}'.format(matrix_vector_product(A, u)))
print('(b) B(u+v) = {}'.format(matrix_vector_product(B, vector_sum(u, v))))
print('(c) (A+B)v = {}'.format(matrix_vector_product(matrix_sum(A, B), v)))
print('(d) A(Bv) = {}'.format(matrix_vector_product(A, matrix_vector_product(B, v))))

