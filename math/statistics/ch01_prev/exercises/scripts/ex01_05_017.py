from library import *

f_length = "1–19 20–39 40–59 60–79 80–99"
frequency = "38 31 59 45 7"

data = []
for pt in f_length.split(" "):
    temp = pt.split("–")
    data.append([int(temp[0]), int(temp[1]), None])

for i, f in enumerate(frequency.split(" ")):
    data[i][2] = int(f)

# print(data)

mean, variance = grouped_data_stats(data)
print('(a) Mean : {}, Variance : {}, Std.Dev : {}'.format(mean, variance, variance**.5))
print('(b) Median : {}'.format(get_group_median(data)))