ystr = "-1 0 2 5 6"
Fstr = "0.1 0.15 0.4 0.8 1"

y = [int(v) for v in ystr.split()]
print(y)
f = [float(v) for v in Fstr.split()]
for i in range(len(f)-1):
    f[len(f)-1-i] -= f[len(f)-2-i]
print(f)

ey = 0
ey2 = 0
ey3 = 0
vary = 0

for i, v in enumerate(y):
    vv = v * f[i]
    ey += vv
    vv *= v
    ey2 += vv
    vv *= v
    ey3 += vv


for i, v in enumerate(y):
    vary += ((v-ey)**2) * f[i]

print('EY = {}'.format(ey))
print('EY^2 = {}'.format(ey2))
print('EY^3 = {}'.format(ey3))
print('VAR(Y) = {}'.format(vary))