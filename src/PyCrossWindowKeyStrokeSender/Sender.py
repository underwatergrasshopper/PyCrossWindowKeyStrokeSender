import ctypes as _c
import ctypes.wintypes as _w
import time as _time

from ._Private import Types as _t
from ._Private import ActionsSupport as _support
from .Debug import debug_print as _debug_print
from .Commons import to_utf16_codes as _to_utf16_codes

from .Actions import Action, Message, SimpleMessage, Key, KeyState, Input, EncodingTypeID, DeliveryTypeID, Delay, Wait
from .Exceptions import SetupFail, FindTargetWindowFail, CleanupFail, ArgumentFail, DeliverMessageFail


def send_to_window(target_window_name : str | bytes, *actions : Action):
    """
    Delivers keyboard key and text messages to the target window.

    target_window name                      
        Name of the window to which messages will be sent.
        Note: If bytes then is interpreted as ascii string.
        If str then is interpreted as unicode string.

    actions                                 
        Actions to be performed in the same order as they are in arguments.
        Allowed actions:
        SEND                           
            (Default) Changes message delivery method to send. 
            Function will wait after sending each message until it's delivered. 
            Might be slow, but it's gives most chance, for massages, to be delivered in order. 
            Example: send_to_window("Some Window", "Some text.", Key.ENTER, Wait(0.1))
            Example: send_to_window("Some Window", SEND, "Some text.", Key.ENTER, Wait(0.1))
                                        
        POST                           
            Changes message delivery method to post. Function will NOT wait after sending each message until it's delivered. 
            In many cases, much more faster than SEND method, but requires setting small delay for messages to help deliver messages in order.
            Example: send_to_window("Some Window", POST, Delay(0.1), "Some text.", Key.ENTER, Wait(0.1))
            
            Delivery methods can be changed multiple times between messages.
            send_to_window("Some Window", Delay(0.1), SEND, "Some text.", "Some other text", POST, u"Some another text", Wait(0.1)) 
                                         
        UTF16                           
            (Default) Messages will be delivered as utf-16 messages. 
            Use this action, if text messages have any unicode character in any encoding format (utf-8, utf-16, utf-32).
            Example: send_to_window("Some Window", UTF16, "Some text. \u0444", Wait(0.1))
            
            Note: Uses internally winapi functions with W suffix.          
                            
        ASCII                           
            Messages will be delivered as ascii messages. 
            Use this action if text message have only ascii characters.
            Example: send_to_window("Some Window", "Some text.", Wait(0.1)) 
            Example: send_to_window("Some Window", ASCII, "Some text.", Wait(0.1)) 
            
            Note: Uses internally winapi functions with A suffix.
            
            Encoding format of delivery can be changed multiple times between messages.
            send_to_window("Some Window", ASCII, "Some ascii text.", "Some other ascii text", UTF16, u"Some unicode text \u0444", Wait(0.1)) 
                                         
        str object                      
            Text message.
                                        
        Key object                      
            Key message. Both key down and key up message. First down and then up will be delivered.
            Example: send_to_window("Some Window", Key.ENTER, Wait(0.1))
           
        tuple[Key, KeyState] object     
            Key message with specified what key action is performed. Either down or up.
            Example: send_to_window("Some Window", (Key.ENTER, KeyState.DOWN), (Key.ENTER, KeyState.UP), Wait(0.1))
                            
        Input object                    
            Input delivery method with messages. Delivers contained messages by simulating keyboard actions. 
            If simulating exact keyboard actions is needed, then this method have most chance of success. 
            Doesn't wait until messages are delivered, so small wait is required to help deliver messages. 
            Speed of delivery messages is comparable with POST method.
            Ignores POST, SEND delivery methods. It always send messages in utf-16. 
            Allowed <Message> types:
                str            Text message.
                Key                     Key message, both down and up.
                tuple(Key, KeyState)    Key message.
            
            Example: send_to_window("Some Game", Input(Key.ENTER, "/exit", Key.ENTER), Wait(0.1))
            
            Note: If send_to_window function is called from callback function, it might fail. 
            This might happen because it's called from non main thread. In this case try use POST delivery method.
                                        
        Delay object                    
            Sets a delay. It's performed after each action of type: bytes, str, Key, tuple(Key, KeyState), Input

        Wait object                     
            Performs wait a single time for given amount of time.

        Note: It's a good practice to put one as last action. To give function time to process all messages.

    Raises: ArgumentFail, SetupFail, DeliverMessageFail, CleanupFail, FindTargetWindowFail.
    """
    target_window = _t.NULL

    # b"..."                    -> ascii    (...A)
    # "...", u"...", U"..."     -> utf-16   (...W)

    if isinstance(target_window_name, bytes):
        _debug_print("target_window_name ascii: ", target_window_name.decode("utf-8"))

        target_window = _t.FindWindowA(_t.NULL, target_window_name)

        _debug_print("target_window handle: ", target_window)
    else:
        _debug_print("target_window_name utf-16: ", target_window_name)

        target_window = _t.FindWindowW(_t.NULL, target_window_name)

        _debug_print("target_window handle: ", target_window)

    if not target_window:
        raise FindTargetWindowFail(target_window_name, True)

    _send_to_window_by_handle(target_window, actions)

################################################################################

def _send_to_window_by_handle(target_window : _t.HWND, actions : tuple[Action]):
    foreground_window = _t.GetForegroundWindow()

    _debug_print("foreground_window handle: ", foreground_window)

    if not foreground_window:
        raise SetupFail("Can not find foreground window.", True)

    target_window_thread_id = _t.GetWindowThreadProcessId(target_window, _t.NULL)

    _debug_print("target_window_thread_id handle: ", target_window_thread_id)

    if not target_window_thread_id:
       return SetupFail("Can not receive target window thread id.")

    caller_window_thread_id = _t.GetCurrentThreadId()

    _debug_print("caller_window_thread_id handle: ", caller_window_thread_id)

    if not caller_window_thread_id:
       return SetupFail("Can not receive caller window thread id.")

    if target_window_thread_id and (target_window_thread_id is not caller_window_thread_id):
        is_success = _t.AttachThreadInput(caller_window_thread_id, target_window_thread_id, _t.TRUE)
        
        if not is_success:
            return SetupFail("Can not attach caller window thread to target window thread.", True)

        try:
            _focus_and_send_messages(target_window, foreground_window, actions)
        except Exception:
            _t.AttachThreadInput(caller_window_thread_id, target_window_thread_id, _t.FALSE)
            raise

        is_success = _t.AttachThreadInput(caller_window_thread_id, target_window_thread_id, _t.FALSE)

        if not is_success:
            return CleanupFail("Can not detach caller window thread from target window thread.", True)
    else:
        # When the target window is the caller window.

        _deliver_messages(target_window, actions)
    

def _focus_and_send_messages(target_window : _t.HWND, foreground_window : _t.HWND, actions : tuple[Action]):
    if _t.IsIconic(target_window):
       _t.ShowWindow(target_window, _t.SW_RESTORE)
    
    is_success = _t.SetForegroundWindow(target_window)
    
    if not is_success:
        raise SetupFail("Can not set target window to be foreground window.", True)

    focus_window = _t.GetFocus()
    
    _debug_print("focus_window: ", focus_window)
    
    if not focus_window: 
        SetupFail("Can not get window with keyboard focus.", True)

    try:
        _deliver_messages(focus_window, actions)
    except Exception:
        _try_set_foreground_window(foreground_window)
        raise

    is_success = _try_set_foreground_window(foreground_window)

    if not is_success:
        raise SetupFail("Can not set previous foreground window back to be foreground window.", True)
    
    _t.SetFocus(foreground_window)


def _try_set_foreground_window(window : _t.HWND, max_num_of_tries : int = 10, interval : float = 0.01) -> bool:
    """
    interval
        In seconds.
    """
    num_of_tries_left = max_num_of_tries

    while num_of_tries_left:
        if _t.SetForegroundWindow(window):
            _debug_print("max_num_of_tries left: ", num_of_tries_left)
            return True

        _time.sleep(interval)
        num_of_tries_left -= 1

    _debug_print("max_num_of_tries left: ", num_of_tries_left)
    return False


def _is_key_and_key_state_tuple(action : Action) -> bool:
    return isinstance(action, tuple) and len(action) > 1 and isinstance(action[0], Key) and isinstance(action[1], int)


def _deliver_messages(focus_window : _t.HWND, actions : tuple[Action]):
    _debug_print("actions: ", *actions)

    encoding_type_id        = EncodingTypeID.UTF16
    delivery_type_id        = DeliveryTypeID.SEND
    delay                   = 0.0                   # in seconds

    for action in actions:
        if isinstance(action, str):                 # text
            _debug_print("deliver text message")
            _deliver_text(focus_window, action, encoding_type_id, delivery_type_id)

            _time.sleep(delay)

        elif isinstance(action, Key):               # key
            _debug_print("deliver key message: ", action.name)
            _deliver_key(focus_window, action, KeyState.DOWN_AND_UP, encoding_type_id, delivery_type_id)

            _time.sleep(delay)
             
        elif _is_key_and_key_state_tuple(action):    # (key, state)
            _debug_print("deliver key message: ", action[0].name)
            _deliver_key(focus_window, action[0], action[1], encoding_type_id, delivery_type_id)

            _time.sleep(delay)

        elif isinstance(action, Input):             # input
            _debug_print("deliver input message: ", action.actions)
            _deliver_input(action.actions)

            _time.sleep(delay)

        elif isinstance(action, EncodingTypeID):
            _debug_print("set encoding_type_id: ", action.name)
            encoding_type_id = action

        elif isinstance(action, DeliveryTypeID):
            _debug_print("set delivery_type_id: ", action.name)
            delivery_type_id = action

        elif isinstance(action, Wait):
            _debug_print("wait: ", action.wait_time)

            _time.sleep(action.wait_time)

        elif isinstance(action, Delay):
            _debug_print("set delay: ", action.delay_time)
            delay = action.delay_time

        else:
            raise ArgumentFail(f"Can not process unexpected action type: {type(action).__name__}.")


def _deliver_text(window : _t.HWND, text : str, encoding_type_id : EncodingTypeID, delivery_type_id : DeliveryTypeID):
    _debug_print("encoding_type_id: ", encoding_type_id.name)
    _debug_print("delivery_type_id: ", delivery_type_id.name)

    if encoding_type_id == EncodingTypeID.ASCII:
        codes = text.encode("utf-8")

        if delivery_type_id == DeliveryTypeID.SEND:
            for code in codes:
                _t.SendMessageA(window, _t.WM_CHAR, code, 0)

        elif delivery_type_id == DeliveryTypeID.POST:
            for code in codes:
                if not _t.PostMessageA(window, _t.WM_CHAR, code, 0):
                    raise DeliverMessageFail(f"Can not deliver ascii message: \"{text}\"")
        else:
            raise DeliverMessageFail(f"Can not process unsupported delivery method: \"{delivery_type_id.name}\".")

    elif encoding_type_id == EncodingTypeID.UTF16:
        codes = _to_utf16_codes(text)

        if delivery_type_id == DeliveryTypeID.SEND:
            for code in codes:
                _t.SendMessageW(window, _t.WM_CHAR, code, 0)

        elif delivery_type_id == DeliveryTypeID.POST:
            for code in codes:
                if not _t.PostMessageW(window, _t.WM_CHAR, code, 0):
                    raise DeliverMessageFail(f"Can not deliver utf-16 message: \"{text}\"")
        else:
            raise DeliverMessageFail(f"Can not process unsupported delivery method: \"{delivery_type_id.name}\".")
    else:
        raise DeliverMessageFail(f"Can not process unsupported encoding format: \"{encoding_type_id.name}\".")


def _deliver_key(window : _t.HWND, key : Key, key_state : int, encoding_type_id : EncodingTypeID, delivery_type_id : DeliveryTypeID):
    """
    key_state 
        Bitfield made from KeyState bit sets.
    """
    _debug_print("encoding_type_id: ", encoding_type_id.name)
    _debug_print("delivery_type_id: ", delivery_type_id.name)

    if encoding_type_id == EncodingTypeID.ASCII:
        SendMessage     = _t.SendMessageA
        PostMessage     = _t.PostMessageA
        MapVirtualKey   = _t.MapVirtualKeyA
    elif encoding_type_id == EncodingTypeID.UTF16:
        SendMessage     = _t.SendMessageW
        PostMessage     = _t.PostMessageW
        MapVirtualKey   = _t.MapVirtualKeyW
    else:
        raise DeliverMessageFail(f"Can not process unsupported encoding format: \"{encoding_type_id.name}\".")

    if key in [Key.ALT, Key.LALT, Key.RALT]:
        # Note: Alt (especially right Alt) keystroke sends more than WM_KEYDOWN and WM_KEYUP message.
        # Couldn't find clear specification which describes what is actually sent and in what format.
        # SendInput() function sends this keystroke correctly.
        raise DeliverMessageFail(f"Can not deliver message with unsupported key: {key.name}. (use Input() instead)")

    vk_code       = _support.key_to_vk_code(key)
    scan_code     = MapVirtualKey(vk_code, _t.MAPVK_VK_TO_VSC)

    l_param_down  = 0x00000001 | (scan_code  << 16)
    l_param_up    = 0xC0000001 | (scan_code  << 16)

    if _support.is_ext_virtual_key(vk_code):
        l_param_down    |= 1 << 24
        l_param_up      |= 1 << 24

    vk_code = _support.vk_code_to_sideless(vk_code)

    if delivery_type_id == DeliveryTypeID.SEND:
        if key_state & KeyState.DOWN:
            _debug_print("DOWN")
            SendMessage(window, _t.WM_KEYDOWN, vk_code, l_param_down)

        if key_state & KeyState.UP:
            _debug_print("UP")
            SendMessage(window, _t.WM_KEYUP, vk_code, l_param_up)

    elif delivery_type_id == DeliveryTypeID.POST:
        if key_state & KeyState.DOWN:
            _debug_print("DOWN")
            if not PostMessage(window, _t.WM_KEYDOWN, vk_code, l_param_down):
                raise DeliverMessageFail(f"Can not post message: {_support.key_to_vk_code(key)} DOWN.")

        if key_state & KeyState.UP:
            _debug_print("UP")
            if not PostMessage(window, _t.WM_KEYUP, vk_code, l_param_up):
                raise DeliverMessageFail(f"Can not post message: {_support.key_to_vk_code(key)} UP.")
    else:
        raise DeliverMessageFail(f"Can not process unsupported delivery method: \"{delivery_type_id.name}\".")


def _deliver_input(actions : tuple[SimpleMessage]):
    inputs : list[_t.INPUT] = []

    for action in actions:
        if isinstance(action, (bytes, str)):        # text
            inputs += _make_text_input(action)
        elif isinstance(action, Key):               # key
            inputs += _make_key_input(action, KeyState.DOWN_AND_UP)
        elif _is_key_and_key_state_tuple(action):    # (key, state)
            inputs += _make_key_input(action[0], action[1])
        else:
            raise DeliverMessageFail(f"Can not process unexpected (for Input) action type: {type(action).__name__}.")

    length = len(inputs)
    raw_inputs = (_t.INPUT * length)(*inputs)  # ctypes requires specific type for array

    count = _t.SendInput(length, raw_inputs, _c.sizeof(_t.INPUT))
    if count != length:
        raise DeliverMessageFail(f"Can not deliver all messages (for Input): {str(actions)}. Delivered {count} messages. ")


def _make_text_input(text : str) -> list[_t.INPUT]:
    inputs : list[_t.INPUT] = []

    codes = _to_utf16_codes(text)

    for code in codes:
        input = _t.INPUT()

        input.type              = _t.INPUT_KEYBOARD
        input.ki.wVk            = 0
        input.ki.wScan          = code
        input.ki.time           = 0
        input.ki.dwFlags        = _t.KEYEVENTF_UNICODE
        input.ki.dwExtraInfo    = 0

        inputs += [input]

        input = _t.INPUT()

        input.type              = _t.INPUT_KEYBOARD
        input.ki.wVk            = 0
        input.ki.wScan          = code
        input.ki.time           = 0
        input.ki.dwFlags        = _t.KEYEVENTF_UNICODE | _t.KEYEVENTF_KEYUP
        input.ki.dwExtraInfo    = 0

        inputs += [input]

    return inputs


def _make_key_input(key : Key, key_state : KeyState) -> list[_t.INPUT]:
    inputs : list[_t.INPUT] = []

    vk_code         = _support.key_to_vk_code(key)
    scan_code       = _t.MapVirtualKeyW(vk_code, _t.MAPVK_VK_TO_VSC)
    ext_key_flag    = _t.KEYEVENTF_EXTENDEDKEY if _support.is_ext_virtual_key(vk_code) else 0

    if key_state & KeyState.DOWN:
        input = _t.INPUT()

        input.type              = _t.INPUT_KEYBOARD
        input.ki.wVk            = 0
        input.ki.wScan          = scan_code
        input.ki.time           = 0
        input.ki.dwFlags        = _t.KEYEVENTF_SCANCODE | ext_key_flag
        input.ki.dwExtraInfo    = 0

        inputs += [input]

    if key_state & KeyState.UP:
        input = _t.INPUT()

        input.type              = _t.INPUT_KEYBOARD
        input.ki.wVk            = 0
        input.ki.wScan          = scan_code
        input.ki.time           = 0
        input.ki.dwFlags        = _t.KEYEVENTF_SCANCODE | _t.KEYEVENTF_KEYUP | ext_key_flag
        input.ki.dwExtraInfo    = 0

        inputs += [input]

    return inputs
