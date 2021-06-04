from IPython.display import display

SMALL_NUMBER = 5

REDACTION_MSG = "[REDACTED]"


def must_redact(df):
    """Returns `True` when the given data frame must be redacted."""
    return df.le(SMALL_NUMBER).any()[0]


def redact_or_display(df):
    """Either redact or display the given data frame."""
    if must_redact(df):
        print(REDACTION_MSG)
    else:
        display(df)
