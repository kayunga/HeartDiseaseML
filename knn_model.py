import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
df = pd.read_csv('dataset/dataset.csv')
dataset = df
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
standardScaler = StandardScaler()
columns_to_scale = ['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']
dataset[columns_to_scale] = standardScaler.fit_transform(dataset[columns_to_scale])

y = dataset['target']
X = dataset.drop(['target'], axis = 1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 0)

knn_classifier = KNeighborsClassifier(n_neighbors = 7)
knn_classifier.fit(X, y)
score = knn_classifier.score(X_test, y_test)

# v = (70,1,0,145,174,0,1,125,1,2.6,0,0,3)
v = (63, 1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1)
user_df = np.array(v).reshape(1,13)
print('-----------------------KNN classifier-------------------------------')

print('score is: '+str(score))
print('-------------------------------------')
print(user_df)
print('-------------------------------------')
user_df = standardScaler.transform(user_df)
print(user_df)
print('-------------------------------------')
predicted = knn_classifier.predict(user_df)
print(predicted)
if predicted == 0:
    print('Negative')

elif predicted == 1:
    print('positive')

from sklearn.metrics import accuracy_score
test_score = accuracy_score(y_test, knn_classifier.predict(X_test)) * 100
train_score = accuracy_score(y_train, knn_classifier.predict(X_train)) * 100

from sklearn.metrics import classification_report,confusion_matrix
predict_train = knn_classifier.predict(X_train)
predict_test = knn_classifier.predict(X_test)
print('-------------------------Train report-------------------------------')
print(confusion_matrix(y_train,predict_train))
print(classification_report(y_train,predict_train))
print('-------------------------Test report--------------------------------')
print(confusion_matrix(y_test,predict_test))
print(classification_report(y_test,predict_test))
print('--------------------------------------------------------------------')
print("test accuracy: "+str(test_score))
print("train accuracy: "+str(train_score))