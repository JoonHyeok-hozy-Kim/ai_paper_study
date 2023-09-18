from library import *

l = [176, 105, 133, 140, 305, 215, 207, 210, 173, 150, 78, 96]

mean = get_mean(l)
variance = get_variance(l, mean)

print("mean : {}, variance : {}".format(mean, variance))