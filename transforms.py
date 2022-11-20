def seconds_to_reaper_js_delay_midi_cc(seconds):
    """
    Transforms a value in seconds between 0 and 4
    to a integer value between 0 and 127.

    This code may be adapted to work with another delay plugin
    by changing the max time from 4000 to the max time of the plugin
    """
    cc_out = (127 / 4000) * seconds * 1000
    if cc_out > 127:
        cc_out = 127
    if cc_out < 0:
        cc_out = 0
    return int(cc_out)