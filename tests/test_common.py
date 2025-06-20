import pytest
import PyCrossWindowKeyStrokeSender as cwkss

def test_dummy():
    assert(True)

def test_to_utf16():
    assert(cwkss.to_utf16_codes(u"\u015B")      == [0x015B])
    assert(cwkss.to_utf16_codes(u"\u0444")      == [0x0444])
    assert(cwkss.to_utf16_codes(u"\U00024B62")  == [0xD852, 0xDF62])

