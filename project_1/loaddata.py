"""loaddata is a module for accessing scraped data about movies from
BoxOfficeMojo and Metacritic.
It's built specifically to work with the data collected for the
CapitalOne Metis Data Science Python Bootcamp Pilot Extravaganza 2K15.
"""

# imports
import os
import json
import pprint
import pandas as pd

# constants
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

def get_boxofficemojo_movies():
    DATA_DIR = os.path.abspath(os.path.join(CURRENT_DIR, 'data'))
    MOJO_DIR = os.path.join(DATA_DIR, 'boxofficemojo')
    file_contents = os.listdir(MOJO_DIR)

    movie_list = []

    for filename in file_contents:
        filepath = os.path.join(MOJO_DIR, filename)

        with open(filepath, 'r') as movie_file:
            movie_data = json.load(movie_file)

        movie_list.append(movie_data)

    print "Parsed %i movies from %i files" % (len(movie_list),
                                              len(file_contents))
    return movie_list

def load_data():
    DATA_DIR = os.path.join('data', 'boxofficemojo')
    all_movies=[]
    NameList = [name for name in os.listdir(DATA_DIR) if ".json" in name]

    for i in NameList:
        target_file_path = os.path.join(DATA_DIR, i)
        with open(target_file_path, 'r') as target_file:
            movie = json.load(target_file)
            all_movies.append(movie)

    movies_df = pd.DataFrame(all_movies)

    DATA_DIR = os.path.join('data', 'metacritic')
    metacritic=[]
    NameList = [name for name in os.listdir(DATA_DIR) if ".json" in name]

    for i in NameList:
        target_file_path = os.path.join(DATA_DIR, i)
        with open(target_file_path, 'r') as target_file:
            movie = json.load(target_file)
            if type(movie) is not dict:
                continue
            metacritic.append(movie)

    metacritic_df = pd.DataFrame(metacritic)

    return metacritic_df,movies_df

if __name__ == "__main__":
    movies = get_boxofficemojo_movies()
