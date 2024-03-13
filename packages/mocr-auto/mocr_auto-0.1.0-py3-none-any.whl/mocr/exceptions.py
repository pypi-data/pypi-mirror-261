import asyncio


class MocrTimeoutError(asyncio.TimeoutError):
    """Timeout Error class."""
    pass


class BaseMocrException(Exception):
    """Base exception for mocr."""
    pass


class ElementHandleError(BaseMocrException):
    """ElementHandle related exception."""
    def __init__(
        self,
        message: str = 'Node is either not visible or not an HTMLElement.',
    ) -> None:
        super().__init__(message)


class NetworkError(BaseMocrException):
    """Network/Protocol related exception."""
    pass


class BrowserError(BaseMocrException):
    """Exception raised from browser."""
    pass


class PageError(BrowserError):
    """Page/Frame related exception."""
    pass


class FirefoxNotImplementedError(NotImplementedError):
    """Exception due to Firefox lacking CDP methods."""
    pass
