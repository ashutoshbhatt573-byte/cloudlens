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


def generate_scatter_plot(
    dataset,
    x_column,
    y_column,
    output_folder="eda_outputs"
):
    """
    Generate a scatter plot between two numerical columns.
    """

    plt.figure(figsize=(8, 5))

    plt.scatter(
        dataset[x_column],
        dataset[y_column]
    )

    plt.title(f"{x_column} vs {y_column}")
    plt.xlabel(x_column)
    plt.ylabel(y_column)

    plt.tight_layout()

    plt.savefig(
        f"{output_folder}/{x_column}_vs_{y_column}_scatter.png"
    )

    plt.close()

    print(
        f"Scatter plot generated: "
        f"{x_column} vs {y_column}"
    )


def generate_correlation_matrix(
    dataset,
    output_folder="eda_outputs"
):
    """
    Generate a correlation matrix and heatmap
    for numerical columns.
    """

    numerical_data = dataset.select_dtypes(
        include="number"
    )

    correlation_matrix = numerical_data.corr()

    print("\n===== CORRELATION MATRIX =====")
    print(correlation_matrix)

    plt.figure(figsize=(10, 7))

    plt.imshow(
        correlation_matrix,
        cmap="coolwarm",
        interpolation="nearest"
    )

    plt.colorbar()

    plt.xticks(
        range(len(correlation_matrix.columns)),
        correlation_matrix.columns,
        rotation=45,
        ha="right"
    )

    plt.yticks(
        range(len(correlation_matrix.columns)),
        correlation_matrix.columns
    )

    plt.title("Correlation Matrix")

    plt.tight_layout()

    plt.savefig(
        f"{output_folder}/correlation_matrix.png"
    )

    plt.close()

    print("Correlation matrix generated successfully.")