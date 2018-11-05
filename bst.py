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

    def find(self):
        return self.value

    """
    Not working as intended!

    def find_height(self):
        if self.find_height_left() > self.find_height_right():
            return self.find_height_left()
        else:
            return self.find_height_right()
    """

    def find_height_left(self, count = 0):
        if self.left == None and self.right == None:
            return(count)
        if self.left:
            self.get_left().find_height_left(count + 1)

    def find_height_right(self, count = 0):
        if self.left == None and self.right == None:
            return(count)
        if self.right:
                self.get_right().find_height_right(count + 1)

    def del_leaf_value(self):
        if self.left == None and self.right == None:
            return None

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
            
    def insert(self, key):
        if self.value == key:
            print("That node already exists.")
        elif self.value > key:
            self.insert_left(key)
        else:
            self.insert_right(key)

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
            if self.get_left():
                self.get_left().inorder()
                return(self.value)
            if self.get_right():
                self.get_right().inorder()
