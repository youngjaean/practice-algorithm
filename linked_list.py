class Node():
    def __init__(self, data, Next=None):
        self.data = data
        self.Next = Next
class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
    
    def add(self, data):
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(data)
    
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.Next

    def delete(self, data):
        if self.head == '':
            print("해당 값을 가진 노드가 없습니다")
            return
        if self.head.data == data:
            temp = self.head
            self.head = self.head.Next
            del temp
        else:
            node = self.head
            while node.Next:
                if node.Next.data == data:
                    temp = node.Next
                    node.Next = node.Next.Next
                    del temp
                    return 
                else:
                    node = node.Next
    def search(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.Next

