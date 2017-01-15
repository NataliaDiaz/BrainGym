import itertools
def select_best_possible_score(possible_values, n_elements):
    """
    Returns all possible combinations, cartesian product, of subsets of values
    in possible_values, where repeat= n_elements is the length of each combination tuple.
    It does not produce same item repetitions
    E.g.: list(itertools.product([1,2], repeat=3))
    """
    possibilities = set(list(itertools.product(possible_values, repeat=n_elements)))
    for combination_tuple in possibilities:
        print "Combination possible: ", combination_tuple
    return possibilities

select_best_possible_score([1,11], 2)
select_best_possible_score([1,11,111], 3)

import random

def sampling_without_replacement(list_of_values, n):
  """
  Samples n samples without replacement
  """
  #random.sample(xrange(len(list_of_values)), n)
  samples = random.sample(list_of_values, n) # n =  samples to take
  print "Sampled elements: ", samples
  # remove if this method is called more than once in our program!
  for s in samples:
      list_of_values.remove(s)
  return samples

sampling_without_replacement([4,5,2,40], 2)
