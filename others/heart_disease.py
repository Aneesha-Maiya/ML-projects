import pandas as pd
import numpy as np
import csv 
import string

hd = pd.read_csv("../datasets/heart.csv")

csv_file_array = []

filename = "../datasets/heart_modified.csv"

m,n = hd.shape

id = np.arange(m)
age = np.array(hd.iloc[:,0])
sex = np.array(hd.iloc[:,1])
cp = np.array(hd.iloc[:,2])
trestbps = np.array(hd.iloc[:,3])
chol = np.array(hd.iloc[:,4])
fbs = np.array(hd.iloc[:,5])
restecg = np.array(hd.iloc[:,6])
thalach = np.array(hd.iloc[:,7])
exang = np.array(hd.iloc[:,8])
oldpeak = np.array(hd.iloc[:,9],dtype=float)
slope = np.array(hd.iloc[:,10])
ca = np.array(hd.iloc[:,11])
thal = np.array(hd.iloc[:,12])
target = np.array(hd.iloc[:,13])

print(m)
print(id)

for i in range(0,m):
    csv_file_array.append([id[i],age[i],sex[i],cp[i],trestbps[i],chol[i],
                           fbs[i],restecg[i],thalach[i],exang[i],oldpeak[i],
                           slope[i],ca[i],thal[i],target[i]])

for i in range(0,5):
    print(csv_file_array[i])

fields = ['id', 'age', 'sex', 'cp','trestbps', 'chol','fbs','restecg','thalach','exang'
          'oldpeak','slope','ca','thal','target'] 

with open(filename, 'w', encoding="utf-8") as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(fields)  
        
    # writing the data rows  
    csvwriter.writerows(csv_file_array)