class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self) -> None:
        self.head = None
    
    def push(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    
    def pop(self):
        if self.head is None:
            raise IndexError('pop from empty stack')
        poppednode = self.head
        self.head = self.head.next
        return poppednode.data

    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return self.size() == 0
    
    def peek(self):
        return self.items[-1]
    
