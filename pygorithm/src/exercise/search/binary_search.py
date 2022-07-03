from collections import deque
import queue
import sys
import math
import random
import datetime
import time
"""
n個の整数を含む数列Sとq個の異なる整数を含む数列Tを読み込み
Tに含まれる整数の中でSに含まれるものの個数Cを出力するプログラム

Returns:
    _type_: _description_
"""
    
class Binary:
    S = []
    n = 0
    T = []
    test=[]
    q=0
    MAX_N = 10
    MAX_Q = 4

    def __init__(self, n = 10, q = 5):
        """_summary_

        Args:
            n (int, optional): _description_. Defaults to 10.
            q (int, optional): _description_. Defaults to 5.
        """
        self.n = n
        self.q = q
        self.S = self.init_list(self.n)
        # TODO
        self.T = self.random_list(self.q, self.MAX_Q, False)
        print(self.S)
        print(self.T)
        
    def init_list(self, max):
        """ create list

        Args:
            num (int): _description_
            max (int): _description_

        Returns:
            _type_: list 
        """
        # return range(max)
        num_list = []
        for i in range(max):
            num_list.append(i + 1)
        return num_list
        
    def random_list(self, num, max, isDouble = False):
        """ create random list

        Args:
            num (int): _description_
            max (int): _description_

        Returns:
            _type_: list 
        """
        numList = list(self.init_list(max))
        if isDouble:
            return random.choices(numList, k=num)
        return random.sample(numList, k=num)
        
        
    def sum(self):
        return self.a + self.b

    def create_test_list(self):            
        return self.random_list(10, 10)
            
    def test_binary(self, key):
        left = 0
        right = self.n
        target_list = self.S
        print('key')
        print(key)
        while left < right :
            mid = (left + right) / 2
            mid = math.floor(mid)
            print('mid is %d' % mid)
            print('target_list[mid] is %d' % target_list[mid])
            if target_list[mid] == key:
                print('mid')
                return mid
            elif key < target_list[mid]:
                print('right')
                right = mid
            else:
                print('left')
                left = mid + 1
        return -1
            

    def binary_search(self, key):
        left = 0
        right = self.n
        target_list = self.S
        # print('key')
        # print(key)
        while left < right :
            mid = (left + right) / 2
            mid = math.floor(mid)
            # print('mid is %d' % mid)
            # print('target_list[mid] is %d' % target_list[mid])
            if target_list[mid] == key:
                # print('mid')
                return mid
            elif key < target_list[mid]:
                # print('right')
                right = mid
            else:
                # print('left')
                left = mid + 1
        return -1
            

    def exec(self):
        search_list = self.T
        result_list = []
        for search in search_list:
            result = self.binary_search(search)
            result_list.append(result)
        print('result is ')
        print(result_list)
        
def test():
    print(sys._getframe().f_code.co_name)
    binary = Binary(10,3)
    result = binary.test_binary(12)
    print(result)
    
    
def main():
    print('start')
    start_time = time.time()
    print(start_time)
    # test()
    binary = Binary(5, 3)
    binary.exec()
    end_time = time.time()
    print(end_time - start_time)
    print('end')
        
    
if __name__ == '__main__':
    main()
