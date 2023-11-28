class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, None)
            self.head = node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        node = Node(data, None)
        itr.next = node
    def print(self):
        if self.head is None:
            print("Linked list empty")
            return
        itr = self.head
        while itr:
            print(itr.data, end="--->")
            itr = itr.next
    def Insert_At_Pos(self, data, index):
        itr = self.head
        count = 0
        while itr:
            if count == index-1:  
                node = Node(data, itr.next)
                itr.next = node
                return
            else:
                count+=1
                itr = itr.next 
    def remove(self, index):
          count = 0
          itr = self.head
          while itr:
                if count == index-1:
                    itr.next = itr.next.next
                    break  
                itr = itr.next
                count += 1
    def Insert_At_Head(self, data):
        itr = self.head
        node = Node(data, itr.next)      
        self.head = node
        return 
         
ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(3)
ll.insert_at_end(2)
ll.Insert_At_Pos(100, 1)
ll.Insert_At_Pos(400,2)
ll.Insert_At_Head(6)
ll.remove(2)
ll.print()
            
