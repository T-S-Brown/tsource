# Extract the Numeric Vectors

# Input Dataset is a pandas DataFrame

def extract_numerics(data):
    out = pd.DataFrame()
    
    for col in data.columns:
         if is_numeric_dtype(data[col]) == True:
             out[col] = data[col]
    return(out)
