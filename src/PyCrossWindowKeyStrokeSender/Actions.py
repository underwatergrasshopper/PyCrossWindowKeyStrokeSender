from enum import Enum as _Enum
from typing import TypeAlias as _TypeAlias


class Key(_Enum):
    BREAK               = 0
    BACKSPACE           = 1
    TAB                 = 2 
    ENTER               = 3 
    SHIFT               = 4 
    CTRL                = 5 
    ALT                 = 6
    PAUSE               = 7
    CAPS_LOCK           = 8
    ESCAPE              = 9  
    SPACE               = 10      
    PAGE_UP             = 11
    PAGE_DOWN           = 12
    END                 = 13
    HOME                = 14
    ARROW_LEFT          = 15
    ARROW_UP            = 16
    ARROW_RIGHT         = 17
    ARROW_DOWN          = 18
    PRINT               = 19
    PRINT_SCREEN        = 20
    INSERT              = 21 
    DELETE              = 22  
    _0                  = 23
    _1                  = 24
    _2                  = 25
    _3                  = 26
    _4                  = 27
    _5                  = 28
    _6                  = 29
    _7                  = 30
    _8                  = 31
    _9                  = 32
    A                   = 33
    B                   = 34
    C                   = 35
    D                   = 36
    E                   = 37
    F                   = 38
    G                   = 39
    H                   = 40
    I                   = 41
    J                   = 42
    K                   = 43
    L                   = 44
    M                   = 45
    N                   = 46
    O                   = 47
    P                   = 48
    Q                   = 49
    R                   = 50
    S                   = 51
    T                   = 52
    U                   = 53
    V                   = 54
    W                   = 55
    X                   = 56
    Y                   = 57 
    Z                   = 58           
    NUMPAD_0            = 59
    NUMPAD_1            = 60
    NUMPAD_2            = 61
    NUMPAD_3            = 62
    NUMPAD_4            = 63
    NUMPAD_5            = 64
    NUMPAD_6            = 65
    NUMPAD_7            = 66
    NUMPAD_8            = 67
    NUMPAD_9            = 68
    NUMPAD_MULTIPLY     = 69
    NUMPAD_ADD          = 70
    NUMPAD_SEPARATOR    = 71
    NUMPAD_SUBTRACT     = 72
    NUMPAD_DECIMAL      = 73
    NUMPAD_DIVIDE       = 74
    F1                  = 75
    F2                  = 76
    F3                  = 77
    F4                  = 78
    F5                  = 79
    F6                  = 80
    F7                  = 81
    F8                  = 82
    F9                  = 83
    F10                 = 84
    F11                 = 85
    F12                 = 86
    F13                 = 87
    F14                 = 88
    F15                 = 89
    F16                 = 90
    F17                 = 91
    F18                 = 92
    F19                 = 93
    F20                 = 94
    F21                 = 95
    F22                 = 96
    F23                 = 97
    F24                 = 98
    NUM_LOCK            = 99
    SCROLL_LOCK         = 100
    LSHIFT              = 101
    RSHIFT              = 102
    LCTRL               = 103
    RCTRL               = 104
    LALT                = 105
    RALT                = 106

class KeyState:
    """
    Bitfields.
    """
    DOWN        = 0x01
    UP          = 0x02
    DOWN_AND_UP = DOWN | UP


Message : _TypeAlias = bytes | str | Key | tuple[Key, KeyState]


class Input:
    messages : list[Message]

    def __init__(self, messages : list[Message]):
        self.messages = messages


class Method(_Enum):
    """
    Message delivery method.
    """
    SEND    = 0
    POST    = 1
    INPUT   = 2

SEND    = Method.SEND
POST    = Method.POST
INPUT   = Method.INPUT


class Encoding(_Enum):
    """
    Message encoding type.
    """
    ASCII   = 0
    UTF16   = 1

ASCII   = Encoding.ASCII
UTF16   = Encoding.UTF16


_STR_TO_ENCODING_MAP = {
    "ascii" : ASCII,
    "utf-16" : UTF16,
}

def str_to_encoding(encoding : str) -> Encoding | None:
    return _STR_TO_ENCODING_MAP.get(encoding, None)


WaitTime : _TypeAlias = float | int
"""Wait time in seconds."""

Action : _TypeAlias = Message | WaitTime
