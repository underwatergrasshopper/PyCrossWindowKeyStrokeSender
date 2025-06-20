
from pathlib import Path as _Path

__author__  = "underwatergrasshopper"
__version__ = (_Path(__file__).parent.resolve() / "version").read_text("utf-8").strip()

from .Debug         import *
from .Commons       import *
from .Exceptions    import *
from .Actions       import *
from .Sender        import *

def print_heyo():
    print("heyo")


