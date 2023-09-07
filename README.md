# PyFootCtrl

PyFootCtrl is a homebrew companion application for M-VAVE Chocolate Footswitch Controller written in Python.

It allows implementing custom behaviours for each footswitch press, organized by the default banks, without using any other companion apps.

### Installation

PyFootCtrl requires python-rtmidi and [loop midi](https://www.tobias-erichsen.de/software/loopmidi.html) (at least on windows, on other OSs you may use another loopback interface or even modify the code to create a virtual MIDI port directly)

Create a virtualenv and activate it, then:
```
pip install python-rtmidi
```

Then, execute it with
```
python pyfootctrl.py
```

### Customizing

It is possible to define custom behaviors for each of the switches in each of the banks.

Behaviors are defined in `config.py` and their implementation are functions in `behaviours.py`.

Behaviours yields functions. In other words, it is a function that returns a function. The created function must have two parameters: midi_out and delta. midi_out is the rtmidi object of the midi output device and allows writing MIDI data to said device. Delta is the time elapsed since the last switch press and is useful for time dependant behaviours.

There are two builtin behavior templates:

- **toggle** - Allows defining two distinct control values for ON and OFF and alternates the output value between each press of the switch. It is used for turning stuff ON and OFF.

- **tap tempo** - Allows outputting a control value that is proportional to the time between a predefined number of pedal presses. It requires tunning according to the range of time values accepted by the application and currently have predefined support for both Reaper JS delay effect and BYOD delay.

- **keyboard** - Allows performing keystrokes from footswitch presses. It requires `pynput` to work. It is possible to send a single key, or a combination of a key plus `Ctrl` or `Shift`.

These behaviors are mainly useful for musical applications but nothing prevents you from coding behaviors to perform any other action in the computer instead of MIDI output.

Custom coded behaviours must not do heavy work (things that take at least hundreds of milliseconds) inside the behavior callback. This is because right now the whole program runs synchronously.This is ok for most purposes since input speed will be limited to how fast someone can press the footswitches.

### Limitations

#### Bluetooth

Currently, Bluetooth support depends entirely on the OS. It should work properly if the OS exposes a MIDI device when connected over Bluetooth.

This program currently does not implement direct BLE handling but it may be possible to implement using [bleak](https://github.com/hbldh/bleak).

So far, it didn't work on Windows 10 but it did work on Linux.

#### Pedal Input

Since I didn't have a pedal here to test, the pedal support is not implemented yet.
