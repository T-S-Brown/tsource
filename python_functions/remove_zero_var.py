import pandas as pd
import numpy as np

def remove_zero_var(data):
    out = pd.DataFrame()
    
    for col in data.columns:
        if np.var(data[col].dropna()) != 0:
            out[col] = data[col]
    return(out)
