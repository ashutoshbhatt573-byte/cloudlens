from sklearn.model_selection import train_test_split


def prepare_data(dataset, target_column):
    """
    Separate features and target, then split the data
    into training and testing sets.
    """

    X = dataset.drop(columns=[target_column])
    y = dataset[target_column]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    return X_train, X_test, y_train, y_test