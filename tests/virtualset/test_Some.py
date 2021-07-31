import unittest

from virtualset import VSet, Some
from virtualset.Exceptions import *


class SomeTests(unittest.TestCase):
    def test_some_basics(self):
        s1 = Some()
        self.assertEqual(s1.types, None)

        s2 = Some(int)
        self.assertEqual(s2.types, (int, ))

        s3 = Some(int, str)
        self.assertEqual(s3.types, (int, str))

    def test_some_strict(self):
        class Foo:
            pass

        class Foo2(Foo):
            pass

        f1 = Foo()
        f2 = Foo2()

        self.assertTrue(Some(Foo) == f1)
        self.assertTrue(Some(Foo2) != f1)
        self.assertTrue(Some(Foo) == f2)
        self.assertTrue(Some(Foo2) == f2)

        self.assertTrue(Some(Foo, strict=True) == f1)
        self.assertTrue(Some(Foo2, strict=True) != f1)
        self.assertTrue(Some(Foo, strict=True) != f2)
        self.assertTrue(Some(Foo2, strict=True) == f2)

    def test_some_func(self):
        # validation
        with self.assertRaises(InvalidValidatorFunction):
            _ = Some(func=12)

        def func_with_two_args(arg1, arg2):
            pass

        with self.assertRaises(InvalidValidatorFunction):
            _ = Some(func=func_with_two_args)

        def invalid_validator_func(arg):
            return "False"
        s1 = Some(func=invalid_validator_func)
        with self.assertRaises(MustReturnBool):
            x = s1 == ""

        def is_png(file: str):
            return file.endswith(".png")

        self.assertTrue(Some(str, func=is_png) == "image.png")
        self.assertTrue(Some(str, func=is_png) == "cat.png")
        self.assertTrue(Some(func=is_png) == "dog.png")
        self.assertFalse(Some(str, func=is_png) == "image.jpg")
        self.assertFalse(Some(int, func=is_png) == "image.png")

    def test_correct_args(self):
        _ = Some(int, str, dict)
        _ = Some(int, Some())

        with self.assertRaises(MustBeTypeOrSome):
            _ = Some(1)

        with self.assertRaises(MustBeTypeOrSome):
            _ = Some(str, 2)

        with self.assertRaises(MustBeTypeOrSome):
            _ = Some(Some(str), "x")
