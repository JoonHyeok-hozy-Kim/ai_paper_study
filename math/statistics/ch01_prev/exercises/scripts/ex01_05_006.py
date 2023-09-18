from library import *

classes = "0–4 5–9 10–14 15–19 20–24".split(" ")
frequencies = "5 14 15 10 6".split(" ")

# print(classes)
# print(frequencies)

data = []
for i, v in enumerate(classes):
    temp = v.split("–")
    data.append([int(temp[0]), int(temp[1]), int(frequencies[i])])

# print(data)
mean, variance = grouped_data_stats(data)
print("mean : {}, variance : {}".format(mean, variance))
