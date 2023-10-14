from Library import *

class OneDimData(Data):
    def __init__(self, val):
        self._val = val
    
    def calculate_distance(self, other):
        temp = self._val - other._val
        return temp if temp >= 0 else -temp
    
    def __str__(self) -> str:
        return '({})'.format(self._val)

S = SetOfPoints()
S.append(Point(OneDimData(5)))
S.append(Point(OneDimData(5.1)))
S.append(Point(OneDimData(5.3)))
S.append(Point(OneDimData(4.9)))
S.append(Point(OneDimData(10)))
S.append(Point(OneDimData(10.1)))
S.append(Point(OneDimData(10.4)))
S.append(Point(OneDimData(20)))

print(S)
# print(S.calculate_distance(S.first(), S.get(1)))

DBSCAN(S, 1, 3)
print(S)


S.append(Point(OneDimData(9.8)))

DBSCAN(S, 1, 3)
print(S)