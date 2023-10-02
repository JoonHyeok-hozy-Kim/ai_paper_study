class Space:
    def __init__(self):
        self._name = 'S'
        self._subsets = {}
    
    def set_intersection(self, P1, P2, val):
        P1._intersections[P2] = val
        P2._intersections[P1] = val
    
    def add_probability(self, name, val):
        new_prob = Probability(self, name, val)
        for s in self._subsets:
            s_prob = self._subsets[s]
            print('Insert intersection value with {} : '.format(s_prob._name), end="")
            s_intersect_val = float(input())
            self.set_intersection(new_prob, s_prob, s_intersect_val)

        self._subsets[name] = new_prob
        return new_prob
    
    
    def calculate_intersection(self, P1, P2):
        result = None
        if P2 in P1._intersections:
            result = P1._intersections[P2]
        elif P2 in P1._complement._intersections:
            result = P2._value
            result -= P1._complement._intersections[P2]
        elif P1 in P2._complement._intersections:
            result = P1._value
            result -= P2._complement._intersections[P1]
        elif P1._complement in P2._complement._intersections:
            result = 1
            result -= self.calculate_union(P1._complement, P2._complement)
        else:
            raise ValueError('Intersection not defined!')
        return result
    

    def calculate_union(self, P1, P2):
        result = P1._value + P2._value
        return result - self.calculate_intersection(P1, P2)



class Probability:
    def __init__(self, space, name, val, comp=None):
        self._space = space
        self._name = name
        self._value = val
        self._intersections = {}
        if comp is None:
            self._complement = Probability(space, self._name+'^c', 1-val, self)
        else:
            self._complement = comp
    
    def __str__(self):
        return 'P({})'.format(self._name)

    def get_value(self):
        return self._value