import itertools
def maximize(lists, m):
    return sum(pow(i,2) for i in itertools.starmap(max, lists)) % 1000
    #raise RuntimeError("Not implemented")

lists = [
    [5, 4],
    [7, 8, 9],
    [5, 7, 8, 9, 10]
]
print(maximize(lists, m=1000))