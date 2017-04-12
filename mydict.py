import bst

class Dict:
    def __init__(self):
        self._elements = bst.EmptyTree()

    def __setitem__(self, key, value):
        if self._elements.empty():
            self._elements = bst.BST(key, value)
        else:
            self._elements.insert(key, value)

    def __getitem__(self, key):
        return self._elements.lookup(key)

    def __contains__(self, key):
        try:
            self._elements.lookup(key)
        except KeyError:
            return False
        else:
            return True


    def __len__(self):
        return len(self._elements)

    def __repr__(self):
        return ('{'  + ', '.join('{}: {}'.format(
            repr(i[0]), repr(i[1])) for i in self._elements.items()) + '}')

    def keys(self):
        for i in self._elements.items():
            yield i[0]

    def values(self):
        for i in self._elements.items():
            yield i[1]

    def items(self):
        return self._elements.items()


import unittest

class TestDict(unittest.TestCase):
    def test_insert_and_lookup(self):
      d = Dict()
      d['a'] = 2
      self.assertEqual(d['a'], 2)
      d['b'] = 4
      self.assertEqual(d['b'], 4)
      self.assertEqual(d['a'], 2)

    def test_insert_and_change(self):
      d = Dict()
      d['a'] = 2
      d['a'] = 3
      self.assertEqual(d['a'], 3)

    def test_contains_key(self):
      d = Dict()
      d['abc'] = 4
      d['ryansux'] = 42069
      self.assertTrue('ryansux' in d)
      self.assertFalse('theseunitestsaresoimmature' in d)
      self.assertTrue('abc' in d)
      # TODO support multiple data types
      # self.assertFalse('4' in d)
      self.assertFalse('a' in d)

    def test_keyerror_on_not_found(self):
      d = Dict()
      with self.assertRaises(KeyError):
        d['a']

    def test_length(self):
        d = Dict()
        self.assertEqual(len(d), 0)
        d['a'] = 1
        d['b'] = 2
        self.assertEqual(len(d), 2)
        d['b'] = 3
        self.assertEqual(len(d), 2)
        d['s'] = 12
        d['g'] = 1
        self.assertEqual(len(d), 4)

    def test_str(self):
      d = Dict()
      d['a'] = 2
      self.assertEqual(str(d), "{'a': 2}")
      d['abc'] = 3
      # order doesn't matter
      self.assertIn(str(d), ("{'a': 2, 'abc': 3}", "{'abc': 3, 'a', 2}"))

    def test_keys(self):
        d = Dict()
        d['abc'] = 50
        d['xyz'] = 100
        d['hello'] = 150
        self.assertNotIsInstance(d.keys(), list)
        keys = sorted(list(d.keys()))
        self.assertEqual(keys, ['abc', 'hello', 'xyz'])

    def test_values(self):
        d = Dict()
        d['abc'] = 50
        d['xyz'] = 100
        d['hello'] = 150
        self.assertNotIsInstance(d.values(), list)
        vals = sorted(list(d.values()))
        self.assertEqual(vals, [50, 100, 150])

    def test_items(self):
        d = Dict()
        d['abc'] = 50
        d['xyz'] = 100
        d['hello'] = 150
        self.assertNotIsInstance(d.items(), list)
        items = sorted(list(d.items()))
        self.assertIsInstance(items[0], tuple)
        self.assertEqual(items, [('abc', 50), ('hello', 150), ('xyz', 100)])

if __name__ == '__main__':
    unittest.main()
