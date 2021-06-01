import pandas as pd
import os

snomed = pd.read_csv(os.path.join("lib", 'snomedct.csv'))
tablenames = ['allergy', 'observation', 'immunisation']

for t in tablenames:
    df = pd.read_csv(os.path.join("output", "other-tables", f"{t}.csv"))
    df["c"] = (100*round(df["c"]/100,0)).astype(int)

    out = df.merge(snomed, how="left", left_on='snomed_concept_id', right_on='id')
    out["description"] = out["term"]
    out = out.drop(['id','term','active'],1)
    
    # export to csv
    out_path = os.path.join("released-outputs", "other-tables")
    os.makedirs(out_path, exist_ok=True)
    out.to_csv(os.path.join(out_path, f"{t}.csv"), index=False)

    if t != 'observation':
    # export for opencodelists
    # remove unnecessary columns, ensure description is not missing (because codelist can't be uploaded with unknown codes present), 
    # and remove "Clinical findings" (this code has a lot of descendents hence takes a lot of processing in opencodelists)
        out_codelist = out[['snomed_concept_id', 'description']].loc[pd.notnull(out["description"]) & (out["snomed_concept_id"]!=404684003)]
        out_codelist.to_csv(os.path.join(out_path, f"{t}_codelist.csv"), index=False, header=False)
