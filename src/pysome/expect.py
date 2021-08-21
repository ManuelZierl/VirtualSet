from typing import Any
from pysome import SameState, ExpectException, SomeStr, Some


class expect:
    def __init__(self, *data: Any):
        self.data = data

    def to_be(self, other):
        for da in self.data:
            if does(da).not_equal(other):
                raise ExpectException(Some.last_unequal)  # todo: message
        return self

    def not_to_be(self, other):
        for da in self.data:
            if does(da).equal(other):
                raise ExpectException(Some.last_unequal)  # todo: message
        return self


class does:
    def __init__(self, data):
        self.data = data

    def equal(self, other):
        SameState._start()  # noqa
        result = other == self.data
        SameState._end()  # noqa
        return result

    def not_equal(self, other):
        SameState._start()  # noqa
        result = other != self.data
        SameState._end()  # noqa
        return result


