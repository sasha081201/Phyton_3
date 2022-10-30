def print_map(function, iterable):
    i =  iter(iterable)
    while True:
        try:
            elem_i = next(i)
            a = function(elem_i)
            print (a)
            #next(i)
        except StopIteration:
            break


def baz(value):
    return value * value

lst = [1, 2, 3, 4, 5]
print(print_map(baz, lst))