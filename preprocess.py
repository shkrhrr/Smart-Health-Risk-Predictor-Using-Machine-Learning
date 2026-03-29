import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


def load_and_preprocess():

    data = pd.read_csv("health_data.csv")

    encoder = LabelEncoder()
    data['risk'] = encoder.fit_transform(data['risk'])

    X = data.drop("risk", axis=1)
    y = data["risk"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42
    )

    return X_train, X_test, y_train, y_test, encoder