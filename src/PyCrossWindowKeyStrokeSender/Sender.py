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
from enum               import Enum

__all__ = [
    "ModeID",
    "Wait",
    "Delay",
    "send_to_window",
]

"""
Any action can be one of the following types.

<Action>
    bytes
    str
    ModeID
    Input
    Wait
    Delay
"""

class ModeID(Enum):
    """
    Message delivery mode.
    """
    SEND = 0
    POST = 1


class Wait:
    def __init__(self, wait_time):
        """
        wait_time : float       Time to wait in seconds.
        """
        self.wait_time = wait_time

class Delay:
    def __init__(self, delay_time):
        """
        delay_time : float      Delay time after sending each message in seconds.
        """
        self.delay_time = delay_time

def send_to_window(target_window_name, *actions):
    """
    Sends keyboard messages to target window.
    target_window_name  : bytes or str      Name of window to which messages will be sent. 
    actions             : <Action>, ...     Actions, which are containing messages to send and informations how to send messages. Each action is defined by it's type:
                                                bytes   - Text message in ASCII encoding format.
                                                          Note: Uses internally WinApi functions with suffix A. 
                                                str     - Text message in UTF-16 encoding format.
                                                          Note: Uses internally WinApi functions with suffix W. 
                                                
    raise                                   Any Exception which inherits from SendToWindowFail. For more details check Exceptions submodule module.
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
    target_window   : HWND
    actions         : tuple(<Action>)
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

        deliver_messages(target_window, actions)
    
def focus_and_send_messages(target_window, foreground_window, actions):
    """
    target_window       : HWND
    foreground_window   : HWND
    actions             : tuple(<Action>)
    """
    if IsIconic(target_window):
       ShowWindow(target_window, SW_RESTORE)
    
    is_success = SetForegroundWindow(target_window)
    
    if not is_success:
        raise SetTargetWindowAsForegroundFail(True)

    focus_window = GetFocus()
    
    debug_print("focus_window: ", focus_window)
    
    if not focus_window: 
        GetWindowWithKeyboardFocusFail(True)

    try:
        deliver_messages(focus_window, actions)
    except SendToWindowFail:
        try_set_foreground_window(foreground_window)
        raise

    is_success = try_set_foreground_window(foreground_window)

    if not is_success:
        raise SetCallerWindowToForegroundFail(True)
    
    SetFocus(foreground_window)

def try_set_foreground_window(window, max_num_of_tries = 10, interval = 0.01):
    num_of_tries_left = max_num_of_tries

    while num_of_tries_left:
        if SetForegroundWindow(window):
            debug_print("max_num_of_tries left: ", num_of_tries_left)
            return True

        time.sleep(interval)
        num_of_tries_left -= 1

    debug_print("max_num_of_tries left: ", num_of_tries_left)
    return False


def deliver_messages(focus_window, actions):
    """
    focus_window        : HWND
    actions             : tuple(<Action>)
    """
    debug_print("actions: ", *actions)

    mode_id     = ModeID.SEND
    delay       = 0.0           # in seconds

    for action in actions:
        if isinstance(action, bytes):
            debug_print("process ascii message")
            deliver_text(focus_window, action, mode_id)

        elif isinstance(action, str):
            debug_print("process utf-16 message")
            deliver_text(focus_window, action, mode_id)

        elif isinstance(action, ModeID):
            debug_print("set mode_id: ", action.name)
            mode_id = action

        elif isinstance(action, Wait):
            debug_print("wait: ", action.wait_time)
            time.sleep(action.wait_time)

        elif isinstance(action, Delay):
            debug_print("set delay: ", action.delay_time)
            delay = action.delay_time

        else:
            raise UndefinedActionFail(type(action).__name__)

        time.sleep(delay)


def deliver_text(window, text, mode_id):
    debug_print("mode_id: ", mode_id.name)

    if isinstance(text, bytes):
        if mode_id == ModeID.SEND:
            for sign in text:
                SendMessageA(window, WM_CHAR, sign, 0)

        elif mode_id == ModeID.POST:
            for sign in text:
                if not PostMessageA(window, WM_CHAR, sign, 0):
                    raise DelivarMessageFail("\"%s\"" % to_utf16(text))
        else:
            raise UndefinedMessageDeliveryModeFail(mode_id)
    else: # as utf-16
        text = to_utf16(text)

        if mode_id == ModeID.SEND:
            for sign in text:
                SendMessageW(window, WM_CHAR, ord(sign), 0)

        elif mode_id == ModeID.POST:
            for sign in text:
                if not PostMessageW(window, WM_CHAR, ord(sign), 0):
                    raise DelivarMessageFail("\"%s\"" % text)
        else:
            raise UndefinedMessageDeliveryModeFail(mode_id)

