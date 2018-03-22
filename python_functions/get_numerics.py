# Extract the Numeric Vectors

# Input Dataset is a pandas DataFrame
# Requires...
import pandas as pd
from pandas.api.types import is_numeric_dtype

def extract_numerics(data):
    out = pd.DataFrame()
    
    for col in data.columns:
         if is_numeric_dtype(data[col]) == True:
             out[col] = data[col]
    return(out)
