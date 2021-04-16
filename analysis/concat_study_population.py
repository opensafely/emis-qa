import re

import pandas
from common_variables import OUTPUT_DIR

DATE_REGEX = re.compile(r".*(?P<date>\d{4}-\d{2}-\d{2}).*")
DATE_FORMAT = "%Y-%m-%d"


def read_feather(f_path):
    date_str = re.match(DATE_REGEX, f_path.name).group("date")
    date_timestamp = pandas.to_datetime(date_str, format=DATE_FORMAT)
    return pandas.read_feather(f_path).assign(date=date_timestamp)


if __name__ == "__main__":
    in_dir = OUTPUT_DIR / "generate_study_population"

    pandas.concat(
        (read_feather(x) for x in in_dir.iterdir()),
        ignore_index=True,
    ).to_feather(OUTPUT_DIR / "input.feather")
