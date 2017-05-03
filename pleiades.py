""" Program to find distance to pleiades cluster using the bootstrap method"""

import random
import numpy as np
import matplotlib.pyplot as plt

def dist_calc():
    '''Function that takes the distance modulus and its respective error for
    each of the 18 stars used to determine the distance to the pleiades'''
    mod = [5.77676, 5.61928, 5.5692, 5.5195, 5.67944, 5.54604, 5.582, 5.5748,
           4.97352, 5.8086, 5.3978, 5.22568, 5.73708, 5.83736, 5.02264, 5.3772,
           5.77752, 5.856] # distance modulus of each star
    distance = [] #list for the calculated distance for each average magnitude
    for i in range(10000):
        sum_m = []
        for n in range(18): # generates a sample of 18 stars
            star = random.randint(0, 17) # randomly choosing a star
            sum_m.append(mod[star])
        m_mod = np.mean(sum_m)
        dist = (10**(m_mod/5))*10 # calculated distance
        distance.append(dist)
    dist_f = np.mean(distance) # mean distance determined from the distribution
    error_f = np.std(distance, ddof=1) # error from distribution's standard deviation
    plt.hist(distance, bins=25)
    plt.xlabel('Distance (kpc)')
    plt.ylabel('No. of trials')
    plt.savefig('pleiades.pdf')
    return dist_f, error_f
