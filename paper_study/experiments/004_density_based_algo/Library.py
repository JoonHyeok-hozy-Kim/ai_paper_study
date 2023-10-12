class Id:
    def __init__(self, val, type=None):
        self._val = val
        if type:
            self._type = type
        else:
            self._type = 'UNCLASSIFIED'
    
    def get_type(self):
        return self._type
    
    def set_type(self, type):
        self._type = type


class IdSpace:
    def __init__(self):
        self._ids = []
    
    def next_id(self, type=None):
        new_id = Id(len(self._ids), type)
        self._ids.append(new_id)
        return new_id
    
    def get_type(self, id):
        return self._ids[id].get_type()


ID_SPACE = IdSpace()

class Data:
    def __init__(self) -> None:
        pass

    def calculate_distance(self, other):
        return
    
    def __str__(self) -> str:
        pass

class Point:
    def __init__(self, data:object):
        self._cluster_id = ID_SPACE.next_id()
        self._data = data
    
    def __str__(self) -> str:
        return 'P(id:{},data:{})'.format(self._cluster_id._val, self._data)

class SetOfPoints:
    def __init__(self):
        self._points = [] # An iterable list of Points
  
    def size(self) -> int:
        return len(self._points)
  
    def get(self, i: int) -> Point:
        if self.size() > i:
            return self._points[i]
    
    def first(self):
        if self.size() > 0:
            return self._points[0]
  
    def append(self, p: Point) -> None:
        self._points.append(p)
  
    def delete(self, p: Point) -> None:
        self._points.pop(p)
  
    def change_cluster_id(self, p: Point, cl_id: Id) -> None:
        if p not in self._points:
            raise ValueError('point not in this set_of_point.')
        p._cluster_id = cl_id
    
    def calculate_distance(self, p: Point, q: Point) -> float:
        return p._data.calculate_distance(q._data)
  
    def region_query(self, p: Point, eps) -> object:
        '''
        Returns the Eps-Neighborhood of point in SetOfPoints
        Supported by spatial access methods such as R*-trees -> O(n log(n))
        For the quick implementation, used O(n^2) for loop in this algorithm
        '''
        result = SetOfPoints()
        for q in self._points:  # O(n^2) for the quick implementation
            if p == q:
                continue
            if self.calculate_distance(p, q) < eps:
                result.append(q)
        return result


def DBSCAN(S: SetOfPoints, eps: float, min_pts: int) -> None:
    # set_of_points is unclassified.    
    for p in S:
        cl_id = ID_SPACE.next_id('NOISE')   # mark this cluster as a noise
        if p._cluster_id._type == 'UNCLASSIFIED':
            if expand_cluster(S, p, cl_id, eps, min_pts):
                cl_id.set_type('CLUSTER')


def expand_cluster(S: SetOfPoints, p: Point, cl_id: Id, eps, min_pts) -> bool:
    seeds = S.region_query(p, eps)
    if seeds.size() < min_pts:  # Not core point : Either a noise or a border_point
        S.change_cluster_id(p, ID_SPACE.next_id('NOISE'))
        return False

    else: # All points in seeds are density-reachable from point
        # CLUSTER_ID.noise_to_cluster(cl_id)
        S.change_cluster_id(p, cl_id)
        seeds.delete(p)

        while seeds.size():
            p_curr = seeds.first()
            result = S.region_query(p_curr, eps)
            if result.size() >= min_pts:
                for q in result:
                    if q._cluster_id._type in ['UNCLASSIFIED', 'NOISE']:
                        if q._cluster_id._type == 'UNCLASSIFIED':
                            seeds.append(q)
                        S.change_cluster_id(q, cl_id)
            seeds.delete(p_curr)
        return True