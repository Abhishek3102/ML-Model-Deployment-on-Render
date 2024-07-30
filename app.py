from flask import Flask, request, render_template, jsonify
import pickle
import pandas as pd
import difflib
import numpy as np

app = Flask(__name__)

# Load the dataset
df = pd.read_csv('movies.csv')

# Load the trained model
model_path = 'movies_model.pkl'
with open(model_path, 'rb') as file:
    similarity = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    movie_name = request.form['movie_name']
    all_movie_names = df['title'].tolist()
    find_close_match = difflib.get_close_matches(movie_name, all_movie_names)

    if not find_close_match:
        return render_template('index.html', recommended_movies=["No match found. Please try again."])

    close_match = find_close_match[0]
    movie_index = df[df.title == close_match].index[0]

    # Get similarity scores
    similarity_score = list(enumerate(similarity[movie_index]))
    sorted_similarity_score = sorted(similarity_score, key=lambda x: x[1], reverse=True)

    recommended_movies = []
    for i, movie in enumerate(sorted_similarity_score[1:31]):  # Skip the first movie as it is the input movie itself
        index = movie[0]
        title_from_index = df.loc[index, 'title']
        recommended_movies.append(title_from_index)

    return render_template('index.html', recommended_movies=recommended_movies)

if __name__ == "__main__":
    app.run(debug=True)
