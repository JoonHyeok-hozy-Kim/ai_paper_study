from collections import defaultdict

U = [None for _ in range(n)]
F = [None for _ in range(n)]


def parents(x):
    result = [] # Append the parents of x
    return result    


def forward_computation(x, U, F):   

    for i in range(0, len(x)):
        U[i] = x[i]
    
    for i in range(len(x), len(U)):
        U[i] = F[i](parents(U[i]))

    return U[-1]

def back_propagation(x, U):

    def partial_derivative(x, y):
        result = 0 # Calculate the partial derivative dx/dy
        return result

    grad_table = defaultdict(float)
    grad_table[U[-1]] = 1

    for j in range(len(U)-1, 0, -1):
        temp =[]
        for i in parents(j):
            temp.append(partial_derivative(i,j))
        grad_table[U[j]] = temp
    
    return grad_table[:len(x)]