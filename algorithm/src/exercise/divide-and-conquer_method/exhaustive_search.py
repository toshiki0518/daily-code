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

class Exhaustive_search:
    n=0
    S=[]
        
    def __init__(self, test = None) -> None:
        if test is not None:
            # self.S = [1,2,3,4]
            self.n = 3
            return
        self.n = int(input('input number n:'))
        A = []
        for i in range(n):
            num = int(input('input number A:'))
            A.append(num)
        q = int(input('input number q:'))
        m=[]
        for i in range(n):
            num = int(input('input number m:'))
            m.append(num)

    def sample(self):
        self.make_combination()
        
    def make_combination(self):
        n = self.n
        for i in range(n):
            print('n:%d,i:%d' % (n,i))
            self.S.insert(i, 0) # i を選択しない
        self.rec(0)
        
    def rec(self, i):
        if i == self.n:
            print(self.S)
            return
        # print('i:%d,n:%d' % (i,self.n))
        self.rec(i+1)
        self.S[i] = 1 # i を選択
        self.rec(i+1)
        self.S[i] = 0 # i を選択しない
        
        
def main():
    exhaustive_search = Exhaustive_search(True)
    print('start')
    start_time = time.time()
    print(start_time)
    exhaustive_search.sample()
    end_time = time.time()
    print(end_time)
    print(end_time - start_time)
    print('end')
        
    
if __name__ == '__main__':
    main()
