from copy import deepcopy


def matrix_vector_product(M, V):
    if len(M) != len(V):
        raise ValueError('Matrix Vector size miss')
    
    result = [0] * len(M)
    for i, row in enumerate(M):
        for j, v in enumerate(row):
            result[j] += v * V[i]
    
    return result


def matrix_sum(M1, M2):
    result = deepcopy(M1)
    for i, row in enumerate(M2):
        for j, val in enumerate(row):
            result[i][j] += val
    
    return result


def vector_sum(V1, V2):
    result = deepcopy(V1)
    for i, val in enumerate(V2):
        result[i] += val
    
    return result