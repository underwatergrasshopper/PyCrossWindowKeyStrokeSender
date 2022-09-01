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

import time

__all__ = [
    "send_to_window",
]

def send_to_window(target_window_name, actions):
    """
    target_window_name : bytes or str       Name of window where messages will be sent. 
                                            As str, when target window support wide characters (utf-16).
                                            As bytes, otherwise.
    raise                                   ExceptionCanNotFindTargetWindow
    """
    target_window = NULL

    # b"..."                    -> ascii    (...A)
    # "...", u"...", U"..."     -> utf-16   (...W)

    if isinstance(target_window_name, bytes):
        debug_print("target_window_name ascii: ", to_utf16(target_window_name))

        target_window = FindWindowA(NULL, target_window_name)

        debug_print("target_window handle: ", target_window)
    else:
        target_window_name = to_utf16(target_window_name)

        debug_print("target_window_name utf-16: ", target_window_name)

        target_window = FindWindowW(NULL, target_window_name)

        debug_print("target_window handle: ", target_window)

    if not target_window:
        raise FindTargetWindowFail(target_window_name, True)

    send_to_window_by_handle(target_window, actions)

def send_to_window_by_handle(target_window, actions):
    """
    target_window : HWND
    """
    foreground_window = GetForegroundWindow();

    debug_print("foreground_window handle: ", foreground_window)

    if not foreground_window:
        raise FindForegroundWindowFail(True)

    target_window_thread_id = GetWindowThreadProcessId(target_window, NULL);

    debug_print("target_window_thread_id handle: ", target_window_thread_id)

    if not target_window_thread_id:
       return ReceiveTargetWindowThreadIdFail()

    caller_window_thread_id = GetCurrentThreadId()

    debug_print("caller_window_thread_id handle: ", caller_window_thread_id)

    if not caller_window_thread_id:
       return ReceiveCallerWindowThreadIdFail()

    if target_window_thread_id and (target_window_thread_id is not caller_window_thread_id):
        is_success = AttachThreadInput(caller_window_thread_id, target_window_thread_id, TRUE)
        
        if not is_success:
            return AttachCallerToTargetFail(True)

        try:
            focus_and_send_messages(target_window, foreground_window, actions)
        except SendToWindowFail:
            AttachThreadInput(caller_window_thread_id, target_window_thread_id, FALSE)
            raise

        is_success = AttachThreadInput(caller_window_thread_id, target_window_thread_id, FALSE)

        if not is_success:
            return DetachCallerFromTargetFail(True)
    else:
        # When the target window is the caller window.

        send_messages(target_window, actions)
    
def focus_and_send_messages(target_window, foreground_window, actions):
    if IsIconic(target_window):
       ShowWindow(target_window, SW_RESTORE)
    
    is_success = SetForegroundWindow(target_window)
    
    if not is_success:
        raise SetTargetWindowAsForegroundFail(True)

    focus_window = GetFocus()
    
    debug_print("focus_window: ", focus_window)
    
    if not focus_window: 
        GetWindowWithKeyboardFocusFail(True)

    send_messages(focus_window, actions)

    is_success = SetForegroundWindow(foreground_window)

    max_num_of_tries = 10
    while not is_success and max_num_of_tries:
        time.sleep(0.01)
        is_success = SetForegroundWindow(foreground_window)
        max_num_of_tries -= 1

    debug_print("max_num_of_tries left: ", max_num_of_tries)

    if not is_success:
        raise SetCallerWindowToForegroundFail(True)
    
    SetFocus(foreground_window)


def send_messages(focus_window, actions):
    # TODO: Implement!!!
    pass



