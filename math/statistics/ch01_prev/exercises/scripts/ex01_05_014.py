from library import *

sdata = "85 51 41 90 91 40 39 69 45 47 \
42 12 70 38 97 34 94 77 88 91 \
79 90 43 40 89 85 71 30 25 21"

data = [float(v) for v in sdata.split()]
# print(data)

mean = get_mean(data)
variance = get_variance(data, mean)
std_dev = get_standard_deviation(data, variance)
data.sort()
Q = get_quartiles(data)
print('(a)')
print('mean : {}, variance : {}, std_dev : {}'.format(mean, variance, std_dev))
print('Q1 : {}, Q2 : {}, Q3 : {}'.format(Q[0], Q[1], Q[2]))

print('\n(b)')
frequency_table = {}
total_length = data[-1] - data[0]
delta = total_length / 5
curr_lower = data[0]
i = 0
for j in range(5):
    cnt = 0
    while i < len(data) and data[i] <= curr_lower + delta:
        cnt += 1
        i += 1
    frequency_table[(curr_lower, curr_lower+delta)] = cnt
    curr_lower += delta
print(frequency_table)

print('\n(c)')
group_format = []
for r in frequency_table:
    l, u = r
    cnt = frequency_table[r]
    group_format.append([l, u, cnt])
# print(group_format)
group_stats = grouped_data_stats(group_format)
# print(group_stats)
print('mean : {}, variance : {}, std_dev : {}'.format(group_stats[0], group_stats[1], (group_stats[1]**.5)))