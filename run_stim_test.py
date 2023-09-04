from time import sleep

from rhythm_trial_code.main import run_stim
from rhythm_trial_code.message import PlayFactories as _PF
from rhythm_trial_code.serial_trigger import init_port


def main():
    port = init_port("COM03", dummy=True)
    _play_trigger_meta = _PF([]).trig_fctr(port, [4])
    play_trigger_meta = lambda: _play_trigger_meta(True)
    play_trigger_meta()

    try:
        delay = -0.152690
        delay = -0.2
        scale = 1.2
        run_stim(
            port,
            delay=delay,
            scale=scale,
            soundfiles=["./sound/SD1010.WAV", "./sound/SD0050.WAV"],
            sound=True,
        )
        sleep(1.0)
        scale = 1
        delay = 0
        run_stim(
            port,
            delay=delay,
            scale=scale,
            soundfiles=["./sound/SD1010.WAV", "./sound/SD0050.WAV"],
            sound=True,
        )
    finally:
        port.write([0])
        port.close()
    sleep(1)


if __name__ == "__main__":
    import os
    from pathlib import Path

    os.chdir(Path(__file__).parent)
    main()
