class DomainException(Exception):
    """Base class for all domain exceptions."""
    pass

class UserAlreadyExistsException(DomainException):
    pass

class UserNotFoundException(DomainException):
    pass