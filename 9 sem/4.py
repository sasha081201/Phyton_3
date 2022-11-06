import numpy as np
import math

class Dispersion(Exception):
    pass

class Average(Exception):
    pass

class Amount(Exception):
    pass

def coroutine():
    a = []
    try:
        while True:
            try:
                x = yield
                a.append(x)
            except Average:
                yield sum(a) / len(a)

            except Dispersion:
                m = sum(a) / len(a)
                yield sum((pow((i-m),2) for i in a)) /(len(a)-1)

            except Amount:
                yield len(a)
    finally:
        return


if __name__ == "__main__":
    c = coroutine()
    next(c)
    for i in range(12):
        c.send(i)


    print("Avarage:", c.throw(Average))
    next(c)
    print("Dispersion:", c.throw(Dispersion))
    next(c)
    print("Amount:", c.throw(Amount))
    next(c)
    c.close()