################################################################################
# MIT License
# 
# Copyright (c) 2022 underwatergrasshopper
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
################################################################################
from ._Private.Types    import *
from .Commons           import *
from .Exceptions        import *

__all__ = [
    "send_to_window",
]

is_debug = False

# b"..."                    -> ascii
# "...", u"...", U"..."     -> utf-16

def send_to_window(target_window_name):
    """
    target_window_name : bytes or str       Name of window where messages will be sent. 
    raise                                   ExceptionCanNotFindTargetWindow
    """
    target_window = NULL

    if isinstance(target_window_name, bytes):
        if is_debug:
            print("target_window_name ascii: ", to_utf16(target_window_name))

        target_window = FindWindowA(NULL, target_window_name)
        if is_debug:
            print("target_window handle: ", target_window)
    else:
        target_window_name = to_utf16(target_window_name)
        if is_debug:
            print("target_window_name utf-16: ", target_window_name)

        target_window = FindWindowW(NULL, target_window_name)
        if is_debug:
            print("target_window handle: ", target_window)

    if not target_window:
        raise ExceptionCanNotFindTargetWindow(target_window_name)

    send_to_window_by_handle(target_window)


def send_to_window_by_handle(target_window):
    """
    target_window : HWND
    """
    pass
