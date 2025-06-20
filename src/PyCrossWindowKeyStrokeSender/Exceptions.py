
from ._Private import Types as _t


class Fail(Exception):
    _error_code : int

    def __init__(self, message : str, is_last_winapi_error : bool = False):
        self._error_code  = 0    

        full_message = f"CWKSS Error: {message}"
        if is_last_winapi_error:
            self._error_code = _t.GetLastError()
            full_message += f" (windows error code: {self._error_code})"

        super().__init__(full_message)

### General Fails ###

class ArgumentFail(Fail):
    pass


class SetupFail(Fail):
    pass


class DeliverMessageFail(Fail):
    pass


class CleanupFail(Fail):
    pass

### Specific Fails ###

class FindTargetWindowFail(Fail):
    def __init__(self, window_name : str, is_last_winapi_error = False):
        super().__init__(f"Can not find target window with name \"{window_name}\".", is_last_winapi_error)


        