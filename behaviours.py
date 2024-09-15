import midi_message

def null_behaviour():
    """
    This is the default behaviour for all footswitches and will not do anything when called. 
    """
    def null_behaviour_call(midi_out, delta):
        print("Do nothing.")

    return null_behaviour_call

def toggle_behaviour(channel=0, control=20, on_cc_value=127, off_cc_value=0):

    state = False

    def toggle_behaviour_call(midi_out, delta):
        nonlocal state
        state = not state
        if state:
            msg = midi_message.control_change(channel, control, on_cc_value)
            midi_out.send_message(msg)
            print(msg)
        else:
            msg = midi_message.control_change(channel, control, off_cc_value)
            midi_out.send_message(msg)
            print(msg)

    return toggle_behaviour_call

def trigger_note_behaviour(channel=0, note=midi_message.MIDDLE_C, velocity=127, release_velocity=127):

    def trigger_note_behaviour_call(midi_out, delta):

        msg = midi_message.note_on(channel, note, velocity)
        midi_out.send_message(msg)
        msg = midi_message.note_off(channel, note, release_velocity)
        midi_out.send_message(msg)
        print("[TRIGGER NOTE]", msg)

    return trigger_note_behaviour_call

def toggle_note_behaviour(channel=0, note=midi_message.MIDDLE_C, velocity=127, release_velocity=127):
    state = False
    def toggle_note_behaviour_call(midi_out, delta):
        nonlocal state
        state = not state
        if state:
            msg = midi_message.note_on(channel, note, velocity)
            midi_out.send_message(msg)
            print(msg)
        else:
            msg = midi_message.note_off(channel, note, release_velocity)
            midi_out.send_message(msg)
            print(msg)

    return toggle_note_behaviour_call


def tap_tempo_behaviour(channel=0, control=20, taps=4, reset_after=1, transform=None):
    """
    Allows using the footswitch as a tap tempo control.
    """
    deltas = []

    def tap_tempo_behaviour_call(midi_out, delta):
        nonlocal deltas

        if delta > reset_after:
            deltas.clear()

        if deltas:
            deltas.append(delta)
        else:
            deltas.append(0)

        if len(deltas) == taps:
            print(deltas)
            mean = sum(filter(lambda d : d > 0, deltas)) / (taps - 1)
            bpm = int(600 / mean) / 10

            if transform:
                cc_value = transform(mean)
                msg = midi_message.control_change(channel, control, cc_value)
                midi_out.send_message(msg)
            else:
                print(f'{bpm} BPM')

            deltas.clear()

    return tap_tempo_behaviour_call

def keyboard_behaviour(key, ctrl=False, shift=False):
    """
    Allows using the footswitch to perform keypresses
    """
    from pynput.keyboard import Key, Controller
    keyboard = Controller()

    def keyboard_behaviour_call(midi_out, delta):
        if ctrl:
            keyboard.press(Key.ctrl)
        if shift:
            keyboard.press(Key.shift)
        keyboard.press(key)
        keyboard.release(key)
        if ctrl:
            keyboard.release(Key.ctrl)
        if shift:
            keyboard.release(Key.shift)

    return keyboard_behaviour_call
