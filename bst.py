class BinarySearchTree:
    
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

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