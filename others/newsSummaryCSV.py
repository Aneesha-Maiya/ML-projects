import pandas as pd
import numpy as np
import csv 
import string

news_summary_csv = pd.read_csv('../datasets/news_summary.csv',encoding='unicode_escape')
m,n = news_summary_csv.shape

total_count = 0
ctext_word_count = []
text_word_count = []
csv_file_array = []
id = np.arange(m)


filename = "../datasets/news_summary(50-200).csv"

for i in range(0,m):
    # print(f"{news_summary_csv.iloc[i]['ctext']}\n")
    word_count = 0
    for j in str(news_summary_csv.iloc[i]['ctext']):
        if j == " ":
            word_count = word_count+1
    ctext_word_count.append(
        {
            "length_ctext" : word_count,
            "index_ctext": i
        }
    )
    if(word_count < 200 and word_count > 50):
        # print(f"wordCount pf Ctext-{i} is less than 200")
        csv_file_array.append([id[i],news_summary_csv.iloc[i]['headlines'],news_summary_csv.iloc[i]['text'],
                               news_summary_csv.iloc[i]['ctext'],word_count])
        total_count = total_count + 1
    
print(f"Total number of articles having less than 200 words and more than 50 words is: {total_count}")

max_word_count,max_word_count_index = 0,0
min_word_count,min_word_count_index = 99999,0


for i in range(0,m):
   if (ctext_word_count[i]['length_ctext']>max_word_count):
       max_word_count = ctext_word_count[i]['length_ctext']
       max_word_count_index = i
   if (ctext_word_count[i]['length_ctext']<min_word_count and ctext_word_count[i]['length_ctext'] != 0 ):
       min_word_count = ctext_word_count[i]['length_ctext']
       min_word_count_index = i
print(f"Maximum word count found in csv for ctext: {max_word_count} at index {max_word_count_index}")
print(f"Minimum word count found in csv for ctext: {min_word_count} at index {min_word_count_index}")

max_word_count,max_word_count_index = 0,0
min_word_count,min_word_count_index = 99999,0

for i in range(0,m):
    # print(f"{news_summary_csv.iloc[i]['ctext']}\n")
    word_count = 0
    for j in str(news_summary_csv.iloc[i]['text']):
        if j == " ":
            word_count = word_count+1
    text_word_count.append(
        {
            "length_text" : word_count,
            "index_text": i
        }
    )

for i in range(0,m):
   if (text_word_count[i]['length_text']>max_word_count):
       max_word_count = text_word_count[i]['length_text']
       max_word_count_index = i
   if (text_word_count[i]['length_text']<min_word_count and text_word_count[i]['length_text'] != 0 ):
       min_word_count = text_word_count[i]['length_text']
       min_word_count_index = i
print(f"Maximum word count found in csv for text: {max_word_count} at index {max_word_count_index}")
print(f"Minimum word count found in csv for text: {min_word_count} at index {min_word_count_index}")
    
fields = ['id','headlines','text','ctext','ctext_len']
with open(filename, 'w', encoding="utf-8") as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(fields)  
        
    # writing the data rows  
    csvwriter.writerows(csv_file_array)