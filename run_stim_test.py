from time import sleep

from rhythm_trial_code.main import run_stim
from rhythm_trial_code.message import play_trigger_factory
from rhythm_trial_code.serial_trigger import init_port


def main():
    port = init_port("COM03", dummy=True)
    _play_trigger_meta = play_trigger_factory(port, [4])
    play_trigger_meta = lambda: _play_trigger_meta(True)
    play_trigger_meta()

    try:
        run_stim(port, 0.2, scale=1, stim_sound_file="./sound/SD0050.WAV", sound=True)
    finally:
        port.write([0])
        port.close()
    sleep(1)


if __name__ == "__main__":
    import os
    from pathlib import Path

    os.chdir(Path(__file__).parent)
    main()
