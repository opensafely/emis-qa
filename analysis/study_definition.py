from datetime import date

from cohortextractor import StudyDefinition, patients

REFERENCE_DATE = date.today().isoformat()

study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1900-01-01", "latest": REFERENCE_DATE},
        "rate": "uniform",
        "incidence": 1,
    },
    population=patients.registered_as_of(REFERENCE_DATE),
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
