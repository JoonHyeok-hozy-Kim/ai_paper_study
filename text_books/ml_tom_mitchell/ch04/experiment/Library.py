from math import exp
from random import randint

def net(w, x):
    if len(w) != len(x):
        raise ValueError('[Error] Dimension mismatch, w and x.')
    result = 0
    for i, v in enumerate(w):
        result += v*x[i]
    return result


def sigmoid(x):
    result = 1+1/exp(x)
    return 1/result

class Data:
    def __init__(self, data_size) -> None:
        self._x = [0 for _ in range(data_size)]
        self._y = 0

    def __str__(self) -> str:
        l = ['D{[']
        for x in self._x:
            l.append(str(x))
            l.append(',')
        l.pop()
        l.append('] ')
        l.append(str(self._y))
        l.append('}')
        return ''.join(l)
    
    def random_init(self, x_range=None, y_options=None):
        if x_range:
            for i, r in enumerate(x_range):
                self._x[i] = randint(r[0], r[1])
        
        if y_options:
            j = randint(0, len(y_options)-1)
            self._y = y_options[j]

'''
def data_creator(dimension: int, upper_bound: int, lower_bound: int, size: int) -> list:
    result = []
    for _ in range(size):
        temp = [randint(lower_bound, upper_bound) for _ in range(dimension)]
        result.append(temp)
    return result
'''

class Unit:
    def __init__(self, data_size, init=0.001) -> None:
        self._weights = [init for _ in range(data_size)]
    
    def __str__(self) -> str:
        l = ['U{']
        for w in self._weights:
            l.append(str(w))
            l.append(',')
        l.pop()
        l.append('}')
        return ''.join(l)
    
    def output(self, x):
        temp = net(self._weights, x)
        return 1 if sigmoid(temp) >= 0.5 else -1
    
    def get_weight(self):
        return self._weight
    
    def set_weight(self, new_weight):
        self._weight = new_weight


class Network:
    def __init__(self, data_size, hidden_layer_num, learning_rate=0.01) -> None:
        self._learning_rate = learning_rate
        self._input_layer = [Unit(data_size) for _ in range(data_size)]
        self._hidden_layer = [Unit(data_size) for _ in range(hidden_layer_num)]
        self._output_layer = [Unit(data_size) for _ in range(data_size)]
    
    def __str__(self) -> str:
        l = ['-----< Network >-----\n']
        for u in self._input_layer:
            l.append(str(u))
            l.append(' ')      
        l.append('\n')  
        for u in self._hidden_layer:
            l.append(str(u))
            l.append(' ')  
        l.append('\n')  
        for u in self._output_layer:
            l.append(str(u))
            l.append(' ')  
        l.append('\n---------------------')
        return ''.join(l)