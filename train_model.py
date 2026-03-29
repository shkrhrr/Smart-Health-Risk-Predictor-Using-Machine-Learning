from sklearn.ensemble import RandomForestClassifier
import pickle
import os

from preprocess import load_and_preprocess


def train_model():

    print("Loading dataset...")

    X_train, X_test, y_train, y_test, encoder = load_and_preprocess()

    print("Training model...")

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    os.makedirs("models", exist_ok=True)

    pickle.dump(model, open("model.pkl", "wb"))
    pickle.dump(encoder, open("encoder.pkl", "wb"))

    print(" Model trained and saved successfully!")


if __name__ == "__main__":
    train_model()