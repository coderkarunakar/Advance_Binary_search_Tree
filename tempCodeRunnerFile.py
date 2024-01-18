
#write code without looking and understand it
#Structure of BST
class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    def __init__(self,data):
        #initially keeping root as None,and no of nodes also zero
        self.root = None
        self.numofnodes = 0
    def printTreeHelper(self,root):
        
        #note:if you want to call recursively on left and right side then you need to pass root as your argument

        if root == None:
            return
        print(root.data,end=':')
        if root.left != None:
            print("L",root.left.data,end=',')
        if root.right != None:
            print('R',root.right.data,end='')
        print()
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)

    def printTree(self):
        self.printTreeHelper(self.root)

    def isdatapresentHelper(self,root,data):
        #if the tree is None simply return Fals
            if root ==  None:
                return False
                #if the searching data is equal to the root data then it is true
            if root.data == data:
                return True
            if root.data > data:
                #call on left
                return self.isdatapresentHelper(root.left,data)
            else:
                #call on right
                return self.isdatapresentHelper(root.right,data)
        
        #THIS IS for searching the data
    def isdatapresent(self,data):
        return self.isdatapresentHelper(self.root,data)


    def insertHelper(self,root,data):
        #it is an empty tree
        if root == None:
            #call it a binary tree and return node and create a node with data and return this node
            node = BinaryTreeNode(data)
            return node

        #if roots data is greater than roots data then call it on left and attach it to roots left 
        if root.data > data:
            root.left = self.insertHelper(root.left, data)
            return root
        else:
            root.right = self.insertHelper(root.right, data)
            return root
            

    def insert(self,data):
        #if it returns you the new root,then change your class root to this
        self.root=self.insertHelper(self.root, data)


    def min(self, root):
        if root == None:
            #if we want to find min of an empty set return a large no
            return 10000
            #check on left ,if left is none,root has to be min,if left is not none then simply get the min from left and return
        if root.left == None:
            return root.data
        #otherwise
        return self.min(root.left)
        #it keeps going on left,left,...and simly returns end of the left as min

    
    #creating an delete helper function
    def deleteDataHelper(self,root,data):
        #will return true,false, and root 
        if root == None:
            return False,root
        #if roots data is less than the data,call it on left side
        if root.data < data:
            deleted, newRightNode = self.deleteDataHelper(root.right,data)
            #simply change right child to be the new right node,if didn't change ,keeping the same right child
            #if we delete some thing on right the overall root is not going to change,return wheather you deleted something or not and root stays the same
            root.right = newRightNode
            return deleted,root
        
        if root.data > data:
            deleted, newLeftNode = self.deleteDataHelper(root.left,data)
            root.left = newLeftNode
            return deleted,root
             
        #special case root data == data

        #root is leaf
        if root.left == None and root.right == None:
            return True,None
            #here return true because am deleting something and roots right becomes new root
        #root has one child
        if root.left == None:
            return True, root.right

        if root.right == None:
            return True,root.left
        
        #root has 2 children
        #find roots replacement by finding the min node from roots right side,then change roots data to be replacement
        replacement = self.min(root.right)
        root.data  = replacement
        deleted, newRightNode = self.deleteDataHelper(root.right, replacement)
        root.right = newRightNode
        return True,root
            



    def deletedata(self,data):
        deleted, newRoot = self.deleteDataHelper(self.root,data)
        #if actually it deleted something then we will reduce the no of nodes,and then next root is the new root and return the deleted,to tell wheather actually we deleted something or not
        if deleted:
            self.numofnodes -= 1
        self.root = newRoot
        return deleted
    def count(self):
        return self.numofnodes

b =BST()
b.insert(10) #->the 1st one will be root
b.insert(5)  #->2nd one will be roots left
b.insert(12)  # ->3rd one will be roots right
b.insert(11)
b.insert(15)
b.printTree()
print(b.count())
b.deletedata(8)
b.printTree()
b.deletedata(5)
b.printTree()