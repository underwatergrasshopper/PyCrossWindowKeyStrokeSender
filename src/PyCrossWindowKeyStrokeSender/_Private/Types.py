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
NULL                    = None

FALSE                   = 0
TRUE                    = 1

LONG_PTR                = LPARAM
LRESULT                 = LONG_PTR

ULONG_PTR               = WPARAM

SW_RESTORE              = 9

WM_CHAR                 = 0x0102
WM_KEYDOWN              = 0x0100
WM_KEYUP                = 0x0101

### SendInput ###
INPUT_MOUSE             = 0
INPUT_KEYBOARD          = 1
INPUT_HARDWARE          = 2

KEYEVENTF_EXTENDEDKEY   = 0x0001
KEYEVENTF_KEYUP         = 0x0002
KEYEVENTF_UNICODE       = 0x0004
KEYEVENTF_SCANCODE      = 0x0008

################################################################################
# WinApi Structures
################################################################################

### SendInput ###
class MOUSEINPUT(Structure):
    _fields_ = [
        ("dx",          LONG),
        ("dy",          LONG),
        ("mouseData",   DWORD),
        ("dwFlags",     DWORD),
        ("time",        DWORD),
        ("dwExtraInfo", ULONG_PTR),
    ]


class KEYBDINPUT(Structure):
    _fields_ = [
        ("wVk",         WORD),
        ("wScan",       WORD),
        ("dwFlags",     DWORD),
        ("time",        DWORD),
        ("dwExtraInfo", ULONG_PTR),
    ]

class HARDWAREINPUT(Structure):
    _fields_ = [
        ("uMsg",        DWORD),
        ("wParamL",     WORD),
        ("wParamH",     WORD),
    ]

class _INPUT_DUMMYUNIONNAME(Union):
    _fields_ = [
        ("mi",          MOUSEINPUT),
        ("ki",          KEYBDINPUT),
        ("hi",          HARDWAREINPUT),
    ]

class INPUT(Structure):
    _anonymous_ = ("DUMMYUNIONNAME",)
    _fields_ = [
        ("type",            DWORD),
        ("DUMMYUNIONNAME",  _INPUT_DUMMYUNIONNAME),
    ]

LPINPUT = POINTER(INPUT)

################################################################################
# WinApi Functions
################################################################################
GetLastError                        = windll.kernel32.GetLastError 
GetLastError.restype                = DWORD 

FindWindowA                         = windll.user32.FindWindowA 
FindWindowA.argtypes                = [LPCSTR, LPCSTR]
FindWindowA.restype                 = HWND 

FindWindowW                         = windll.user32.FindWindowW 
FindWindowW.argtypes                = [LPCWSTR, LPCWSTR]
FindWindowW.restype                 = HWND

IsIconic                            = windll.user32.IsIconic 
IsIconic.argtypes                   = [HWND]
IsIconic.restype                    = BOOL  

ShowWindow                          = windll.user32.ShowWindow 
ShowWindow.argtypes                 = [HWND, c_int]
ShowWindow.restype                  = BOOL  

GetForegroundWindow                 = windll.user32.GetForegroundWindow 
GetForegroundWindow.restype         = HWND

GetWindowThreadProcessId            = windll.user32.GetWindowThreadProcessId 
GetWindowThreadProcessId.argtypes   = [HWND, LPDWORD]
GetWindowThreadProcessId.restype    = DWORD 


GetCurrentThreadId                  = windll.kernel32.GetCurrentThreadId 
GetCurrentThreadId.restype          = DWORD 

AttachThreadInput                   = windll.user32.AttachThreadInput 
AttachThreadInput.argtypes          = [DWORD, DWORD, BOOL]
AttachThreadInput.restype           = BOOL 

SetForegroundWindow                 = windll.user32.SetForegroundWindow  
SetForegroundWindow .argtypes       = [HWND]
SetForegroundWindow .restype        = BOOL 

GetFocus                            = windll.user32.GetFocus  
GetFocus.restype                    = HWND  

SetFocus                            = windll.user32.SetFocus  
SetFocus .argtypes                  = [HWND]
SetFocus.restype                    = HWND  

PostMessageA                        = windll.user32.PostMessageA 
PostMessageA.argtypes               = [HWND, UINT, WPARAM, LPARAM]
PostMessageA.restype                = BOOL 

PostMessageW                        = windll.user32.PostMessageW 
PostMessageW.argtypes               = [HWND, UINT, WPARAM, LPARAM]
PostMessageW.restype                = BOOL 

SendMessageA                        = windll.user32.SendMessageA 
SendMessageA.argtypes               = [HWND, UINT, WPARAM, LPARAM]
SendMessageA.restype                = LRESULT

SendMessageW                        = windll.user32.SendMessageW 
SendMessageW.argtypes               = [HWND, UINT, WPARAM, LPARAM]
SendMessageW.restype                = LRESULT 

SendInput                           = windll.user32.SendInput 
SendInput.argtypes                  = [UINT, LPINPUT, c_int]
SendInput.restype                   = UINT  

