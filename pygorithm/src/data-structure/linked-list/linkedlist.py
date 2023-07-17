# linked list is one of the development way
# abstract list data type.
###

# print('test')
# node has value and next node point.
# head ...
# next node point ...
# last node pointer is...
# 

class LinkedList:
    def __init__(self):
        self.head = None

    ###
    def __str__ (self):
        """ magic method
        Returns:
            _type_: _description_
        """
        data_list = []
        node = self.head
        while node is not None:
            data_list.append(node.data)
            node = node.next
        return "\n".join(data_list)
    
    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        # 先頭を現在
        current = self.head
        # nextがNoneになるまで
        while current.next:
            # nextを現在に
            current = current.next
        # 最後尾にデータをセット
        current.next = Node(data)

    def append_cycle(self, data):
        if not self.head:
            self.head = Node(data)
            return
        # 先頭を現在
        current = self.head
        # nextがNoneになるまで
        while current.next:
            # nextを現在に
            current = current.next
        # 最後尾にデータをセット
        current.next = Node(data, self.head)

    def search(self, target):
        current = self.head
        while current:
            if current.data == target:
                return True
            else:
                current = current.next
        return False
    
    def __contains__(self, target):
        """
        magic method.
        you can use print(10 in LinkedList())

        Args:
            target (_type_): _description_

        Returns:
            _type_: _description_
        """
        return self.search(target)

    def remove(self, target):
        if self.head.data == target:
            self.head = self.head.next
            return
        current = self.head
        previous = None
        while current:
            if current.data == target:
                previous.next = current.next
            previous = current
            current = current.next

    def reverse(self):
        current = self.head
        previous = None
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

    def detect_cycle(self):
        slow = self.head
        fast = self.head
        while True:
            try:
                slow = slow.next
                fast = fast.next.next
                print("slow: %s fast: %s." % (slow, fast))
                if slow is fast:
                    return True
            except:
                print(f"this is not cycle list")
                return False

class Node:
    def __init__(self, data, next=None):
        # pass
        self.data = data
        self.next = next
