import pickle
import pandas as pd

model = pickle.load(open("model.pkl", "rb"))
encoder = pickle.load(open("encoder.pkl", "rb"))


def predict():

    age = float(input("Enter age: "))
    BMI = float(input("Enter BMI: "))
    sleep = float(input("Enter sleep hours: "))
    steps = float(input("Enter daily steps: "))
    water = float(input("Enter water intake (litres): "))
    screen = float(input("Enter screen time (hours): "))
    exercise = float(input("Enter exercise minutes: "))
    heart = float(input("Enter heart rate: "))

    input_data = pd.DataFrame([[
        age,
        BMI,
        sleep,
        steps,
        water,
        screen,
        exercise,
        heart
    ]], columns=[
        "age",
        "BMI",
        "sleep_hours",
        "steps",
        "water_intake",
        "screen_time",
        "exercise_minutes",
        "heart_rate"
    ])

    prediction = model.predict(input_data)

    result = encoder.inverse_transform(prediction)

    print("Predicted Health Risk:", result[0])


if __name__ == "__main__":
    predict()