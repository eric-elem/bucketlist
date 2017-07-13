import unittest
from .src.item import Item

class TestItemMethods(unittest.TestCase):

    def test_get_item_(self):        
        self.assertEqual(get_item(None), 'Input cannot be None')

    

if __name__ == '__main__':
    unittest.main()