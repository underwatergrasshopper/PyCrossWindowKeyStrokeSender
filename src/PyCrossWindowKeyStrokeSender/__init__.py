
from pathlib import Path as _Path

__author__  = "underwatergrasshopper"
__version__ = (_Path(__file__).parent.resolve() / "version").read_text("utf-8").strip()


from .Sender        import send_to_window
from .Actions       import Action, Message, SimpleMessage, Key, KeyState, Input, EncodingTypeID, DeliveryTypeID, Delay, Wait
from .Exceptions    import SetupFail, FindTargetWindowFail, CleanupFail, ArgumentFail, DeliverMessageFail
from .Debug         import enable_debug
