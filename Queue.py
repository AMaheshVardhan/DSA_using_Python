class Queue:
    def __init__(self):
        self.items = []
    def Enqueue(self, item):
        self.items.append(item)
        print("Item inserted Successfully")
        return
    def Dequeue(self):
        if (len(self.items)==0):
            print("Queue is Empty")
            return
        self.items.pop(0)
        print("POPPED!!!")
        return
    def size(self):
        print(len(self.items))
    def Print(self):
        for el in self.items:
            print(el, end = "--->")   
        return    
q = Queue()
q.Enqueue(10)
q.Enqueue(20)
q.Enqueue(40)
q.Enqueue(100)    
q.Dequeue() 
q.size()
q.Print()
