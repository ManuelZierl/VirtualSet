from typing import Any

# TODO: better explanation why assert failed
# TODO: needs to reset State of same
# todo: can we make to_be chainabel expect(...).to_be().to_be() test it but also reset the state ...?
from pysome import SameState

class expect:
    def __init__(self, data: Any):
        self.data = data

    def to_be(self, other):
        SameState._allow_same_usage = True
        SameState._state = {}
        print("is_all", SameState._allow_same_usage)
        print(other)
        assert other == self.data
        SameState._state = {}
        SameState._allow_same_usage = False
        return self

    def not_to_be(self, other):
        SameState._allow_same_usage = True
        SameState._state = {}
        assert not other == self.data
        SameState._state = {}
        SameState._allow_same_usage = False
        return self