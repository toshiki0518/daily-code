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

class Exhaustive_search:
    n=0
    A=[]

    m=[]
    q=0
        
    S=[]
    result=[]
    def __init__(self, test = None) -> None:
        if test is not None:
            # self.S = [1,2,3,4]
            self.n = 3
            return

    def init1(self):
        self.n = int(input('input number n:'))
        
        for i in range(self.n):
            num = int(input('input number A:'))
            self.A.append(num)
        self.q = int(input('input number q:'))
        for i in range(self.q):
            num = int(input('input number m:'))
            self.m.append(num)
        
    def sample(self):
        self.make_combination()
        
    def make_combination(self):
        n = self.n
        for i in range(n):
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
    
    def randomname(self, n):
        randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
        return ''.join(randlst)
    
    def solve(self, i, m):
        # str = self.randomname(i)
        # print('i:%d,m:%d,n:%d'%(i,m,self.n))
        if m==0:
            return 1
        if i>= self.n:
            return 0
        # print('res1_str:%s'% str)
        res1=self.solve(i+1, m)
        # print('res2_str:%s'% str)
        # print('A[i]:%d'% self.A[i])
        res2=self.solve(i+1, m - self.A[i])
        # print('res1:%d,res2:%d'%(res1,res2))        
        self.result.append([res1,res2])
        print('i:%d,m:%d,n:%d'%(i,m,self.n))
        print('res1:%d,res2:%d' % (res1,res2) )
        return res1 or res2
    
    def check(self):
        self.init1()
        for num in self.m:
            if self.solve(0, num):
                print('yes')
            else:
                print('no')
        # print(self.result)
        
def main():
    exhaustive_search = Exhaustive_search(True)
    print('start')
    start_time = time.time()
    print(start_time)
    # exhaustive_search.sample()
    exhaustive_search.check()
    end_time = time.time()
    print(end_time)
    print(end_time - start_time)
    print('end')
    
    
if __name__ == '__main__':
    main()
