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
        self.kv_pairs = [('d', 12),('f', 30), ('e', 10), ('b', 2), ('c', 4),
                ('a', 1), ('l', 7), ('i', 8), ('h', 15), ('j', 72), ('k', 21),
                ('r', 2), ('m', 40), ('o', 9), ('z', 212), ('t', 11)]
        for k, v in self.kv_pairs:
            self.bst.insert(k, v)
        self.kv_pairs.insert(0, ('g', 25))

    def test_length(self):
        self.assertEqual(len(self.bst), len(self.kv_pairs))
        self.bst.insert('q', 16)
        self.assertEqual(len(self.bst), len(self.kv_pairs) + 1)

    def test_lookup(self):
        for k, v in self.kv_pairs:
            self.assertEqual(self.bst.lookup(k), v)

    def test_items(self):
        self.assertNotIsInstance(self.bst.items(), list)
        items = list(self.bst.items())
        self.assertIsInstance(items[0], tuple)
        self.assertEqual(items, sorted(self.kv_pairs))

    def test_tree_structure(self):
        self.assertEqual(self.bst._key, 'g')
        self.assertEqual(self.bst._left._left._key, 'b')
        self.assertEqual(self.bst._left._right._left._key, 'e')
        self.assertEqual(self.bst._left._left._right._key, 'c')
        self.assertEqual(self.bst._right._right._right._left._key, 't')
        self.assertEqual(self.bst._right._left._right._right._key, 'k')
        with self.assertRaises(KeyError):
            self.bst._left._right._right.lookup('x')


if __name__ == '__main__':
    unittest.main()
