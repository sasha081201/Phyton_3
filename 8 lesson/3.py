import itertools
#from timeit import repeat
#from itertools import product

def map_new(func, iterable):
    for item in iterable:
        yield func(item)

def zip_new(*iterable):
    #count = 0
    it = [iter(i) for i in iterable]
    while True:
        try:
            yield tuple([next(i) for i in it])
        except StopIteration:
            break

def enumerate_new(iterable, start= 0):
    m = start
    for i in iterable:
        yield m, i
        m += 1


A = [1, 2, 3]
B = [5, 7, 9]


print(list(enumerate_new(B)))
print(list(enumerate(B)))

print (list(zip(A,B)))
print(list(zip_new(A,B)))

print(list(map(max, [[2,1],[0,1]])))
print(list(map_new(max, [[2,1],[0,1]])))


    