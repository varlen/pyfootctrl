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