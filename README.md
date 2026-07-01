# Intelligent Disease Diagnosis System

## Project Overview

This project implements an Intelligent Disease Diagnosis System using Machine Learning algorithms to predict diseases based on symptoms provided by the user.

The system compares the performance of multiple classification algorithms and predicts the most probable disease through an interactive Streamlit web application.

The main objective of this project is to demonstrate the application of machine learning techniques in healthcare for symptom-based disease prediction.

---

## Dataset Information

The dataset contains information about various diseases and their associated symptoms.

Features include:

- 132 Symptoms
- 41 Diseases
- Binary symptom values (0 = Absent, 1 = Present)
- Target variable: **Prognosis (Disease Name)**

---

## Project Objectives

- Build an intelligent disease prediction system.
- Compare different machine learning classification algorithms.
- Predict diseases based on user-selected symptoms.
- Evaluate model performance using various evaluation metrics.
- Develop a user-friendly web interface using Streamlit.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Matplotlib
- Seaborn

---

## Machine Learning Algorithms

The project uses the following classification algorithms:

- Decision Tree
- Random Forest
- Gaussian Naive Bayes

---

## Project Workflow

### 1. Data Loading

- Import training and testing datasets
- Load symptom and disease information

### 2. Data Preprocessing

- Check missing values
- Separate features and target variable
- Prepare data for model training

### 3. Model Training

Train three machine learning models:

- Decision Tree
- Random Forest
- Gaussian Naive Bayes

### 4. Model Evaluation

Evaluate models using:

- Accuracy Score
- Classification Report
- Confusion Matrix
- Cross Validation

### 5. Model Saving

- Save trained models using Joblib
- Store symptom list for prediction

### 6. Disease Prediction

- Accept user-selected symptoms
- Generate disease prediction
- Display prediction through Streamlit interface

---

## Key Insights

### Dataset Analysis

- The dataset contains 132 symptoms associated with 41 diseases.
- Symptoms are represented using binary values.

### Model Performance

- Random Forest achieved the best overall prediction performance.
- Decision Tree also provided high accuracy with fast prediction.
- Gaussian Naive Bayes offered efficient probabilistic classification.

### Prediction System

- Users can select symptoms through the web interface.
- The trained model predicts the most probable disease instantly.

---

## Features

- Disease prediction based on symptoms
- Multiple machine learning algorithms
- Model comparison
- Interactive Streamlit interface
- Saved trained models
- Easy-to-use prediction system
- Modular project structure

---

## Repository Structure

```
Disease-Diagnosis-System/

├── data/
│   ├── training.csv
│   └── testing.csv
│
├── models/
│   ├── decision_tree.pkl
│   ├── random_forest.pkl
│   ├── naive_bayes.pkl
│   
│
├── train_model.py
├── app.py
├── requirements.txt
├── README.md
└── screenshots/
```

---

## Future Improvements

- Disease description
- Precaution recommendations
- Diet suggestions
- Exercise recommendations
- Medicine information (Educational Purpose Only)
- Doctor specialization suggestions
- Prediction history
- PDF report generation
- Cloud deployment
- User authentication

---

## Author

**Sahil Berwal**

---

## License

This project is developed for educational and portfolio purposes.

---

## Disclaimer

This application is intended for educational purposes only and should not be considered a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare professional for medical concerns.
