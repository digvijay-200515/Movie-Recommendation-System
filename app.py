import streamlit as st
import pickle
import pandas as pd
import requests
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve the API key
api_key = os.getenv("TMDB_API_KEY")

def fetch_poster(movie_id):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US'
    )
    data = response.json()
    return 'http://image.tmdb.org/t/p/w500/' + data['poster_path']


def recommend(movie):
    # Find the index of the movie in the movies DataFrame
    movie_index = movies[movies['title'] == movie].index[0]
    # Get the similarity values for the movie
    distances = similarity[movie_index]
    # Sort the movies based on similarity, exclude the first movie (which is the selected one)
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies = []
    recommended_movies_poster = []
    
    for i in movies_list:
        movie_id = movies.iloc[i[0]]['movie_id']  # Correctly access the movie_id
        recommend_movies.append(movies.iloc[i[0]]['title'])  # Get movie title
        recommended_movies_poster.append(fetch_poster(movie_id))  # Get movie poster
    
    return recommend_movies, recommended_movies_poster


# Load necessary pickled data
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Streamlit app UI
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "Which Movie are you looking for:",
    movies['title'].values
)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)
    
    # Use st.columns instead of beta_columns
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.text(names[0])
        st.image(posters[0])
    
    with col2:
        st.text(names[1])
        st.image(posters[1])
    
    with col3:
        st.text(names[2])
        st.image(posters[2])
    
    with col4:
        st.text(names[3])
        st.image(posters[3])
    
    with col5:
        st.text(names[4])
        st.image(posters[4])
