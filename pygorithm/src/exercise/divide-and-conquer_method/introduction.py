from calendar import c
from collections import deque
import queue
import sys
import math
import random
import datetime
import time
import sys

sys.setrecursionlimit(20)

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

def findMax(A, l ,r):
    m = (l+r) // 2 # divide
    print('m:%d,l:%d,r:%d' % (m,l,r))
    if l == r-1: # 要素数が1つ
        print('A[l]:%d' % A[l])
        return A[l]
    print('find u')
    u = findMax(A,l,m) 
    print('find v')
    v = findMax(A,m,r)
    print('u:%d,v:%d' % (u,v))
    x = max(u, v)
    return x
        
def main():
    print('start')
    start_time = time.time()
    print(start_time)
    # ans = factorial(10)
    # print('answer:%d' % ans)
    A = [10,20,15,40,18,11,21,28]
    # A = [10,20]
    # print(len(A))
    max_ans = findMax(A, 0, len(A))
    print('max_ans:%d'% max_ans)
    end_time = time.time()
    print(end_time)
    print(end_time - start_time)
    print('end')
        
    
if __name__ == '__main__':
    main()
