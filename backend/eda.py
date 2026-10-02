import matplotlib.pyplot as plt
import pandas as pd


def generate_histograms(dataset, output_folder="eda_outputs"):
    """
    Generate histograms for all numerical columns.
    """

    numerical_columns = dataset.select_dtypes(
        include="number"
    ).columns

    for column in numerical_columns:

        plt.figure(figsize=(8, 5))

        plt.hist(dataset[column].dropna(), bins=10)

        plt.title(f"Distribution of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")

        plt.tight_layout()

        plt.savefig(
            f"{output_folder}/{column}_histogram.png"
        )

        plt.close()

    print("Histograms generated successfully.")