from library import *

l = [1188, 1050, 2882, 2802, 780, 1171, 685, 537, 519, 2523, 316, 1117, 1578, 261]

mean = get_mean(l) 
variance = get_variance(l, mean)
print("(a) mean : {}, variance : {}".format(mean, variance))

l.sort()
q1, q2, q3 = get_quartiles(l)
print("(b) upper quartile : {}, median : {} lower quartile : {},".format(q1, q2, q3))
iqr = q2-q1
print("IQR : {}".format(iqr))
print("Outliers : {}".format(get_outliers(l)))



