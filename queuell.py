class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isempty(self):
        return self.front == None

    def Enqueue(self,data):
        newnode = Node(data)
        if self.rear == None:
            self.front=self.rear=newnode
        else:
            self.rear.next = newnode
            self.rear = newnode

    def Dequeue(self):
        if self.isempty():
            return None
        else:
            temp = self.front
            self.front = temp.next
            if(self.front == None):
                self.rear = None

    def display(self):
        if self.isempty():
            return None
        else:
            currentnode = self.front
            while(currentnode!=None):
                print(currentnode.data , end=" ")
                currentnode = currentnode.next
            print()

q = Queue()
q.Enqueue(10)
q.Enqueue(20)
q.Enqueue(30)
q.Enqueue(40)
q.display()
q.Dequeue()
q.display()
