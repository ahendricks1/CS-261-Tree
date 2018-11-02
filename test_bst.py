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
        fake_value = "FAKE"
        fake_child = "FAKE"
        bst = BinarySearchTree(fake_value, fake_child, fake_child)
        bst.insert(fake_child)

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

if __name__ == '__main__':
    unittest.main()