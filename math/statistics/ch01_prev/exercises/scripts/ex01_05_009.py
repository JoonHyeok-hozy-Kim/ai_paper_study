from library import *

data = \
[10.25, 5.31, 11.25, 13.13, 18.00, 32.56, 37.06, 39.00,
43.25, 45.00, 40.06, 28.56, 22.75, 51.50, 47.00, 53.50,
32.00, 25.44, 22.50, 30.00, 24.75, 53.37, 51.38, 26.00,
53.50, 29.87, 32.00, 28.87, 42.19, 37.50, 30.44, 41.37]

print('(a)')
mean = get_mean(data)
variance = get_variance(data, mean)


print('\n(b)')
data.sort()
Q = get_quartiles(data)
outliers = get_outliers(data)
print('mean : {}, variance : {}'.format(mean, variance))
print('Q1 : {}, Q2 : {}, Q3 : {}'.format(Q[0], Q[1], Q[2]))
print('outliers : {}'.format(outliers))