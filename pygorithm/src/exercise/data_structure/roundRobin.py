from collections import deque
import queue
import sys
import math

class schedule:
    # quantum
    q = 100
    name = ''
    time = 0
    
    def __init__( self, name, time): 
        self.name = name
        self.time = time
    
class RoundRobin:
    head = 0
    tail = 0
    queue = []
    # quantum
    q = 100
    name = ''
    time = 0
    MAX = 5
    
    def __init__( self): 
        self.head = self.tail = 0
        self.createProcessList()
        self.head = 0
        self.tail = len(self.queue)
        
    def isEmpty(self):
        return self.head == self.tail
    
    
    def isFull(self):
        return self.head == (self.tail + 1) % self.MAX
        
    def enqueue(self, fact):
        print(sys._getframe().f_code.co_name)
        if self.isFull():
            print('エラー(オーバーフロー)')
            sys.exit()
        self.queue[self.tail] = fact
        if self.tail + 1 == self.MAX:
            self.tail = 0
        else:
            self.tail += 1
        
    def dequeue(self):
        print(sys._getframe().f_code.co_name)
        if self.isEmpty():
            print('エラー(アンダーフロー)')
            sys.exit()
        x = self.queue[self.head]
        if self.head + 1 == self.MAX:
            self.head = 0
        else:
            self.head += 1
        return x

    def createProcessList(self):
        processList = []
        
        processList.append(schedule('A', 150))
        processList.append(schedule('B', 80))
        processList.append(schedule('C', 200))
        processList.append(schedule('D', 200))
        self.queue = processList
        
    def queueRoundRobin(self):
        print(sys._getframe().f_code.co_name)
        while self.head != self.tail:
            u = self.dequeue()

    def testQueueRoundRobin(self):
        print(sys._getframe().f_code.co_name)
        self.queueRoundRobin()

def main():
    print('start')
    roundRobin = RoundRobin()
    roundRobin.testQueueRoundRobin()
    
if __name__ == '__main__':
    main()
