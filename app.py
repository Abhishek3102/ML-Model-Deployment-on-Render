from flask import Flask, request, render_template
import pickle
import difflib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load the dataset
model_path = 'movies_model.pkl'
with open(model_path, 'rb') as file:
    df = pickle.load(file)

# Recompute the similarity matrix
selected_features = ["genres", "keywords", "tagline", "cast", "director"]
for feature in selected_features:
    df[feature] = df[feature].fillna("")
combined_features = df["genres"] + " " + df["keywords"] + " " + df["tagline"] + " " + df["cast"] + " " + df["director"]
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)
similarity = cosine_similarity(feature_vectors)

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

    try:
        movie_index = df[df.title == close_match].index[0]
    except IndexError:
        return render_template('index.html', recommended_movies=["Error finding movie index. Please try again."])

    try:
        similarity_score = list(enumerate(similarity[movie_index]))
    except IndexError:
        return render_template('index.html', recommended_movies=["Error accessing similarity scores. Please try again."])

    sorted_similarity_score = sorted(similarity_score, key=lambda x: x[1], reverse=True)

    recommended_movies = []
    for i, movie in enumerate(sorted_similarity_score[1:31]):  # Skip the first movie as it is the input movie itself
        index = movie[0]
        try:
            title_from_index = df.loc[index, 'title']
        except KeyError:
            continue
        recommended_movies.append(title_from_index)

    return render_template('index.html', recommended_movies=recommended_movies)

if __name__ == "__main__":
    app.run(debug=True)
