import unittest

from virtualset import VSet, Some
from virtualset.Exceptions import *
from virtualset.Some import has_len, is_in


class SomeTests(unittest.TestCase):
    def test_init(self):
        s1 = Some()
        self.assertEqual(s1.types, None)

        s2 = Some(int)
        self.assertEqual(s2.types, [int])

        s3 = Some(int, str)
        self.assertEqual(s3.types, [int, str])

        def func(_):
            return True
        s3 = Some(int, str, func)
        self.assertEqual(s3.types, [int, str, func])

        with self.assertRaises(InvalidArgument):
            _ = Some(int, "a")

        with self.assertRaises(InvalidFunction):
            def func(_, __):
                return True
            _ = Some(int, func)

        class Foo:
            pass

        s4 = Some(Foo)
        self.assertEqual(s4.types, [Foo])

    def test_some_func(self):
        def invalid_validator_func(arg):
            return "False"

        s1 = Some(invalid_validator_func)
        with self.assertRaises(MustReturnBool):
            _ = s1 == ""

        def is_png(file: str):
            if not isinstance(file, str):
                return False
            return file.endswith(".png")

        self.assertTrue(Some(is_png) == "image.png")
        self.assertTrue(Some(is_png) == "cat.png")
        self.assertTrue(Some(is_png) == "dog.png")
        self.assertFalse(Some(is_png) == 12)
        self.assertFalse(Some(is_png) == "image.jpg")
        self.assertTrue(Some(is_png, int) == "image.png")
        self.assertFalse(Some(is_png, int) == 1)

    def test_correct_args(self):
        _ = Some(int, str, dict)
        _ = Some(int, Some())

        with self.assertRaises(InvalidArgument):
            _ = Some(1)

        with self.assertRaises(InvalidArgument):
            _ = Some(str, 2)

        with self.assertRaises(InvalidArgument):
            _ = Some(Some(str), "x")


class TestHasLen(unittest.TestCase):
    def test_basics(self):
        self.assertTrue(has_len(3) == [1, 2, 3])
        self.assertTrue(has_len(2) == [1, "a"])
        self.assertTrue(has_len(2) == {"a": 1, "b": 2})
        self.assertTrue(has_len(4) == {1, 2, 3, 4})
        self.assertTrue(has_len(0) == [])

        self.assertFalse(has_len(2) == [1, "a", str])
        self.assertFalse(has_len(2) == [])
        self.assertFalse(has_len(5) == {"a": 1, "b": 2})

        self.assertFalse(has_len(5) == 1) # 1 has no __len__

    def test_min_max(self):
        self.assertTrue(has_len(min_length=2) != [])
        self.assertTrue(has_len(min_length=2) != [1])
        self.assertTrue(has_len(min_length=2) == [1, 2])
        self.assertTrue(has_len(min_length=2) == [1, 2, 3])

        self.assertTrue(has_len(max_length=2) == [])
        self.assertTrue(has_len(max_length=2) == [1])
        self.assertTrue(has_len(max_length=2) == [1, 2])
        self.assertTrue(has_len(max_length=2) != [1, 2, 3])

        self.assertTrue(has_len(min_length=1, max_length=2) != [])
        self.assertTrue(has_len(min_length=1, max_length=2) == [1])
        self.assertTrue(has_len(min_length=1, max_length=2) == [1, 2])
        self.assertTrue(has_len(min_length=1, max_length=2) != [1, 2, 3])


class TestIsIn(unittest.TestCase):
    def test_basics(self):
        self.assertTrue(is_in([1, 2, 3]) == 1)
        self.assertTrue(is_in([1, 2, 3]) != 4)
        self.assertTrue(is_in({"a", "b"}) == "a")
        self.assertTrue(is_in({"a", "b"}) != "ab")
        self.assertTrue(is_in("abcdefg") == "ab")
        self.assertTrue(is_in("abcdefg") == "b")
        self.assertTrue(is_in("abcdefg") != "ac")

        with self.assertRaises(InvalidArgument):
            _ = is_in(42)