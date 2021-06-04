import pandas

from notebooks import utils


class TestMustRedact:
    def test_is_disclosive(self):
        assert utils.must_redact(
            pandas.DataFrame(
                {
                    "redact_me": [utils.SMALL_NUMBER],
                    "display_me": [utils.SMALL_NUMBER + 1],
                }
            )
        )

    def test_is_not_disclosive(self):
        assert not utils.must_redact(
            pandas.DataFrame({"display_me": [utils.SMALL_NUMBER + 1]})
        )
