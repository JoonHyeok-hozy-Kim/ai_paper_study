from random import random

N = 1000000
cnt = 0
for _ in range(N):
    x = random()
    y = random()
    if x**2 + y**2 <= 1:
        cnt += 1

'''
Square : 2X2 = 4
Circle : 1X1Xpi = pi

'''
print(cnt/N*4)