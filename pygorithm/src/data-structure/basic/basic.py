import time

def start():
    start = time.time()
    count = 0
    n = 6
    for i in range(1, n):
        print(i)
        # f(n) = 5
        count += i
        # f(n) = 11
    end = time.time()
    print(end- start)

start()
