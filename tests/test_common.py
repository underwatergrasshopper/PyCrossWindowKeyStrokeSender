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

import pytest
import PyCrossWindowKeyStrokeSender as cwkss

def test_dummy():
    assert(True)

def test_to_utf16():
    assert(cwkss.to_utf16(b"abc") == u"abc")
    assert(cwkss.to_utf16("abc") == u"abc")
    assert(cwkss.to_utf16(u"abc") == u"abc")
    assert(cwkss.to_utf16(U"abc") == u"abc")

def test_to_bytes():
    assert(cwkss.to_bytes(b"abc") == b"abc")
    assert(cwkss.to_bytes("abc") == b"abc")
    assert(cwkss.to_bytes(u"abc") == b"abc")
    assert(cwkss.to_bytes(U"abc") == b"abc")
