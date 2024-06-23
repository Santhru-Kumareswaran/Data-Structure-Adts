class slist:
    class node:
        def __init__(self,data):
            self.element = data
            self.next = None
            self.prev = None

    def __init__(self):
            self.head = self.node(None)
            self.size = 0

    def insertfirst(self,value):
        newnode = self.node(value)
        if self.size == 0:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
        self.size = self.size+1

    def insertend(self,value):
        newnode = self.node(value)
        if self.size == 0:
            self.head = newnode
        else:
            currentnode = self.head
            while currentnode.next!=None:
                currentnode = currentnode.next
            currentnode.next = newnode
            newnode.prev = currentnode
        self.size = self.size+1

    def delfirst(self):
        if self.size == 0:
            print("List is empty")
        elif self.size == 1:
            self.head.element = None
            self.size = self.size-1
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            del temp
            self.size = self.size-1

    def delend(self):
        if self.size == 0:
            print("List is empty")
        elif self.size == 1:
            self.head.element = None
            self.size = self.size-1
        else:
            currentnode = self.head
            while currentnode.next!=None:
                temp = currentnode
                currentnode = currentnode.next
            temp.next = None
            currentnode.prev = None
            del currentnode
            self.size = self.size-1

    def displayforward(self):
        if self.size == 0:
            print("List is empty")
        else:
            currentnode = self.head
            while currentnode!=None:
                print(currentnode.element , end=" ")
                currentnode = currentnode.next
        print()

    def displayreverse(self):
        if self.size == 0:
            print("List is empty")
        else:
            currentnode = self.head
            while currentnode.next!=None:
                currentnode = currentnode.next
            while currentnode!=None:
                print(currentnode.element , end=" ")
                currentnode = currentnode.prev
        print()

l = slist()
l.delend()
l.insertfirst(20)
l.insertfirst(10)
l.insertend(30)
l.insertend(40)
l.displayforward()
l.displayreverse()
l.delend()
l.delfirst()
l.displayforward()

            
            

















            
            
