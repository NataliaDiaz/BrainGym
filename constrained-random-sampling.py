

from random import random  # no other imports from random! no np and no time for seeds (not needed!)
# random()        # Random float x, 0.0 <= x < 1.0

def sample_population(pop, sample_size):
    # with replacement
    result = []
    for trial in range(sample_size):
        sample_value = random()
        result.append(pop[int(sample_value * len(pop))])
    return result

def sample_population_without_replacement(pop, sample_size):
    # without replacement
    result = set()
    while len(result) < sample_size:
        sample_value = random()
        result.add(pop[int(sample_value * len(pop))])
    return result

if __name__ == "__main__":
    list1 = list(range(123456))
    print sample_population(list1, 10)
    print len(sample_population(list1, 100))   # should return list of length 100
    print len(sample_population(list1, 1000))  # should return list of length 1000



    # REJECTED: how to do it better? With expected value formula for uniform distribution?
    # see William Chen Quora stats cheatsheet




############
#EXERCISE 2:
# -- Write a simple function that returns a tuple (x, y) where the point
# (x, y) is uniformly distributed within the unit (so x**2 + y**2 <= 1)

import random

def getTuple():
    """
    returns "x" between [0, 1] uniformly
    """
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    while x**2 + y**2 > 1:
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)

    return (x, y)

print getTuple()
print getTuple()
