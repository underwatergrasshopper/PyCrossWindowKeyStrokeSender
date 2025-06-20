from . import Types as _t
from ..Actions import Key


_KEY_TO_VK_CODE_MAP = {
    Key.BREAK               : _t.VK_CANCEL,  
    Key.BACKSPACE           : _t.VK_BACK,             
    Key.TAB                 : _t.VK_TAB,              
    Key.ENTER               : _t.VK_RETURN,     
    Key.SHIFT               : _t.VK_SHIFT,            
    Key.CTRL                : _t.VK_CONTROL,          
    Key.ALT                 : _t.VK_MENU,                
    Key.PAUSE               : _t.VK_PAUSE,            
    Key.CAPS_LOCK           : _t.VK_CAPITAL,          
    Key.ESCAPE              : _t.VK_ESCAPE,           
    Key.SPACE               : _t.VK_SPACE,            
    Key.PAGE_UP             : _t.VK_PRIOR,            
    Key.PAGE_DOWN           : _t.VK_NEXT,             
    Key.END                 : _t.VK_END,              
    Key.HOME                : _t.VK_HOME,             
    Key.ARROW_LEFT          : _t.VK_LEFT,             
    Key.ARROW_UP            : _t.VK_UP,               
    Key.ARROW_RIGHT         : _t.VK_RIGHT,            
    Key.ARROW_DOWN          : _t.VK_DOWN,             
    Key.PRINT               : _t.VK_PRINT,            
    Key.PRINT_SCREEN        : _t.VK_SNAPSHOT,         
    Key.INSERT              : _t.VK_INSERT,           
    Key.DELETE              : _t.VK_DELETE,           
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
    Key.NUMPAD_0            : _t.VK_NUMPAD0,          
    Key.NUMPAD_1            : _t.VK_NUMPAD1,          
    Key.NUMPAD_2            : _t.VK_NUMPAD2,          
    Key.NUMPAD_3            : _t.VK_NUMPAD3,          
    Key.NUMPAD_4            : _t.VK_NUMPAD4,          
    Key.NUMPAD_5            : _t.VK_NUMPAD5,          
    Key.NUMPAD_6            : _t.VK_NUMPAD6,          
    Key.NUMPAD_7            : _t.VK_NUMPAD7,          
    Key.NUMPAD_8            : _t.VK_NUMPAD8,          
    Key.NUMPAD_9            : _t.VK_NUMPAD9,          
    Key.NUMPAD_MULTIPLY     : _t.VK_MULTIPLY,         
    Key.NUMPAD_ADD          : _t.VK_ADD,              
    Key.NUMPAD_SEPARATOR    : _t.VK_SEPARATOR,        
    Key.NUMPAD_SUBTRACT     : _t.VK_SUBTRACT,         
    Key.NUMPAD_DECIMAL      : _t.VK_DECIMAL,          
    Key.NUMPAD_DIVIDE       : _t.VK_DIVIDE,           
    Key.F1                  : _t.VK_F1,               
    Key.F2                  : _t.VK_F2,               
    Key.F3                  : _t.VK_F3,               
    Key.F4                  : _t.VK_F4,               
    Key.F5                  : _t.VK_F5,               
    Key.F6                  : _t.VK_F6,               
    Key.F7                  : _t.VK_F7,               
    Key.F8                  : _t.VK_F8,               
    Key.F9                  : _t.VK_F9,               
    Key.F10                 : _t.VK_F10,              
    Key.F11                 : _t.VK_F11,              
    Key.F12                 : _t.VK_F12,              
    Key.F13                 : _t.VK_F13,              
    Key.F14                 : _t.VK_F14,              
    Key.F15                 : _t.VK_F15,              
    Key.F16                 : _t.VK_F16,              
    Key.F17                 : _t.VK_F17,              
    Key.F18                 : _t.VK_F18,              
    Key.F19                 : _t.VK_F19,              
    Key.F20                 : _t.VK_F20,              
    Key.F21                 : _t.VK_F21,              
    Key.F22                 : _t.VK_F22,              
    Key.F23                 : _t.VK_F23,              
    Key.F24                 : _t.VK_F24,              
    Key.NUM_LOCK            : _t.VK_NUMLOCK,          
    Key.SCROLL_LOCK         : _t.VK_SCROLL,   
    Key.LSHIFT              : _t.VK_LSHIFT,           
    Key.RSHIFT              : _t.VK_RSHIFT,           
    Key.LCTRL               : _t.VK_LCONTROL,         
    Key.RCTRL               : _t.VK_RCONTROL,         
    Key.LALT                : _t.VK_LMENU,            
    Key.RALT                : _t.VK_RMENU,   
}

def key_to_vk_code(key : Key) -> int | None:
    """
    Returns WinApi Virtual Key Code.
    """
    return _KEY_TO_VK_CODE_MAP.get(key, None)  


_EXT_VIRTUAL_KEYS = set([
    _t.VK_INSERT,
    _t.VK_DELETE,

    _t.VK_HOME,
    _t.VK_END,
    _t.VK_PRIOR,
    _t.VK_NEXT,

    _t.VK_LEFT,
    _t.VK_UP,
    _t.VK_DOWN,
    _t.VK_RIGHT,

    _t.VK_RMENU,     
    _t.VK_RCONTROL,

    _t.VK_SNAPSHOT,
    _t.VK_SCROLL,
    _t.VK_CANCEL,

    _t.VK_NUMLOCK,
    _t.VK_DIVIDE,
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
    _t.VK_LSHIFT   : _t.VK_SHIFT,           
    _t.VK_RSHIFT   : _t.VK_SHIFT,           
    _t.VK_LCONTROL : _t.VK_CONTROL,         
    _t.VK_RCONTROL : _t.VK_CONTROL,         
    _t.VK_LMENU    : _t.VK_MENU,            
    _t.VK_RMENU    : _t.VK_MENU,   
}

def vk_code_to_sideless(vk_code : Key) -> int:
    """
    Returns WinApi Virtual Key Code.
    """
    return _VK_CODE_TO_SIDELESS_MAP.get(vk_code, vk_code)  
