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
        printTreeHelper(root.left)
        printTreeHelper(root.right)

    def printTree(self):
        printTreeHelper(self.root)

    def isdatapresentHelper(self,root,data):
        #if the tree is None simply return Fals
            if root ==  None:
                return False
                #if the searching data is equal to the root data then it is true
            if root.data == data:
                return True
            if root.data > data:
                #call on left
                return isdatapresentHelper(root.left,data)
            else:
                #call on right
                return isdatapresentHelper(root.right,data)
        
        #THIS IS for searching the data
    def isdatapresent(self,data):
        return isdatapresentHelper(self.root,data)

    def insert(self,data):
        return
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