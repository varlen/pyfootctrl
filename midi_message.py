from notes import MIDDLE_C

def _build(message_type, channel, control_index, value):
    if channel > 15 or channel < 0:
        raise AssertionError("Channel must be a value between 0 and 15")
    if control_index < 0 or control_index > 120:
        raise AssertionError("Control index must be between 0 and 120")
    if value < 0 or value > 127:
        raise AssertionError("Value must be between 0 and 127")

    message_type_with_channel = message_type | channel
    return [ message_type_with_channel, control_index, value ]

def control_change(channel, control_index, value):
    return _build(0b1011_0000, channel, control_index, value)

def note_on(channel, note, velocity):
    return _build(0x90, channel, note, velocity)

def note_off(channel, note, velocity):
    return _build(0x80, channel, note, velocity)
