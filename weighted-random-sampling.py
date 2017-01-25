
# # Given some weighted items, randomly output the item id with the probability calculated by the weights.
# # Example:
# # (item id, weight)
# # items = {(1, 3), (2, 4), (3, 5), (4, 1), (5, 2)}
# # rand() ->
# # return 1 with 3/15 possibility
# # return 2 with 4/15 possibility
# # return 3 with 5/15 possibility
# # return 4 with 1/15 possibility
# # return 5 with 2/15 possibility


import numpy as np

def weighted_sample(list_of_tuples, replace=True):
    """
    This method returns one sample from the first value in the input
    tuples with corresponding probability (default is with replacement)
    """

    weights = [weight for (item, weight) in list_of_tuples]
    items = [item for (item, weight) in list_of_tuples]
    total_sum = float(sum(weights))
    probabilities = [weight/total_sum for (item, weight) in list_of_tuples]   #print probabilities
    item_id = np.random.choice(items, 1, p=probabilities, replace= replace)

    return item_id

print weighted_sample([(1, 3), (2, 4), (3, 5), (4, 1), (5, 2)])
print weighted_sample([(1, 3), (2, 4), (3, 5), (4, 1), (5, 2)])
print weighted_sample([(1, 3), (2, 4), (3, 5), (4, 1), (5, 2)])
print weighted_sample([(1, 3), (2, 4), (3, 5), (4, 1), (5, 2)])
print weighted_sample([(1, 3), (2, 4), (3, 5), (4, 1), (5, 2)])
print weighted_sample([(1, 3), (2, 4), (3, 5), (4, 1), (5, 2)])
print weighted_sample([(1, 3), (2, 4), (3, 5), (4, 1), (5, 2)])
print weighted_sample([(1, 3), (2, 4), (3, 5), (4, 1), (5, 2)])
