from Probability import *

S = Space()
p1 = S.add_probability('A', 0.17)
print(p1, p1.get_value())
print(p1._complement, p1._complement.get_value())

p2 = S.add_probability('B', 0.46)

print(S.calculate_union(p1, p2))
print(S.calculate_intersection(p1, p2))
print(S.calculate_intersection(p1._complement, p2))
print(S.calculate_intersection(p1, p2._complement))
print(S.calculate_intersection(p1._complement, p2._complement))