
a = {}
num = input()
value =input()
while num != "end":
    a[num] = value
    num = input()
    value =input()


print({v: k for (k, v) in a.items()})