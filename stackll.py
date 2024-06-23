class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.top=None
        self.size=0

    def push(self,data):
        newnode=Node(data)
        newnode.next = self.top
        self.top = newnode
        self.size+=1

    def pop(self):
        if self.size==0:
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        if self.size==0:
            return None
        return self.top.data

    def display(self):
        currentnode = self.top
        while currentnode!=None:
            print(currentnode.data , end=" ");
            currentnode = currentnode.next
        print()

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
print(s.pop())
s.display()
print(s.peek())

            
        
