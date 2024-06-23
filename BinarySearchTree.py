#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 09:10:41 2023

@author: vidhyas
"""

import math

class BinarySearchTree:
    """
    This defines the node class. The children can be individually declared or stored
    in a list. We are adding a pos value which stores the nodes position. root nodes pos value is 1
    """
    class Node:
        def __init__(self):
            self.element = 0
            self.leftchild = None
            self.rightchild = None
            self.pos = -1
            self.parent = None

    """
        This initializes the binary search tree. ht is the height of the tree, sz is the
        number of nodes. You may define this appropriately.
    """
    def __init__(self):
        self.sz = 0
        self.root = None
        self.ht = 0

    """
        This method implements the functionality of finding an element in the tree. The function
        findElement(e) finds the node in the current tree, whose element is e. Depending on the
        value of e and in relation to the current element visited, the algorithm visits the left
        or the right child till the element is found, or an external node is visited. Your
        algorithm can be iterative or recursive

        Output: Returns the pointer to the node
    """    
    def findElement(self, e, curnode):
        if curnode is None or curnode.element == e:
            return curnode
        if e < curnode.element:
            return self.findElement(e, curnode.leftchild)
        return self.findElement(e, curnode.rightchild)

    """
        This method implements insertion of an element into the binary search tree. Using the
        findElement(e) method find the position to insert, and insert a node with element e,
        as left or right child accordingly. Make sure that you update the value of pos attribute.
        curnode.leftchild.pos = curnode.pos * 2
        curnode.rightchild.pos = curnode.pos * 2 + 1    
    """
    def insertElement(self, e):
        if self.root is None:
            self.root = self.Node()
            self.root.element = e
            self.root.pos = 1
            self.sz = 1
            return
        curnode = self.root
        while True:
            if e < curnode.element:
                if curnode.leftchild is None:
                    curnode.leftchild = self.Node()
                    curnode.leftchild.parent = curnode
                    curnode.leftchild.pos = curnode.pos * 2
                    curnode.leftchild.element = e
                    self.sz += 1
                    return
                curnode = curnode.leftchild
            else:
                if curnode.rightchild is None:
                    curnode.rightchild = self.Node()
                    curnode.rightchild.parent = curnode
                    curnode.rightchild.pos = curnode.pos * 2 + 1
                    curnode.rightchild.element = e
                    self.sz += 1
                    return
                curnode = curnode.rightchild

    """
        This method inorderTraverse(self,v) performs an inorder traversal of the BST, starting
        from node v which is initially the root and prints the elements of the nodes as they
        are visited. Remember the inorder traversal first visits the left child, followed by
        the parent, followed by the right child. This could be used to print the tree.
    """
    def inorderTraverse(self, v):
        if v is not None:
            self.inorderTraverse(v.leftchild)
            print(v.element, end=" ")
            self.inorderTraverse(v.rightchild)

    """
        Given a node v this will return the next element that should be visited after v in the
        inorder traversal. You can define this recursively
    """
    def returnNextInorder(self, v):
        if v.rightchild is not None:
            return self.findMinimum(v.rightchild)
        parent = v.parent
        while parent is not None and v == parent.rightchild:
            v = parent
            parent = parent.parent
        return parent

    """
        This method deleteElement(self, e), removes the node with element e from the tree T.
        There are three cases:
            1. Deleting a leaf or external node:Just remove the node
            2. Deleting a node with one child: Remove the node and replace it with its child
            3. Deleting a node with two children: Instead of deleting the node replace with
                a) its inorder successor node or b)Inorder predecessor node
    """
    def deleteElement(self, e):
        node_to_delete = self.findElement(e, self.root)
        if node_to_delete is None:
            return
        parent = node_to_delete.parent

        if node_to_delete.leftchild is None and node_to_delete.rightchild is None:
            if parent is None:  # Deleting root
                self.root = None
            elif parent.leftchild == node_to_delete:
                parent.leftchild = None
            else:
                parent.rightchild = None
        elif node_to_delete.leftchild is None:
            if parent is None:  # Deleting root
                self.root = node_to_delete.rightchild
                self.root.parent = None
            elif parent.leftchild == node_to_delete:
                parent.leftchild = node_to_delete.rightchild
                node_to_delete.rightchild.parent = parent
            else:
                parent.rightchild = node_to_delete.rightchild
                node_to_delete.rightchild.parent = parent
        elif node_to_delete.rightchild is None:
            if parent is None:  # Deleting root
                self.root = node_to_delete.leftchild
                self.root.parent = None
            elif parent.leftchild == node_to_delete:
                parent.leftchild = node_to_delete.leftchild
                node_to_delete.leftchild.parent = parent
            else:
                parent.rightchild = node_to_delete.leftchild
                node_to_delete.leftchild.parent = parent
        else:
            successor = self.findMinimum(node_to_delete.rightchild)
            node_to_delete.element = successor.element
            self.deleteElement(successor.element)

    """
        There are other support methods which maybe useful for implementing your functionalities.
        These include
            1. isExternal(self,v): which returns true if the node v is external
    """
    def isExternal(self, curnode):
        if curnode.leftchild is None and curnode.rightchild is None:
            return True
        else:
            return False

    def getChildren(self, ele):
        node = self.findElement(ele, self.root)
        if node is None:
            return None
        children = []
        if node.leftchild:
            children.append(node.leftchild.element)
        if node.rightchild:
            children.append(node.rightchild.element)
        return children

    def preorderTraverse(self, v):
        if v is not None:
            print(v.element, end=" ")
            self.preorderTraverse(v.leftchild)
            self.preorderTraverse(v.rightchild)

    def postorderTraverse(self, v):
        if v is not None:
            self.postorderTraverse(v.leftchild)
            self.postorderTraverse(v.rightchild)
            print(v.element, end=" ")

    def findDepthIter(self, v):
        depth = 0
        while v.parent is not None:
            v = v.parent
            depth += 1
        return depth

    def findDepth(self, ele):
        curnode = self.findElement(ele, self.root)
        if curnode.element != ele:
            print("No such Element")
            return
        else:
            return self.findDepthIter(curnode)

    def findHeight(self, ele):
        node = self.findElement(ele, self.root)
        if node is None:
            return -1
        return self._findHeight(node)

    def _findHeight(self, node):
        if node is None:
            return -1
        return 1 + max(self._findHeight(node.leftchild), self._findHeight(node.rightchild))

    def findMinimum(self, node):
        current = node
        while current.leftchild is not None:
            current = current.leftchild
        return current


def main():
    tree = BinarySearchTree()
    #print("Array Size:")
    arraySize = int(input())
    #print("Array Elements:")
    arr = list(map(int, input().split()))
    for i in range(arraySize):
        tree.insertElement(arr[i])
    """tree.insertElement(50)
    tree.insertElement(20)
    tree.insertElement(70)
    tree.insertElement(1)
    tree.insertElement(10)
    tree.insertElement(90)
    tree.insertElement(15)
    tree.insertElement(30)
    tree.insertElement(60)
    tree.insertElement(61)
    tree.insertElement(62)
    tree.insertElement(65)
    tree.insertElement(8)
    tree.insertElement(100)"""
    inputs = int(input())
    while inputs > 0:
        command = input()
        operation = command.split()
        if operation[0] == "I":
            tree.inorderTraverse(tree.root)
            print()
        elif operation[0] == "P":
            tree.preorderTraverse(tree.root)
            print()
        elif operation[0] == "Post":
            tree.postorderTraverse(tree.root)
            print()
        elif operation[0] == "D":
            tree.deleteElement(int(operation[1]))
        elif operation[0] == "H":
            print(tree.findHeight(int(operation[1])))
        elif operation[0] == "Depth":
            print(tree.findDepth(int(operation[1])))
        elif operation[0] == 'Find':
            key = tree.findElement(int(operation[1]), tree.root)
            if key.element == int(operation[1]):
                print("Element Found at", key.pos)
            else:
                print("Element not Found")
        elif operation[0] == "GetC":
            childs = tree.getChildren(int(operation[1]))
            print(childs)
        inputs -= 1


if __name__ == '__main__':
    main()
