from math import comb

sample_space = [1,1,1,0,0] # good : 1, spoiled : 0
print('(a) sample space : {} (good : 1, spoiled : 0)'.format(sample_space))

print('(b) {}'.format(comb(3,2)/comb(5,2)))

print('(c) {}'.format(1-1/comb(5,2)))