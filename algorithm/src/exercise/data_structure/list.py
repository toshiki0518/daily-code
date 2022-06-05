from collections import deque
import sys

def main():
    print('start')
    enqueue()
    
def enqueue():
    print(sys._getframe().f_code.co_name)
    enList = [1,2,3,4]
    enList.append(5)
    print(enList[0])
    
if __name__ == '__main__':
    main()
