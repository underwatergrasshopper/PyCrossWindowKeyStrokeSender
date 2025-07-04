﻿import PyCrossWindowKeyStrokeSender as cwkss
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

        ### README.md ###

        # Input Example 1
        if False:
            cwkss.send_to_window(
                "Untitled - Notepad", 
                "Some Text.\nOther text.\n",
                0.1
            )

        # Input Example 2
        if False:
            # Note: Enters as text won't work.
            cwkss.send_to_window(
                "*new 41 - Notepad++", 
                U"Some Text.\r\nOther text.\r\nф𤭢\n",
                1)
        
        # Input Example 3
        if True:
            cwkss.send_to_window(
                "Untitled - Notepad", 
                "Some Text.",
                cwkss.Key.ENTER,
                "Other Text.",
                cwkss.Key.ENTER,
                "ф𤭢",
                method = cwkss.Method.SEND)
            
        # Input Example 3.5
        if False:
            cwkss.send_to_window("Path of Exile", cwkss.Key.ENTER, "/kills", cwkss.Key.ENTER, delay = 0.05)

        # Input Example 4
        if False:
            cwkss.send_to_window(
                "Untitled - Notepad", 
                cwkss.Delay(0.01),
                cwkss.Input("Some Text."),
                cwkss.Input(cwkss.Key.ENTER),
                cwkss.Input("Other Text."),
                cwkss.Input(cwkss.Key.ENTER),
                cwkss.Wait(0.1))

        # Input Example 5
        if False:
            cwkss.send_to_window(
                "Untitled - Notepad", 
                cwkss.Input(
                    (cwkss.Key.RALT, cwkss.KeyState.DOWN),
                    cwkss.Key.S,
                    (cwkss.Key.RALT, cwkss.KeyState.UP)),
                cwkss.Wait(0.1))

        # Input Example 6
        if False:
            cwkss.send_to_window(
                "Path of Exile", 
                cwkss.Input(
                    cwkss.Key.ENTER,
                    "/kills",
                    cwkss.Key.ENTER),
                cwkss.Wait(0.1))

        # Send Example 1
        if False:
            cwkss.send_to_window(
                "Untitled - Notepad", 
                "Some Text.\nOther text.\n")

        # Send Example 2
        if False:
            cwkss.send_to_window(
                "Untitled - Notepad", 
                cwkss.UTF16,
                U"Some Text.\nOther text.\nф𤭢\n")

        # Send Example 3
        if False:
            cwkss.send_to_window(
                "Untitled - Notepad", 
                "Some Text.\n",
                "Other Text.\n")

        # Send Example 4
        if False:
            cwkss.send_to_window(
                "Path of Exile", 
                cwkss.Key.ENTER,
                "/kills",
                cwkss.Key.ENTER)

        # Post Example 1
        if False:
            cwkss.send_to_window(
                "Untitled - Notepad", 
                cwkss.POST,
                cwkss.Delay(0.01),
                "Some Text.\nOther text.\n")

        # Post Example 2
        if False:
            cwkss.send_to_window(
                "Untitled - Notepad", 
                cwkss.UTF16,
                cwkss.POST,
                cwkss.Delay(0.01),
                U"Some Text.\nOther text.\nф𤭢\n")

        # Post Example 3
        if False:
            cwkss.send_to_window(
                "Untitled - Notepad", 
                cwkss.POST,
                cwkss.Delay(0.01),
                "Some Text.\n",
                "Other Text.\n")

        # Post Example 4
        if False:
            cwkss.send_to_window(
                "Path of Exile", 
                cwkss.POST,
                cwkss.Delay(0.01),
                cwkss.Key.ENTER,
                "/kills",
                cwkss.Key.ENTER)

        pass
    except cwkss.Fail as fail:
        print(fail)

