class Dict:
    def __init__(self):
        self._elements = []

    def __setitem__(self, key, value):
        for kv in self._elements:
            if kv[0] == key:
                kv[1] = value
                break
        else:
            self._elements.append([key, value])

    def __getitem__(self, key):
        for k, v in self._elements:
            if k == key:
                return v
        raise KeyError(str(key))

    def __contains__(self, key):
        for kv in self._elements:
            if kv[0] == key:
                return True
        else:
            return False

    def __len__(self):
        return len(self._elements)

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
      self.assertFalse(4 in d)
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
#
#    def test_str(self):
#      d = Dict()
#      d['a'] = 2 
#      self.assertEqual(str(d), "{'a': 2}")
#      d['abc'] = 3 
#      # order doesn't matter
#      self.assertIn(str(d), ("{'a': 2, 'abc': 3}", "{'abc': 3, 'a', 2}"))


if __name__ == '__main__':
    unittest.main()
