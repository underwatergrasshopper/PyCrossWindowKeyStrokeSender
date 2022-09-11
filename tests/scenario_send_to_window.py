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
import os

cwkss.enable_debug()

if __name__ == "__main__":
    try:
        # find window
        #cwkss.send_to_window("*Untitled - Notepad")
        #cwkss.send_to_window(b"*Untitled - Notepad")

        # undefined action type
        #cwkss.send_to_window("*Untitled - Notepad", (False))

        # send text ascii
        #cwkss.send_to_window("*Untitled - Notepad", cwkss.ASCII, "Some text.", "Other text.")
        #cwkss.send_to_window("*Untitled - Notepad", cwkss.ASCII, cwkss.SEND, "Some text.", "Other text.")
        #cwkss.send_to_window("*Untitled - Notepad", cwkss.ASCII, cwkss.POST, "Some text.", "Other text.")

        # send text utf-16
        #cwkss.send_to_window(b"*Untitled - Notepad", "Some text.\u0444", "Other text.\U00024B62")
        #cwkss.send_to_window("*Untitled - Notepad", cwkss.UTF16, "Some text.\u0444", "Other text.\U00024B62")
        #cwkss.send_to_window("*Untitled - Notepad", cwkss.UTF16, cwkss.SEND, "Some text.\u0444", "Other text.\U00024B62")
        #cwkss.send_to_window("*Untitled - Notepad", cwkss.UTF16, cwkss.POST, "Some text.\u0444", "Other text.\U00024B62")

        # wait
        #cwkss.send_to_window("*Untitled - Notepad", "Some text.", cwkss.Wait(3), "Another text.")

        # delay
        #cwkss.send_to_window("*Untitled - Notepad", cwkss.Delay(1.0), "One. ", "Two. ", "Three. ", "Four. ")

        # key
        #cwkss.send_to_window("*Untitled - Notepad", cwkss.POST, cwkss.Delay(0.1), "Some text.", cwkss.Key.ENTER, "Another text.", cwkss.Key.ENTER)
        #cwkss.send_to_window("*Untitled - Notepad", cwkss.ASCII, cwkss.POST, cwkss.Delay(0.1), "Some text.", cwkss.Key.ENTER, "Another text.", cwkss.Key.ENTER)
        #cwkss.send_to_window("*Untitled - Notepad", cwkss.UTF16, cwkss.POST, cwkss.Delay(0.1), "Some text.", cwkss.Key.ENTER, "Another text.", cwkss.Key.ENTER)
        #cwkss.send_to_window("*Untitled - Notepad", cwkss.POST, cwkss.Delay(0.1), "Some text.", (cwkss.Key.ENTER, cwkss.KeyState.DOWN), (cwkss.Key.ENTER, cwkss.KeyState.UP), "Another text.", (cwkss.Key.ENTER, cwkss.KeyState.DOWN), (cwkss.Key.ENTER, cwkss.KeyState.UP))
        #cwkss.send_to_window("Path of Exile", cwkss.Key.ENTER, "/kills", cwkss.Key.ENTER)
        #cwkss.send_to_window("Path of Exile", cwkss.POST, cwkss.Delay(0.01), cwkss.Key.ENTER, "/kills", cwkss.Key.ENTER)
        #cwkss.send_to_window("Path of Exile", cwkss.POST, cwkss.Key.ENTER, "/kills", cwkss.Key.ENTER, cwkss.Wait(0.1))

        #cwkss.send_to_window("Simple Window 안녕하세요", cwkss.Key.CTRL, cwkss.Key.SHIFT, cwkss.Wait(0.1))
        #cwkss.send_to_window("Simple Window 안녕하세요", cwkss.Key.LCTRL, cwkss.Key.RCTRL, cwkss.Key.LSHIFT, cwkss.Key.RSHIFT, cwkss.Wait(0.1))

        # key - unsupported keys fail - all this calls will fail
        #cwkss.send_to_window("Simple Window 안녕하세요", cwkss.Key.CTRL, cwkss.Key.ALT, cwkss.Key.SHIFT, cwkss.Wait(0.1))
        #cwkss.send_to_window("Simple Window 안녕하세요", cwkss.Key.LCTRL, cwkss.Key.RCTRL, cwkss.Key.LALT, cwkss.Key.RALT, cwkss.Key.LSHIFT, cwkss.Key.RSHIFT, cwkss.Wait(0.1))

        # input
        #cwkss.send_to_window("*Untitled - Notepad", cwkss.Delay(0.1), cwkss.Input("Some text.", cwkss.Key.ENTER, "Another text.\u0444\U00024B62", cwkss.Key.ENTER))
        #cwkss.send_to_window("*Untitled - Notepad", cwkss.Delay(0.1), cwkss.Input("Some text.", cwkss.Key.ENTER, "Another text.", cwkss.Key.ENTER))
        #cwkss.send_to_window("Path of Exile", cwkss.Input(cwkss.Key.ENTER, "/kills", cwkss.Key.ENTER), cwkss.Wait(0.1))

        # input - alt shift ctrl
        #cwkss.send_to_window("Simple Window 안녕하세요", cwkss.Input(cwkss.Key.CTRL, cwkss.Key.ALT, cwkss.Key.SHIFT), cwkss.Wait(0.1))

        # input - left|right alt shift ctrl
        #cwkss.send_to_window("Simple Window 안녕하세요", cwkss.Input(cwkss.Key.LCTRL, cwkss.Key.RCTRL, cwkss.Key.LALT, cwkss.Key.RALT, cwkss.Key.LSHIFT, cwkss.Key.RSHIFT), cwkss.Wait(0.1))

        # input - other extended keys
        #cwkss.send_to_window("Simple Window 안녕하세요", cwkss.Delay(0.1), cwkss.Input(cwkss.Key.HOME))

        # input - capital a
        #cwkss.send_to_window("*Untitled - Notepad", cwkss.Delay(0.1), cwkss.Input((cwkss.Key.SHIFT, cwkss.KeyState.DOWN), (cwkss.Key.A), (cwkss.Key.SHIFT, cwkss.KeyState.UP)))

        # input - ś
        #cwkss.send_to_window("*Untitled - Notepad", cwkss.Delay(0.1), cwkss.Input(
        #    (cwkss.Key.RALT, cwkss.KeyState.DOWN), 
        #    (cwkss.Key.S), 
        #    (cwkss.Key.RALT, cwkss.KeyState.UP),
        #))

        # input - ś by using Ctrl + Alt
        #cwkss.send_to_window("*Untitled - Notepad", cwkss.Delay(0.1), cwkss.Input(
        #    (cwkss.Key.CTRL, cwkss.KeyState.DOWN), 
        #    (cwkss.Key.ALT, cwkss.KeyState.DOWN), 
        #    (cwkss.Key.S), 
        #    (cwkss.Key.ALT, cwkss.KeyState.UP),
        #    (cwkss.Key.CTRL, cwkss.KeyState.UP)
        #))

        # input - double backspace
        #cwkss.send_to_window("*Untitled - Notepad", cwkss.Delay(0.1), cwkss.Input(cwkss.Key.BACKSPACE, cwkss.Key.BACKSPACE))


        # other
        #cwkss.send_to_window("Untitled - Notepad", "Some text.\nAnother text.\n", cwkss.Wait(0.1))
        #cwkss.send_to_window("Untitled - Notepad", cwkss.Delay(0.01), cwkss.Input("Some text.", cwkss.Key.ENTER, "Another text.", cwkss.Key.ENTER), cwkss.Wait(0.1))

        #cwkss.send_to_window("Path of Exile", cwkss.Input(cwkss.Key.ENTER, "/kills", cwkss.Key.ENTER), cwkss.Wait(0.1))

        #cwkss.send_to_window("Command Prompt", cwkss.Wait(1), cwkss.Input("notepad"), cwkss.Wait(1), cwkss.Input(cwkss.Key.ENTER), cwkss.Wait(0.1))
        #cwkss.send_to_window("Untitled - Notepad", cwkss.Wait(1), cwkss.Delay(2), "Some text.\n", "Another text.", "\n\u0444\U00024B62", cwkss.Wait(0.1))


        pass
    except cwkss.Fail as fail:
        print(fail)

