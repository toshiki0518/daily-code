from calendar import c
from collections import deque
import queue
import sys
import math
import random
import datetime
import time

"""
与えられた問題を部分問題に分割する。divide
部分問題を再帰的に解く。solve
得られた部分問題の解を統合して、元の問題を解く。conquer
"""
def factorial(n):
    ans = 0
    if n==1:
        ans = 1
    else:
        ans = n * factorial(n-1)
    print ('n:%d,ans:%d' % (n,ans))
    return ans 
    
def main():
    print('start')
    start_time = time.time()
    print(start_time)
    ans = factorial(10)
    print('answer:%d' % ans)
    end_time = time.time()
    print(end_time)
    print(end_time - start_time)
    print('end')
        
    
if __name__ == '__main__':
    main()
