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

    def insert(self, value):
        self.value = value

    def insert_left(self, newNode):
        if self.left == None:
            self.left = BinarySearchTree(newNode)
        else:
            t = BinarySearchTree(newNode)
            t.left = self.left
            self.left = t

    def insert_right(self, newNode):
        if self.right == None:
            self.right = BinarySearchTree(newNode)
        else:
            t = BinarySearchTree(newNode)
            t.right = self.right
            self.right = t

    def preorder(self):
        print(self.value)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def postorder(self):
        if self:
            if self.get_left():
                self.get_left().postorder()
            if self.get_right():
                self.get_right().postorder()
            print(self.get_root_val())            

    def inorder(self, child):
        if self:
            inorder(self.get_left())
            print(self.get_root_val())
            inorder(self.get_right())