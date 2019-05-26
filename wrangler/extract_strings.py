# Extract the String Vectors

# Input Dataset is a pandas DataFrame
# Requires...
import pandas as pd
from pandas.api.types import is_string_dtype

def extract_strings(data):
    out = pd.DataFrame()
    
    for col in data.columns:
         if is_string_dtype(data[col]) == True:
             out[col] = data[col]
    return(out)
