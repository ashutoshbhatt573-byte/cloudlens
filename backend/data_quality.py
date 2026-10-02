import pandas as pd


def analyze_data_quality(dataset):
    """
    Analyze the basic quality and structure of a dataset.
    """

    report = {
        "rows": dataset.shape[0],
        "columns": dataset.shape[1],
        "missing_values": dataset.isnull().sum(),
        "duplicate_rows": dataset.duplicated().sum(),
        "data_types": dataset.dtypes,
        "numerical_columns": dataset.select_dtypes(
            include="number"
        ).columns.tolist(),
        "categorical_columns": dataset.select_dtypes(
            exclude="number"
        ).columns.tolist(),
    }

    return report