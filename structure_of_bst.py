#Dry run it has doubt on delete data
#write code without looking and understand it
#Structure of BST
#it is used to create node and link them to construct binary tree for various application,it has data the information stored in the node,and pointers to the left and right children forming heirarchiical structure of the binary tree
class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    def __init__(self,data=None):
        #initially keeping root as None,and no of nodes also zero
        self.root = None
        self.numofnodes = 0
        #just because of code readability and To make it user friendly we are using an helper function
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

#just returns true or false,
    def isdatapresentHelper(self,root,data):
        #if the tree is None simply return Fals
            if root ==  None:
                return False
                #if the searching data is equal to the root data then it is true,checks at every root value
            if root.data == data:
                return True
            if root.data > data:
                #call on left,and checks at every node by using above lines
                return self.isdatapresentHelper(root.left,data)
            else:
                #call on right
                return self.isdatapresentHelper(root.right,data)
        
        #THIS IS for searching the data
    def isdatapresent(self,data):
        return self.isdatapresentHelper(self.root,data)

#Note:the root remains same untill completion of the tree
    def insertHelper(self,root,data): 
        #for an empty tree we are creating an new node and returning it ,in order to insert new nodes
        #it is an empty tree, the first one will be root created
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
        self.numofnodes +=1


    def min(self, root):
        #if we want to find a min of set we will return a large no of set so 1000,if root is none we return a large no
        if root == None:
            return 10000
            #if no left value simply return root value since it is the min value
        if root.left == None:

            return root.data
                # Otherwise, we recursively search for the minimum in the left subtree.of right side   

        return self.min(root.left)
        #the above function keep going left,left ,left and so on and it reaches where there are no more left children simply return that nodes data,that how we will be able to find

    
    def  deleteDataHelper(self,root,data):
#if root is empty simply return false(no root is deleted and root stays to be none)        
        if root == None:
            return False,None
            #if roots data is less than data so it will on right side so call it
        if root.data < data:
#it is telling that if deleted something or not and returning newrightnode,this line checks the match with the root.right and data value i.e compares mathching or not if mathces goes to next line or agai back
            deleted, newRightNode = self.deleteDataHelper(root.right,data)
            #changing right child to be the new right node since we deleted root and that should be replaced by something
            root.right = newRightNode
            #incase didn't changed the root remains same
            return deleted,root
            #similar for left child
        if root.data > data:
            deleted, newLeftNode = self.deleteDataHelper(root.left,data)
            root.left = newLeftNode
            return deleted,root
             
#if you are reaching here this case is roots data == data ,again 3cases
#case1:root has data and no left,right data so return true and nothing to replace as a root so return none
        if root.left == None and root.right == None:
            return True,None
       #case2:if roots left == none i.e no left child only right child is there and return true since deleting something and root.right as the new root similar for right side as well    
        if root.left == None:
            return True, root.right
        if root.right == None:
            return True,root.left
#root has 2children ,in this case after deleting root we need to replace it with something so finding replacement as the min value of the right side for beter clarifcation look at class Notes
        replacement = self.min(root.right)
        #once you get replacement value then assign it to root value
        root.data  = replacement
        #here you replaced right side min value as a root and still right side min value exist so we are deleting that min value from right side,on root right side deleting the replacement,and it is going to return 2things deleted or not and new right side node
        deleted, newRightNode = self.deleteDataHelper(root.right, replacement)
        #roots right will be new right node,
        root.right = newRightNode
        #simply return true since deleted somthing and root stays the same,it does not change
        return True,root
            #in the above case we didnot removed the data ,we have replaced the nodes data,
            #node is same ,nodes data has been changed ,just copied the content here so root stays same ,and deleted that replacement value in the right side



    def deletedata(self,data):
        deleted, newRoot = self.deleteDataHelper(self.root,data)
        if deleted:
            #if deleted any tehn the no of nodes value is getting decreased
            self.numofnodes -= 1
#the updated new root is getting assigned to the actual root postion
        self.root = newRoot
        #finally a true or false if deleted then it is true
        return deleted
        #simply it gives count by no of nodes
    def count(self):
        return self.numofnodes

b =BST()
(b.insert(10)) #->the 1st one will be root
(b.insert(5))  #->2nd one will be roots left
(b.insert(7))  # ->3rd one will be roots right
(b.insert(6))
(b.insert(8))
(b.insert(12))
(b.insert(11))
(b.insert(15))
(b.printTree())
print(b.count())
b.deletedata(8)
b.printTree()

