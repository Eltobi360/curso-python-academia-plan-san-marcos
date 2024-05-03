class Queue:
    def __init__(self) -> None:
        self.items=[]
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self):
        self.items.pop(0)
    def is_empty(self):
        if self.items.count()> 0:
            print("la cola no esta vacia")
        else:
            print("la cola esta vacia")
            
def show_items(self):
    for i in range(len(self.items)):
        print(self.items[i])

Queue_1=Queue()
for i in range(1,10):
    Queue_1.enqueue(i)
    
print(Queue_1.items)

Queue_1.dequeue()
print(Queue_1.items)
Queue_1.show_items()