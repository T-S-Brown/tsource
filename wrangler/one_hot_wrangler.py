def one_hot_wrangler(data, threshold=12):
    """
    Performs one hot encoding on all vars that have a
    number of unique values below a given threshold.
    """

    # Get Potential vars
    key_vars = data.loc[:, data.dtypes == 'object'].columns.values

    for feature in key_vars:
        if len(data[feature].unique()) <= threshold:
            data = pd.get_dummies(data,
                                  prefix=feature,
                                  columns=[feature])
    return(data)
