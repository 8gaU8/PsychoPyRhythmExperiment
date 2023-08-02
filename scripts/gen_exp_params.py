import random
from pathlib import Path

import numpy as np

NB_EXP = 5
NB_TRIALS = 3

INITIAL_SEED = 2

MOVE_MSGS = "MOVE"
STOP_MSGS = "DON'T MOVE"
REST_MSGS = "REST"


def main():
    content = "trials_file_name\n"
    for exp in range(NB_EXP):
        line = f"exp_params/{exp}.csv\n"
        content += line

    with open("./exp_params/session.csv", "w") as f:
        f.write(content)

    seed = INITIAL_SEED

    param_dir = Path("exp_params")
    param_dir.mkdir(exist_ok=True)
    for seed in range(NB_EXP):
        file_name = param_dir / f"{seed}.csv"

        np.random.seed(seed)
        delays_ary = np.random.normal(loc=0, scale=0.1, size=NB_TRIALS)

        b_ary = (delays_ary < 0).astype("int") * (-1)
        n_ary = (delays_ary > 0).astype("int")
        ans_ary = b_ary + n_ary
        ans_ary = ans_ary.astype("U")
        ans_ary[(ans_ary == "-1")] = "b"
        ans_ary[(ans_ary == "1")] = "n"

        np.random.seed(seed * 10)
        scale_ary = np.random.normal(loc=1, scale=0.1, size=NB_TRIALS)

        random.seed(seed * 20)
        msgs_ary = (
            [MOVE_MSGS] * 66
            + [STOP_MSGS] * 66
            + [REST_MSGS] * 66
            + random.choices((MOVE_MSGS, STOP_MSGS, REST_MSGS), k=2)
        )
        random.shuffle(msgs_ary)

        file_content = "delay,scale,ans,msg\n"
        for delay, scale, ans, msg in zip(delays_ary, scale_ary, ans_ary, msgs_ary):
            text = f"{delay},{scale},{ans},{msg}\n"
            file_content += text

        with open(file_name, "w") as f:
            f.write(file_content)


if __name__ == "__main__":
    main()
