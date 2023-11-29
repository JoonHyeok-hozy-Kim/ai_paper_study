from Library import sigmoid, net, data_creator, Unit, Network, Data
from random import randint


'''
# 1. Sigmoid Test : Success
l = []
for i in range(10):
    x = randint(-30,30)
    l.append((x, sigmoid(x)))

l.sort()

for i in l:
    print(i)
'''

'''
# 2. Net Test : Success
for _ in range(5):
    w = [randint(-5, 5) for _ in range(3)]
    x = [randint(-5, 5) for _ in range(3)]
    print('{}*{} = {}'.format(w, x, net(w, x)))
'''

'''
# 3. Data Creator Test : Success
training_set = data_creator(5, 100, -100, 3)
print(training_set)
observation_set = data_creator(3, 10, -10, 5)
print(observation_set)
'''

'''
# 4. Unit Test
## 4-1. Initialization Test : Success
u1 = Unit(5)
# print(u1)

## 4-2. output test : Success
dt = data_creator(5, 10, -10, 30)
# print(dt)

for d in dt:
    y = u1.output(d)
    print(u1, d, y)
'''

'''
# 5. Network Test
## 5-1. Init Test : Success
n1 = Network(3, 8, 3, 8)
print(n1)
'''

'''
# 6. Data Test : Success
d1 = Data(3)
print(d1)
d1.random_init(None, [0,1,2,3])
print(d1)
for _ in range(10):
    d1.random_init([[-100,-50], [-50,50], [50, 100]], [0,1,2,3])
    print(d1)
'''