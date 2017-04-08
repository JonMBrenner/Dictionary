import unittest

class TestDict(unittest.TestCase):
    pass
#    def test_insert_and_lookup(self):
#      d = Dict()
#      d['a'] = 2
#      self.assertEqual(d['a'], 2)
#      d['b'] = 4
#      self.assertEqual(d['b'], 4)
#      self.assertEqual(d['a'], 2)
#
#    def test_insert_and_change(self):
#      d = Dict()
#      d['a'] = 2
#      d['a'] = 3
#      self.assertEqual(d['a'], 3)
#
#    def test_contains_key(self):
#      d = Dict()
#      d['abc'] = 4
#      d['ryansux'] = 42069
#      self.assertTrue('ryansux' in d)
#      self.assertFalse('theseunitestsaresoimmature' in d)
#      self.assertTrue('abc' in d)
#      self.assertFalse(4 in d)
#      self.assertFalse('a' in d)
#
#    def test_keyerror_on_not_found(self):
#      d = Dict()
#      with self.assertRaises(KeyError):
#        d['a']
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
