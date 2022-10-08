
def introduce(n):
    def swap(random_func):
        def wrapper(*args, **kwargs):
            args = args[::-1]
            random_func(*args, **kwargs)
        return wrapper
    return swap

N = input()

@introduce(N)
def div(x, y, show=False):
    res = x / y
    if show:
        print(res)
    return res

div(2, 4, show=True)