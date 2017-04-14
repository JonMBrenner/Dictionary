class EmptyTree:
    def empty(self):
        return True

    def __len__(self):
        return 0

    def lookup(self, key):
        raise KeyError(str(key))

    def items(self):
        return
        yield

class BST:
    def __init__(self, key, value):
        self._key = key
        self._value = value
        self._left = EmptyTree()
        self._right = EmptyTree()

    def empty(self):
        return False

    def insert(self, key, value):
        if key > self._key:
            if self._right.empty():
                self._right = BST(key, value)
            else:
                self._right.insert(key, value)
        elif key < self._key:
            if self._left.empty():
                self._left = BST(key, value)
            else:
                self._left.insert(key, value)
            return
        else:
            self._value = value 

    def __len__(self):
        return 1 + len(self._right) + len(self._left)

    def lookup(self, key):
        if key == self._key:
            return self._value
        elif key > self._key:
            return self._right.lookup(key)
        elif key < self._key:
            return self._left.lookup(key)

    def items(self):
        yield from self._left.items()
        yield (self._key, self._value)
        yield from self._right.items()


import unittest

class TestBST(unittest.TestCase):
    def setUp(self):
        self.bst = BST('g', 25)
        self.bst.insert('d', 12)
        self.bst.insert('f', 30)
        self.bst.insert('e', 10)
        self.bst.insert('b', 2)
        self.bst.insert('c', 4)
        self.bst.insert('a', 1)
        self.bst.insert('l', 7)
        self.bst.insert('i', 8)
        self.bst.insert('h', 15)
        self.bst.insert('j', 72)
        self.bst.insert('k', 21)
        self.bst.insert('r', 2)
        self.bst.insert('m', 40)
        self.bst.insert('o', 9)
        self.bst.insert('z', 212)
        self.bst.insert('t', 11)

    def test_length(self):
        self.assertEqual(len(self.bst), 17)
        self.bst.insert('q', 16)
        self.assertEqual(len(self.bst), 18)

    def test_lookup(self):
        self.assertEqual(self.bst.lookup('d'), 12)
        self.assertEqual(self.bst.lookup('z'), 212)
        self.assertEqual(self.bst.lookup('j'), 72)
        self.assertEqual(self.bst.lookup('h'), 15)
        self.assertEqual(self.bst.lookup('t'), 11)
        self.assertEqual(self.bst.lookup('g'), 25)
        self.assertEqual(self.bst.lookup('a'), 1)
        self.assertEqual(self.bst.lookup('e'), 10)
        self.assertEqual(self.bst.lookup('k'), 21)
        self.assertEqual(self.bst.lookup('o'), 9)
        self.assertEqual(self.bst.lookup('c'), 4)
        self.assertNotEqual(self.bst.lookup('k'), 2)

    def test_items(self):
        self.assertNotIsInstance(self.bst.items(), list)
        items = list(self.bst.items())
        self.assertIsInstance(items[0], tuple)
        self.assertEqual(items[0][0], 'a')
        self.assertEqual(items[16][1], 212)
        self.assertEqual(items[5][1], 30)

    def test_tree_structure(self):
        self.assertEqual(self.bst._value, 25)
        self.assertEqual(self.bst._left._left._value, 2)
        self.assertEqual(self.bst._left._right._left._value, 10)
        self.assertEqual(self.bst._left._left._right._value, 4)
        self.assertEqual(self.bst._right._right._right._left._value, 11)
        self.assertEqual(self.bst._right._left._right._right._value, 21)
        with self.assertRaises(KeyError):
            self.bst._left._right._right.lookup('x')


if __name__ == '__main__':
    unittest.main()
