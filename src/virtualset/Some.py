import inspect
from typing import Union, Callable, Any

from virtualset.Exceptions import MustReturnBool, InvalidSomeFunction, MustBeArgOrSome


class Some:
    def __init__(self, *args: Union[type, "Some"], strict: bool = False, func: Callable = None):
        if func is not None:
            if not callable(func) or len(inspect.signature(func).parameters) != 1:
                raise InvalidSomeFunction("todo")  # todo: test
        self.func = func
        self.strict = strict

        if args:
            for arg in args:
                if not isinstance(arg, type) and not isinstance(arg, Some):
                    raise MustBeArgOrSome(f"all args provided to Some must be of type <type> or <Some> but {arg} is "
                                          f"of type {type(arg)}")  # todo: test
            self.types = args
        else:
            self.types = None

    def __eq__(self, other: Any):
        if self.func is not None:
            eq = self.func(other)
            if not isinstance(eq, bool):  # todo: test
                raise MustReturnBool(f"Some.func must return bool (True or False) but returned {eq} of type {type(eq)} "
                                     "instead")
            return eq
        if self.types is None:
            return True

        if self.strict:
            return self._eq_strict(other)
        else:
            return self._eq(other)

    def _eq_strict(self, other: Any):
        # todo: test
        for t in self.types:
            if isinstance(other, Some):
                return other in Some
            if type(other) == t:
                return True
        return False

    def _eq(self, other: Any):
        # todo: test
        for t in self.types:
            if isinstance(other, Some):
                return other in Some
            if isinstance(other, t):
                return True
        return False

# TODO: SOMES
# TODO: SomeStrict()
# TODO: SomeIterator(len=, first=, last=, nth=,)
# TODO: SomeList()
# TODO: SomeTuple()
# TODO: SomeDict()
# TODO: SomeCallable()
# TODO: SomeIn()
# TODO: SomeEmail()
# TODO: NotSome()
# TODO: SomeStr(regex=, pattern=Hal_o W__t)
# TODO: SomeNumber(min=, max=) -> Some(int, float, ...?)

# TODO: HELPER (Actually also SOMES) that do not fit with the SOME NAME
# TODO: has_len()
# TODO: is_in()
# TODO: has_attribute()
# TODO: is_callable()
