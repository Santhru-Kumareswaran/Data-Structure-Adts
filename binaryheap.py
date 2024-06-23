class BinHeap():
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    """ This method defines the upheap function when inserting an element
    """
    def upHeapp(self,i):
        #@start-editable@

        while i//2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]
            i = i // 2
			
	    #@end-editable@
            
    def insert(self,k):
        #@start-editable@
        self.heapList.append(k)
        self.currentSize += 1
        self.upHeapp(self.currentSize)
        #@end-editable@

    """ This method defines the downheap function when removing min
    """
    def downHeap(self,i):
        #@start-editable@		
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc	
	    #@end-editable@

    def minChild(self,i):
        #@start-editable@	
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1		
	    #@end-editable@

    def deleteop(self):
        #@start-editable@   
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.downHeap(1)			
	    #@end-editable@
    
    def buildHeap(self,alist,k):
        #@start-editable@
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.downHeap(i)
            i -= 1
        #@end-editable@
        self.printHeap()


    #create a method to print the contents of the heap in level order 
    def printHeap(self):
        print(self.heapList)
        
    def klargest(self,alist,k):
        #@start-editable@
        for i in range(k - 1):
            self.deleteop()
        return self.heapList[1]            
        #@end-editable@
        return self.heapList[1]

def main():
    heap = BinHeap()
    arraysize=int(input())
    arr = list(map(int, input().split()))
    k=int(input())
    heap.buildHeap(arr,k)
    inputs = int(input())
    while inputs > 0:
         command = input()
         operation = command.split()
         if (operation[0] == "I"):
              heap.insert(int(operation[1]))
              
         elif (operation[0] == "D"):
              heap.deleteop()
              
         elif (operation[0] == "K"):
              kthlargest=heap.klargest(arr,k)
              print(kthlargest)
              
         inputs -= 1

if __name__ == '__main__':
    main()