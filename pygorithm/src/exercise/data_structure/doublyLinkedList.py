from collections import deque
import queue
import sys
import math

class Node:
    key = 0
    b = 0

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
    insert()
    
    print('end')
        
if __name__ == '__main__':
    main()
