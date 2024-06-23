class slist:
    class node:
        def __init__(self,value):
            self.element = value
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insertfirst(self,value):
        newnode = self.node(value)
        if self.size == 0:
            self.head = newnode
            self.tail = newnode
            self.tail.next = self.head
        else:
            newnode.next = self.head
            self.head = newnode
            self.tail.next = self.head
        self.size = self.size+1

    def insertend(self,value):
        newnode = self.node(value)
        if self.size == 0:
            self.head = newnode
            self.tail = newnode
            self.tail.next = self.head
        else:
            self.tail.next = newnode
            self.tail = newnode
            self.tail.next = self.head
        self.size = self.size+1

    def delfirst(self):
        if self.size == 0:
            print("List is empty")
        elif self.size == 1:
            self.head.element = None
            self.tail.next = None
            self.size = self.size-1
        else:
            self.head = self.head.next
            self.tail.next = self.head
            self.size = self.size-1

    def delend(self):
        if self.size == 0:
            print("List is empty")
        elif self.size == 1:
            self.head.element = None
            self.tail.next = None
            self.size = self.size-1
        else:
            currentnode = self.head
            while currentnode.next!=self.tail:
                currentnode = currentnode.next
            currentnode.next = self.head
            self.tail = currentnode
            del currentnode
            self.size = self.size-1  

    def display(self):
            if self.size == 0:
                print("List is  empty")
            else:
                currentnode = self.head
                while True:
                    print(currentnode.element , end=" ")
                    currentnode = currentnode.next
                    if currentnode == self.head:
                        break
            print()

    def showtail(self):
            if self.size == 0:
                print("List is empty")
            else:
                print(self.tail.element)
            print()

l = slist()
l.delend()
l.insertfirst(20)
l.insertfirst(10)
l.showtail()
l.insertend(30)
l.showtail()
l.display()
l.insertend(40)
l.display()
l.delend()
l.showtail()














        
            
        
    
