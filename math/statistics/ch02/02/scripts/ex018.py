from copy import deepcopy

scenarios = []
temp = [['', 0, 0]]

while temp:
    popped = temp.pop()
    c1 = deepcopy(popped)
    c1[0] += 'A'
    c1[1] += 1
    c2 = deepcopy(popped)
    c2[0] += 'B'
    c2[2] += 1
    
    if len(c1[0]) == 7:
        scenarios.append(c1)
        scenarios.append(c2)
    else:
        temp.append(c1)
        temp.append(c2)

cnt = 0
for s in scenarios:
    if s[0][0] == 'A' and s[1] > s[2]:
        cnt += 1
    elif s[0][0] == 'B' and s[1] < s[2]:
        cnt += 1

print(cnt/len(scenarios))