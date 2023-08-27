from time import sleep

from rhythm_trial_code.main import run_stim
from rhythm_trial_code.serial_trigger import init_port
from rhythm_trial_code.message import PlayFactories as _PF


def main():
    port = init_port("COM03", dummy=True)
    _play_trigger_meta = _PF([]).trig_fctr(port, [4])
    play_trigger_meta = lambda: _play_trigger_meta(True)

    play_trigger_meta()

    try:
        run_stim(
            port=port,
            delay=-0.5,
            scale=0.8,
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
