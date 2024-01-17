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
        self.insertHelper(self.root, data)
    def deletedata(self,data):
        return False
    def count(self):
        return

b =BST()
b.insert(10) #->the 1st one will be root
b.insert(5)  #->2nd one will be roots left
b.insert(12)  # ->3rd one will be roots right
print(b.isdatapresent(10))
print(b.isdatapresent(7))
print(b.deletedata(4))
print(b.deletedata(10))
print(b.count())
b.printTree()