class VirtualSetException(Exception):
    pass


class MustReturnBool(VirtualSetException):
    pass


class MustBeArgOrSome(VirtualSetException):
    pass


class InvalidSomeFunction(VirtualSetException):
    pass
