class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

   
    def temp(self):
        if self.right is None:
            return -1
        if self.right is not None:
            print(self.data)
            self.right().temp()
            self.left.temp()



    def Addchild(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.Addchild(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.Addchild(data)
            else:
                self.right = BinarySearchTreeNode(data)                

    def inorder(self):
        if self.left:
            self.left.inorder()

        print(self.data, end=" ")
        if self.right:
            self.right.inorder()

    def preorder(self):
        print(self.data, end=" ")         
        if self.left:
            self.left.preorder()

        if self.right:
            self.right.preorder()

    def postorder(self):       
        if self.left:
            self.left.postorder()

        if self.right:
            self.right.postorder() 
        print(self.data, end=" ")   

    def search(self, value):
        if self.data == value:
            return True
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        if value > self.data:
            if self.right:
               return    self.right.search(value)
            else:
                return False 
    
    def delete(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            # Node with only one child or no child
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            # Node with two children
            # Find the in-order successor (smallest node in the right subtree)
            temp = self.right
            while temp.left:#(Need to get min element from right most side or max element from left most side)
                temp = temp.left
            # Copy the in-order successor's value to this node
            self.data = temp.data
            # Delete the in-order successor
            self.right = self.right.delete(temp.data)

        return self

        


bst = BinarySearchTreeNode(10)
bst.Addchild(20)
bst.Addchild(0)
bst.Addchild(30)
bst.Addchild(32)
# print("inorder: ", end=" ")
# bst.inorder()
# print()
# print("Preorder: ", end=" ")
# bst.preorder()
# print()
# print("PostOrder: ", end=" ")
# bst.postorder()
# bst.delete(32)
# print()
# print("inorder: ", end=" ")
# bst.inorder()
bst.temp()
