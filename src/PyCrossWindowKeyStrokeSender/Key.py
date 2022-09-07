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

from enum import Enum

__all__ = [
    "Key",
    "key_to_vk_code",
    # "vk_code_to_sideless", # Note: Left and right specific special keys are not supported.  Maybe in future.
    "is_special_key",
]

class Key(Enum):
    BACKSPACE           = 0
    TAB                 = 1
    ENTER               = 2 
    SHIFT               = 3 
    CTRL                = 4 
    ALT                 = 5 
    PAUSE               = 6
    CAPS_LOCK           = 7
    ESCAPE              = 8
    SPACE               = 9        
    PAGE_UP             = 10
    PAGE_DOWN           = 11
    END                 = 12
    HOME                = 13
    ARROW_LEFT          = 14
    ARROW_UP            = 15
    ARROW_RIGHT         = 16
    ARROW_DOWN          = 17
    PRINT               = 18
    PRINT_SCREEN        = 19
    INSERT              = 20
    DELETE              = 21   
    _0                  = 22
    _1                  = 23
    _2                  = 24
    _3                  = 25
    _4                  = 26
    _5                  = 27
    _6                  = 28
    _7                  = 29
    _8                  = 30
    _9                  = 31
    A                   = 32
    B                   = 33
    C                   = 34
    D                   = 35
    E                   = 36
    F                   = 37
    G                   = 38
    H                   = 39
    I                   = 40
    J                   = 41
    K                   = 42
    L                   = 43
    M                   = 44
    N                   = 45
    O                   = 46
    P                   = 47
    Q                   = 48
    R                   = 49
    S                   = 50
    T                   = 51
    U                   = 52
    V                   = 53
    W                   = 54
    X                   = 55
    Y                   = 56
    Z                   = 57            
    NUMPAD_0            = 58
    NUMPAD_1            = 59
    NUMPAD_2            = 60
    NUMPAD_3            = 61
    NUMPAD_4            = 62
    NUMPAD_5            = 63
    NUMPAD_6            = 64
    NUMPAD_7            = 65
    NUMPAD_8            = 66
    NUMPAD_9            = 67
    NUMPAD_MULTIPLY     = 68
    NUMPAD_ADD          = 69
    NUMPAD_SEPARATOR    = 70
    NUMPAD_SUBTRACT     = 71
    NUMPAD_DECIMAL      = 72
    NUMPAD_DIVIDE       = 73
    F1                  = 74
    F2                  = 75
    F3                  = 76
    F4                  = 77
    F5                  = 78
    F6                  = 79
    F7                  = 80
    F8                  = 81
    F9                  = 82
    F10                 = 83
    F11                 = 84
    F12                 = 85
    F13                 = 86
    F14                 = 87
    F15                 = 88
    F16                 = 89
    F17                 = 90
    F18                 = 91
    F19                 = 92
    F20                 = 93
    F21                 = 94
    F22                 = 95
    F23                 = 96
    F24                 = 97
    NUM_LOCK            = 98
    SCROLL_LOCK         = 99
    # Note: Left and right specific special keys are not supported.  Maybe in future.
    #LSHIFT              = 100
    #RSHIFT              = 101
    #LCTRL               = 102
    #RCTRL               = 103
    #LALT                = 104
    #RALT                = 105

def is_special_key(key):
    """
    key : Key
    return bool
    """
    return key in [
        Key.ALT, Key.SHIFT, Key.CTRL, 
        # Note: Left and right specific special keys are not supported.  Maybe in future.
        #Key.LALT, Key.LSHIFT, Key.LCTRL, 
        #Key.RALT, Key.RSHIFT, Key.RCTRL
    ]

def key_to_vk_code(key):
    """
    key : Key
    return int      WinApi Virtual Key Code.
    """
    return {
        Key.BACKSPACE           : VK_BACK,             
        Key.TAB                 : VK_TAB,              
        Key.ENTER               : VK_RETURN,     
        Key.SHIFT               : VK_SHIFT,            
        Key.CTRL                : VK_CONTROL,          
        Key.ALT                 : VK_MENU,                
        Key.PAUSE               : VK_PAUSE,            
        Key.CAPS_LOCK           : VK_CAPITAL,          
        Key.ESCAPE              : VK_ESCAPE,           
        Key.SPACE               : VK_SPACE,            
        Key.PAGE_UP             : VK_PRIOR,            
        Key.PAGE_DOWN           : VK_NEXT,             
        Key.END                 : VK_END,              
        Key.HOME                : VK_HOME,             
        Key.ARROW_LEFT          : VK_LEFT,             
        Key.ARROW_UP            : VK_UP,               
        Key.ARROW_RIGHT         : VK_RIGHT,            
        Key.ARROW_DOWN          : VK_DOWN,             
        Key.PRINT               : VK_PRINT,            
        Key.PRINT_SCREEN        : VK_SNAPSHOT,         
        Key.INSERT              : VK_INSERT,           
        Key.DELETE              : VK_DELETE,           
        Key._0                  : ord('0'),                   
        Key._1                  : ord('1'),                   
        Key._2                  : ord('2'),                   
        Key._3                  : ord('3'),                   
        Key._4                  : ord('4'),                  
        Key._5                  : ord('5'),                   
        Key._6                  : ord('6'),                   
        Key._7                  : ord('7'),                   
        Key._8                  : ord('8'),                   
        Key._9                  : ord('9'),                   
        Key.A                   : ord('A'),                   
        Key.B                   : ord('B'),                   
        Key.C                   : ord('C'),                   
        Key.D                   : ord('D'),                   
        Key.E                   : ord('E'),                   
        Key.F                   : ord('F'),                   
        Key.G                   : ord('G'),                   
        Key.H                   : ord('H'),                   
        Key.I                   : ord('I'),                   
        Key.J                   : ord('J'),                   
        Key.K                   : ord('K'),                   
        Key.L                   : ord('L'),                   
        Key.M                   : ord('M'),                   
        Key.N                   : ord('N'),                   
        Key.O                   : ord('O'),                   
        Key.P                   : ord('P'),                   
        Key.Q                   : ord('Q'),                   
        Key.R                   : ord('R'),                   
        Key.S                   : ord('S'),                   
        Key.T                   : ord('T'),                   
        Key.U                   : ord('U'),                   
        Key.V                   : ord('V'),                   
        Key.W                   : ord('W'),                   
        Key.X                   : ord('X'),                   
        Key.Y                   : ord('Y'),                   
        Key.Z                   : ord('Z'),                   
        Key.NUMPAD_0            : VK_NUMPAD0,          
        Key.NUMPAD_1            : VK_NUMPAD1,          
        Key.NUMPAD_2            : VK_NUMPAD2,          
        Key.NUMPAD_3            : VK_NUMPAD3,          
        Key.NUMPAD_4            : VK_NUMPAD4,          
        Key.NUMPAD_5            : VK_NUMPAD5,          
        Key.NUMPAD_6            : VK_NUMPAD6,          
        Key.NUMPAD_7            : VK_NUMPAD7,          
        Key.NUMPAD_8            : VK_NUMPAD8,          
        Key.NUMPAD_9            : VK_NUMPAD9,          
        Key.NUMPAD_MULTIPLY     : VK_MULTIPLY,         
        Key.NUMPAD_ADD          : VK_ADD,              
        Key.NUMPAD_SEPARATOR    : VK_SEPARATOR,        
        Key.NUMPAD_SUBTRACT     : VK_SUBTRACT,         
        Key.NUMPAD_DECIMAL      : VK_DECIMAL,          
        Key.NUMPAD_DIVIDE       : VK_DIVIDE,           
        Key.F1                  : VK_F1,               
        Key.F2                  : VK_F2,               
        Key.F3                  : VK_F3,               
        Key.F4                  : VK_F4,               
        Key.F5                  : VK_F5,               
        Key.F6                  : VK_F6,               
        Key.F7                  : VK_F7,               
        Key.F8                  : VK_F8,               
        Key.F9                  : VK_F9,               
        Key.F10                 : VK_F10,              
        Key.F11                 : VK_F11,              
        Key.F12                 : VK_F12,              
        Key.F13                 : VK_F13,              
        Key.F14                 : VK_F14,              
        Key.F15                 : VK_F15,              
        Key.F16                 : VK_F16,              
        Key.F17                 : VK_F17,              
        Key.F18                 : VK_F18,              
        Key.F19                 : VK_F19,              
        Key.F20                 : VK_F20,              
        Key.F21                 : VK_F21,              
        Key.F22                 : VK_F22,              
        Key.F23                 : VK_F23,              
        Key.F24                 : VK_F24,              
        Key.NUM_LOCK            : VK_NUMLOCK,          
        Key.SCROLL_LOCK         : VK_SCROLL,   
        # Note: Left and right specific special keys are not supported. Maybe in future.
        #Key.LSHIFT              : VK_LSHIFT,           
        #Key.RSHIFT              : VK_RSHIFT,           
        #Key.LCTRL               : VK_LCONTROL,         
        #Key.RCTRL               : VK_RCONTROL,         
        #Key.LALT                : VK_LMENU,            
        #Key.RALT                : VK_RMENU,   
    }.get(key, None)  

# Note: Left and right specific special keys are not supported.  Maybe in future.
#def vk_code_to_sideless(vk_code):
#    """
#    key : Key
#    return int      WinApi Virtual Key Code.
#    """
#    return {                      
#        VK_LSHIFT   : VK_SHIFT,           
#        VK_RSHIFT   : VK_SHIFT,           
#        VK_LCONTROL : VK_CONTROL,         
#        VK_RCONTROL : VK_CONTROL,         
#        VK_LMENU    : VK_MENU,            
#        VK_RMENU    : VK_MENU,   
#    }.get(vk_code, vk_code)  