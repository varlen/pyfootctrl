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

### Bluetooth Support

Currently, direct BLE connectivity is not implemented and not tested using Loop MIDI. It may be possible to implement it using `bleak` but it is not a priority.