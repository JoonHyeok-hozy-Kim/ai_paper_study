def get_mean(L):
    return sum(L)/len(L)

def get_variance(L, mean=None):
    if mean is None:
        mean = get_mean(L)

    temp = 0
    for v in L:
        temp += (v-mean)**2
    return temp/(len(L)-1)

def get_standard_deviation(L, variance=None):
    if variance is None:
        variance = get_variance(L)

    return variance**.5

def get_median(SL):
    med_i = len(SL)//2

    if len(SL) % 2 == 0:
        return (SL[med_i-1] + SL[med_i]) / 2
    
    else:
        return SL[med_i]

def get_quartiles(SL):
    med_i = len(SL)//2
    return [get_median(SL[:med_i]), get_median(SL), get_median(SL[med_i:])]

def get_outliers(SL):
    q1, q2, q3 = get_quartiles(SL)
    iqr = q2-q1
    result = []
    for v in SL:
        if v < q1-1.5*iqr or v > q3+1.5*iqr:
            result.append(v)
    return result

def grouped_data_stats(D):
    mean = 0
    variance = 0
    total_freq = 0

    for d in D:
        mean += ((d[0] + d[1]) / 2) * d[2]
        total_freq += d[2]
    
    mean /= total_freq
    # print(mean)

    for d in D:
        variance += (((d[0] + d[1]) / 2)**2) * d[2] 
        variance -= ((((d[0] + d[1]) / 2) * d[2])**2) / total_freq
    
    variance /= total_freq-1

    return mean, variance


def get_group_median(D):
    m_idx = 0
    n = 0

    for d in D:
        n += d[2]
    
    f_b = 0
    for i, d in enumerate(D):
        if f_b + d[2] >= n//2:
            m_idx = i
            break
        f_b += d[2]
    
    L = D[m_idx][0]
    f_m = D[m_idx][2]
    w = D[m_idx][1] - D[m_idx][0]
    # print('L : {}, w : {}, n : {}, f_b : {}, f_m : {}'.format(L, w, n, f_b, f_m))

    return L + w * (0.5*n - f_b) / f_m