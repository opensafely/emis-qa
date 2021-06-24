import shutil

import utils

if __name__ == "__main__":
    f_in = utils.OUTPUT_DIR / "input.feather"
    f_out = utils.OUTPUT_DIR / "input-last.feather"
    print(f"Copying from {f_in} to {f_out}")
    shutil.copy(f_in, f_out)
