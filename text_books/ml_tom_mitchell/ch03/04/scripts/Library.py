from math import log2
from collections import deque

def calculate_entropy(D):
    if len(D) == 0:
        return 0
    
    pcnt = ncnt = 0
    for d in D:
        if d[1]:
            pcnt += 1
        else:
            ncnt += 1
    pp, nn = pcnt/(pcnt+ncnt), ncnt/(pcnt+ncnt)
    lpp = 0 if pp == 0 else log2(pp)
    lnn = 0 if nn == 0 else log2(nn)
    return -pp*lpp - nn*lnn


def calculate_information_gain(A, D, attr):
    # print('calculate_information_gain, attr : {}, D : {}'.format(attr, D))
    entropy = calculate_entropy(D)
    data_partition = {}
    for val in A[attr]:
        data_partition[val] = []
    for d in D:
        d_val = d[0][attr]
        data_partition[d_val].append(d)
    # print('data_partition : {}'.format(data_partition))
    for val in data_partition.keys():
        temp_entropy = calculate_entropy(data_partition[val])
        temp_entropy *= len(data_partition[val])
        temp_entropy /= len(D)
        entropy -= temp_entropy
    
    return entropy


class ID3Node:
    def __init__(self, attribute_set, attributes_avail, data_set_avail) -> None:
        # print('<ID3Node>\nattributes_avail : {}\ndata_set_avail : {}\n\n'.format(attributes_avail, data_set_avail))
        self._attributes_avail = attributes_avail
        self._curr_attribute = None
        self._children = []

        if len(data_set_avail) == 0:
            return
        
        max_ig = [None, 0]
        for attr in self._attributes_avail:
            ig = calculate_information_gain(attribute_set, data_set_avail, attr)
            if ig > max_ig[1]:
                max_ig = [attr, ig]
        # print('max_ig : {}'.format(max_ig))
        if max_ig[0] is None:
            return
        
        self._curr_attribute = max_ig[0]        
        self._attributes_avail.remove(self._curr_attribute)
        part_data = {}
        for d in data_set_avail:
            curr_val = d[0][self._curr_attribute]
            if curr_val not in part_data:
                part_data[curr_val] = []
            part_data[curr_val].append(d)
        
        for val in part_data:
            child = [val, ID3Node(attribute_set, self._attributes_avail, part_data[val])]
            self._children.append(child)

        self._attributes_avail.append(self._curr_attribute)

    def __str__(self) -> str:
        return self._curr_attribute
    
    def print_all(self, depth=0, Q=None):
        if Q is None:
            Q = deque()
        if self._curr_attribute is None:
            return
        Q.append([depth, self._curr_attribute])
        for c in self._children:
            c[1].print_all(depth+1, Q)
        curr_depth = 0
        while Q:
            popped = Q.popleft()
            if curr_depth != popped[0]:
                print()
            print(popped[1], end=" ")