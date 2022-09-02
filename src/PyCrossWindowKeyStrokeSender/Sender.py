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
from turtle import down, up
from ._Private.Types    import *
from .Commons           import *
from .Exceptions        import *

import time
from enum               import Enum

__all__ = [
    "ModeID",
    "Wait",
    "Delay",
    "Key",
    "KeyAction",
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

# used for int bitfield 
class KeyAction:
    DOWN        = 0x01
    UP          = 0x02
    DOWN_AND_UP = DOWN | UP

class Key(Enum):
    BACKSPACE           = 0
    TAB                 = 1
    ENTER               = 2 
    SHIFT               = 3 
    CONTROL             = 4 
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
    # TODO: implement
    # LEFT_SHIFT          = 100
    # RIGHT_SHIFT         = 101
    # LEFT_CONTROL        = 102
    # RIGHT_CONTROL       = 103
    # LEFT_ALT            = 104
    # RIGHT_ALT           = 105

def key_to_vk_code(key):
    """
    key : Key
    return int
    """
    return {
        Key.BACKSPACE           : VK_BACK,             
        Key.TAB                 : VK_TAB,              
        Key.ENTER               : VK_RETURN,     
        Key.SHIFT               : VK_SHIFT,            
        Key.CONTROL             : VK_CONTROL,          
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
        # TODO: implement support: LEFT... = ..., RIGHT -> (l_param &= (1 << 24))
        # Key.LEFT_SHIFT          : VK_LSHIFT,           
        # Key.RIGHT_SHIFT         : VK_RSHIFT,           
        # Key.LEFT_CONTROL        : VK_LCONTROL,         
        # Key.RIGHT_CONTROL       : VK_RCONTROL,         
        # Key.LEFT_ALT            : VK_LMENU,            
        # Key.RIGHT_ALT           : VK_RMENU,   
    }.get(key, None)      

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

        elif isinstance(action, Key):
            debug_print("process key message: ", action.name)
            deliver_key(focus_window, action, KeyAction.DOWN_AND_UP, mode_id)
             
        elif isinstance(action, tuple) and len(action) > 1 and isinstance(action[0], Key) and isinstance(action[1], int):
            debug_print("process key message: ", action[0].name)
            deliver_key(focus_window, action[0], action[1], mode_id)

        else:
            raise UndefinedActionFail(type(action).__name__)

        time.sleep(delay)


def deliver_text(window, text, mode_id):
    """
    window      : HWND
    text        : str or bytes
    mode_id     : ModeID
    """
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

def deliver_key(window, key, key_action, mode_id):
    """
    window      : HWND
    key         : Key
    key_action  : int           Bifield of KeyAction bits.
    mode_id     : ModeID
    """
    debug_print("mode_id: ", mode_id.name)

    vk_code       = key_to_vk_code(key)

    scan_code     = MapVirtualKeyA(vk_code, MAPVK_VK_TO_VSC);

    l_param_down  = 0x00000001 | (scan_code  << 16);
    l_param_up    = 0xC0000001 | (scan_code  << 16);

    if mode_id == ModeID.SEND:
        if key_action & KeyAction.DOWN:
            debug_print("DOWN")
            SendMessageA(window, WM_KEYDOWN, vk_code, l_param_down)

        if key_action & KeyAction.UP:
            debug_print("UP")
            SendMessageA(window, WM_KEYUP, vk_code, l_param_up)

    elif mode_id == ModeID.POST:
        if key_action & KeyAction.DOWN:
            debug_print("DOWN")
            if not PostMessageA(window, WM_KEYDOWN, vk_code, l_param_down):
                raise DelivarMessageFail("%s DOWN" % key_to_vk_code(key))

        if key_action & KeyAction.UP:
            debug_print("UP")
            if not PostMessageA(window, WM_KEYUP, vk_code, l_param_up):
                raise DelivarMessageFail("%s UP" % key_to_vk_code(key))
    else:
        raise UndefinedMessageDeliveryModeFail(mode_id)
