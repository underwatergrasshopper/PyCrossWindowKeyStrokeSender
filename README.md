# PyCrossWindowKeyStrokeSender
Simple module which provides ability to send a key messages or text messages from one window to another window.
Any of both windows can be either an application window or a console window.

It's designed for sending short messages, which have around 1000 character or keystrokes.

It might be used for:
- Sending command to other window. For example, to a video game or specific console window.
- Sending text messages to open text editor.

Module is exclusively for operating systems from Windows family (Windows 7/8/10).

## Install

Go to releases section and download last release package with `tar.gz` extension.
Run `pip install PyCrossWindowKeyStrokeSender-<version>.tar.gz` in directory where is the package.

*Note: The `<version>` in install command need to be replaced with a version of the package.*

## Unistall

Run `pip uninstall PyCrossWindowKeyStrokeSender`.

# Message Delivery Method
Library uses three message delivery methods: Input, Send, Post

## Input Delivery Method
Input delivery method simulates keyboard input messages. Messages are delivered as they would be pressed on keyboard. 
After sending input message, a wait time (`cwkss.Wait(time_in_seconds)`) is required to be relatively sure if message is processed by target window.
If multiple input messages are send, setting delay time (`cwkss.Delay(time_in_seconds)`) is required. 
Delay makes `send_to_window` function to wait a given amount of time after sending each input message, to relatively prevent collision of processing input messages.
Function `send_to_window` must be called from main thread of application.
Using this method is most recommended.

*Note: Setting correct amount of time in `Delay` action and `Wait` action depends on: size of messages, speed of processor, reactability of target window.*

### Input Example 1
Sends text message to Notepad window as single text message.
```python
import PyCrossWindowKeyStrokeSender as cwkss

cwkss.send_to_window(
    "Untitled - Notepad", 
    cwkss.Input("Some Text.\nOther text.\n"),
    cwkss.Wait(0.1))
```

### Input Example 2
Sends text message in utf-16 encoding format to Notepad window as single text message.
```python
import PyCrossWindowKeyStrokeSender as cwkss

cwkss.send_to_window(
    "Untitled - Notepad", 
    cwkss.Input(U"Some Text.\nOther text.\nф𤭢\n"),
    cwkss.Wait(0.1))
```

### Input Example 3
Sends text message to Notepad window as single input of multiple messages.
```python
import PyCrossWindowKeyStrokeSender as cwkss

cwkss.send_to_window(
    "Untitled - Notepad", 
    cwkss.Input(
        "Some Text.",
        cwkss.Key.ENTER,
        "Other Text.",
        cwkss.Key.ENTER),
    cwkss.Wait(0.1))
```

### Input Example 4
Sends text message to Notepad window as multiple inputs of single messages.
```python
import PyCrossWindowKeyStrokeSender as cwkss

 cwkss.send_to_window(
     "Untitled - Notepad", 
     cwkss.Delay(0.01),
     cwkss.Input("Some Text."),
     cwkss.Input(cwkss.Key.ENTER),
     cwkss.Input("Other Text."),
     cwkss.Input(cwkss.Key.ENTER),
     cwkss.Wait(0.1))
```

### Input Example 5
Sends `ś` character to Notepad window by using key sequence.
```python
import PyCrossWindowKeyStrokeSender as cwkss

cwkss.send_to_window(
    "Untitled - Notepad", 
    cwkss.Input(
        (cwkss.Key.RALT, cwkss.KeyState.DOWN),
        cwkss.Key.S,
        (cwkss.Key.RALT, cwkss.KeyState.UP)),
    cwkss.Wait(0.1))
```

### Input Example 6
Sends `/kills` command to "Path of Exile" game window.
```python
import PyCrossWindowKeyStrokeSender as cwkss

cwkss.send_to_window(
    "Path of Exile", 
    cwkss.Input(
        cwkss.Key.ENTER,
        "/kills",
        cwkss.Key.ENTER),
    cwkss.Wait(0.1))
```

## Send Delivery Method
Allows to send key messages and text messages to target window. For each message sent, `send_to_window` function waits until message is processed by target window.
Sending messages might take some time. Setting delay time or wait time is NOT required.
Function `send_to_window` must be called from main thread of application.

### Send Example 1
Sends text message to Notepad window as single text message.
```python
import PyCrossWindowKeyStrokeSender as cwkss

cwkss.send_to_window(
    "Untitled - Notepad", 
    "Some Text.\nOther text.\n")
```

### Send Example 2
Sends text message in utf-16 encoding format to Notepad window as single message.
```python
import PyCrossWindowKeyStrokeSender as cwkss

cwkss.send_to_window(
    "Untitled - Notepad", 
    cwkss.UTF16,
    U"Some Text.\nOther text.\nф𤭢\n")
```

### Send Example 3
Sends text message to Notepad window as multiple messages.
```python
import PyCrossWindowKeyStrokeSender as cwkss

cwkss.send_to_window(
    "Untitled - Notepad", 
    "Some Text.\n",
    "Other Text.\n")
```

### Send Example 4
Sends `/kills` command to "Path of Exile" game window.
```python
import PyCrossWindowKeyStrokeSender as cwkss

cwkss.send_to_window(
    "Path of Exile", 
    cwkss.Key.ENTER,
    "/kills",
    cwkss.Key.ENTER)
```

## Post Delivery Method
Allows to send key messages and text messages to target window. Messages are sent to target window message queue before they are processed.
Setting delay time (`cwkss.Delay(time_in_seconds)`) is required. Delay makes `send_to_window` function to wait given amount of time after sending each message, to relatively prevent collision of processing messages.
Function `send_to_window` not necessary needs to be called from main thread of application.

If sent message seems to be crangled when arrives to target window, try using bigger value in `cwkss.Delay(time_in_seconds)` or `cwkss.Wait(time_in_seconds)` in `send_to_window` function.

*Note: Setting correct amount of time in `Delay` action and `Wait` action depends on: size of messages, speed of processor, reactability of target window.*

### Post Example 1
Sends text message to Notepad window as single text message.
```python
import PyCrossWindowKeyStrokeSender as cwkss

cwkss.send_to_window(
    "Untitled - Notepad", 
    cwkss.POST,
    cwkss.Delay(0.01),
    "Some Text.\nOther text.\n")
```

### Post Example 2
Sends text message in utf-16 encoding format to Notepad window as single message.
```python
import PyCrossWindowKeyStrokeSender as cwkss

cwkss.send_to_window(
    "Untitled - Notepad", 
    cwkss.UTF16,
    cwkss.POST,
    cwkss.Delay(0.01),
    U"Some Text.\nOther text.\nф𤭢\n")
```

### Post Example 3
Sends text message to Notepad window as multiple messages.
```python
import PyCrossWindowKeyStrokeSender as cwkss

cwkss.send_to_window(
    "Untitled - Notepad", 
    cwkss.POST,
    cwkss.Delay(0.01),
    "Some Text.\n",
    "Other Text.\n")
```

### Post Example 4
Sends `/kills` command to "Path of Exile" game window.
```python
import PyCrossWindowKeyStrokeSender as cwkss

cwkss.send_to_window(
    "Path of Exile", 
    cwkss.POST,
    cwkss.Delay(0.01),
    cwkss.Key.ENTER,
    "/kills",
    cwkss.Key.ENTER)
```