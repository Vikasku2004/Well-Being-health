# 🩺 Well Being Health – AI-Powered Disease Prediction & Medicine Recommendation System

An AI/ML-based healthcare recommendation system that predicts possible diseases from user-provided symptoms and provides relevant health information, precautions, medications, diet recommendations, and workout suggestions.

## 📌 Project Overview

Well Being Health is a machine-learning-powered web application designed to provide preliminary health recommendations based on symptoms entered by the user.

The system uses a trained Support Vector Classifier (SVC) model to predict a possible disease and then provides additional information such as:

- Disease description
- Recommended precautions
- Suggested medications
- Diet recommendations
- Workout recommendations

> ⚠️ **Disclaimer:** This project is intended for educational and informational purposes only. It is not a substitute for professional medical diagnosis, treatment, or consultation with a qualified healthcare professional.

---

## ✨ Key Features

### 🤖 Disease Prediction
Users can enter multiple symptoms and the trained machine-learning model predicts a possible disease.

### 💊 Medicine Recommendation
Provides medicine-related information associated with the predicted condition.

### 🥗 Diet Recommendations
Suggests dietary recommendations based on the predicted condition.

### 🏃 Workout Recommendations
Provides workout and lifestyle recommendations.

### ⚠️ Precaution Suggestions
Displays precautions that may be relevant to the predicted condition.

### 📚 Disease Information
Provides a description and basic information about the predicted disease.

### 🌐 Web-Based Interface
The system provides a simple web interface where users can enter symptoms and receive results.

---

## 🧠 Machine Learning

The project uses a **Support Vector Classifier (SVC)** for disease prediction.

### Prediction Workflow

```text
User enters symptoms
        ↓
Symptom processing
        ↓
Feature extraction
        ↓
Trained SVC model
        ↓
Disease prediction
        ↓
Health information retrieval
        ↓
Recommendations displayed
| Dataset                | Purpose                          |
| ---------------------- | -------------------------------- |
| `Training.csv`         | Disease prediction training data |
| `Symptom-severity.csv` | Symptom severity information     |
| `symptoms_df.csv`      | Symptom-related data             |
| `description.csv`      | Disease descriptions             |
| `medications.csv`      | Medication recommendations       |
| `precautions_df.csv`   | Precaution information           |
| `diets.csv`            | Diet recommendations             |
| `workout_df.csv`       | Workout recommendations          |

┌─────────────────────────┐
│      User Interface     │
│    Enter Symptoms       │
└────────────┬────────────┘
             │
             ↓
┌─────────────────────────┐
│     Flask Backend       │
│       main.py           │
└────────────┬────────────┘
             │
             ↓
┌─────────────────────────┐
│   Machine Learning      │
│      SVC Model          │
│       svc.pkl           │
└────────────┬────────────┘
             │
             ↓
┌─────────────────────────┐
│   Disease Prediction    │
└────────────┬────────────┘
             │
             ↓
┌────────────────────────────────┐
│ Health Recommendations         │
│                                │
│ • Description                  │
│ • Precautions                  │
│ • Medications                  │
│ • Diet                         │
│ • Workout
              │

thank you 
└────────────────────────────────┘
