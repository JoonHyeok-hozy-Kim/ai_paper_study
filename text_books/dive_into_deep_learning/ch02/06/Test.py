import random

N = 100000
result = 0
for _ in range(N):
    x = random.randint(0, 1)
    result += x
print(result/N)