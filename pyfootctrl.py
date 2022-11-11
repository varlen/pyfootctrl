import rtmidi # https://spotlightkid.github.io/python-rtmidi/
from collections import defaultdict
from behaviours import null_behaviour, toggle_behaviour
from chocolate import display

# get loop midi at https://www.tobias-erichsen.de/software/loopmidi.html
# midiberry for BLE https://apps.microsoft.com/store/detail/midiberry/9N39720H2M05?hl=pt-br&gl=br

midi_in = rtmidi.MidiIn()
in_ports_by_name = midi_in.get_ports()

midi_out = rtmidi.MidiOut()
out_ports_by_name = midi_out.get_ports()

print("Available MIDI IN ports:", '\n'.join([ f'{number} -> {name}' for number,name in enumerate(in_ports_by_name)]), sep='\n')
print()
print("Available MIDI OUT ports:", '\n'.join([ f'{number} -> {name}' for number,name in enumerate(out_ports_by_name)]), sep='\n')
print()

in_port = int(input("Input port number:"))
out_port = int(input("Output port number:"))

midi_in.open_port(in_port)
midi_out.open_port(out_port)

print(f"Input: {in_ports_by_name[in_port]} | Output: {out_ports_by_name[out_port]}")

# behaviours per switch
behaviour = defaultdict(null_behaviour)

behaviour['1A'] = toggle_behaviour(channel=0, control=20, off_cc_value=1)
behaviour['1B'] = toggle_behaviour(channel=0, control=21, off_cc_value=1)

def start_midi_loop():
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
    start_midi_loop()


