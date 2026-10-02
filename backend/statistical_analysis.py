import pandas as pd


def generate_statistics(dataset):
    """
    Generate descriptive statistics for numerical columns.
    """

    numerical_data = dataset.select_dtypes(include="number")

    statistics = {
        "count": numerical_data.count(),
        "mean": numerical_data.mean(),
        "median": numerical_data.median(),
        "std": numerical_data.std(),
        "minimum": numerical_data.min(),
        "maximum": numerical_data.max(),
        "25_percentile": numerical_data.quantile(0.25),
        "50_percentile": numerical_data.quantile(0.50),
        "75_percentile": numerical_data.quantile(0.75),
    }

    return statistics