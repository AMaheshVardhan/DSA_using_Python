class Stack:
    def __init__(self):
        self.items = []
    def Push(self, item):
        self.items.append(item)
        print("Item inserted Successfully")
        return
    def Pop(self):
        if (len(self.items)==0):
            print("Stack is Empty")
            return
        self.items.pop()
        print("POPPED!!!")
        return
    def size(self):
        print(len(self.items))
    def Print(self):
        for el in self.items:
            print(el, end = "--->")   
        return    
s = Stack()
s.Push(10)
s.Push(20)
s.Push(40)
s.Push(100)    
s.Pop() 
s.size()
s.Print()
