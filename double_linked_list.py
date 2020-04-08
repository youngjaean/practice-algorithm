class Node:
    def __init__(self, data, prev=None, Next=None):
        self.prev = prev
        self.data = data
        self.Next = Next

class NodeMgmt:
    def __init__(self, data):
        self.head = data
        self.tail = self.head
    
    def insert(self, data):
        node = self.head
        while node.Next:
            node = node.Next
        new = Node(data)
        new.prev = node
        node.Next = new
        self.tail = new

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.Next
    def serach_from_head(self, data):
        node = self.tail

        while node:
            if node.data == data:
                return node
            else:
                node = node.prev
    def insert_befor(self, data, befor_data):
        node = self.tail
        while node.data != befor_data:
            node = node.prev
            if node == None:
                return False
        new = Node(data)
        before_new = node.prev
        before_new.next = new
        new.prev = before_new
        new.next = node
        node.prev = new
        return True
