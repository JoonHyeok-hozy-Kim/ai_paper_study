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
