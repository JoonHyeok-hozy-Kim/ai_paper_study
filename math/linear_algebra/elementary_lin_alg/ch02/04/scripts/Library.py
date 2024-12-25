class Matrix:
    def __init__(self, data=None):
        self._data = data

    def __str__(self):
        result = []
        for r in self._data:
            result.append(str(r))
            result.append('\n')
        return ''.join(result)


    def get_reduced_row_echelon(self):
        curr_col = 0
        row_cnt = 0
        curr_row = None
        while curr_col < len(self._data[0]):
            curr_row = 0 if curr_row is None else curr_row + 1
            if curr_row == len(self._data):
                return
            
            while self._data[curr_row][curr_col] == 0:
                curr_row += 1
                if curr_row == len(self._data):
                    curr_col += 1
                    continue
            
            print('curr_row : {}, curr_col : {}'.format(curr_row, curr_col))
            self._data[row_cnt], self._data[curr_row] = self._data[curr_row], self._data[row_cnt]
            for i, c in enumerate(self._data[row_cnt]):
                self._data[row_cnt][i] /= self._data[row_cnt][curr_col]
            print(self)

            for r in range(len(self._data)):
                if r == row_cnt:
                    continue
                if self._data[r][curr_col] != 0:
                    x = self._data[r][curr_col]
                    for i, c in enumerate(self._data[r]):
                        self._data[r][i] -= self._data[row_cnt][i] * x
                        if self._data[r][i] == -0.0:
                            self._data[r][i] *= -1
            
            print(self)
            row_cnt += 1
            curr_col += 1


if __name__ == '__main__':
    m = Matrix([[1,2,3,1,0,0], [2,5,6,0,1,0], [3,4,8,0,0,1]])
    print(m)

    m.get_reduced_row_echelon()