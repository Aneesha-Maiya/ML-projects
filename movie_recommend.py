import pandas as pd
import numpy as np
import csv 
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import sigmoid_kernel

movies = pd.read_csv('datasets/movies_cassandra.csv')
print(movies.info())

tfv = TfidfVectorizer(min_df=3,  max_features=None,
            strip_accents='unicode', analyzer='word',token_pattern=r'\w{1,}',
            ngram_range=(1, 3),
            stop_words = 'english')

tfv_matrix = tfv.fit_transform(movies['overview'].values.astype(str))

sig = sigmoid_kernel(tfv_matrix, tfv_matrix)

indices = pd.Series(movies.index, index=movies['original_title']).drop_duplicates()

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
        return movies['original_title'].iloc[movie_indices]
    
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
        