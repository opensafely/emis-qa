from datetime import date

from cohortextractor import StudyDefinition, patients

REFERENCE_DATE = date.today().isoformat()

# Where do we specify that this study definition should be executed against
# the EMIS data store?
study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1900-01-01", "latest": REFERENCE_DATE},
        "rate": "uniform",
        "incidence": 1,
    },
    # Does this mean "Where the value of `is_registered` is True"?
    population=patients.satisfying("is_registered"),
    is_registered=patients.registered_as_of(
        REFERENCE_DATE,
        # We think that EMIS and TPP cover 97% of the population?
        return_expectations={"incidence": 0.97},
    ),
    date_deregistered=patients.date_deregistered_from_all_supported_practices(
        on_or_before=REFERENCE_DATE,
        date_format="YYYY-MM",
        return_expectations={
            "date": {
                "latest": REFERENCE_DATE,
            }
        },
    ),
    age=patients.age_as_of(
        REFERENCE_DATE,
        return_expectations={
            "rate": "universal",
            "int": {"distribution": "population_ages"},
        },
    ),
    sex=patients.sex(
        return_expectations={
            "rate": "universal",
            "category": {"ratios": {"M": 0.49, "F": 0.51}},
        }
    ),
    practice_pseudo_id=patients.registered_practice_as_of(
        REFERENCE_DATE,
        "pseudo_id",
        # Is there a better way? We'd expect about 68% of patients to be
        # assigned practices with IDs from 900 to 1,100.
        return_expectations={
            "int": {
                "distribution": "normal",
                "mean": 1_000,
                "stddev": 100,
                "incidence": 1,
            },
        },
    ),
)
