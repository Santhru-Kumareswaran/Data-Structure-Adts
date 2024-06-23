class BinaryTree:
    class node:
        def __init__(self):
            # Initialize node attributes
            self.element = 0  # Value of the node
            self.parent = None  # Parent node
            self.leftchild = None  # Left child node
            self.rightchild = None  # Right child node

    def __init__(self):
        # Initialize the binary tree
        self.sz = 0  # Size of the tree
        self.root = self.node()  # Root node of the tree
        self.ht = 0  # Height of the tree

    # Get the children of a node
    def getChildren(self, curnode):
        # Initialize a list to store children nodes
        children = []
        # Check if left child exists
        if curnode.leftchild != None:
            children.append(curnode.leftchild)
        # Check if right child exists
        if curnode.rightchild != None:
            children.append(curnode.rightchild)
        return children

    # Check if a node is external (i.e., a leaf node)
    def isExternal(self, curnode):
        # If node has no left or right child, it's external
        if (curnode.leftchild == None and curnode.rightchild == None):
            return True
        else:
            return False

    # Check if a node is the root of the tree
    def isRoot(self, curnode):
        # If node has no parent, it's root
        if (curnode.parent == None):
            return True
        else:
            return False

    # Inorder traversal of the tree
    def inorderTraverse(self, v):
        # Traverse left subtree
        if v.leftchild:
            self.inorderTraverse(v.leftchild)
        # Print node value
        print(v.element, end=" ")
        # Traverse right subtree
        if v.rightchild:
            self.inorderTraverse(v.rightchild)

    # Preorder traversal of the tree
    def preorderTraverse(self, v):
        # Print node value
        print(v.element, end=" ")
        # Traverse left subtree
        if v.leftchild:
            self.preorderTraverse(v.leftchild)
        # Traverse right subtree
        if v.rightchild:
            self.preorderTraverse(v.rightchild)

    # Postorder traversal of the tree
    def postorderTraverse(self, v):
        # Traverse left subtree
        if v.leftchild:
            self.postorderTraverse(v.leftchild)
        # Traverse right subtree
        if v.rightchild:
            self.postorderTraverse(v.rightchild)
        # Print node value
        print(v.element, end=" ")

    # Levelorder traversal of the tree
    def levelorderTraverse(self, v):
        # If tree is empty, return
        if v is None:
            return
        # Initialize a queue for level-order traversal
        queue = []
        queue.append(v)
        while(len(queue) > 0):
            # Print node value
            print(queue[0].element, end=" ")
            # Pop the first node from the queue
            node = queue.pop(0)
            # Enqueue left child if exists
            if node.leftchild is not None:
                queue.append(node.leftchild)
            # Enqueue right child if exists
            if node.rightchild is not None:
                queue.append(node.rightchild)

    # Find the depth of a node in the tree
    def findDepth(self, v):
        depth = 0
        # Traverse up to the root counting the edges
        while v.parent:
            depth += 1
            v = v.parent
        return depth

    # Find the height of a node in the tree
    def findHeight(self, v):
        if v is None:
            return -1
        # Recursively calculate height of left and right subtrees
        return 1 + max(self.findHeight(v.leftchild), self.findHeight(v.rightchild))

    # Delete all leaf nodes in the tree
    def delLeaves(self, v):
        if v is None:
            return
        # Recursively delete leaf nodes
        if self.isExternal(v):
            if v.parent.leftchild == v:
                v.parent.leftchild = None
            else:
                v.parent.rightchild = None
            return
        if v.leftchild:
            self.delLeaves(v.leftchild)
        if v.rightchild:
            self.delLeaves(v.rightchild)

    # Check if the tree is proper
    def isProper(self, v):
        if v is None:
            return True
        # If a node has one child or no children, tree is not proper
        if self.isExternal(v):
            return True
        if v.leftchild is None or v.rightchild is None:
            return False
        # Recursively check left and right subtrees
        return self.isProper(v.leftchild) and self.isProper(v.rightchild)

    # Create a mirror image of the tree
    def mirror(self, v):
        if v is None:
            return
        # Swap left and right children recursively
        self.mirror(v.leftchild)
        self.mirror(v.rightchild)
        v.leftchild, v.rightchild = v.rightchild, v.leftchild

    # Build the binary tree from a list
    def buildTree(self, eltlist):
        nodelist = []
        nodelist.append(None)
        for i in range(len(eltlist)):
            if (i != 0):
                if (eltlist[i] != -1):
                    tempnode = self.node()
                    tempnode.element = eltlist[i]
                    if i != 1:
                        tempnode.parent = nodelist[int(i/2)]
                        if (i % 2 == 0):
                            nodelist[int(i/2)].leftchild = tempnode
                        else:
                            nodelist[int(i/2)].rightchild = tempnode
                    nodelist.append(tempnode)
                else:
                    nodelist.append(None)

        self.root = nodelist[1]
        self.sz = len(nodelist)
        return nodelist

    # Print the tree
    def printTree(self, nlist):
        for i in range(len(nlist)):
            if (nlist[i] != None):
                print(nlist[i].element, end=" ")
            else:
                print(None)

    # Check if the tree is empty
    def isEmpty(self):
        return (self.sz == 0)

    # Get the size of the tree
    def size(self):
        return self.sz

# Main function to run the program
def main():
    tree = BinaryTree()
    arraySize = int(input())
    arr = list(map(int, input().split()))
    nlist = tree.buildTree(arr)
    inputs = int(input())
    while inputs > 0:
         command = input()
         operation = command.split()
         if (operation[0] == "I"):
              tree.inorderTraverse(tree.root)
              print()
         elif (operation[0] == "P"):
              tree.preorderTraverse(tree.root)
              print()
         elif (operation[0] == "Post"):
              tree.postorderTraverse(tree.root)
              print()
         elif (operation[0] == "L"):
              tree.levelorderTraverse(tree.root)
              print()
         elif (operation[0] == "D"):
              pos = int(operation[1])
              print(tree.findDepth(nlist[pos]))
         elif (operation[0] == "H"):
              pos = int(operation[1])
              print(tree.findHeight(nlist[pos]))
         elif (operation[0] == "IP"):
              print(tree.isProper(tree.root))
         elif (operation[0] == 'M'):
              tree.mirror(tree.root)
              tree.levelorderTraverse(tree.root)
              print()
         elif (operation[0] == 'DL'):
              tree.delLeaves(tree.root)
              tree.levelorderTraverse(tree.root)
              print()
         elif (operation[0] == 'RL'):
              tree.root2leafsum(int(operation[1]))
              print()
         elif (operation[0] == 'ML'):
              tree.leastleaf()
              print()
         inputs -= 1

# Entry point of the program
if __name__ == '__main__':
    main()
