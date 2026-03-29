import pickle
from sklearn.metrics import accuracy_score, classification_report
from preprocess import load_and_preprocess


def evaluate():

    model = pickle.load(open("model.pkl", "rb"))

    X_train, X_test, y_train, y_test, encoder = load_and_preprocess()

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print("Accuracy:", accuracy)
    print("\nClassification Report:\n")
    print(classification_report(y_test, predictions))


if __name__ == "__main__":
    evaluate()