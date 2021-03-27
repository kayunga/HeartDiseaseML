from sklearn.externals import joblib
import os
import numpy as np
import pickle

age = 0
sex = 0
cp = 0
trestbps = 0
chol = 0
fbs = 0
restecg = 0
thalach = 0
exang = 0
oldpeak = 0 
slope = 0
ca = 0
thal = 0 

# x = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]).reshape(1, -1)
# v = (63, 1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1) #positive
# v = (57,1,0,130,131,0,1,115,1,1.2,1,1,2) #negative
v = (57, 1, 0, 145, 233, 0, 0, 174, 0, 0, 0, 1, 1)
user_df=np.array(v).reshape(1, 13)

scaler_path = os.path.join(os.path.dirname(__file__), 'models/scaler.pkl')
# standardScaler = None
with open(scaler_path, 'rb') as f:
    standardScaler = pickle.load(f)

x = standardScaler.transform(user_df)

model_path = os.path.join(os.path.dirname(__file__), 'models/rfc.sav')
clf = joblib.load(model_path)

y = clf.predict(x)
print(y)

# No heart disease
if y == 0:
    print('no disease')

# y=1,2,4,4 are stages of heart disease
elif y == 1:
    print('you are sick')

else:
    print('idk what happened :(')
