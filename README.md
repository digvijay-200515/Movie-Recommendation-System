# Movie Recommendation System

## Overview
The **Movie Recommendation System** is a machine learning-based project that suggests movies to users based on their preferences. It utilizes content-based filtering technique to provide personalized movie recommendations.

## Features
- Personalized movie recommendations
- Content-based filtering using movie metadata
- Interactive web interface for users
- Scalable and efficient model for large datasets

## Technologies Used
- **Programming Language**: Python
- **Machine Learning Libraries**: scikit-learn, pandas, numpy
- **Web Framework**: Flask (for the web interface)
- **Dataset**: MovieLens dataset
- **API**: TMDb (The Movie Database) API

## Installation
### Prerequisites
Ensure you have Python installed on your system. You can download it from [Python's official website](https://www.python.org/).

### Steps to Install
1. Clone the repository:
   ```bash
   git clone https://github.com/adityachavan17/Movie-Recommendation-System.git
   cd Movie-Recommendation-System
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Obtain an API key from TMDb:
   - Go to [TMDb's official website](https://www.themoviedb.org/)
   - Sign up or log in
   - Navigate to the API section and generate your API key
   - Add the API key to your project (e.g., in a `.env` file or as a variable in your script)

4. Run the application:
   ```bash
   streamlit run app.py
   ```
5. Open your browser and go to the provided Streamlit URL to access the web interface.

## Usage
1. Open the web application in your browser.
2. Enter a movie name or select from the list.
3. Get recommendations based on the selected movie.

## Dataset
The system uses the **MovieLens dataset**, which includes user ratings, genres, and movie metadata to provide accurate recommendations.


