from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import pickle
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

svc = pickle.load(open(os.path.join(BASE_DIR, 'svc.pkl'), 'rb'))

sym_des = pd.read_csv(os.path.join(BASE_DIR, 'symptoms_df.csv'))
precautions = pd.read_csv(os.path.join(BASE_DIR, 'precautions_df.csv'))
workout = pd.read_csv(os.path.join(BASE_DIR, 'workout_df.csv'))
description = pd.read_csv(os.path.join(BASE_DIR, 'description.csv'))
medications = pd.read_csv(os.path.join(BASE_DIR, 'medications.csv'))
diets = pd.read_csv(os.path.join(BASE_DIR, 'diets.csv'))

# ✅ FIXED - using Training.csv for 132 features
training_data = pd.read_csv(os.path.join(BASE_DIR, 'Training.csv'))
symptoms_dict = {symptom: index for index, symptom in enumerate(training_data.drop('prognosis', axis=1).columns)}
diseases_list = {i: disease for i, disease in enumerate(svc.classes_)}

# ✅ FIXED - return prediction directly
def get_predicted_value(patient_symptoms):
    input_vector = np.zeros(len(symptoms_dict))
    for symptom in patient_symptoms:
        if symptom in symptoms_dict:
            input_vector[symptoms_dict[symptom]] = 1
    return svc.predict([input_vector])[0]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    symptoms = request.form.get('symptoms')
    if not symptoms:
        return render_template('index.html', message="Please enter symptoms")

    user_symptoms = [s.strip() for s in symptoms.split(',')]
    user_symptoms = [s.strip("[]' ") for s in user_symptoms]

    predicted_disease = get_predicted_value(user_symptoms)

    desc = description[description['Disease'] == predicted_disease]['Description'].values
    dis_des = desc[0] if len(desc) > 0 else "No description available"

    prec = precautions[precautions['Disease'] == predicted_disease][
        ['Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']].values
    my_precautions = [p for p in prec[0] if pd.notna(p)] if len(prec) > 0 else []

    med = medications[medications['Disease'] == predicted_disease]['Medication'].values
    medications_list = list(med) if len(med) > 0 else []

    work = workout[workout['disease'] == predicted_disease]['workout'].values
    workout_list = list(work) if len(work) > 0 else []

    diet = diets[diets['Disease'] == predicted_disease]['Diet'].values
    diet_list = list(diet) if len(diet) > 0 else []

    return render_template(
        'index.html',
        predicted_disease=predicted_disease,
        dis_des=dis_des,
        my_precautions=my_precautions,
        medications=medications_list,
        workout=workout_list,
        my_diet=diet_list
    )

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/developer')
def developer():
    return render_template('developer.html')

if __name__ == "__main__":
    app.run(debug=True)