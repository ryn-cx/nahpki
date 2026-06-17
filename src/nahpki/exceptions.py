"""Exceptions."""


class NahpkiError(Exception):
    """Base exception for nahpki library."""


class HTTPError(NahpkiError):
    """Raised when HTTP request fails with unexpected status code."""
