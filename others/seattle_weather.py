import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv

weather_data = pd.read_csv('../datasets/seattle-weather.csv')

print(weather_data.describe())

csv_file_array = []

filename = "../datasets/seattle_weather_modified.csv"

m,n = weather_data.shape

id = np.arange(m)
precipitation = np.array(weather_data.iloc[:,1],dtype=float)
temp_max = np.array(weather_data.iloc[:,2],dtype=float)
temp_min = np.array(weather_data.iloc[:,3],dtype=float)
wind = np.array(weather_data.iloc[:,4],dtype=float)
weather = np.array(weather_data.iloc[:,5],dtype=str)

print(m)
print(id)

for i in range(0,m):
    csv_file_array.append([id[i],precipitation[i],temp_max[i],temp_min[i],
                           wind[i],weather[i]])
    
for i in range(0,5):
    print(csv_file_array[i])

fields = ['id','precipitation','temp_max','temp_min','wind','weather'] 

with open(filename, 'w', encoding="utf-8") as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(fields)  
        
    # writing the data rows  
    csvwriter.writerows(csv_file_array)