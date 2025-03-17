 Spotify Music Recommendation System

Overview

This project is a machine learning-based music recommendation system that predicts whether a song will be repeatedly played within a given timeframe using Spotify song attributes. The model analyzes various features such as danceability, energy, loudness, and genre to determine a song's popularity.

 Dataset

The dataset consists of song metadata with the following features:

Numerical Attributes: Duration (ms), Danceability, Energy, Loudness, Tempo, Valence, Speechiness, etc.

Categorical Attributes: Genre, Mode, Explicitness.

Target Variable: Popularity (Binary: 1 = Popular, 0 = Not Popular).

The model is trained to classify whether a song is likely to be played repeatedly within a given period.


 Testing Locally

If testing locally → Open http://127.0.0.1:5001 in your browser.

 Summary

Implements a machine learning model for music recommendation.

Uses Flask API for interaction.

Scalable deployment with Gunicorn.

Predicts song popularity based on key features.

This project serves as a foundation for personalized music recommendations and can be extended further with real-time streaming data.

