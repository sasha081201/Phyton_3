def mergeSort(array):
    if len(array) > 1:
        l = array[:len(array) // 2]
        r = array[len(array) // 2:]
        mergeSort(l)
        mergeSort(r)
        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                array[k] = l[i]
                i += 1
            else:
                array[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            array[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            array[k] = r[j]
            j += 1
            k += 1
array_1 = []
n = input()

while n != "end":
    array_1.append(int(n))
    n = input()


print(array_1)
mergeSort(array_1)
print(array_1)

