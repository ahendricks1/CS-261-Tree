class BinarySearchTree:
    
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right

    def get_root_val(self):
        return self.value
    
    def is_leaf(self):
        return not(self.left or self.right)

    def find(self):
        return self.value

    # def find_height(self, count = 0):
    #     if self.left == None and self.right == None:
    #         return(count + 1)
    #     elif self.left == None:
    #         return self.right.find_height(count) + 1
    #     elif self.right == None:
    #         return self.left.find_height(count) + 1
    #     else:
    #         lefth = self.left.find_height(count)
    #         righth = self.right.find_height(count)
    #         if lefth > righth:
    #             return lefth
    #         else:
    #             return righth

    def find_height(self):
        if self.left == None and self.right == None:
            return 1
        else:
            lefth = 0
            righth = 0
            if self.left != None:
                lefth = self.left.find_height()
            if self.right != None:
                righth = self.right.find_height()
            if lefth > righth:
                return lefth + 1
            else:
                return righth + 1


    def find_height_right(self, count = 0):
        if self.left == None and self.right == None:
            return(count)
        if self.right:
                self.get_right().find_height_right(count + 1)

    def del_leaf_value(self):
        if self.is_leaf():
            return None
        if self.left:
            self.get_left().del_leaf_value()
        if self.right:
            self.get_right().del_leaf_value()

    def insert(self, value):
        if self.value > value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        elif self.value < value:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def preorder(self):
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
        return(self.value)

    def postorder(self):
        if self:
            if self.get_left():
                self.get_left().postorder()
            if self.get_right():
                self.get_right().postorder()
            return(self.get_root_val())            

    def inorder(self):
        if self:
            yield(self.value)
            if self.get_left():
                self.get_left().inorder()
            if self.get_right():
                self.get_right().inorder()