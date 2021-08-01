from typing import Any


# todo: better explanation why assert failed
class expect:
    def __init__(self, data: Any):
        self.data = data

    def to_be(self, other):  # todo: possible to raise exception here for production code?
        print(other, self.data)
        assert other == self.data

    def not_to_be(self, other):
        assert not other == self.data
