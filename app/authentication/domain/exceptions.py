class DomainException(Exception):
    pass

class UserAlreadyExistsException(DomainException):
    pass

class UserNotFoundException(DomainException):
    pass

class InvalidCredentialsException(DomainException):
    pass

class InvalidTokenException(DomainException):
    pass