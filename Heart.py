from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter
import os
import random


def clear():
    age_entry.delete(0, END)
    thal_entry.delete(0, END)
    thalach_entry.delete(0, END)
    cp_entry.delete(0, END)
    oldpeak_entry.delete(0, END)
    ca_entry.delete(0, END)
    fbs_entry.delete(0, END)
    restecg_entry.delete(0, END)
    exang_entry.delete(0, END)
    chol_entry.delete(0, END)
    trestbps_entry.delete(0, END)
    slope_entry.delete(0, END)
    v.set(0)


def quit_win():
    bl = messagebox.askquestion("Question", "Do you want to quit")
    if bl == 'yes':
        window.quit()


def submit_data():
    gen_val = v.get()

    if gen_val == 1:
        gender = 1
    else:
        gender = 0

    age = int(age_entry.get())
    sex = gender
    cp = int(cp_entry.get())
    trestbps = int(trestbps_entry.get())
    chol = int(chol_entry.get())
    fbs = int(fbs_entry.get())
    restecg = int(restecg_entry.get())
    thalach = int(thalach_entry.get())
    exang = int(exang_entry.get())
    oldpeak = float(oldpeak_entry.get())
    slope = int(slope_entry.get())
    ca = int(ca_entry.get())
    thal = int(thal_entry.get())

    scale = (age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)

    from sklearn.externals import joblib
    import os
    import numpy as np
    import pickle

    user_df = np.array(scale).reshape(1, 13)

    scaler_path = os.path.join(os.path.dirname(__file__), 'models/scaler.pkl')
    with open(scaler_path, 'rb') as f:
        standardScaler = pickle.load(f)

    x = standardScaler.transform(user_df)

    model_path = os.path.join(os.path.dirname(__file__), 'models/rfc.sav')
    clf = joblib.load(model_path)

    predicted = clf.predict(x)
    print(predicted)
    print(user_df, "\n")

    if predicted == 0:
        print('Negative')
        messagebox.showinfo("heart disease results", 'you are ok, no heart disease')
    elif predicted == 1:
        messagebox.showwarning("heart disease results", 'you have heart disease')
        print('positive')


window = tkinter.Tk()
window.resizable(0, 0)
window.title('Heart Disease Diagnosis')
window.iconbitmap(r'icon.ico')
window.geometry("1050x600")
# Create a Labels
age_label = ttk.Label(text='Age :')
gender_label = ttk.Label(text='Gender (1 = male, 0 = female) :')
cp_label = ttk.Label(text='CP(Chest Pain Type) (0 = typical angina, 1 = atypical angina, 2 = non-anginal, 3 = asymptomatic) :')
trestbps_label = ttk.Label(text='Trestbps (Resting blood pressure(in mm Hg on admission to the hospital)) :')
chol_label = ttk.Label(text='Chol (serum cholesterol in mg/dl) :')
fbs_label = ttk.Label(text='Fbs (fasting blood sugar < 120 mg/dl) (1 = true; 0 = false):')
restecg_label = ttk.Label(text='Restecg (resting ecg) (0=normal, 1=ST-T wave abnormality, 2=definite left ventricular hypertrophy):')
thalach_label = ttk.Label(text='thalach (maximum heart rate achieved):')
exang_label = ttk.Label(text='Exang (exercise induced angina (1 = yes; 0 = no)):')
oldpeak_label = ttk.Label(text='Oldpeak (ST depression induced by exercise relative to rest):')
slope_label = ttk.Label(text='Slope (of the peak exercise ST segment (0 = up-sloping, 1 = flat, 2 = down-sloping)):')
ca_label = ttk.Label(text='Ca (The number of major vessels (0-3) colored by flourosopy):')
thal_label = ttk.Label(text='thal (thalassemia)(1: normal; 2: fixed defect; 3: reversable defect) :')

val_x = 0
val_y = 8

age_label.grid(row=0, column=1, sticky=W, pady=val_y, padx=val_x)
gender_label.grid(row=1, column=1, sticky=W, pady=val_y, padx=val_x)
cp_label.grid(row=3, column=1, sticky=W, pady=val_y, padx=val_x)
trestbps_label.grid(row=4, column=1, sticky=W, pady=val_y, padx=val_x)
chol_label.grid(row=5, column=1, sticky=W, pady=val_y, padx=val_x)
fbs_label.grid(row=6, column=1, sticky=W, pady=val_y, padx=val_x)
restecg_label.grid(row=7, column=1, sticky=W, pady=val_y, padx=val_x)
thalach_label.grid(row=8, column=1, sticky=W, pady=val_y, padx=val_x)
exang_label.grid(row=9, column=1, sticky=W, pady=val_y, padx=val_x)
oldpeak_label.grid(row=10, column=1, sticky=W, pady=val_y, padx=val_x)
slope_label.grid(row=11, column=1, sticky=W, pady=val_y, padx=val_x)
ca_label.grid(row=12, column=1, sticky=W, pady=val_y, padx=val_x)
thal_label.grid(row=13, column=1, sticky=W, pady=val_y, padx=val_x)

# Create a Entry Fields And Radio Button For Form
age_entry = Entry()
cp_entry = Entry()
trestbps_entry = Entry()
chol_entry = Entry()
fbs_entry = Entry()
restecg_entry = Entry()
thalach_entry = Entry()
exang_entry = Entry()
oldpeak_entry = Entry()
slope_entry = Entry()
ca_entry = Entry()
thal_entry = Entry()
v = IntVar()
gender1 = ttk.Radiobutton(text='Male', value=1, variable=v)
gender2 = ttk.Radiobutton(text='Female', value=2, variable=v)

val_x = 3
val_y = 3

age_entry.grid(row=0, column=3, padx=(2, 15), ipadx=val_x, ipady=val_y)

gender1.grid(row=1, column=3, sticky=E+W, pady=0, ipadx=3, ipady=3)
gender2.grid(row=2, column=3, sticky= E+W, pady=0, ipadx=3, ipady=3)

cp_entry.grid(row=3, column=3, padx=(2, 15), ipadx=val_x, ipady=val_y)
trestbps_entry.grid(row=4, column=3, padx=(2, 15), ipadx=val_x, ipady=val_y)
chol_entry.grid(row=5, column=3, padx=(2, 15), ipadx=val_x, ipady=val_y)
fbs_entry.grid(row=6, column=3, padx=(2, 15), ipadx=val_x, ipady=val_y)
restecg_entry.grid(row=7, column=3, padx=(2, 15), ipadx=val_x, ipady=val_y)
thalach_entry.grid(row=8, column=3, padx=(2, 15), ipadx=val_x, ipady=val_y)
exang_entry.grid(row=9, column=3, padx=(2, 15), ipadx=val_x, ipady=val_y)
oldpeak_entry.grid(row=10, column=3, padx=(2, 15), ipadx=val_x, ipady=val_y)
slope_entry.grid(row=11, column=3, padx=(2, 15), ipadx=val_x, ipady=val_y)
ca_entry.grid(row=12, column=3, padx=(2, 15), ipadx=val_x, ipady=val_y)
thal_entry.grid(row=13, column=3, padx=(2, 15), ipadx=val_x, ipady=val_y)

# Create Buttons
submit = ttk.Button(text='Submit', command=submit_data, width=17, )
submit.grid(row=15, column=2, sticky=E + W, padx=2, ipadx=3, ipady=3)

clear = ttk.Button(text='Clear', command=clear, )
clear.grid(row=15, column=3, sticky=E + W, pady=5, padx=(2, 15), ipadx=3, ipady=3)

exits = ttk.Button(text='Exit', command=quit_win, )
exits.grid(row=16, column=2, columnspan=2, sticky=W + E, padx=(2, 15), pady=(0, 15), ipadx=3, ipady=3)

# Add an Image
img_list = os.listdir(r'images')
random.shuffle(img_list)
file_name = random.choice(img_list)
file_path = r"images\\" + file_name
photo = PhotoImage(file=file_path)
img_lb = Label(image=photo)
img_lb.image = photo
img_lb.grid(row=0, column=0, rowspan=6)

window.mainloop()