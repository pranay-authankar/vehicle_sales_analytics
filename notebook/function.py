def compare_null_cols(dataset, col_name):
    return dataset[dataset[col_name].isnull()][dataset.columns.drop(col_name)].isnull().sum()

