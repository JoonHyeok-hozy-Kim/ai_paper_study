from library import *

strings = [\
"2.9 0.6 13.5 17.1 2.8 3.8 16.0 2.1 6.4 17.2",
"7.9 0.5 13.7 11.5 2.9 3.6 6.1 8.8 2.2 9.4",
"15.9 8.8 9.8 11.5 12.3 3.7 8.9 13.0 7.9 11.7",
"6.2 6.9 12.8 13.7 2.7 3.5 8.3 15.9 5.1 6.0",]

data = []
for s in strings:
    temp = s.split(" ")
    for v in temp:
        data.append(float(v))

# print(data)

print('(a)')
mean = get_mean(data)
variance = get_variance(data, mean)
print('mean : {}, variance : {}'.format(mean, variance))


print('\n(b)')
data.sort()
Q = get_quartiles(data)
outliers = get_outliers(data)
print('Q1 : {}, Q2 : {}, Q3 : {}'.format(Q[0], Q[1], Q[2]))
print('outliers : {}'.format(outliers))