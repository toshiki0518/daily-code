from calendar import c
from collections import deque
import queue
import sys
import math
import random
import datetime
import time
import sys
import string

sys.setrecursionlimit(20)

class Koch_curve:
    def __init__(self) -> None:
        pass
    
    def check(self):
        print('check')

def main():
    koch_curve = Koch_curve()
    print('start')
    start_time = time.time()
    print(start_time)
    koch_curve.check()
    end_time = time.time()
    print(end_time)
    print(end_time - start_time)
    print('end')
    
    
if __name__ == '__main__':
    main()
