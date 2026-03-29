import pandas as pd
import matplotlib.pyplot as plt


def plot_distribution():

    data = pd.read_csv("health_data.csv")

    data['risk'].value_counts().plot(kind='bar')

    plt.title("Health Risk Distribution")
    plt.xlabel("Risk Level")
    plt.ylabel("Count")

    plt.show()


if __name__ == "__main__":
    plot_distribution()