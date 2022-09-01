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
from .Commons import *

__all__ = [
    "ExcpetionBase",
    "ExceptionCanNotFindTargetWindow",
]

class ExcpetionBase(Exception):
    def __init__(self, message):
        super().__init__("CWKSS Error: %s" % message)

class ExceptionCanNotFindTargetWindow(ExcpetionBase):
    def __init__(self, window_name):
        """
        window_name : str or bytes
        """
        self.window_name = to_utf16(window_name)
        super().__init__("Can not find target window with name \"%s\"." % self.window_name)
