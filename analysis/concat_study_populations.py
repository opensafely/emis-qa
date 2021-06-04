import pandas
import utils

AGE_GROUP_WIDTH = 10


def read_feather(f_path):
    return pandas.read_feather(f_path).assign(f_name=f_path.name)


def get_records():
    records = pandas.concat(
        read_feather(x)
        for x in [
            utils.OUTPUT_DIR / "input.feather",
            utils.OUTPUT_DIR / "input-last.feather",
        ]
    )

    # From Int64Index to RangeIndex (the default)
    records = records.reset_index(drop=True)

    records["f_name"] = records["f_name"].astype("category")

    assert records.set_index(["f_name", "patient_id"]).index.is_unique

    return records


def get_age_group(age):
    return pandas.cut(
        age,
        range(0, age.max() + AGE_GROUP_WIDTH, AGE_GROUP_WIDTH),
        # Don't include the right-edge,
        # meaning [lower, upper) or lower <= x < upper
        right=False,
        # Return the zero-based integer index to the category, rather than
        # the category. Pandas will write the category to a feather file but
        # it won't read it from a feather file.
        labels=False,
    )


if __name__ == "__main__":
    records = get_records()

    records["age_group"] = get_age_group(records["age"])

    records.to_feather(utils.OUTPUT_DIR / "output.feather")
