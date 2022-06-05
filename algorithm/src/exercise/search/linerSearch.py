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

    def liner_search(self):
        searchTargetList = self.S
        for i in range(self.n):
            num = searchTargetList[i]

    def create_test_list(self):            
        return self.random_list(10, 10)
            
    def liner_test1(self, key):
        test_list = self.create_test_list()
        print("key is %d" % key)
        print('test_list is')
        print(test_list)
        compare = 0
        for i in range(len(test_list)):
            compare+=1
            eq = test_list[i] == key
            compare+=1
            if eq:
                return i
        print ("compare times is %d" % compare)
        return -1
    
    def liner_test2(self, key):
        test_list = self.create_test_list()
        test_list.append(key)
        print("key is %d" % key)
        print('test_list is')
        print(test_list)

        i = 0
        n = len(test_list) - 1
        
        compare = 0
        while test_list[i] != key:
            compare += 1
            i += 1
        compare += 1
        print ("compare times is %d" % compare)
        if i == n:
            # print('not found')
            return -1
        return i
    
    def liner_search1(self, key):
        test_list = self.create_test_list()
        print("key is %d" % key)
        print('test_list is')
        print(test_list)
        compare = 0
        for i in range(len(test_list)):
            compare+=1
            eq = test_list[i] == key
            compare+=1
            if eq:
                return i
        print ("compare times is %d" % compare)
        return -1
    
    def liner_search2(self):
        
        target_list = self.S
        search_list = self.T
        i = n = 0
        answer=[]
        for target in target_list:
            i +=1
            n=0
            last_index = len(search_list)
            search_list.append(target)
            # print(search_list)
            while target != search_list[n]:
                n +=1
            if n != last_index:
                print("target is %d ,search is %d, n is %d" % (target, search_list[n], n))
                answer.append(n)
            else:
                answer.append(-1)            
        return answer
    
    def set(self, a, b):
        self.a = a
        self.b = b

def test():
    print(sys._getframe().f_code.co_name)
    liner = Liner(5, 3)
    # result = liner.liner_test1(11)
    # print('error test result is ')
    # print(result)
    result = liner.liner_test1(11)
    print("test result1 is %d" % result)
    result = liner.liner_test2(11)
    print("test resul2 is %d" % result)    
    
def main():
    print('start')
    liner = Liner(5, 3)
    answer = liner.liner_search2()
    print('answer is ')
    print(answer)
    print('end')
        
    
if __name__ == '__main__':
    main()
