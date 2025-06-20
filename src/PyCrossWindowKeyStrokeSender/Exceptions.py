from .Commons           import *
from ._Private.Types    import *

from enum               import Enum

__all__ = [
    "Fail",

    "ArgumentFail",
    "SetupFail",
    "DeliverMessageFail",
    "CleanupFail",

    "FindTargetWindowFail",
]

class Fail(Exception):
    # error_code : int

    def __init__(self, message, is_last_winapi_error = False):
        """
        message                 : str
        is_last_winapi_error    : bool
        """
        self.error_code  = 0    

        full_message = "CWKSS Error: %s" % message
        if is_last_winapi_error:
            self.error_code = GetLastError()
            full_message += " (windows error code: %d)" % self.error_code
        super().__init__(full_message)

### General Fails ###

class ArgumentFail(Fail):
    def __init__(self, message, is_last_winapi_error = False):
        """
        message                 : str
        is_last_winapi_error    : bool
        """
        super().__init__(message, is_last_winapi_error)

class SetupFail(Fail):
    def __init__(self, message, is_last_winapi_error = False):
        """
        message                 : str
        is_last_winapi_error    : bool
        """
        super().__init__(message, is_last_winapi_error)

class DeliverMessageFail(Fail):
    def __init__(self, message, is_last_winapi_error = False):
        """
        message                 : str
        is_last_winapi_error    : bool
        """
        super().__init__(message, is_last_winapi_error)

class CleanupFail(Fail):
    def __init__(self, message, is_last_winapi_error = False):
        """
        message                 : str
        is_last_winapi_error    : bool
        """
        super().__init__(message, is_last_winapi_error)

### Specific Fails ###

class FindTargetWindowFail(Fail):
    def __init__(self, window_name, is_last_winapi_error = False):
        """
        is_last_winapi_error    : bool
        """
        super().__init__("Can not find target window with name \"%s\"." % window_name, is_last_winapi_error)


        