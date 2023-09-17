from library import *

l = [105, 80, 115, 95, 100, 85, 90, 70, 135, 105, 45, 115, 40, 115, 95]

l.sort()
mean = get_mean(l)
variance = get_variance(l, mean)

print('mean : {}, variance : {}'.format(mean, variance))
r1 = 0
for v in l:
    r1 += (v-mean)**2
print('LHS : {}'.format(r1))

r2 = 0
sum = sum(l)
for v in l:
    r2 += v**2
r2 -= (sum**2)/len(l)
print('RHS : {}'.format(r2))