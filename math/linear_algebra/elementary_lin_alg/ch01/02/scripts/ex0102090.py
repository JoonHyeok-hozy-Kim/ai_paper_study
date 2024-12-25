from library import *

stochastic_mat = [
    [.85, .03],
    [.15, .97],
]

population = [400000, 300000]

for i in range(10):
    population = matrix_vector_product(stochastic_mat, population)
    print('After {} year(s) : {}'.format(i+1, population))
