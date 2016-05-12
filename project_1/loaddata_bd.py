import os
import json
# constants
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.abspath(os.path.join(CURRENT_DIR, 'data'))
MOJO_DIR = os.path.join(DATA_DIR, 'boxofficemojo')


def load_mojo_data():
    movies = []

    for file_name in os.listdir(MOJO_DIR):
        target_file_path = os.path.join(MOJO_DIR, file_name)
        with open(target_file_path, 'r') as target_file:
            movie = json.load(target_file)
            movies.append(movie)

    return movies

def load_data(directory):
    movies = []
    folderpath = os.path.join(DATA_DIR, directory)
    for file_name in os.listdir(folderpath):
        target_file_path = os.path.join(directory, file_name)
        with open(target_file_path, 'r') as target_file:
            movie = json.load(target_file)
            movies.append(movie)

    return movies
