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

    def postorder(self, child):
        if self != None:
            self.postorder(self.get_left)
            self.postorder(self.get_right)
            print(self.get_root_val)

    def inorder(self, child):
        if self != None:
            self.inorder(self.get_left())
            print(self.get_root_val())
            self.inorder(self.get_right())