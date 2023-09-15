from library import *

l = [105, 80, 115, 95, 100, 85, 90, 70, 135, 105, 45, 115, 40, 115, 95]

l.sort()
q1, q2, q3 = get_quartiles(l)
print("(a) upper quartile : {}, median : {} lower quartile : {},".format(q1, q2, q3))
iqr = q2-q1
print("IQR : {}".format(iqr))
print("Outliers : {}".format(get_outliers(l)))



