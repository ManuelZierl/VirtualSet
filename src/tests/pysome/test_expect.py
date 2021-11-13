import unittest

from pysome import *


class TestExpect(unittest.TestCase):
    def test_expect_basics(self):
        response = {"message": "OK", "randomInt": 42, "auth_id": "ölsusmnrzv8dhbw2j93"}
        expect(response).to_be({
            "message": "OK",
            "randomInt": Some(int),
            "auth_id": Some(str)
        })
        expect(response).not_to_be({
            "message": "OK",
            "randomInt": Some(str),
            "auth_id": Some(int)
        })
        response = {
            "menu": {
                "header": "SVG Viewer",
                "items": [
                    "day1",
                    2,
                    "day3",
                    "day4",
                    5,
                    "day6",
                    7,
                    "day8",
                    "day9",
                    "day10",
                ]
            }
        }

        expect(response).to_be({
            "menu": {
                "header": "SVG Viewer",
                "items": SomeList(Some(str, int))
            }
        })
        response["menu"]["items"].append(9.3)
        with self.assertRaises(ExpectException):
            expect(response).to_be({
                "menu": {
                    "header": "SVG Viewer",
                    "items": SomeList(Some(str, int))
                }
            })

        response = {
            "menu": {
                "header": "SVG Viewer",
                "items": [
                    {"id": "Open"},
                    {"id": "OpenNew", "label": "Open New"},
                    None,
                    {"id": "ZoomIn", "label": "Zoom In"},
                    {"id": "ZoomOut", "label": "Zoom Out"},
                    {"id": "OriginalView", "label": "Original View"},
                    None,
                    {"id": "Quality"},
                    {"id": "Pause"},
                    {"id": "Mute"},
                    None,
                    {"id": "Find", "label": "Find..."},
                    {"id": "FindAgain", "label": "Find Again"},
                    {"id": "Copy"},
                    {"id": "CopyAgain", "label": "Copy Again"},
                    {"id": "CopySVG", "label": "Copy SVG"},
                    {"id": "ViewSVG", "label": "View SVG"},
                    {"id": "ViewSource", "label": "View Source"},
                    {"id": "SaveAs", "label": "Save As"},
                    None,
                    {"id": "Help"},
                    {"id": "About", "label": "About Adobe CVG Viewer..."}
                ]
            }
        }
        expect(response).to_be(
            {
                "menu": {
                    "header": "SVG Viewer",
                    "items": Some(list)
                }
            }
        )
        expect(response).to_be({"menu": Some(dict)})

    def test_partial_dict(self):
        response = {
            "menu": {
                "tags": [
                    {"id": 1, "z-index": 12},
                    {"id": 2, "name": "ax7"},
                    {"id": 5, "name": "ax7", "z-index": 12},
                    {"id": 2, "alias": "iivz"},
                ]
            }
        }

        expect(response).to_be({
            "menu": {
                "tags": SomeList()
            }
        })

        expect(response).to_be({
            "menu": {
                "tags": SomeList(Some(dict))
            }
        })
        expect(response).to_be({
            "menu": {
                "tags": SomeList(SomeDict({
                    "id": Some(int)
                }))
            }
        })

        response = {
            "menu": {
                "tags": [
                    {"id": 1, "z-index": 12},
                    {"id": 2, "name": "ax7"},
                    {"id": 5, "name": "ax7", "z-index": 12},
                    {"id": "2", "alias": "iivz"},
                ]
            }
        }

        expect(response).not_to_be({
            "menu": {
                "tags": SomeList(SomeDict({
                    "id": Some(int)
                }))
            }
        })

        expect(response).to_be({
            "menu": {
                "tags": SomeList(SomeDict({
                    "id": Some(int, str)
                }))
            }
        })

    def test_partial_dict_optional(self):
        response = {
            "menu": {
                "tags": [
                    {"id": 1, "z-index": 12},
                    {"id": 2, "name": "ax7"},
                    {"id": 5, "name": "ax7", "z-index": 12},
                    {"id": 2, "alias": "iivz"},
                ]
            }
        }

        expect(response).to_be({
            "menu": {
                "tags": SomeList(SomeDict({
                    "id": Some(int),
                    "name": SomeOrNone(str)
                }))
            }
        })

        expect(response).not_to_be({
            "menu": {
                "tags": SomeList(SomeDict({
                    "id": Some(int),
                    "name": SomeOrNone(int)
                }))
            }
        })

    def test_chainable(self):
        def not_5(x):
            return x != 5
        expect(12).to_be(Some(int)).to_be(Some(not_5))

        expect(5).to_be(Some(int))

        with self.assertRaises(ExpectException):
            expect(5).to_be(Some(int)).to_be(Some(not_5))

        class Foo:
            pass

        class Bar(Foo):
            pass

        foo = Foo()
        bar = Bar()

        expect(foo).to_be(Some(Foo)).not_to_be(Some(Bar))
        expect(bar).to_be(Some(Bar)).to_be(Some(Foo)).to_be(Some(Bar)).not_to_be(Some(int))

    def test_multiple(self):
        expect({"a": 12}, {"a": 13}).to_be({"a": Some(int)}).not_to_be({"a": Some(str)})
        with self.assertRaises(ExpectException):
            expect({"a": 12}, {"a": "x"}).not_to_be({"a": Some(int)})

    def test_error_msg(self):
        # todo: ...
        pass

    def test_template(self):
        template = SomeList({"id": Some(int), "name": Some(str)})
        expect({
            "users": [
                {"id": 1, "name": "anna"},
                {"id": 2, "name": "bert"},
                {"id": 3, "name": "claus"},
                {"id": 4, "name": "diana"},
            ],
            "others": {
                "counter": 3,
                "list": [
                    {"id": 12, "name": "alice"},
                    {"id": 13, "name": "bob"},
                    {"id": 14, "name": "clair"},
                ]
            },
            "special": [{"id": 99, "name": "Mr. X"}],
        }).to_be({
            "users": template,
            "others": {
                "counter": Some(int),
                "list": template
            },
            "special": template

        })


class TestDoes(unittest.TestCase):
    def test_basics(self):
        # todo:
        pass
