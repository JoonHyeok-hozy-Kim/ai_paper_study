p_coffee = .65
p_tea = .5
p_coffee_and_tea = .25
p_coffee_or_tea = p_coffee+p_tea-p_coffee_and_tea
print('p_coffee_or_tea : {}'.format(p_coffee_or_tea))
print('p_neither : {}'.format(1-p_coffee_or_tea))