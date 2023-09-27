from library import get_group_median

s_data = [
    "10–14 895",
    "15–19 55373",
    "20–24 122591",
    "25–29 139615",
    "30–34 127502",
    "35–39 68685",
]

data = []
for s in s_data:
    s1 = s.split(" ")
    s2 = s1[0].split("–")
    data.append([int(s2[0]), int(s2[1]), int(s1[1])])
print(data)

print('Group Median : {}'.format(get_group_median(data)))