import itertools

def get_combinations(s, n):
    a = []
    for k in range(n):
        b = []
        c = itertools.combinations(s, k + 1)
        for j in c:
            b.append("".join(sorted(j)))
        b.sort()
        a.extend(b)
    return a

print(list(get_combinations("cat", 2)))