from collections import deque
import queue
import sys
import math
import random

class Liner:
    S = []
    n = 0
    T = []
    q=0
    MAX_N = 10000
    MAX_Q = 500

    def __init__(self, n = 0, q = 0):
        """ initial class instance
        Args:
            n (int): _description_
        """
        self.n= n
        self.q = q
        S = self.init_list(n, self.MAX_N)
        T = self.init_list(n, self.MAX_Q)
        print(S)
        print(T)

    def init_list(self, num, max):
        """ create list

        Args:
            num (int): _description_
            max (int): _description_

        Returns:
            _type_: list 
        """
        numList = range(max)
        return ramdom.sample(numList, num)
        
        
    def sum(self):
        return self.a + self.b

    def set(self, a, b):
        self.a = a
        self.b = b

def insert():
    print(sys._getframe().f_code.co_name)
    
def delete():
    print(sys._getframe().f_code.co_name)
    
def deleteFirst():
    print(sys._getframe().f_code.co_name)
    
def deleteLast():
    print(sys._getframe().f_code.co_name)


def main():
    print('start')
    liner = Liner(100, 10)
    
    print('end')
        
if __name__ == '__main__':
    main()
