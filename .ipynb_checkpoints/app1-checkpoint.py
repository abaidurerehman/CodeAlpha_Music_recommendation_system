from flask import Flask, request, render_template_string
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
import os

# Load the dataset
try:
    df = pd.read_csv('spotify_data.csv')
except FileNotFoundError:
    print("Error: Dataset 'spotify_data.csv' not found.")
    exit()

# Drop duplicates
df = df.drop_duplicates(subset=['song'])

# Normalize numerical features
numerical_features = ['duration_ms', 'danceability', 'energy', 'loudness', 'speechiness', 
                      'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'popularity']
scaler = MinMaxScaler()
df[numerical_features] = scaler.fit_transform(df[numerical_features])

# Create feature vectors
df['feature_vector'] = df[numerical_features].apply(lambda x: x.tolist(), axis=1)
feature_matrix = np.array(df['feature_vector'].tolist())

# Compute cosine similarity
cosine_sim = cosine_similarity(feature_matrix)
similarity_df = pd.DataFrame(cosine_sim, index=df['song'], columns=df['song'])

# Recommendation function
def recommend_songs(song_name, num_recommendations=5):
    if song_name not in similarity_df.columns:
        return ["Song not found in the dataset. Please check the spelling or try another song."]
    sim_scores = similarity_df[song_name]
    sim_scores = sim_scores.sort_values(ascending=False)
    top_recommendations = sim_scores.iloc[1:num_recommendations+1].index.tolist()
    if not top_recommendations:
        return ["No recommendations found for this song."]
    return top_recommendations

# HTML template as a string
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Music Recommendation System</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            flex-direction: column;
        }
        h1 {
            color: #333;
        }
        form {
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        input[type="text"] {
            width: 300px;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        input[type="submit"] {
            padding: 10px 20px;
            background-color: #28a745;
            color: #fff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #218838;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            background: #fff;
            margin: 5px 0;
            padding: 10px;
            border-radius: 4px;
            box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>
<body>
    <h1>Music Recommendation System</h1>
    <form method="POST">
        <input type="text" name="song_name" placeholder="Enter a song name" required>
        <input type="submit" value="Get Recommendations">
    </form>
    {% if recommendations %}
    <h2>Recommended Songs:</h2>
    <ul>
        {% for song in recommendations %}
        <li>{{ song }}</li>
        {% endfor %}
    </ul>
    {% endif %}
</body>
</html>
"""

# Save the HTML template to a file
def save_html_template():
    if not os.path.exists('templates'):
        os.makedirs('templates')
    with open('templates/index.html', 'w') as file:
        file.write(html_template)

# Flask app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    recommendations = []
    if request.method == 'POST':
        song_name = request.form['song_name']
        recommendations = recommend_songs(song_name)
    return render_template_string(html_template, recommendations=recommendations)

if __name__ == '__main__':
    # Save the HTML template before running the app
    save_html_template()
    
    # Run the Flask app
    app.run(debug=True, port=5001)  # Runs on http://127.0.0.1:5001