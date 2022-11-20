import rtmidi # https://spotlightkid.github.io/python-rtmidi/
from collections import defaultdict
from behaviours import null_behaviour, toggle_behaviour, tap_tempo_behaviour
from transforms import seconds_to_reaper_js_delay_midi_cc
from chocolate import display

# get loop midi at https://www.tobias-erichsen.de/software/loopmidi.html
# midiberry for BLE https://apps.microsoft.com/store/detail/midiberry/9N39720H2M05?hl=pt-br&gl=br

midi_in = rtmidi.MidiIn()
in_ports_by_name = midi_in.get_ports()

midi_out = rtmidi.MidiOut()
out_ports_by_name = midi_out.get_ports()

def display_midi_ports():
    print("Available MIDI IN ports:", '\n'.join([ f'{number} -> {name}' for number,name in enumerate(in_ports_by_name)]), sep='\n')
    print()
    print("Available MIDI OUT ports:", '\n'.join([ f'{number} -> {name}' for number,name in enumerate(out_ports_by_name)]), sep='\n')
    print()

def user_input_midi_ports():
    in_port = int(input("Input port number:"))
    out_port = int(input("Output port number:"))
    print(f"Input: {in_ports_by_name[in_port]} | Output: {out_ports_by_name[out_port]}")
    return in_port, out_port

def default_midi_ports():
    """
    Return the default MIDI ports indexes, with MIDI IN as USB-Midi and MIDI OUT as loopMIDI
    """

    DEFAULT_MIDI_IN_PORT_NAME = 'USB-Midi'
    DEFAULT_MIDI_OUT_PORT_NAME = 'loopMIDI'
    for index, port_name in enumerate(in_ports_by_name):
        if DEFAULT_MIDI_IN_PORT_NAME in port_name:
            in_port_index = index
            break
    for index, port_name in enumerate(out_ports_by_name):
        if DEFAULT_MIDI_OUT_PORT_NAME in port_name:
            out_port_index = index
            break
    return in_port_index, out_port_index



# behaviours per switch
behaviour = defaultdict(null_behaviour)

behaviour['1A'] = toggle_behaviour(channel=0, control=20, off_cc_value=1)
behaviour['1B'] = toggle_behaviour(channel=0, control=21, off_cc_value=1)
behaviour['1C'] = toggle_behaviour(channel=0, control=22, off_cc_value=1)
behaviour['1D'] = tap_tempo_behaviour(channel=0, control=23, reset_after=4.001, transform=seconds_to_reaper_js_delay_midi_cc)

def start_midi_loop(midi_in, midi_out):
    print("Starting MIDI message processing loop...")
    while True:
        message = midi_in.get_message()
        if message:
            try:
                ([midi_msg_type, midi_msg_data], delta_seconds) = message
                footswitch = display(midi_msg_data)
                print(f"{footswitch} | {midi_msg_type} | {midi_msg_data} | {delta_seconds:0.000f}s")
                behaviour[footswitch](midi_out, delta_seconds)
            except ValueError as e:
                print(e)
                print(message)

if __name__ == '__main__':
    in_port, out_port = default_midi_ports()
    midi_in.open_port(in_port)
    midi_out.open_port(out_port)
    start_midi_loop(midi_in, midi_out)


