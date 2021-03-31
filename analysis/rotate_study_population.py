import shutil
from pathlib import Path

BASE_DIR = Path("output")

if __name__ == "__main__":
    f_in = BASE_DIR / "input.feather"
    f_out = BASE_DIR / "input-last.feather"
    print(f"Copying from {f_in} to {f_out}")
    shutil.copy(f_in, f_out)
