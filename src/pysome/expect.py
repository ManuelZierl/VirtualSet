from typing import Any
from pysome import SameState, ExpectException, SomeStr, Some


class expect:
    def __init__(self, *data: Any):
        self.data = data

    def to_be(self, other):
        for da in self.data:
            if does(da).not_equal(other):
                raise ExpectException(self.format_error_msg())
        return self

    def not_to_be(self, other):
        for da in self.data:
            if does(da).equal(other):
                raise ExpectException()
        return self

    @staticmethod
    def format_error_msg():
        out = "\n"
        for ue in Some.unequals:
            out += f"  - {ue}\n"
        return out


class does:
    def __init__(self, data):
        self.data = data
        Some.unequals = []

    def equal(self, other):
        SameState._start()  # noqa
        result = other == self.data
        SameState._end()  # noqa
        return result

    def not_equal(self, other):
        SameState._start()  # noqa
        Some.unequals = []
        result = other != self.data
        SameState._end()  # noqa
        return result


