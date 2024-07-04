import math

def get_codword_length(pi):
    return math.log(math.pow(pi,-1), 2)

if __name__ == '__main__':
    probabilities = [0.9999, 0.0001]
    for p in probabilities:
        print(get_codword_length(p))