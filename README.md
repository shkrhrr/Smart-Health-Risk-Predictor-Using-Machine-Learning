# Smart Health Risk Predictor Using Machine Learning

## Project Overview

The Smart Health Risk Predictor is a machine learning-based application that predicts a person's health risk level based on lifestyle indicators such as sleep duration, BMI, exercise time, water intake, daily steps, screen time, and heart rate.

The system classifies individuals into three categories:

- Low Risk
- Medium Risk
- High Risk

This project demonstrates how machine learning can assist in early health awareness using simple lifestyle data.

---

## Problem Statement

Many individuals are unaware of their potential health risks caused by lifestyle habits such as poor sleep, low physical activity, high screen time, and insufficient hydration.

This project builds a machine learning model that predicts health risk levels using these parameters and helps users understand their condition early.

---

## Objectives

The objectives of this project are:

- To apply machine learning concepts learned in the course
- To build a classification model using lifestyle data
- To predict health risk levels accurately
- To visualize dataset distribution
- To provide an interactive prediction interface
- To organize code into a structured ML pipeline

---

## Technologies Used

Programming Language:

- Python

Libraries Used:

- pandas
- scikit-learn
- matplotlib
- pickle

Machine Learning Algorithm:

- Random Forest Classifier

---

## Dataset Description

The dataset contains the following features:

| Feature | Description |
|--------|-------------|
| age | Age of the individual |
| BMI | Body Mass Index |
| sleep_hours | Average sleep duration |
| steps | Daily step count |
| water_intake | Daily water intake (litres) |
| screen_time | Screen usage hours |
| exercise_minutes | Daily exercise duration |
| heart_rate | Resting heart rate |
| risk | Target variable (Low / Medium / High) |

---

## Project Structure
```
VITyarthi_shikhar/
│
├── health_data.csv
├── preprocess.py
├── train_model.py
├── evaluate_model.py
├── predictor.py
├── graphs.py
├── main.py
├── models/
│ ├── model.pkl
│ └── encoder.pkl
└── README.md
```

---

## Machine Learning Workflow

The project follows these steps:

1. Load dataset
2. Preprocess dataset
3. Encode categorical output labels
4. Split dataset into training and testing sets
5. Train Random Forest classifier
6. Evaluate model accuracy
7. Save trained model
8. Predict health risk using user input
9. Visualize dataset distribution

---

## How to Run the Project

### Step 1: Install dependencies
```
pip install pandas scikit-learn matplotlib
```

---

### Step 2: Train the model
```
python train_model.py
```

This creates:
```
models/model.pkl
models/encoder.pkl
```

---

### Step 3: Evaluate model performance
```
python evaluate_model.py
```

Outputs:

- Accuracy score
- Classification report

---

### Step 4: Predict health risk
```
python predictor.py
```

Enter values when prompted.

Example:
```
Enter age: 22
Enter BMI: 21
Enter sleep hours: 7
Enter daily steps: 9000
Enter water intake (litres): 3
Enter screen time (hours): 2
Enter exercise minutes: 45
Enter heart rate: 70
```

Output:
```
Predicted Health Risk: Low
```

---

### Step 5: Run full application interface
```
python main.py
```

Menu options:

- Train model
- Evaluate model
- Predict health risk
- Show dataset graph

---

## Model Evaluation

The model performance is evaluated using:

- Accuracy Score
- Precision
- Recall
- F1-score

Random Forest classifier was selected because it performs well on classification problems involving multiple numerical features and reduces overfitting.

---

## Visualization

The project includes dataset visualization using bar charts to show risk distribution among individuals.

This helps in understanding dataset balance.

---

## Applications of the Project

This system can be used for:

- Health awareness tools
- Lifestyle monitoring applications
- Preventive healthcare support systems
- Educational machine learning demonstrations

---

## Learning Outcomes

Through this project, the following concepts were implemented:

- Data preprocessing
- Label encoding
- Train-test split
- Classification using Random Forest
- Model evaluation techniques
- Model saving using pickle
- Data visualization using matplotlib
- Building an interactive prediction interface

---

## Future Improvements

Possible enhancements include:

- Increasing dataset size
- Adding more health indicators
- Deploying as a web application
- Integrating real-time wearable device data
- Comparing multiple ML algorithms

---

## Conclusion

This project demonstrates how machine learning can be applied to predict health risk levels using simple lifestyle data. It highlights the importance of early awareness and showcases practical implementation of classification algorithms learned during the course.
