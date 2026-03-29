from train_model import train_model
from evaluate_model import evaluate
from predictor import predict
from graphs import plot_distribution


def main():

    while True:

        print("\nSMART HEALTH RISK PREDICTOR")
        print("----------------------------")

        print("1 Train Model")
        print("2 Evaluate Model")
        print("3 Predict Health Risk")
        print("4 Show Dataset Graph")
        print("5 Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            train_model()

        elif choice == "2":
            evaluate()

        elif choice == "3":
            predict()

        elif choice == "4":
            plot_distribution()

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()