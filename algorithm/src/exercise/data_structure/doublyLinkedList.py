from collections import deque
import queue
import sys
import math

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
