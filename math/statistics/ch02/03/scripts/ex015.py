def calculate_prob(n):
    result = 1
    x = 365
    for i in range(n):
        result *= x-i
        result /= 365
    
    return 1-result


print('n=20; P(A) = {}'.format(calculate_prob(20)))
print('n=30; P(A) = {}'.format(calculate_prob(30)))

def calculate_my_bday_prob(p):
    prob = 1
    x = 365
    n = 1
    while True:
        prob *= x-n
        prob /= 365
        if 1-prob > p:
            return n+1
        n += 1

print('Estimated n = {}'.format(calculate_my_bday_prob(0.5)))