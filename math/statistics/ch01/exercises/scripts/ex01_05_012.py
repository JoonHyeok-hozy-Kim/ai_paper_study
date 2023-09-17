from library import *

sdata = "40 46 40 54 18 45 34 60 39 42"
data = [float(v) for v in sdata.split()]
# print(data)

mean = get_mean(data)
std_dev = get_standard_deviation(data)
data.sort()
Q = get_quartiles(data)
print('(a)')
print('mean : {}, std_dev : {}'.format(mean, std_dev))
print('Q1 : {}, Q2 : {}, Q3 : {}'.format(Q[0], Q[1], Q[2]))

print('\n(b)')
b_result = 0
for v in data:
    b_result += v - mean
print('result : {}'.format(b_result))