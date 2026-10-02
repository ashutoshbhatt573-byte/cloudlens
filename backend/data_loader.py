import pandas as pd


def load_dataset(file_path):
    """
    Load a CSV dataset into a Pandas DataFrame.
    """

    try:
        dataset = pd.read_csv(file_path)

        print("Dataset loaded successfully.")
        print(f"Rows: {dataset.shape[0]}")
        print(f"Columns: {dataset.shape[1]}")

        return dataset

    except FileNotFoundError:
        print("Error: Dataset file not found.")
        return None

    except Exception as error:
        print(f"Error loading dataset: {error}")
        return None