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
            print(msg)
            midi_out.send_message(msg)
        else:
            msg = midi_message.control_change(channel, control, off_cc_value)
            print(msg)
            midi_out.send_message(msg)

    return toggle_behaviour_call

def tap_tempo_behaviour(channel=0, control=20, taps=4, reset_after=1, transform=None):

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

