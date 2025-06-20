import inspect as _inspect


_is_debug = False


def enable_debug():
    global _is_debug
    _is_debug = True


def disable_debug():
    global _is_debug
    _is_debug = False


def get_is_debug() -> bool:
    return _is_debug


def debug_print(*params):
    """
    params 
        Same arguments as for print function.
    """
    if _is_debug:
        caller_function_name = _inspect.currentframe().f_back.f_code.co_name
        print("[" + caller_function_name + "]", *params)

