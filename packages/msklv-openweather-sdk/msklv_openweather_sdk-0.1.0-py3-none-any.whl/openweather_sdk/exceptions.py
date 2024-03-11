class ClientAlreadyExistsError(ValueError):
    def __init__(self):
        super().__init__("Client already exists")


class ClientDoesntExistError(ValueError):
    def __init__(self):
        super().__init__("Client doesn't exist")


class BadResponseError(ValueError):
    def __init__(self, code, message):
        super().__init__(f"Code: {code}, message: {message}")


class InvalidLocationError(IndexError):
    def __init__(self):
        super().__init__("Invalid location")


class AttributeValidationError(ValueError):
    def __init__(self, name, values):
        super().__init__(f"{name} must be one of {', '.join(values)}")


class UnexpectedError(Exception):
    def __init__(self, message):
        super().__init__(f"Unexpected error! Error: {message}")
