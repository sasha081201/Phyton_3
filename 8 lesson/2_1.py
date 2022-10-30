import itertools
from timeit import repeat
from itertools import product
def get_cartesian_product(a, b):
    return list(product(a, b))
    #raise RuntimeError("Not implemented")

print(get_cartesian_product([1, 2], [3, 4])) 