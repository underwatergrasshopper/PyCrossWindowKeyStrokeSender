import ctypes           as _c
import ctypes.wintypes  as _w

################################################################################
# WinApi Macros
################################################################################

def LOWORD(l):
    return l & 0xffff
    

def HIWORD(l):
    return (l >> 16) & 0xffff

################################################################################
# WinApi Constants
################################################################################

NULL                    = None

FALSE                   = 0
TRUE                    = 1

LONG_PTR                = _w.LPARAM
LRESULT                 = LONG_PTR

ULONG_PTR               = _w.WPARAM
HWND                    = _w.HWND

SW_RESTORE              = 9

WM_CHAR                 = 0x0102
WM_KEYDOWN              = 0x0100
WM_KEYUP                = 0x0101

VK_CANCEL               = 0x03
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
class MOUSEINPUT(_c.Structure):
    _fields_ = [
        ("dx",          _w.LONG),
        ("dy",          _w.LONG),
        ("mouseData",   _w.DWORD),
        ("dwFlags",     _w.DWORD),
        ("time",        _w.DWORD),
        ("dwExtraInfo", ULONG_PTR),
    ]


class KEYBDINPUT(_c.Structure):
    _fields_ = [
        ("wVk",         _w.WORD),
        ("wScan",       _w.WORD),
        ("dwFlags",     _w.DWORD),
        ("time",        _w.DWORD),
        ("dwExtraInfo", ULONG_PTR),
    ]


class HARDWAREINPUT(_c.Structure):
    _fields_ = [
        ("uMsg",        _w.DWORD),
        ("wParamL",     _w.WORD),
        ("wParamH",     _w.WORD),
    ]


class _INPUT_DUMMYUNIONNAME(_c.Union):
    _fields_ = [
        ("mi",          MOUSEINPUT),
        ("ki",          KEYBDINPUT),
        ("hi",          HARDWAREINPUT),
    ]


class INPUT(_c.Structure):
    _anonymous_ = ("DUMMYUNIONNAME",)
    _fields_ = [
        ("type",            _w.DWORD),
        ("DUMMYUNIONNAME",  _INPUT_DUMMYUNIONNAME),
    ]


LPINPUT = _c.POINTER(INPUT)

################################################################################
# WinApi Functions
################################################################################

_kernel32   = _c.windll.kernel32
_user32     = _c.windll.user32


GetLastError                = _c.WINFUNCTYPE(_w.DWORD)(
    ("GetLastError", _kernel32),
    ()
)

FindWindowA                 = _c.WINFUNCTYPE(_w.HWND, _w.LPCSTR, _w.LPCSTR)(
    ("FindWindowA", _user32),
    ((1, "lpClassName"), (1, "lpWindowName"))
)

FindWindowW                 = _c.WINFUNCTYPE(_w.HWND, _w.LPCWSTR, _w.LPCWSTR)(
    ("FindWindowW", _user32),
    ((1, "lpClassName"), (1, "lpWindowName"))
)

IsIconic                    = _c.WINFUNCTYPE(_w.BOOL, _w.HWND)(
    ("IsIconic", _user32),
    ((1, "hWnd"),)
)

ShowWindow                  = _c.WINFUNCTYPE(_w.BOOL, _w.HWND, _c.c_int)(
    ("ShowWindow", _user32),
    ((1, "hWnd"), (1, "nCmdShow"))
)

GetForegroundWindow         = _c.WINFUNCTYPE(_w.HWND)(
    ("GetForegroundWindow", _user32),
    ()
)


GetWindowThreadProcessId    = _c.WINFUNCTYPE(_w.DWORD, _w.HWND, _w.LPDWORD)(
    ("GetWindowThreadProcessId", _user32),
    ((1, "hWnd"), (1, "lpdwProcessId"))
)

GetCurrentThreadId          = _c.WINFUNCTYPE(_w.HWND)(
    ("GetCurrentThreadId", _kernel32),
    ()
)

AttachThreadInput           = _c.WINFUNCTYPE(_w.BOOL, _w.DWORD, _w.DWORD, _w.BOOL)(
    ("AttachThreadInput", _user32),
    ((1, "idAttach"), (1, "idAttachTo"), (1, "fAttach"))
)

SetForegroundWindow         = _c.WINFUNCTYPE(_w.BOOL, _w.HWND)(
    ("SetForegroundWindow", _user32),
    ((1, "hWnd"),)
)

GetFocus                    = _c.WINFUNCTYPE(_w.HWND)(
    ("GetFocus", _user32),
    ()
)

SetFocus                    = _c.WINFUNCTYPE(_w.HWND, _w.HWND)(
    ("SetFocus", _user32),
    ((1, "hWnd"),)
)

PostMessageA                = _c.WINFUNCTYPE(_w.BOOL, _w.HWND, _w.UINT, _w.WPARAM, _w.LPARAM)(
    ("PostMessageA", _user32),
    ((1, "hWnd"), (1, "Msg"), (1, "wParam"), (1, "lParam"))
)

PostMessageW                = _c.WINFUNCTYPE(_w.BOOL, _w.HWND, _w.UINT, _w.WPARAM, _w.LPARAM)(
    ("PostMessageW", _user32),
    ((1, "hWnd"), (1, "Msg"), (1, "wParam"), (1, "lParam"))
)

SendMessageA                = _c.WINFUNCTYPE(LRESULT, _w.HWND, _w.UINT, _w.WPARAM, _w.LPARAM)(
    ("SendMessageA", _user32),
    ((1, "hWnd"), (1, "Msg"), (1, "wParam"), (1, "lParam"))
)

SendMessageW                = _c.WINFUNCTYPE(LRESULT, _w.HWND, _w.UINT, _w.WPARAM, _w.LPARAM)(
    ("SendMessageW", _user32),
    ((1, "hWnd"), (1, "Msg"), (1, "wParam"), (1, "lParam"))
)

SendInput                   = _c.WINFUNCTYPE(_w.UINT, _w.UINT, LPINPUT, _c.c_int)(
    ("SendInput", _user32),
    ((1, "cInputs"), (1, "pInputs"), (1, "cbSize"))
)

MapVirtualKeyA              = _c.WINFUNCTYPE(_w.UINT, _w.UINT, _w.UINT)(
    ("MapVirtualKeyA", _user32),
    ((1, "uCode"), (1, "uMapType"))
)

MapVirtualKeyW              = _c.WINFUNCTYPE(_w.UINT, _w.UINT, _w.UINT)(
    ("MapVirtualKeyW", _user32),
    ((1, "uCode"), (1, "uMapType"))
)
