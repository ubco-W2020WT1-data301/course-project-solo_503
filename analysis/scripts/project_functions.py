import pandas as pd
import numpy as np


def load_and_process(url):
    #Method Chain 1 to load in data, drop columns that aren't needed, dop any NAN values, and reset the index
    df = (
    pd.read_csv(url)
    .drop(columns=['league_id', 'adj_score1'])
    .dropna()
    .reset_index(drop=True)
)
    return df



    
