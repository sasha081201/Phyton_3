import time 
from time import time
from time import sleep
from threading import Thread
A = [1, 2, 6, 8]
start = time.time()
def sum_l(i, array):
    global s
    if i == 0:
        s = 0
    s += sum(array)
count = int(input())
threads = []
D = len(A)//count +1
for i in range(count):
    array = A[i*D:(i+1)*D]
    t = Thread(target = sum_l, args=(i, array))
    threads.append(t)
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(s)
# код, время работы которого надо замерить
print(time.time() - start)