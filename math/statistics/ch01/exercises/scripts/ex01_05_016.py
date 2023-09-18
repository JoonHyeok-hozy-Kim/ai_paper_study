from library import *

weight = "155–164 165–174 175–184 185–194 195–204"
frequency = "8 11 18 9 4"

data = []
for pt in weight.split(" "):
    temp = pt.split("–")
    data.append([int(temp[0]), int(temp[1]), None])

for i, f in enumerate(frequency.split(" ")):
    data[i][2] = int(f)

print(data)

mean, variance = grouped_data_stats(data)
print('(a) Mean : {}, Variance : {}, Std.Dev : {}'.format(mean, variance, variance**.5))
print('(b) Median : {}'.format(get_group_median(data)))