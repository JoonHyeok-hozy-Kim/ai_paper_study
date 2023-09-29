* [Back to the note](./note.md)

![](./images/ex001.png)

![](./images/ex002.png)

![](./images/ex003.png)

![](./images/ex004.png)

![](./images/ex005.png)

![](./images/ex007.png)
```python
if __name__ == '__main__':
    prob_space = []
    for i in range(6):
        for j in range(6):
            prob_space.append((i+1, j+1))
    print('(a) : {}'.format(prob_space))

    N = len(prob_space)
    bcnt = 0
    for x1, x2 in prob_space:
        if x1 + x2 == 7:
            bcnt += 1
    print('(b) {}/{}'.format(bcnt, N))

    print('(c) 1/{}'.format(N))
```

![](./images/ex008.png)
```python
p_coffee = .65
p_tea = .5
p_coffee_and_tea = .25
p_coffee_or_tea = p_coffee+p_tea-p_coffee_and_tea
print('p_coffee_or_tea : {}'.format(p_coffee_or_tea))
print('p_neither : {}'.format(1-p_coffee_or_tea))
```

![](./images/ex009.png)
```python
from math import comb

sample_space = [1,1,1,0,0] # good : 1, spoiled : 0
print('(a) sample space : {} (good : 1, spoiled : 0)'.format(sample_space))

print('(b) {}'.format(comb(3,2)/comb(5,2)))

print('(c) {}'.format(1-1/comb(5,2)))
```

![](./images/ex010.png)
```python
from math import perm

print(1/perm(3,3))
```

![](./images/ex011.png)
sol.) ${p+2q}\over{p+2q+r}$

![](./images/ex012.png)




* [Back to the note](./note.md)