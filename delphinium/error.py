class PhloxException(Exception):
    """Base class for all Delphinium exceptions."""

    pass


class PhloxHTTPError(PhloxException):
    """Exception raised for HTTP errors."""
