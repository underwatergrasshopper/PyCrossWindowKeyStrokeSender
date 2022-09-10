# PyCrossWindowKeyStrokeSender
Small module which provides ability to send a key messages or text messages to chosen window.

There are three ways of sending message to window: Input, Send, Post.

If one of the method do not work, try another. Input method is most reliable.

*Note: For Input and Send methods, `send_to_window` functions should be called from main thread. 
Sometimes callback functions are called from non main threads. In this case, Input and Sent methods might not work, if `send_to_window` function is called from that callback function.*

---

## Input
Simulates keyboard key strokes. 

### Game Input Example

Sends `/kills` command to "Path of Exile" game window. 
At the end waits (`cwkss.Wait(0.1)`) for some amount of time to give the target window a time to process messages. 

*Note: The given wait time depends on: length of messages, speed of the processor, target window reactability.*

```python
import PyCrossWindowKeyStrokeSender as cwkss

cwkss.send_to_window(
    "Path of Exile", 
    cwkss.Input(cwkss.Key.ENTER, "/kills", cwkss.Key.ENTER), 
    cwkss.Wait(0.1))
```

If multiple input messages are sent, delay (`Delay(0.01)`) should be set. 
It makes `send_to_window` function to wait, after each sent input message, a delay time before sending another message to make relatively sure, those messages do not collide with each other.

```python
import PyCrossWindowKeyStrokeSender as cwkss

cwkss.send_to_window(
    "Path of Exile", 
    cwkss.Delay(0.01),
    cwkss.Input(cwkss.Key.ENTER, "/kills", cwkss.Key.ENTER), 
    cwkss.Input(cwkss.Key.ENTER, "/played", cwkss.Key.ENTER), 
    cwkss.Wait(0.1))
```

It can be send as one long message also. 

*Note: It needs to be remembered, for very long single input messages, a wait time (`cwkss.Wait(0.1)`) needs to be adjusted.*

```python
import PyCrossWindowKeyStrokeSender as cwkss

cwkss.send_to_window(
    "Path of Exile", 
    cwkss.Input(cwkss.Key.ENTER, "/kills", cwkss.Key.ENTER, cwkss.Key.ENTER, "/played", cwkss.Key.ENTER), 
    cwkss.Wait(0.1))
```

### Notepad Input Example

Sends capital a.

```python
import PyCrossWindowKeyStrokeSender as cwkss

cwkss.send_to_window("Untitled - Notepad", cwkss.Input("A"), cwkss.Wait(0.1))
```

```python
import PyCrossWindowKeyStrokeSender as cwkss

cwkss.send_to_window(
    "Untitled - Notepad", 
    cwkss.Delay(0.1), 
    cwkss.Input(
        (cwkss.Key.SHIFT, cwkss.KeyState.DOWN), 
        (cwkss.Key.A), 
        (cwkss.Key.SHIFT, cwkss.KeyState.UP)), 
    cwkss.Wait(0.1))
```

Sends ś.

```python
import PyCrossWindowKeyStrokeSender as cwkss

cwkss.send_to_window("Untitled - Notepad", cwkss.Input(u"ś"), cwkss.Wait(0.1))
```

```python
import PyCrossWindowKeyStrokeSender as cwkss

cwkss.send_to_window(
    "Untitled - Notepad", 
    cwkss.Input(
        (cwkss.Key.RALT, cwkss.KeyState.DOWN), 
        (cwkss.Key.S), 
        (cwkss.Key.RALT, cwkss.KeyState.UP)),  
    cwkss.Wait(0.1))
```

Sends two lines of text.
```python
import PyCrossWindowKeyStrokeSender as cwkss

cwkss.send_to_window("Untitled - Notepad", cwkss.Input("Some text.\nAnother text.\n"), cwkss.Wait(0.1))
```

```python
import PyCrossWindowKeyStrokeSender as cwkss

cwkss.send_to_window(
    "Untitled - Notepad", 
    cwkss.Delay(0.01), 
    cwkss.Input(
        "Some text.", 
        cwkss.Key.ENTER, 
        "Another text.", 
        cwkss.Key.ENTER), 
    cwkss.Wait(0.1))
```

---

## Sent
Sends text messages or key messages (does not simulate key strokes) directly to window and for each message separately waits until it's processed by target window.

Sends `/kills` command to "Path of Exile" game window. 
At the end waits (`cwkss.Wait(0.1)`) for some amount of time to give the target window a time to process messages. 

*Note: The given wait time depends on: length of messages, speed of the processor, target window reactability.*

```python
import PyCrossWindowKeyStrokeSender as cwkss

cwkss.send_to_window("Path of Exile", cwkss.Key.ENTER, "/kills", cwkss.Key.ENTER, cwkss.Wait(0.1))
```

Sends `/kills` command and `/played` command to "Path of Exile" game window. 
```python
import PyCrossWindowKeyStrokeSender as cwkss

cwkss.send_to_window(
    "Path of Exile", 
    
    cwkss.Key.ENTER, 
    "/kills", 
    cwkss.Key.ENTER, 
    
    cwkss.Key.ENTER, 
    "/played", 
    cwkss.Key.ENTER, 
    
    cwkss.Wait(0.1))
```

---

### Post
Sends text or key messages to target window message queue, where they waits to be executed. **Can be called from non main thread.**

Sends `/kills` command to "Path of Exile" game window. 
If multiple messages are sent, delay (`Delay(0.01)`) should be set. 
It makes send_to_window function waits, after each sent message, a delay time, before sending another message, to make relatively sure, those messages do not collide with each other.
At the end waits (`cwkss.Wait(0.1)`) for some amount of time to give the target window a time to process messages. 

*Note: The given wait time depends on: length of messages, speed of the processor, target window reactability.*

```python
import PyCrossWindowKeyStrokeSender as cwkss

cwkss.send_to_window(
    "Path of Exile", 
    cwkss.POST, 
    cwkss.Delay(0.01), 
    cwkss.Key.ENTER, 
    "/kills", 
    cwkss.Key.ENTER, 
    cwkss.Wait(0.1))
```