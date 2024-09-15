from collections import defaultdict

from transforms import *
from behaviours import \
    null_behaviour, toggle_behaviour, tap_tempo_behaviour, \
        keyboard_behaviour, toggle_note_behaviour, trigger_note_behaviour

import notes

behaviour = defaultdict(null_behaviour)

"""
Define the desired behaviours per preset slot here:
"""

behaviour['1A'] = toggle_behaviour(channel=0, control=20, off_cc_value=1)
behaviour['1B'] = toggle_behaviour(channel=0, control=21, off_cc_value=1)
behaviour['1C'] = toggle_behaviour(channel=0, control=22, off_cc_value=1)
behaviour['1D'] = tap_tempo_behaviour(channel=0, control=23, reset_after=4.001, transform=seconds_to_reaper_js_delay_midi_cc)

#behaviour['2A'] = keyboard_behaviour('r', ctrl=True)
behaviour['2A'] = toggle_note_behaviour(channel=1, note=notes.Bb2)
behaviour['2B'] = toggle_note_behaviour(channel=1, note=notes.C2)
behaviour['2C'] = toggle_note_behaviour(channel=1, note=notes.D2)
behaviour['2D'] = toggle_note_behaviour(channel=1, note=notes.F2)

behaviour['3A'] = trigger_note_behaviour(channel=1, note=notes.MIDDLE_C - 24)
behaviour['3B'] = trigger_note_behaviour(channel=1, note=notes.MIDDLE_C - 24 + 1)
behaviour['3C'] = trigger_note_behaviour(channel=1, note=notes.MIDDLE_C - 24 + 2)
behaviour['3D'] = trigger_note_behaviour(channel=1, note=notes.MIDDLE_C - 24 + 3)