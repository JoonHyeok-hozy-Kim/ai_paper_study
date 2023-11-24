
def graph(x, a, b):
    result = (x-a)
    result **= 2
    result += b
    return result

class Graph:
    def __init__(self, length, peak) -> None:
        self._a = length/2
        self._b = self._a**2
        self._t = 0
        self._val = 0
    
    def calculate_val(self):
        val = self._t - self._a
        val **= 2
        val *= -1
        self._val = val + self._b
    
    def get_val(self):
        return self._val
    
    def pass_time(self):
        self._t += 1
        self.calculate_val()

class Strategy:
    def __init__(self, initial, ratio) -> None:
        self._balance = initial
        self._ratio = ratio
        self._asset_amt = 0
    
    def invest(self, price):
        self._balance = self._balance * (1-self._ratio)
        if price > 0:
            self._asset_amt += self._balance * self._ratio / price
    
    def curr_asset(self, price):
        balance = self._balance + self._asset_amt * price
        return balance

if __name__ == '__main__':
    g = Graph(20, 400)
    s1 = Strategy(1000, 0.1)
    s2 = Strategy(1000, 0.2)
    s3 = Strategy(1000, 0.001)
    while g.get_val() >= 0:
        print('Curr Price : {}'.format(g.get_val()))
        curr_price = g.get_val()
        s1.invest(curr_price)
        s2.invest(curr_price)
        s3.invest(curr_price)
        print('s1 : {}, s2 : {}, s3 : {}'.format(s1.curr_asset(curr_price), s2.curr_asset(curr_price), s3.curr_asset(curr_price)))
        g.pass_time()