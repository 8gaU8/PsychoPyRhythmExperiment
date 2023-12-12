from time import sleep
import time

from rhythm_trial_code.main import build_stim, play_stim
from rhythm_trial_code.message import PlayFactories as _PF
from rhythm_trial_code.serial_trigger import init_port


def main():
    port = init_port("COM3", dummy=False)
    _play_trigger_meta = _PF([]).trig_fctr(port, [4])
    play_trigger_meta = lambda: _play_trigger_meta(True)
    play_trigger_meta()

    try:
        delay = -0.152690
        delay = -0.2
        scale = 1.2

        stim = build_stim(
            port,
            delay=delay,
            scale=scale,
            soundfiles=["./sound/SD1010.WAV", "./sound/SD0050.WAV"],
        )
        t0 = time.time()
        play_stim(stim_series=stim, sound=True)
        print(time.time() - t0)
        sleep(1.0)
    finally:
        port.write([0])
        port.close()
    sleep(1)


if __name__ == "__main__":
    import os
    from pathlib import Path

    os.chdir(Path(__file__).parent)
    main()
