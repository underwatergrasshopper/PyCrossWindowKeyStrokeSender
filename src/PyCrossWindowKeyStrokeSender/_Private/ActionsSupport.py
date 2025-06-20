from . import WinApi as _WinApi
from ..Actions import Key


_KEY_TO_VK_CODE_MAP = {
    Key.BREAK               : _WinApi.VK_CANCEL,  
    Key.BACKSPACE           : _WinApi.VK_BACK,             
    Key.TAB                 : _WinApi.VK_TAB,              
    Key.ENTER               : _WinApi.VK_RETURN,     
    Key.SHIFT               : _WinApi.VK_SHIFT,            
    Key.CTRL                : _WinApi.VK_CONTROL,          
    Key.ALT                 : _WinApi.VK_MENU,                
    Key.PAUSE               : _WinApi.VK_PAUSE,            
    Key.CAPS_LOCK           : _WinApi.VK_CAPITAL,          
    Key.ESCAPE              : _WinApi.VK_ESCAPE,           
    Key.SPACE               : _WinApi.VK_SPACE,            
    Key.PAGE_UP             : _WinApi.VK_PRIOR,            
    Key.PAGE_DOWN           : _WinApi.VK_NEXT,             
    Key.END                 : _WinApi.VK_END,              
    Key.HOME                : _WinApi.VK_HOME,             
    Key.ARROW_LEFT          : _WinApi.VK_LEFT,             
    Key.ARROW_UP            : _WinApi.VK_UP,               
    Key.ARROW_RIGHT         : _WinApi.VK_RIGHT,            
    Key.ARROW_DOWN          : _WinApi.VK_DOWN,             
    Key.PRINT               : _WinApi.VK_PRINT,            
    Key.PRINT_SCREEN        : _WinApi.VK_SNAPSHOT,         
    Key.INSERT              : _WinApi.VK_INSERT,           
    Key.DELETE              : _WinApi.VK_DELETE,           
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
    Key.NUMPAD_0            : _WinApi.VK_NUMPAD0,          
    Key.NUMPAD_1            : _WinApi.VK_NUMPAD1,          
    Key.NUMPAD_2            : _WinApi.VK_NUMPAD2,          
    Key.NUMPAD_3            : _WinApi.VK_NUMPAD3,          
    Key.NUMPAD_4            : _WinApi.VK_NUMPAD4,          
    Key.NUMPAD_5            : _WinApi.VK_NUMPAD5,          
    Key.NUMPAD_6            : _WinApi.VK_NUMPAD6,          
    Key.NUMPAD_7            : _WinApi.VK_NUMPAD7,          
    Key.NUMPAD_8            : _WinApi.VK_NUMPAD8,          
    Key.NUMPAD_9            : _WinApi.VK_NUMPAD9,          
    Key.NUMPAD_MULTIPLY     : _WinApi.VK_MULTIPLY,         
    Key.NUMPAD_ADD          : _WinApi.VK_ADD,              
    Key.NUMPAD_SEPARATOR    : _WinApi.VK_SEPARATOR,        
    Key.NUMPAD_SUBTRACT     : _WinApi.VK_SUBTRACT,         
    Key.NUMPAD_DECIMAL      : _WinApi.VK_DECIMAL,          
    Key.NUMPAD_DIVIDE       : _WinApi.VK_DIVIDE,           
    Key.F1                  : _WinApi.VK_F1,               
    Key.F2                  : _WinApi.VK_F2,               
    Key.F3                  : _WinApi.VK_F3,               
    Key.F4                  : _WinApi.VK_F4,               
    Key.F5                  : _WinApi.VK_F5,               
    Key.F6                  : _WinApi.VK_F6,               
    Key.F7                  : _WinApi.VK_F7,               
    Key.F8                  : _WinApi.VK_F8,               
    Key.F9                  : _WinApi.VK_F9,               
    Key.F10                 : _WinApi.VK_F10,              
    Key.F11                 : _WinApi.VK_F11,              
    Key.F12                 : _WinApi.VK_F12,              
    Key.F13                 : _WinApi.VK_F13,              
    Key.F14                 : _WinApi.VK_F14,              
    Key.F15                 : _WinApi.VK_F15,              
    Key.F16                 : _WinApi.VK_F16,              
    Key.F17                 : _WinApi.VK_F17,              
    Key.F18                 : _WinApi.VK_F18,              
    Key.F19                 : _WinApi.VK_F19,              
    Key.F20                 : _WinApi.VK_F20,              
    Key.F21                 : _WinApi.VK_F21,              
    Key.F22                 : _WinApi.VK_F22,              
    Key.F23                 : _WinApi.VK_F23,              
    Key.F24                 : _WinApi.VK_F24,              
    Key.NUM_LOCK            : _WinApi.VK_NUMLOCK,          
    Key.SCROLL_LOCK         : _WinApi.VK_SCROLL,   
    Key.LSHIFT              : _WinApi.VK_LSHIFT,           
    Key.RSHIFT              : _WinApi.VK_RSHIFT,           
    Key.LCTRL               : _WinApi.VK_LCONTROL,         
    Key.RCTRL               : _WinApi.VK_RCONTROL,         
    Key.LALT                : _WinApi.VK_LMENU,            
    Key.RALT                : _WinApi.VK_RMENU,   
}

def key_to_vk_code(key : Key) -> int | None:
    """
    Returns WinApi Virtual Key Code.
    """
    return _KEY_TO_VK_CODE_MAP.get(key, None)  


_EXT_VIRTUAL_KEYS = set([
    _WinApi.VK_INSERT,
    _WinApi.VK_DELETE,

    _WinApi.VK_HOME,
    _WinApi.VK_END,
    _WinApi.VK_PRIOR,
    _WinApi.VK_NEXT,

    _WinApi.VK_LEFT,
    _WinApi.VK_UP,
    _WinApi.VK_DOWN,
    _WinApi.VK_RIGHT,

    _WinApi.VK_RMENU,     
    _WinApi.VK_RCONTROL,

    _WinApi.VK_SNAPSHOT,
    _WinApi.VK_SCROLL,
    _WinApi.VK_CANCEL,

    _WinApi.VK_NUMLOCK,
    _WinApi.VK_DIVIDE,
    # TODO: 'Numpad Enter' is also an extended key. Does he have virtual key code? Find it!
])

def is_ext_virtual_key(vk_code : int) -> bool:
    """
    vk_code 
        WinApi Virtual Key Code.
    """
    return vk_code in _EXT_VIRTUAL_KEYS


_SPECIAL_KEYS = set([
    Key.ALT, Key.SHIFT, Key.CTRL, 
    Key.LALT, Key.LSHIFT, Key.LCTRL, 
    Key.RALT, Key.RSHIFT, Key.RCTRL
])

def is_special_key(key : Key) -> bool:
    return key in _SPECIAL_KEYS


_VK_CODE_TO_SIDELESS_MAP = {
    _WinApi.VK_LSHIFT   : _WinApi.VK_SHIFT,           
    _WinApi.VK_RSHIFT   : _WinApi.VK_SHIFT,           
    _WinApi.VK_LCONTROL : _WinApi.VK_CONTROL,         
    _WinApi.VK_RCONTROL : _WinApi.VK_CONTROL,         
    _WinApi.VK_LMENU    : _WinApi.VK_MENU,            
    _WinApi.VK_RMENU    : _WinApi.VK_MENU,   
}

def vk_code_to_sideless(vk_code : Key) -> int:
    """
    Returns WinApi Virtual Key Code.
    """
    return _VK_CODE_TO_SIDELESS_MAP.get(vk_code, vk_code)  
