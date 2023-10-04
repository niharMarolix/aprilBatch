class Queue:
    def __init__(self,size):
        self.items = []
        self.size = size

    def is_empty(self):
        return len(self.items)==0
    
    def is_full(self):
        return len(self.items)==self.size

    # pushing an elemnt to queue is called enqueing
    def enqueue(self,item):
        if self.is_full():
            print("Queue is Full, try dequing some elements")
        else:
            self.items.append(item)

    # deleting from the front is dequeing
    def dequeue(self):
        if self.is_empty():
            return("Queue is empty")
        else:
            return self.items.pop(0)
        
    def front(self):
        if self.is_empty():
            return("Queue is empty")
        else:
            return self.items[0]
        
    def rear(self):
        if self.is_empty():
            return("Queue is empty")
        else:
            return self.items[-1]
        
    def display(self):
        return self.items
        

q = Queue(10)
q.enqueue(1)
q.enqueue(3)
q.enqueue(4)
q.dequeue()
q.enqueue(5)
q.dequeue()
q.enqueue(1)
q.enqueue(3)
q.enqueue(4)
q.enqueue(1)
q.enqueue(3)
q.enqueue(4)
q.enqueue(4)
q.enqueue(4)
q.enqueue(4)
print(q.display())
    