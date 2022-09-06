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
from .Key               import *

from enum import Enum

__all__ = [
    "Key",
    "key_to_vk_code",
    "KeyAction",
    "Input",
    "DeliveryTypeID",
    "SEND",
    "POST",
    "EncodingTypeID",
    "ASCII",
    "UTF16",
    "Wait",
    "Delay",
]

"""
An action can be one of the following types.

<Action>
    <Message>
    DeliveryTypeID
    EncodingTypeID
    Input
    Wait
    Delay

<Message>
    <SimpleMessage>
    Input

<SimpleMessage>
    <Text>
    Key
    tuple(Key, KeyAction)

<Text>
    str
    bytes
"""

class KeyAction:
    """
    Sets of bit for bitfield.
    """
    DOWN        = 0x01
    UP          = 0x02
    DOWN_AND_UP = DOWN | UP

class Input:
    actions = () # tuple(<SimpleMessage>)

    def __init__(self, *actions):
        """
        actions : <SimpleMessage>, ...        Only simple message actions are allowed: str, bytes, Key, tuple(Key, KeyAction).
        """
        self.actions = actions

class DeliveryTypeID(Enum):
    """
    Message delivery type.
    """
    SEND = 0
    POST = 1

SEND = DeliveryTypeID.SEND
POST = DeliveryTypeID.POST

class EncodingTypeID(Enum):
    """
    Text message encoding format type.
    """
    ASCII = 0
    UTF16 = 1

ASCII = EncodingTypeID.ASCII
UTF16 = EncodingTypeID.UTF16

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
