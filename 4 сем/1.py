import sys
import argparse

def Fibanachi(n):
    if n == 1 or n == 2:
        return 1
    else:
        return Fibanachi(n - 1) + Fibanachi(n - 2)

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', default='10')

    return parser

if __name__ == '__main__':
    if len(sys.argv) == 2:
        print("kek")
        sys.exit('Invalid number of arguments')
    parser = createParser()
    args = parser.parse_args(sys.argv[1:])
    print("wrong")
    N = int(sys.argv)
    print(Fibanachi(N))
