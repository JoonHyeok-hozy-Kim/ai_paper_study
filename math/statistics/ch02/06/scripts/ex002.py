xi = [96, 87, 65, 49, 77, 74, 99, 68, 56, 84]
pxi = [3/15, 2/15, 1/15, 1/15, 2/15, 1/15, 1/15, 1/15, 1/15, 2/15]

mean = 0
var = 0

for i, v in enumerate(xi):
    mean += v*pxi[i]

print(mean)

for i, v in enumerate(xi):
    temp = (v-mean)**2
    var += temp * pxi[i]

print(var)