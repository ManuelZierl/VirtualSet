import unittest

from pysome import expect, Same, SomeDict, Some, SameOutsideExpect

class SameTests(unittest.TestCase):
    def test_basics(self):
        expect("abcs").to_be(Same())

        expect({
            "a": 12,
            "b": 12,
            "c": 14
        }).to_be({
            "a": Same(),
            "b": Same(),
            "c": 14
        }).to_be(
            SomeDict()
        ).not_to_be({
            "a": Some(int),
            "b": Some(str),
            "c": Some(int)
        }).not_to_be({
            "a": Same(),
            "b": Some(int),
            "c": Same()
        })

        expect({
            "a": 12,
            "b": 12
        }).not_to_be({
            "a": Same(str),
            "b": Same(str)
        })

        expect({
            "a": 12,
            "b": 13
        }).not_to_be({
            "a": Same(),
            "b": Same()
        }).to_be({
            "a": Same(name="s1"),
            "b": Same(name="s2")
        })

        s = Same()
        with self.assertRaises(SameOutsideExpect):
            assert s == 3
        with self.assertRaises(SameOutsideExpect):
            assert 3 == s
