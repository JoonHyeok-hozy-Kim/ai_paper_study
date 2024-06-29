from sys import maxsize

def early_stopping(n, p, theta):
    '''
    n : the number of steps between evaluations
    p : the patience, i.e., the number of times to observe worsening validation set error before giving up
    theta : initial parameters
    '''
    curr_theta = theta
    i = j = 0
    v = maxsize
    final_theta = curr_theta
    final_i = i
    while j < p:
        curr_theta = train(n)   # Train for n times
        i += n
        v_temp = validation_set_error(curr_theta)   # Get the current validation error
        if v_temp < v:
            j, v, final_theta, final_i = 0, v_temp, curr_theta, i
        else:
            j += 1
    return final_theta, final_i