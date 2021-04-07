import pandas as pd
import os
from IPython.display import display, Markdown

df1 = pd.read_csv(os.path.join("..","released-outputs", "unknown-dates-tpp", '1899.csv'), header=None, names=['code','description','freq (nearest 100)'])
df2 = pd.read_csv(os.path.join("..","released-outputs", "unknown-dates-tpp", '1900.csv'), header=None, names=['code','description','freq (nearest 100)'])
df3 = pd.read_csv(os.path.join("..","released-outputs", "unknown-dates-tpp", '1901.csv'), header=None, names=['code','description','freq (nearest 100)'])

snomed = pd.read_csv(os.path.join("..","lib", 'snomedct.csv'), dtype={"id":"str"})

years = {1:"1899", 2:"1900", 3:"1901"}
for n, df in enumerate([df1, df2, df3]):
    out = df.merge(snomed, how="left", left_on='code', right_on='id')
    out["description"] = out['description'].combine_first(out["term"])
    out = out.drop(['id','term','active'],1)
    out.to_csv(os.path.join("..","released-outputs", "unknown-dates-tpp", f'{years[n+1]}_with_descriptions.csv'), index=False)

    display(out)