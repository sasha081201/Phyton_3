
def my_decorator(random_func):
    def the_wrapper_function(list):
        N = random_func(list)
        if N > 0:
            return ("Очень много")
        elif N == 0:
            return ("Нет")
        else:
            return 0
        return N
    return the_wrapper_function

@my_decorator
def count_even_number(list):
    even_count = 0
    i = 0
    while(i < len(list)):
        if list[i] % 2 == 0:
            even_count +=1
        i += 1
    return even_count
A = []
A.append(3)
A.append(4)
A.append(9)
print (count_even_number(A))


