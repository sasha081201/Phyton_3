import itertools


def get_combinations_with_r(s, n):
    c= []      
    c = sorted(itertools.combinations_with_replacement(s, n))
    for j in range(len(c)):
        c[j] = ''.join(sorted((c[j])))
    return c
    #raise RuntimeError("Not implemented")
    #c= itertools.combinations_with_replacement
print(list(get_combinations_with_r("cat", 2)))