
from functools import wraps
from time import time


def introduce(path):
   
    def decorator1(random_func):
        file = open(path, 'w', encoding='utf8')
        @wraps(random_func)
        def wrapper(*args):
            start_time = time()
            result = random_func(*args)
            end_time = time()
            with open(path, 'w') as file:
                file.write("Function call time =" + str(start_time) + '\n')
                file.write("Function shutdown time = "+str(end_time) + '\n')
                file.write("Function operation time ="+ str(end_time - start_time) + '\n')
                file.write("Incoming arguments ="+ str(args)+ '\n')
                file.write("Result ="+ (str(result) if result is not None else '-') + '\n')
            return result
        
        return wrapper
    
    return decorator1
path = input()

@introduce("file_3.txt")
def test_func(a, b=None, c=None):
    print(sum([a, b, c]))

if __name__ == "__main__":
    test_func(1, 2, 3)