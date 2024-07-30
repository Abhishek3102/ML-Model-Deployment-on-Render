# Movie Recommendation System

This repository contains a movie recommendation system built using a dataset of movies and a Flask web application for deployment. The model is first deployed locally and then on Render for production.

## Dataset

The dataset used in this project contains various features of movies, including:
- **genres**: The genres of the movie.
- **keywords**: Keywords associated with the movie.
- **tagline**: The tagline of the movie.
- **cast**: The main cast of the movie.
- **director**: The director of the movie.
- **title**: The title of the movie.
- **popularity**: The popularity score of the movie.

### Data Preprocessing

The selected features for building the recommendation model are `genres`, `keywords`, `tagline`, `cast`, and `director`. These features are combined into a single string and converted into numerical values using TF-IDF vectorization. Cosine similarity is then used to compute the similarity scores between movies.

## Model Deployment

### Local Deployment

The Flask web application is created to serve the recommendation model. The application consists of the following main components:

- **app.py**: The main application file that loads the model, handles user input, computes recommendations, and renders the results.
- **templates/index.html**: The HTML template for the web interface.

### Render Deployment

The application is deployed on Render, a cloud platform for hosting web applications. You can check the deployment using the following link: [Movie Recommendation System on Render](https://ml-model-deployment-on-render.onrender.com)

## Files in the Repository

- **app.py**: Main Flask application.
- **movies_model.pkl**: Pickle file containing the preprocessed movie dataset.
- **templates/index.html**: HTML template for the web interface.
- **README.md**: This file.

## Usage

### Local Deployment

1. Clone the repository:
   git clone https://github.com/yourusername/movies-recommendation-system.git

2. Navigate to the project directory:
   cd movies-recommendation-system

3. Install the required packages:
   pip install -r requirements.txt

4. Run the Flask application:
   python app.py

5. Open a web browser and go to http://127.0.0.1:5000/.
   
Render Deployment
The application is already deployed on Render. You can access it using the following link: Movie Recommendation System on Render

Features
- Enter Movie Name: Users can input the name of their favorite movie to get recommendations.
- Movie Recommendations: The system provides a list of 30 movies similar to the input movie based on the similarity scores.
Example
- Open the web application.
- Enter the name of your favorite movie.
- Click on the "Recommend" button.
- The application displays a list of 30 recommended movies.
Conclusion
This project demonstrates a simple yet effective way to build and deploy a movie recommendation system using Flask and Render. It utilizes TF-IDF vectorization and cosine similarity to provide recommendations based on movie features.

Feel free to explore and enhance the project by adding more features or improving the recommendation algorithm.

## This is how it looks:
![image](https://github.com/user-attachments/assets/5359eaa5-bce0-4173-8859-af08737b76d8)
