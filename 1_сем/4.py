import math
a = []
for i in range(1, round(math.sqrt(2500))):
    if i % 10 == 1:
        a.append(i*i)
    elif i % 10 == 9:
        a.append(i*i)
print(a)