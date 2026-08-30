import pandas as pd
import pickle
from sklearn.svm import SVC

df = pd.read_csv('Training.csv')
X = df.drop('prognosis', axis=1)
y = df['prognosis']

svc = SVC(kernel='linear')
svc.fit(X, y)

pickle.dump(svc, open('svc.pkl', 'wb'))
print('✅ Model retrained and saved successfully!')