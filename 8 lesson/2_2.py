import itertools
from itertools import permutations

from pandas import array
def get_permutations(n, s):
    #raise RuntimeError("Not implemented")
    array = list(sorted(itertools.permutations(n, s)))
    for i in range(len(array)):
        array[i] ="".join(list(array[i]))
    return array

print(list(get_permutations("cat", 2)))