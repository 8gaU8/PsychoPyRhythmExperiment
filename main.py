import logging
import time

import numpy as np

from config import BASE_MSGS, BASE_TIME, PROBE_TONE, TIGGER_MSGS
from rhythm_trial_code.message import Message, get_stim_series
from rhythm_trial_code.utils import init_sound_player, wait_until


def run_stim(delay, scale):
    Message.time_scale = scale
    stim_sound_file = "./sound/SD0050.WAV"
    init_sound_player(stim_sound_file=stim_sound_file)

    stim_series = get_stim_series(
        base_msgs=BASE_MSGS,
        base_times=BASE_TIME,
        trigger_msgs=TIGGER_MSGS,
        probe_tone=PROBE_TONE,
        probe_delay=delay,
    )
    print(stim_series)

    error_list = []

    start_time = time.time()
    for msg in stim_series:
        wait_until(start_time + msg.time)
        msg.play()
        logging.info(msg)
        error_list.append((time.time() - start_time) - msg.time)

    diff_array = np.array(error_list)
    mean = diff_array.mean()
    std = diff_array.std()

    print(f"error is {mean} ± {std} sec")
    return start_time, stim_series[-1].time


def main():
    print(run_stim(-0.2, 1.61973499606565001))
    time.sleep(1)


if __name__ == "__main__":
    import os
    from pathlib import Path

    os.chdir(Path(__file__).parent)
    main()
