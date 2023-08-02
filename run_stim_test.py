from serial import Serial

from rhythm_trial_code.dummy_serial import Serial
from rhythm_trial_code.main import run_stim


def main():
    port = Serial("COM03")
    port.write([0])
    try:
        run_stim(port, 0.2, scale=0.8, stim_sound_file="./sound/SD0050.WAV", sound=True)
    finally:
        port.write([0])
        port.close()


if __name__ == "__main__":
    import os
    from pathlib import Path

    os.chdir(Path(__file__).parent)
    main()
