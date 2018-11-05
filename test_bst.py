#python -m unittest test_bst
#start every test with 'test_'

import unittest
from bst import BinarySearchTree

class TestBinarySearchTreeTree(unittest.TestCase):

    """
    Initialization
    """
    
    def test_instantiation(self):
        try:
            BinarySearchTree()
        except NameError:
            self.fail("Could not instantiate BinarySearchTree.")

    def test_instantiation_with_value(self):
        fake_value = "FAKE"
        bst = BinarySearchTree(fake_value)
        self.assertEqual(fake_value, bst.value)

    def test_instantiation_with_value_left_right(self):
        fake_value = "FAKE"
        fake_child = "FAKE"
        bst = BinarySearchTree(fake_value, fake_child, fake_child)
        self.assertEqual(fake_child, bst.left)
        self.assertEqual(fake_child, bst.right)

    """
    Insert
    """

    def test_insert(self):
        bst = BinarySearchTree(50)
        bst.insert(1)
        bst.insert(55)
        self.assertEqual(1, bst.left.value)
        self.assertEqual(55, bst.right.value)

    def test_insert_with_value_left(self):
        bst = BinarySearchTree("FAKE", BinarySearchTree(), BinarySearchTree())
        bst.insert_left(41)
        self.assertEqual(41, bst.left.value)
    
    def test_insert_with_value_right(self):
        bst = BinarySearchTree("FAKE", BinarySearchTree(), BinarySearchTree())
        bst.insert_right(41)
        self.assertEqual(41, bst.right.value)

    """
    Traverse
    """

    def test_traverse_preorder(self):
        bst_1 = BinarySearchTree(40)
        bst_2 = BinarySearchTree(53)
        bst_3 = BinarySearchTree(10, bst_1, bst_2)
        bst_3.preorder()

    def test_traverse_postorder(self):
        bst_1 = BinarySearchTree(33)
        bst_2 = BinarySearchTree(47)
        bst_3 = BinarySearchTree(77, bst_1, bst_2)
        bst_3.postorder()

    def test_traverse_inorder(self):
        bst_1 = BinarySearchTree(33)
        bst_2 = BinarySearchTree(45)
        bst_3 = BinarySearchTree(80, bst_1, bst_2)
        bst_3.inorder()

    """
    Find
    """

    def test_find_value(self):
        test_value = "FAKE"
        bst = BinarySearchTree(test_value)
        self.assertEqual(test_value, bst.value)

    def test_find_height(self):
        bst = BinarySearchTree(50)
        bst.insert(40)
        bst.insert(32)
        bst.insert(69)
        bst.find_height_left()

    """
    Deletion
    """

    def test_del_leaf(self):
        bst = BinarySearchTree(35)
        bst.insert(30)
        bst.insert(43)
        bst.insert(45)
        bst.del_leaf_value()

if __name__ == '__main__':
    unittest.main()