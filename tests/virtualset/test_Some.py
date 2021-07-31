import unittest

from virtualset import VSet, Some


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
        # todo: ...
        pass
