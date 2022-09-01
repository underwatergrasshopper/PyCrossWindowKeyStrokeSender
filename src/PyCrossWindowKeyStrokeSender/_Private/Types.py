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
from ctypes             import *
from ctypes.wintypes    import *

################################################################################
# WinApi Macros
################################################################################
def LOWORD(l):
    return l & 0xffff
    
def HIWORD(l):
    return (l >> 16) & 0xffff

################################################################################
# WinApi Constatns
################################################################################
NULL = None

################################################################################
# WinApi Functions
################################################################################
GetLastError            = windll.kernel32.GetLastError 
GetLastError.restype    = DWORD 

FindWindowA             = windll.user32.FindWindowA 
FindWindowA.argtypes    = [LPCSTR, LPCSTR]
FindWindowA.restype     = HWND 

FindWindowW             = windll.user32.FindWindowW 
FindWindowW.argtypes    = [LPCWSTR, LPCWSTR]
FindWindowW.restype     = HWND