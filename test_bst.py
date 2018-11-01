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

if __name__ == '__main__':
    unittest.main()