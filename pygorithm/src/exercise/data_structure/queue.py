from collections import deque
import sys

class schedule:
    # quantum
    q = 100
    name = ''
    time = 0
    
    def __init__( self, name, time): 
        self.name = name
        self.time = time
    
def main():
    print('start')
    testQueueRoundRobin()
    
def enqueue():
    print(sys._getframe().f_code.co_name)
    enList = [1,2,3,4]
    enList.append(5)
    print(enList[0])
    
def testQueueRoundRobin():
    print(sys._getframe().f_code.co_name)
    queueRoundRobin()
    
def queueRoundRobin():
    print(sys._getframe().f_code.co_name)
    processList = createProcessList()
    
    for process in processList:
     print(process.name)
     print(process.time)

def createProcessList():
    processList = []
    
    processList.append(schedule('A', 150))
    processList.append(schedule('B', 80))
    processList.append(schedule('C', 200))
    processList.append(schedule('D', 200))
    return processList
    
    
if __name__ == '__main__':
    main()
