import inspect
from collections import Iterable
from typing import Union, Callable, Any

from pysome.Exceptions import *


class Some:
    """
    Some() validates agains given arguments if any matches it equals
    if no argument is given Some always equals

    examples:
    >>> Some() == ...
    True
    >>> Some(int) == 1
    True
    >>> Some(str, int) == 21
    True
    >>> Some(int) == "abc"
    False
    >>> Some(int) == None
    False
    """
    def __init__(self, *args: Union[type, Callable, "Some"]):
        self.types = []
        if args:
            for arg in args:
                if isinstance(arg, type):
                    self.types.append(arg)
                    continue
                elif isinstance(arg, Some):
                    self.types.append(arg)
                    continue
                elif callable(arg):
                    if len(inspect.signature(arg).parameters) != 1:
                        raise InvalidFunction("function must accept exactly one parameter")
                    self.types.append(arg)
                    continue
                raise InvalidArgument(f"Some accepts only objects of the types <type>, <Some> or a function but {arg} "
                                      f"is of type {type(arg)}")
        else:
            self.types = None

    def __eq__(self, other: Any):
        if self.types is None:
            return True
        # todo: what of other is also a Some is this something we want
        for t in self.types:
            if isinstance(t, type):
                if isinstance(other, t):
                    return True
            elif isinstance(t, Some):
                if t == other:
                    return True
            elif callable(t):
                eq = t(other)
                if not isinstance(eq, bool):
                    raise MustReturnBool(
                        f"validator function must return bool (True or False) but returned {eq} of type {type(eq)} "
                        "instead")
                if eq:
                    return True
        return False


class AllOf(Some):
    """
    AllOf validates against all given arguments an only equals if all match.

    examples:
    >>> AllOf(int) == 12
    True
    >>> AllOf(int, str) == 12
    False
    >>> AllOf(object, str) == "abc"
    True
    """
    def __init__(self, *args: Union[type, Callable, "Some"]):
        def validate_all(other):
            return all(Some(arg) == other for arg in args)
        super().__init__(validate_all)


# Todo SomeOrNone()
# works exactly like Some but is also true for SomeOrNone() == None
class SomeOrNone(Some):
    # todo: testcas
    """
    Works exactly like Some() but also equals None

    examples:
    >>> SomeOrNone() == ...
    True
    >>> SomeOrNone(int) == 1
    True
    >>> SomeOrNone(str, int) == 21
    True
    >>> SomeOrNone(int) == "abc"
    False
    >>> SomeOrNone(int) == None
    True
    """
    def __init__(self, *args: Union[type, Callable, "Some"]):
        def is_none(x):
            return x is None
        if args:
            super().__init__(*args, is_none)
        else:
            super().__init__()


class SomeIterable(Some):
    """
    SomeIterable equals all iterable objects that are equal to its given arguemnts

    example:
    >>> SomeIterable() == [1, 2, 3]
    True
    >>> SomeIterable() == 12
    False
    >>> SomeIterable(int) == (1, 2, 4)
    True
    >>> SomeIterable(str) == (1, 3, 4)
    False
    """
    # todo: first=None, last=None, nth=None,
    def __init__(self, *args: Union[type, Callable, "Some"], length=None, is_type=Iterable):
        def some_iterable_validator(others):
            if not isinstance(others, is_type):
                return False
            if length is not None and len(others) != length:
                return False
            some = Some(*args)

            return all(some == x for x in others)
        super().__init__(some_iterable_validator)


class SomeList(SomeIterable):
    """
    SomeList is just like SomeIterator but only True if other is of type 'list'

    examples
    >>> SomeList() == []
    True
    >>> SomeList() == [1, 2]
    True
    >>> SomeList() == (1, 2)
    False
    """
    # todo: test
    # todo: first=None, last=None, nth=None,
    def __init__(self, *args: Union[type, Callable, "Some"], length=None):
        super().__init__(*args, length=length, is_type=list)


# TODO: SomeTuple(SomeIterable)


class SomeDict(Some):
    """
    SomeDict is equal to any dict

    examples:
    >>> SomeDict() == {}
    True
    >>> SomeDict() == {"a": {"a1": 1, "a2": 2}, "b": 3}
    True
    >>> SomeDict() == 12
    False
    >>> SomeDict(a=Some(dict)) == {"a": {"a1": 1, "a2": 2}, "b": 3}
    True
    >>> SomeDict({"a": Some(dict)}) == {"a": {"a1": 1, "a2": 2}, "b": 3}
    True
    >>> SomeDict({"a": Some(int)}) == {"a": {"a1": 1, "a2": 2}, "b": 3}
    False
    """

    def __init__(self, partial_dict: dict = None, **kwargs):
        if partial_dict is None:
            partial_dict = {}
        if not isinstance(partial_dict, dict):
            raise InvalidArgument("SomeDict except either dict or **kwargs")
        partial_dict = dict(partial_dict, **kwargs)

        def some_dict_validator(other):
            if not isinstance(other, dict):
                return False
            for key, value in partial_dict.items():
                if not other.get(key, None) == value:
                    return False
            return True

        super().__init__(some_dict_validator)


# TODO: SomeSet(SomeIterable)

# TODO: class SomeStrict(Some):

# TODO: SomeCallable() -> is_callable

# TODO: SomeIn() -> is_in()


class SomeWithLen(Some):
    """
    SomeWithLen quals every object that has same length

    examples:
    >>> SomeWithLen(2) == [1, 2]
    True
    >>> SomeWithLen(0) == []
    True
    >>> SomeWithLen(2) == (1, )
    False
    """

    def __init__(self, length=None, min_length=None, max_length=None):
        def len_validator(other):
            if not hasattr(other, '__len__'):
                return False
            if length:
                if not len(other) == length:
                    return False
            if min_length:
                if len(other) < min_length:
                    return False
            if max_length:
                if len(other) > max_length:
                    return False
            return True

        super().__init__(len_validator)


# TODO: NotSome() -> is_not()


# TODO: SomeStr(regex=, pattern=Hal_o W__t, endswith=, startswith=)


# TODO: SomeNumber(min=, max=) -> Some(int, float, long...?)


# alias names
has_len = SomeWithLen


class is_in(Some):
    """
    is true if other is in the given container

    examples:
    >>> is_in({"a", "b"}) == "a"
    True
    >>> is_in(["a", "b"]) == "b"
    True
    >>> is_in({"a", "b"}) == "c"
    False
    """

    def __init__(self, container):
        if not hasattr(container, '__contains__'):
            raise InvalidArgument("is_in container doesn't implement __contains__")

        def is_in_validator(other):
            return other in container

        super().__init__(is_in_validator)


class has_attr(Some):
    """
    true if other has any of given attr(s)

    examples:
    >>> has_attr("split") == "a"
    True
    >>> has_attr("split") == 1
    False
    >>> has_attr("imag", "split") == "a"
    True
    >>> has_attr("imag", "real") == "a"
    False
    """
    def __init__(self, *args: Union[str]):
        def has_attr_validator(other):
            for attr in args:
                if hasattr(other, attr):
                    return True
            return False

        super().__init__(has_attr_validator)


class has_all_attr(Some):
    """
    true if other has all of given attr(s)

    examples:
    >>> has_all_attr("split") == "a"
    True
    >>> has_all_attr("split") == 1
    False
    >>> has_all_attr("split", "imag") == "a"
    False
    >>> has_all_attr("real", "imag") == 1
    True
    """

    def __init__(self, *args: Union[str]):
        def has_any_attr_validator(other):
            return all(hasattr(other, attr) for attr in args)

        super().__init__(has_any_attr_validator)

# TODO: is_callable()