import functools
from functools import wraps
from time import time


class decorator:
    def __init__(self, path):
        self.path = path

    def __call__(self, random_func):
        @functools.wraps(random_func)
        def wrapper(*args):
            start_time = time()
            result = random_func(*args)
            end_time = time()
            with open(self.path, 'w') as file:
                file.write("Function call time =" + str(start_time) + '\n')
                file.write("Function shutdown time = " + str(end_time) + '\n')
                file.write("Function operation time =" + str(end_time - start_time) + '\n')
                file.write("Incoming arguments =" + str(args) + '\n')
                file.write("Result =" + (str(result) if result is not None else '-') + '\n')
            return result
        return wrapper


path = input()


@decorator("test_file.txt")
def test_func(a, b=None):
    if a != b:
        c = a + b
        return c
    else:
        return a


if __name__ == "__main__":
    print(test_func(1, 2))