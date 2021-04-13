# EMIS QA

The aim of this project is to verify the EMIS database.
By comparing two snapshots that we generate before and after the EMIS database is rebuilt,
we can better understand any unexpected changes in, for example, numbers of patients and numbers of practices.

* Released outputs are in the [released outputs folder][].
* If you are interested in how we defined our variables,
  then take a look at the [study definition][];
  this is written in Python, but non-programmers should be able to understand what is going on there.
* If you are interested in how we defined our codelists,
  then take look in the [codelists folder][].
* Developers and epidemiologists interested in the framework should review the [OpenSAFELY documentation][].

## Running

On first run, execute:

```sh
opensafely run run_all
```

This will generate the current and last snapshots, which will be identical,
and a summary notebook that compares the current snapshot to the last snapshot.

On second and subsequent runs, execute:

```sh
opensafely run generate_study_population
opensafely run generate_summary_notebook
```

This will generate the current snapshot and a summary notebook.

Then, execute:

```sh
opensafely run rotate_study_population
```

This will generate the new last snapshot, which will be identical to the current snapshot.
However, because it was executed after the summary notebook was generated,
the summary notebook will compare the current snapshot to the old last snapshot.

## Contributing

For local (non-Docker) development, execute:

```sh
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip

# Either one or the other of the following
pip install -r requirements.txt
pip install -r requirements.dev.txt # For also running bin/codestyle.sh

# For QA
bin/codestyle.sh .
```

## About the OpenSAFELY framework

The OpenSAFELY framework is a secure analytics platform for electronic health records research in the NHS.

Instead of requesting access for slices of patient data and transporting them elsewhere for analysis,
the framework supports developing analytics against dummy data
and then running against the real data *within the same infrastructure that the real data is stored*.
Read more at [OpenSAFELY.org](https://opensafely.org).


[codelists folder]:codelists
[OpenSAFELY documentation]:https://docs.opensafely.org
[released outputs folder]:released_outputs
[study definition]:analysis/study_definition.py
