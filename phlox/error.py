class PhloxException(Exception):
    """Base class for all Phlox exceptions."""

    pass


class PhloxHTTPError(PhloxException):
    """Exception raised for HTTP errors."""
