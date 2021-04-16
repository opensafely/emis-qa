import shutil

from common_variables import OUTPUT_DIR

if __name__ == "__main__":
    f_in = OUTPUT_DIR / "input.feather"
    f_out = OUTPUT_DIR / "input-last.feather"
    print(f"Copying from {f_in} to {f_out}")
    shutil.copy(f_in, f_out)
