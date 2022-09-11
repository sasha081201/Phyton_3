import math
import statistics as s

def Min(array):
    min_array = array[0]
    for i in range(1, len(array)):
        if min_array > array[i]:
            min_array = array[i]
    return min_array


def Max(array):
    max_array = array[0]
    for i in range(1, len(array)):
        if max_array < array[i]:
            max_array = array[i]
    return max_array


def Average(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i]
    return sum/len(array)


array_1 = []

num = input()

while num != "end":
    array_1.append(int(num))
    num = input()

print(Min(array_1))
print(Max(array_1))
print(Average(array_1))
print(s.stdev(array_1))
