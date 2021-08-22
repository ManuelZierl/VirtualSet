class PySomeException(Exception):
    pass


class MustReturnBool(PySomeException):
    pass


class ExpectException(PySomeException):
    pass


class InvalidArgument(PySomeException):
    pass


class InvalidFunction(InvalidArgument):
    pass


class SameOutsideExpect(PySomeException):
    pass
