import pandas as pd
import os

df_a = pd.read_csv(os.path.join("released-outputs", "other-tables", "allergy.csv"))
df_i = pd.read_csv(os.path.join("released-outputs", "other-tables", "immunisation.csv"))
df_o = pd.read_csv(os.path.join("released-outputs", "other-tables", "observation.csv"))


out_path = os.path.join("released-outputs", "other-tables")
os.makedirs(out_path, exist_ok=True)


# crossover between allergy and imms:
out = df_a.merge(df_i, how="inner", on='snomed_concept_id', suffixes=["_allergy", "_imms"])
print(out.head())  

# crossover between allergy and obs:
out = df_a.merge(df_o, how="inner", on='snomed_concept_id', suffixes=["_allergy", "_obs"])
out["% overlap"] = (100*out[["c_obs","c_allergy"]].min(axis=1)/out[["c_obs","c_allergy"]].max(axis=1)).astype(int)
out = out.loc[(out["c_obs"]>0) & (out["c_allergy"]>0)]
out = out.drop("description_obs", 1)
print(out.head(20))  

# export to csv
out.to_csv(os.path.join(out_path, "allergy_obs.csv"), index=False)

# crossover between imms and obs:
out = df_i.merge(df_o, how="inner", on='snomed_concept_id', suffixes=["_imms", "_obs"])
out["% overlap"] = (100*out[["c_obs","c_imms"]].min(axis=1)/out[["c_obs","c_imms"]].max(axis=1)).astype(int)
out = out.loc[(out["c_obs"]>0) & (out["c_imms"]>0)]
out = out.drop("description_obs", 1)
print(out.head(20))  

# export to csv
out.to_csv(os.path.join(out_path, "imms_obs.csv"), index=False)
