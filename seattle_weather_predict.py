import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv

df = pd.read_csv('datasets/seattle_weather_data.csv')
print(df.describe())
m,n = df.shape
# plt.figure(figsize=(8,6))
# sns.countplot(data=df,x=df.weather,palette="Set1")
# plt.show()

# x=df.weather.value_counts()
# plt.figure(figsize=(12, 10))
# plt.pie(x, labels=x.index, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'gold', 'lightgray', 'lightgreen', 'lightcoral'])
# plt.title('Distribution of Weather Types')
# plt.show()

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder

df.info()

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df['weather']=le.fit_transform(df['weather'])

x = df[['temp_min', 'temp_max', 'precipitation', 'wind']]
y=df['weather']
le_name_mapping = dict(zip(le.classes_, le.transform(le.classes_)))
print(le_name_mapping)
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print(X_test)

nb_model = GaussianNB()
nb_model.fit(X_train, y_train)

y_pred = nb_model.predict(X_test)
print(y_pred)

accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred, zero_division=1)


print(f"Accuracy: {accuracy:.2f}")

print("Confusion Matrix:")
print(conf_matrix)
print("Classification Report:")
print(classification_rep)

print(f"Enter Weather Data: ")

print(f"Enter Precipitation: ")
precipitation = float(input())

print(f"Enter temp_max: ")
temp_max = float(input())

print(f"Enter temp_min: ")
temp_min = float(input())

print(f"Enter wind: ")
wind = float(input())

input_data = (temp_min,temp_max,precipitation,wind)
input_data_as_numpy_array= np.asarray(input_data)
print(input_data_as_numpy_array)
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
print(input_data_reshaped)

prediction = nb_model.predict(input_data_reshaped)
# prediction1 = nb_model.predict([[3.8,5.3,0,1.2]])
print(f"The weather based on given data is : {prediction}")
# print(f"The weather based on given data is : {prediction1}")

if(prediction[0] == 0):
    print(f"The weather based on given data is : drizzle")
elif(prediction[0] == 1):
    print(f"The weather based on given data is : fog")
elif(prediction[0] == 2):
    print(f"The weather based on given data is : rain")
elif(prediction[0] == 3):
    print(f"The weather based on given data is : snow")
elif(prediction[0] == 4):
    print(f"The weather based on given data is : sun")