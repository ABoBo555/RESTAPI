class EmployeeError(Exception):
    """
    Base exception for all employee-related errors.
    """

    pass


class EmployeeNotFoundError(EmployeeError):
    """
    Raised when the requested employee does not exist.
    """

    pass


class EmployeeCreationError(EmployeeError):
    """
    Raised when an employee cannot be created.
    """

    pass