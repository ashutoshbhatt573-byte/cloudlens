import matplotlib.pyplot as plt
import pandas as pd


def identify_columns(dataset):
    """
    Identify numerical, categorical, and identifier columns.
    """

    identifier_columns = []

    for column in dataset.columns:

        column_name = column.lower()

        if (
            column_name == "id"
            or column_name.endswith("_id")
            or column_name.startswith("id_")
        ):
            identifier_columns.append(column)

    numerical_columns = dataset.select_dtypes(
        include="number"
    ).columns.tolist()

    categorical_columns = dataset.select_dtypes(
        exclude="number"
    ).columns.tolist()

    numerical_features = [
        column
        for column in numerical_columns
        if column not in identifier_columns
    ]

    return {
        "identifier_columns": identifier_columns,
        "numerical_features": numerical_features,
        "categorical_columns": categorical_columns,
    }


def generate_histograms(dataset, output_folder="eda_outputs"):
    """
    Generate histograms for numerical features.
    """

    column_info = identify_columns(dataset)

    numerical_columns = column_info["numerical_features"]

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
    for numerical features.
    """

    column_info = identify_columns(dataset)

    numerical_features = column_info["numerical_features"]

    correlation_matrix = dataset[numerical_features].corr()

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

def generate_box_plots(
    dataset,
    output_folder="eda_outputs"
):
    """
    Generate box plots for numerical features.
    """

    column_info = identify_columns(dataset)

    numerical_columns = column_info["numerical_features"]

    for column in numerical_columns:

        plt.figure(figsize=(8, 5))

        plt.boxplot(
            dataset[column].dropna()
        )

        plt.title(f"Box Plot of {column}")
        plt.ylabel(column)

        plt.tight_layout()

        plt.savefig(
            f"{output_folder}/{column}_boxplot.png"
        )

        plt.close()

    print("Box plots generated successfully.")

def generate_eda_insights(dataset):
    """
    Generate basic insights from numerical features.
    """

    column_info = identify_columns(dataset)

    numerical_features = column_info["numerical_features"]

    correlation_matrix = dataset[numerical_features].corr()

    print("\n===== CLOUDLENS EDA INSIGHTS =====")

    print("\nStrong Correlations:")

    found_correlation = False

    for i in range(len(correlation_matrix.columns)):
        for j in range(i + 1, len(correlation_matrix.columns)):

            column_1 = correlation_matrix.columns[i]
            column_2 = correlation_matrix.columns[j]

            correlation = correlation_matrix.iloc[i, j]

            if abs(correlation) >= 0.7:

                print(
                    f"- {column_1} and {column_2}: "
                    f"correlation = {correlation:.2f}"
                )

                found_correlation = True

    if not found_correlation:
        print("- No strong correlations detected.")