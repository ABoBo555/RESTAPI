class InvalidPageError(Exception):
    """
    Raised when the requested page exceeds
    the available number of pages.
    """
    pass