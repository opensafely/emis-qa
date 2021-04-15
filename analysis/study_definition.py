from cohortextractor import StudyDefinition, patients

study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1900-01-01", "latest": "index_date"},
        "rate": "uniform",
        "incidence": 1,
    },
    # We will pass the --index-date-range argument to cohortextractor, so
    # the value of the index_date kwarg will be replaced. However, we must
    # supply it and it must be in YYYY-MM-DD format.
    index_date="2021-01-01",
    population=patients.registered_as_of("index_date"),
    age=patients.age_as_of(
        "index_date",
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
        "index_date",
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
