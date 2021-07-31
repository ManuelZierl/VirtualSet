import unittest

from virtualset import VSet, Some


class MainTests(unittest.TestCase):
    def test_some_basic_stuff(self):
        self.assertTrue({"a": 1, "b": "xyz"} in VSet({"a": Some(int), "b": Some(str)}))
        self.assertTrue({"a": 1, "b": "xyz"} not in VSet({"a": Some(str), "b": Some(str)}))
