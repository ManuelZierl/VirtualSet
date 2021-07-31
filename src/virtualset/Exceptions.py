class VirtualSetException(Exception):
    pass


class MustReturnBool(VirtualSetException):
    pass


class MustBeTypeOrSome(VirtualSetException):
    pass


class InvalidValidatorFunction(VirtualSetException):
    pass
