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
from .Commons           import *
from ._Private.Types    import *

from enum               import Enum

__all__ = [
    "Fail",
    "SendToWindowFail",
    "SendMessageFail",
    "FindTargetWindowFail",
    "FindForegroundWindowFail",
    "ReceiveTargetWindowThreadIdFail",
    "ReceiveCallerWindowThreadIdFail",
    "AttachCallerToTargetFail",
    "SetTargetWindowAsForegroundFail",
    "GetWindowWithKeyboardFocusFail",
    "SetCallerWindowToForegroundFail",
    "DetachCallerFromTargetFail",
]

class Fail(Exception):
    error_code = 0          # int

    def __init__(self, message, is_last_error = False):
        """
        message         : str
        is_last_error   : bool
        """
        full_message = "CWKSS Error: %s" % message
        if is_last_error:
            self.error_code = GetLastError()
            full_message += " (windows error code: %d)" % self.error_code
        super().__init__(full_message)

### SendToWindow Fails ###

class SendToWindowFail(Fail):
    def __init__(self, message, is_last_error = False):
        """
        message         : str
        is_last_error   : bool
        """
        super().__init__(message, is_last_error)

class SendMessageFail(SendToWindowFail):
    def __init__(self, is_last_error = False):
        """
        is_last_error   : bool
        """
        super().__init__("Can not send message.", is_last_error)

class FindTargetWindowFail(SendToWindowFail):
    def __init__(self, window_name, is_last_error = False):
        """
        is_last_error   : bool
        """
        super().__init__("Can not find target window with name \"%s\"." % window_name, is_last_error)

class FindForegroundWindowFail(SendToWindowFail):
    def __init__(self, is_last_error = False):
        """
        is_last_error   : bool
        """
        super().__init__("Can not find foreground window.", is_last_error)

class ReceiveTargetWindowThreadIdFail(SendToWindowFail):
    def __init__(self, is_last_error = False):
        """
        is_last_error   : bool
        """
        super().__init__("Can not receive target window thread id.", is_last_error)

class ReceiveCallerWindowThreadIdFail(SendToWindowFail):
    def __init__(self, is_last_error = False):
        """
        is_last_error   : bool
        """
        super().__init__("Can not receive caller window thread id.", is_last_error)

class AttachCallerToTargetFail(SendToWindowFail):
    def __init__(self, is_last_error = False):
        """
        is_last_error   : bool
        """
        super().__init__("Can not attach caller window thread to target window thread.", is_last_error)

class SetTargetWindowAsForegroundFail(SendToWindowFail):
    def __init__(self, is_last_error = False):
        """
        is_last_error   : bool
        """
        super().__init__("Can not set target window as foreground window.", is_last_error)

class GetWindowWithKeyboardFocusFail(SendToWindowFail):
    def __init__(self, is_last_error = False):
        """
        is_last_error   : bool
        """
        super().__init__("Can not get handle of window with keyboard focus.", is_last_error)

class SetCallerWindowToForegroundFail(SendToWindowFail):
    def __init__(self, is_last_error = False):
        """
        is_last_error   : bool
        """
        super().__init__("Can not set caller window to be foreground window.", is_last_error)

class DetachCallerFromTargetFail(SendToWindowFail):
    def __init__(self, is_last_error = False):
        """
        is_last_error   : bool
        """
        super().__init__("Can not detach caller window thread from target window thread.", is_last_error)




