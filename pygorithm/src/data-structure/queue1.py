
from unittest import result


class Queue:
    MAX=11
    queue=[0]*MAX
    head=0
    tail=0

    def __init__(self) -> None:
        pass

    def enqueue(self, d):
        nt = (self.tail +1) % self.MAX
        if nt == self.head:
            print("can not add data")
        else:
            self.queue[self.tail] = d
            self.tail = nt
            print("added",d)
    
    def dequeue(self):
        if self.head == self.tail:
            print("can not get data")
            return None
        else:
            d = self.queue[self.head]
            self.head = (self.head + 1) %self.MAX
            return d
def main():
    que = Queue()
    for i in range(11):
        que.enqueue(i)
    print(que.queue)
    for i in range(11):
        d = que.dequeue()
        print("get data is:",d)
    
if __name__ =='__main__':
    main()
    