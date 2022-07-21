
from unittest import result


class Stack:
    MAX=5
    stack=[0]*MAX
    sp=0

    def __init__(self) -> None:
        pass
   
    def push(self, d):
        if self.sp < self.MAX:
            self.stack[self.sp] = d
            self.sp += 1
            print("add:",d)
        else:
            print("can't add data")
    
    def pop(self):
        if self.sp > 0:
            self.sp -= 1
            return self.stack[self.sp]
        else:
            print("can'n get data")
            return None
            
    
def main():
    stack = Stack()
    for i in range(7):
        stack.push(i)
    for i in range(7):
        d = stack.pop()
        print("get data is:",d)
    
if __name__ =='__main__':
    main()
    