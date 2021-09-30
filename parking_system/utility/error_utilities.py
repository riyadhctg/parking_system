class InvalidInputError(Exception):
    """
    Raised when the input provided is invalid
    """

    pass


class MissingInputParameterError(Exception):
    """
    Raised when the input is missing expected parameter(s)
    """

    pass


class InvalidAllotmentError(Exception):
    """
    Raised when there is an issue with slot allotment related input
    """

    pass
