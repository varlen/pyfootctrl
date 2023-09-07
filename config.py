from collections import defaultdict

from transforms import *
from behaviours import null_behaviour, toggle_behaviour, tap_tempo_behaviour, keyboard_behaviour

behaviour = defaultdict(null_behaviour)

"""
Define the desired behaviours per preset slot here:
"""

behaviour['1A'] = toggle_behaviour(channel=0, control=20, off_cc_value=1)
behaviour['1B'] = toggle_behaviour(channel=0, control=21, off_cc_value=1)
behaviour['1C'] = toggle_behaviour(channel=0, control=22, off_cc_value=1)
behaviour['1D'] = tap_tempo_behaviour(channel=0, control=23, reset_after=4.001, transform=seconds_to_byod_delay_midi_cc)

behaviour['2A'] = keyboard_behaviour('r', ctrl=True)