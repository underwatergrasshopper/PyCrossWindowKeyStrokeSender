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

import PyCrossWindowKeyStrokeSender as cwkss

cwkss.Commons.is_debug = True

if __name__ == "__main__":
    try:
        # find window
        #cwkss.send_to_window(b"*Untitled - Notepad")
        #cwkss.send_to_window("*Untitled - Notepad")

        # undefined action type
        #cwkss.send_to_window(b"*Untitled - Notepad", (False))

        # send text ascii
        #cwkss.send_to_window(b"*Untitled - Notepad", b"Some text.")
        #cwkss.send_to_window(b"*Untitled - Notepad", cwkss.ModeID.SEND, b"Some text.")
        #cwkss.send_to_window(b"*Untitled - Notepad", cwkss.ModeID.POST, b"Some text.")

        # send text utf-16
        #cwkss.send_to_window("*Untitled - Notepad", "Some text.")
        #cwkss.send_to_window("*Untitled - Notepad", cwkss.ModeID.SEND, "Some text.")
        #cwkss.send_to_window("*Untitled - Notepad", cwkss.ModeID.POST, "Some text.")

        # wait
        #cwkss.send_to_window("*Untitled - Notepad", "Some text.", cwkss.Wait(3), "Another text.")

        # delay
        #cwkss.send_to_window("*Untitled - Notepad", cwkss.Delay(1.0), "One. ", "Two. ", "Three. ", "Four. ")

        # key
        #cwkss.send_to_window("*Untitled - Notepad", cwkss.ModeID.POST, cwkss.Delay(0.1), "Some text.", cwkss.Key.ENTER, "Another text.", cwkss.Key.ENTER)
        #cwkss.send_to_window("*Untitled - Notepad", cwkss.ModeID.POST, cwkss.Delay(0.1), "Some text.", (cwkss.Key.ENTER, cwkss.KeyAction.DOWN), (cwkss.Key.ENTER, cwkss.KeyAction.UP), "Another text.", (cwkss.Key.ENTER, cwkss.KeyAction.DOWN), (cwkss.Key.ENTER, cwkss.KeyAction.UP))
        #cwkss.send_to_window("Path of Exile", cwkss.Key.ENTER, "/kills", cwkss.Key.ENTER)
        #cwkss.send_to_window("Path of Exile", cwkss.ModeID.POST, cwkss.Key.ENTER, "/kills", cwkss.Key.ENTER, cwkss.Wait(0.1))

        pass
    except cwkss.Fail as fail:
        print(fail)

