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

VK_BACK                 = 0x08   
VK_TAB                  = 0x09
VK_RETURN               = 0x0D  
VK_SHIFT                = 0x10
VK_CONTROL              = 0x11
VK_MENU                 = 0x12
VK_PAUSE                = 0x13
VK_CAPITAL              = 0x14 
VK_ESCAPE               = 0x1B
VK_SPACE                = 0x20   
VK_PRIOR                = 0x21   
VK_NEXT                 = 0x22   
VK_END                  = 0x23   
VK_HOME                 = 0x24   
VK_LEFT                 = 0x25   
VK_UP                   = 0x26   
VK_RIGHT                = 0x27   
VK_DOWN                 = 0x28   
VK_PRINT                = 0x2A   
VK_SNAPSHOT             = 0x2C   
VK_INSERT               = 0x2D   
VK_DELETE               = 0x2E   
VK_NUMPAD0              = 0x60   
VK_NUMPAD1              = 0x61   
VK_NUMPAD2              = 0x62   
VK_NUMPAD3              = 0x63   
VK_NUMPAD4              = 0x64   
VK_NUMPAD5              = 0x65   
VK_NUMPAD6              = 0x66   
VK_NUMPAD7              = 0x67   
VK_NUMPAD8              = 0x68   
VK_NUMPAD9              = 0x69   
VK_MULTIPLY             = 0x6A   
VK_ADD                  = 0x6B   
VK_SEPARATOR            = 0x6C   
VK_SUBTRACT             = 0x6D   
VK_DECIMAL              = 0x6E   
VK_DIVIDE               = 0x6F   
VK_F1                   = 0x70  
VK_F2                   = 0x71  
VK_F3                   = 0x72  
VK_F4                   = 0x73  
VK_F5                   = 0x74  
VK_F6                   = 0x75  
VK_F7                   = 0x76  
VK_F8                   = 0x77  
VK_F9                   = 0x78  
VK_F10                  = 0x79  
VK_F11                  = 0x7A  
VK_F12                  = 0x7B  
VK_F13                  = 0x7C  
VK_F14                  = 0x7D  
VK_F15                  = 0x7E  
VK_F16                  = 0x7F  
VK_F17                  = 0x80  
VK_F18                  = 0x81  
VK_F19                  = 0x82  
VK_F20                  = 0x83  
VK_F21                  = 0x84  
VK_F22                  = 0x85  
VK_F23                  = 0x86  
VK_F24                  = 0x87  
VK_NUMLOCK              = 0x90   
VK_SCROLL               = 0x91   
VK_LSHIFT               = 0xA0   
VK_RSHIFT               = 0xA1   
VK_LCONTROL             = 0xA2   
VK_RCONTROL             = 0xA3   
VK_LMENU                = 0xA4   
VK_RMENU                = 0xA5   

### SendInput ###
INPUT_MOUSE             = 0
INPUT_KEYBOARD          = 1
INPUT_HARDWARE          = 2

KEYEVENTF_EXTENDEDKEY   = 0x0001
KEYEVENTF_KEYUP         = 0x0002
KEYEVENTF_UNICODE       = 0x0004
KEYEVENTF_SCANCODE      = 0x0008

MAPVK_VK_TO_VSC         = 0

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

MapVirtualKeyA                      = windll.user32.MapVirtualKeyA 
MapVirtualKeyA.argtypes             = [UINT, UINT]
MapVirtualKeyA.restype              = UINT  
