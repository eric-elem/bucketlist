import unittest
from src.modals import Bucket, Item, TheUser


class TestBucketMethods(unittest.TestCase):
    # None attribute
    def test_add_item_none(self):
        self.assertEqual(Bucket('Test').add_item(None), 'Input cannot be None')

    # Non Item attribute
    def test_add_item_non_Item(self):
        self.assertEqual(Bucket('Test').add_item('item'),
                         'Input should be of type Item')

    # Valid attribute
    def test_add_item_valid(self):
        self.assertEqual(Bucket('Test').add_item(Item('item')), True)


class TestTheUserMethods(unittest.TestCase):
    # None attribute
    def test_add_bucket_none(self):
        self.assertEqual(TheUser('Test', 'test', 'test').add_bucket(
            None), 'Input cannot be None')

    # Non Item attribute
    def test_add_bucket_non_Bucket(self):
        self.assertEqual(TheUser('Test', 'test', 'test').add_bucket(
            'bucket'), 'Input must be of type Bucket')

    # Valid attribute
    def test_add_bucket_valid(self):
        self.assertEqual(TheUser('Test', 'test', 'test').add_bucket(
            Bucket('bucket')), True)


class TestItemMethods(unittest.TestCase):
    # Name should not be empty
    def test_set_name_empty(self):
        self.assertEqual(Item('Test').set_name(''), 'Name cannot be empty')

    # Name should not be None
    def test_set_name_none(self):
        self.assertEqual(Item('Test').set_name(None), 'Name cannot be None')

    # Valid name
    def test_set_name_valid(self):
        self.assertEqual(Item('Test').set_name('item'), True)

    # Valid status Pending
    def test_set_status_valid_pending(self):
        self.assertEqual(Item('Test').set_status('Pending'), True)

    # Valid status Done
    def test_set_status_valid_done(self):
        self.assertEqual(Item('Test').set_status('Done'), True)

    # Invalid status
    def test_set_status_invalid(self):
        self.assertEqual(Item('Test').set_status('item'), 'Invalid status')


if __name__ == '__main__':
    unittest.main()
