import inspect

__all__ = [
    "enable_debug",
    "disable_debug",
    "debug_print",
]

is_debug = False

def enable_debug():
    global is_debug
    is_debug = True

def disable_debug():
    global is_debug
    is_debug = False

def get_is_debug():
    """
    return bool
    """
    return is_debug

def debug_print(*params):
    """
    params : arg, ...       Same arguments as for print function.
    """
    if is_debug:
        caller_function_name = inspect.currentframe().f_back.f_code.co_name
        print("[" + caller_function_name + "]", *params)

