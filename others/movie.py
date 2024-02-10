import pandas as pd
import numpy as np
import csv 
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import sigmoid_kernel

credits = pd.read_csv("datasets/tmdb_5000_credits.csv")
movies = pd.read_csv("datasets/tmdb_5000_movies.csv")

# print(movies.head(5))
# print(credits.head(5))

# print(credits.info())
print(movies.info())
movie_id = np.array(movies.iloc[:,3],dtype=int)
movie_names = np.array(movies.iloc[:,6],dtype=str)
movie_desc = np.array(movies.iloc[:,7],dtype=str)
fields = ['id', 'original_title', 'overview']  
csv_file_array = []
filename = "datasets/movies_modified.csv"

for i in range(0,len(movie_id)):
    csv_file_array.append([movie_id[i],movie_names[i],movie_desc[i].replace('"','`')])

for i in range(0,len(movie_id)):
    if(movie_id[i] == 8337):
        print(csv_file_array[i])
# with open(filename, 'w', encoding="utf-8") as csvfile:  
#     # creating a csv writer object  
#     csvwriter = csv.writer(csvfile)  
        
#     # writing the fields  
#     csvwriter.writerow(fields)  
        
#     # writing the data rows  
#     csvwriter.writerows(csv_file_array)
movies_modified = pd.read_csv('datasets/movies_modified.csv')
print(movies_modified.info())

credits_column_renamed = credits.rename(index=str, columns={"movie_id": "id"})
# print(credits_column_renamed.head(2))
# print(credits_column_renamed.info())

movies_merge = movies.merge(credits_column_renamed, on='id')
# print(movies_merge.head(3))
# print(movies_merge.info())

movies_cleaned = movies_merge.drop(columns=['homepage', 'title_x', 'title_y', 'status','production_countries'])
# print(movies_cleaned.head())
# print(movies_cleaned.info())
# print(movies_cleaned.head(1)['overview'])

tfv = TfidfVectorizer(min_df=3,  max_features=None,
            strip_accents='unicode', analyzer='word',token_pattern=r'\w{1,}',
            ngram_range=(1, 3),
            stop_words = 'english')

tfv_matrix = tfv.fit_transform(movies_cleaned['overview'].values.astype(str))
# print(tfv_matrix)
# print(tfv_matrix.shape)

# Compute the sigmoid kernel
sig = sigmoid_kernel(tfv_matrix, tfv_matrix)
# print(sig)
# print(sig[0])


indices = pd.Series(movies_cleaned.index, index=movies_cleaned['original_title']).drop_duplicates()
# print(indices)
# print(indices['Newlyweds'])
# print(sig[4799])
# print(list(enumerate(sig[indices['Newlyweds']])))
# print(sorted(list(enumerate(sig[indices['Newlyweds']])), key=lambda x: x[1], reverse=True))

# sig_scores = sorted(list(enumerate(sig[indices['Newlyweds']])), key=lambda x: x[1], reverse=True)
# sig_scores = sig_scores[1:11]
# print(sig_scores)

# movie_indices = [i[0] for i in sig_scores]
# print(movie_indices)
# print(movies_cleaned['original_title'].iloc[movie_indices])
# print(dict(indices).keys())

def give_recomendations(title, sig=sig):
    # Get the index corresponding to original_title
    indices_as_dict = dict(indices)
    if title in indices_as_dict.keys():
        check = indices[title]
    else:
        check = -1    

    if check == -1:
        print("Sorry we could not find that movie in our database")
        return []
    else:
        idx = indices[title]

        # Get the pairwsie similarity scores
        sig_scores = list(enumerate(sig[idx]))

        # Sort the movies
        sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)

        # Scores of the 10 most similar movies
        sig_scores = sig_scores[1:11]

        # Movie indices
        movie_indices = [i[0] for i in sig_scores]

        # Top 10 most similar movies
        return movies_cleaned['original_title'].iloc[movie_indices]
        
        
        

print("Enter movie name")
movie_name = input()
movie_name = movie_name.title()
recommendations = list(give_recomendations(movie_name))
if(len(recommendations) > 0):
    print(f"\nHere are the list of top 10 movies whose content matches with movie - {movie_name}\n")
    for index, value in enumerate(recommendations):
        print(f"{index}) {value}")
else:
    print("Exiting now ...")
