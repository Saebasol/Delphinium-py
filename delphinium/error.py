class DelphiniumException(Exception):
    """Base class for all Delphinium exceptions."""

    pass


class DelphiniumHTTPError(DelphiniumException):
    """Exception raised for HTTP errors."""
