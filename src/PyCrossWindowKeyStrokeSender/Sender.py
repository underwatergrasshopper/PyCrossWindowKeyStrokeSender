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
from ._Private.Types            import *
from ._Private.ActionsSupport   import *
from .Debug                     import *
from .Commons                   import *
from .Exceptions                import *
from .Actions                   import *

import time
from enum                       import Enum

__all__ = [
    "send_to_window",
]

def send_to_window(target_window_name, *actions):
    """
    Sends keyboard messages to target window.
    target_window_name  : bytes or str      Name of window to which messages will be sent. 
    actions             : <Action>, ...     Actions, which are containing messages to send and informations how to send messages. Each action is defined by it's type:
                                                bytes   - Text message in ASCII encoding format.
                                                          Note: Uses internally WinApi functions with suffix A. 
                                                str     - Text message in UTF-16 encoding format.
                                                          Note: Uses internally WinApi functions with suffix W. 
                                            Note: Input text is utf-16 only? and key messages also?
                                                
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
        raise SetupFail("Can not find foreground window.", True)

    target_window_thread_id = GetWindowThreadProcessId(target_window, NULL);

    debug_print("target_window_thread_id handle: ", target_window_thread_id)

    if not target_window_thread_id:
       return SetupFail("Can not receive target window thread id.")

    caller_window_thread_id = GetCurrentThreadId()

    debug_print("caller_window_thread_id handle: ", caller_window_thread_id)

    if not caller_window_thread_id:
       return SetupFail("Can not receive caller window thread id.")

    if target_window_thread_id and (target_window_thread_id is not caller_window_thread_id):
        is_success = AttachThreadInput(caller_window_thread_id, target_window_thread_id, TRUE)
        
        if not is_success:
            return SetupFail("Can not attach caller window thread to target window thread.", True)

        try:
            focus_and_send_messages(target_window, foreground_window, actions)
        except Exception:
            AttachThreadInput(caller_window_thread_id, target_window_thread_id, FALSE)
            raise

        is_success = AttachThreadInput(caller_window_thread_id, target_window_thread_id, FALSE)

        if not is_success:
            return CleanupFail("Can not detach caller window thread from target window thread.", True)
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
        raise SetupFail("Can not set target window to be foreground window.", True)

    focus_window = GetFocus()
    
    debug_print("focus_window: ", focus_window)
    
    if not focus_window: 
        SetupFail("Can not get window with keyboard focus.", True)

    try:
        deliver_messages(focus_window, actions)
    except Exception:
        try_set_foreground_window(foreground_window)
        raise

    is_success = try_set_foreground_window(foreground_window)

    if not is_success:
        raise SetupFail("Can not set previous foreground window back to be foreground window.", True)
    
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

def is_key_and_key_state_tuple(action):
    """
    action : <Action>
    return bool
    """
    return isinstance(action, tuple) and len(action) > 1 and isinstance(action[0], Key) and isinstance(action[1], int)

def deliver_messages(focus_window, actions):
    """
    focus_window        : HWND
    actions             : tuple(<Action>)
    """
    debug_print("actions: ", *actions)

    encoding_type_id        = EncodingTypeID.ASCII
    delivery_type_id        = DeliveryTypeID.SEND
    delay                   = 0.0           # in seconds

    for action in actions:
        if isinstance(action, (bytes, str)):        # text
            debug_print("deliver text message")
            deliver_text(focus_window, action, encoding_type_id, delivery_type_id)

            time.sleep(delay)

        elif isinstance(action, Key):               # key
            debug_print("deliver key message: ", action.name)
            deliver_key(focus_window, action, KeyState.DOWN_AND_UP, encoding_type_id, delivery_type_id)

            time.sleep(delay)
             
        elif is_key_and_key_state_tuple(action):    # (key, state)
            debug_print("deliver key message: ", action[0].name)
            deliver_key(focus_window, action[0], action[1], encoding_type_id, delivery_type_id)

            time.sleep(delay)

        elif isinstance(action, Input):             # input
            debug_print("deliver input message: ", action.actions)
            deliver_input(focus_window, action.actions)

            time.sleep(delay)

        elif isinstance(action, EncodingTypeID):
            debug_print("set encoding_type_id: ", action.name)
            encoding_type_id = action

        elif isinstance(action, DeliveryTypeID):
            debug_print("set delivery_type_id: ", action.name)
            delivery_type_id = action

        elif isinstance(action, Wait):
            debug_print("wait: ", action.wait_time)

            time.sleep(action.wait_time)

        elif isinstance(action, Delay):
            debug_print("set delay: ", action.delay_time)
            delay = action.delay_time

        else:
            raise ArgumentFail("Can not process unexpected action type: %s." % type(action).__name__)


def deliver_text(window, text, encoding_type_id, delivery_type_id):
    """
    window              : HWND
    text                : str or bytes
    encoding_type_id    : EncodingTypeID
    delivery_type_id    : DeliveryTypeID
    """
    debug_print("encoding_type_id: ", encoding_type_id.name)
    debug_print("delivery_type_id: ", delivery_type_id.name)

    if encoding_type_id == EncodingTypeID.ASCII:
        text = to_bytes(text)

        if delivery_type_id == DeliveryTypeID.SEND:
            for sign in text:
                SendMessageA(window, WM_CHAR, sign, 0)

        elif delivery_type_id == DeliveryTypeID.POST:
            for sign in text:
                if not PostMessageA(window, WM_CHAR, sign, 0):
                    raise DeliverMessageFail("Can not deliver ascii message: \"%s\"" % to_utf16(text))
        else:
            raise DeliverMessageFail("Can not process unsupported delivery method: \"%s\"." % delivery_type_id.name)

    elif encoding_type_id == EncodingTypeID.UTF16:
        text = to_utf16(text)

        if delivery_type_id == DeliveryTypeID.SEND:
            for sign in text:
                SendMessageW(window, WM_CHAR, ord(sign), 0)

        elif delivery_type_id == DeliveryTypeID.POST:
            for sign in text:
                if not PostMessageW(window, WM_CHAR, ord(sign), 0):
                    raise DeliverMessageFail("Can not deliver utf-16 message: \"%s\"" % to_utf16(text))
        else:
            raise DeliverMessageFail("Can not process unsupported delivery method: \"%s\"." % delivery_type_id.name)
    else:
        raise DeliverMessageFail("Can not process unsupported encoding format: \"%s\"." % encoding_type_id.name)

def deliver_key(window, key, key_state, encoding_type_id, delivery_type_id):
    """
    window              : HWND
    key                 : Key
    key_state           : int               Bitfield made from KeyState bit sets.
    encoding_type_id    : EncodingTypeID
    delivery_type_id    : DeliveryTypeID
    """
    debug_print("encoding_type_id: ", encoding_type_id.name)
    debug_print("delivery_type_id: ", delivery_type_id.name)

    if encoding_type_id == EncodingTypeID.ASCII:
        SendMessage     = SendMessageA
        PostMessage     = PostMessageA
        MapVirtualKey   = MapVirtualKeyA
    elif encoding_type_id == EncodingTypeID.UTF16:
        SendMessage     = SendMessageW
        PostMessage     = PostMessageW
        MapVirtualKey   = MapVirtualKeyW
    else:
        raise DeliverMessageFail("Can not process unsupported encoding format: \"%s\"." % encoding_type_id.name)

    if key in [Key.ALT, Key.LALT, Key.RALT]:
        # Note: Alt (especially right Alt) keystroke sends more than WM_KEYDOWN and WM_KEYUP message.
        # Couldn't find clear specification which describes what is actually done.
        # SendInput() function sends this keystroke correctly.
        raise DeliverMessageFail("Can not deliver message with unsupported key: %s. (use Input() instead)" % key.name)

    vk_code       = key_to_vk_code(key)
    scan_code     = MapVirtualKey(vk_code, MAPVK_VK_TO_VSC)

    l_param_down  = 0x00000001 | (scan_code  << 16)
    l_param_up    = 0xC0000001 | (scan_code  << 16)

    if is_ext_virtuel_key(vk_code):
        l_param_down    |= 1 << 24
        l_param_up      |= 1 << 24

    vk_code = vk_code_to_sideless(vk_code)

    if delivery_type_id == DeliveryTypeID.SEND:
        if key_state & KeyState.DOWN:
            debug_print("DOWN")
            SendMessage(window, WM_KEYDOWN, vk_code, l_param_down)

        if key_state & KeyState.UP:
            debug_print("UP")
            SendMessage(window, WM_KEYUP, vk_code, l_param_up)

    elif delivery_type_id == DeliveryTypeID.POST:
        if key_state & KeyState.DOWN:
            debug_print("DOWN")
            if not PostMessage(window, WM_KEYDOWN, vk_code, l_param_down):
                raise DeliverMessageFail("Can not post message: %s DOWN." % key_to_vk_code(key))

        if key_state & KeyState.UP:
            debug_print("UP")
            if not PostMessage(window, WM_KEYUP, vk_code, l_param_up):
                raise DeliverMessageFail("Can not post message: %s UP." % key_to_vk_code(key))
    else:
        raise DeliverMessageFail("Can not process unsupported delivery method: \"%s\"." % delivery_type_id.name)

def deliver_input(window, actions):
    """
    window      : HWND
    actions     : tuple(<SimpleMessage>)
    """
    inputs = [] # list(INPUT)

    for action in actions:
        if isinstance(action, (bytes, str)): # text
            inputs += make_text_input(action)
        elif isinstance(action, Key): # key
            inputs += make_key_input(action, KeyState.DOWN_AND_UP)
        elif is_key_and_key_state_tuple(action): # key
            inputs += make_key_input(action[0], action[1])
        else:
            raise DeliverMessageFail("Can not process unexpected (for Input) action type: %s." % type(action).__name__)

    length = len(inputs)
    raw_inputs = (INPUT * length)(*inputs)  # ctypes requires specific type for array

    count = SendInput(length, raw_inputs, sizeof(INPUT))
    if count != length:
        raise DeliverMessageFail("Can not deliver all messages (for Input): %s. Delivered %d messages. " % (str(actions), count))


def make_text_input(text):
    """
    text : bytes or str
    return list(INPUT)
    """
    inputs = [] # INPUT

    text = to_utf16(text)

    for sign in text:
        input = INPUT()

        input.type              = INPUT_KEYBOARD
        input.ki.wVk            = 0
        input.ki.wScan          = ord(sign)
        input.ki.time           = 0
        input.ki.dwFlags        = KEYEVENTF_UNICODE
        input.ki.dwExtraInfo    = 0

        inputs += [input]

        input = INPUT()

        input.type              = INPUT_KEYBOARD
        input.ki.wVk            = 0
        input.ki.wScan          = ord(sign)
        input.ki.time           = 0
        input.ki.dwFlags        = KEYEVENTF_UNICODE | KEYEVENTF_KEYUP
        input.ki.dwExtraInfo    = 0

        inputs += [input]

    return inputs

def make_key_input(key, key_state):
    """
    key         : Key
    key_state   : KeyState
    return list(INPUT)
    """
    inputs = [] # INPUT

    vk_code       = key_to_vk_code(key)
    scan_code     = MapVirtualKeyW(vk_code, MAPVK_VK_TO_VSC)

    ext_key_flag = KEYEVENTF_EXTENDEDKEY if is_ext_virtuel_key(vk_code) else 0

    if key_state & KeyState.DOWN:
        input = INPUT()

        input.type              = INPUT_KEYBOARD
        input.ki.wVk            = 0
        input.ki.wScan          = scan_code
        input.ki.time           = 0
        input.ki.dwFlags        = KEYEVENTF_SCANCODE | ext_key_flag
        input.ki.dwExtraInfo    = 0

        inputs += [input]

    if key_state & KeyState.UP:
        input = INPUT()

        input.type              = INPUT_KEYBOARD
        input.ki.wVk            = 0
        input.ki.wScan          = scan_code
        input.ki.time           = 0
        input.ki.dwFlags        = KEYEVENTF_SCANCODE | KEYEVENTF_KEYUP | ext_key_flag
        input.ki.dwExtraInfo    = 0

        inputs += [input]

    return inputs

