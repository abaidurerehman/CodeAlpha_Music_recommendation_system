Spotify Music Recommendation System
 Overview

This project is a machine learning-based music recommendation system that predicts whether a song will be repeatedly played within a given timeframe using Spotify song attributes. It uses a Flask API to provide song recommendations based on user input.
 Dataset

The dataset used contains song features with the following columns:

['artist', 'song', 'duration_ms', 'explicit', 'year', 'popularity',
 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo',
 'genre']

The target variable is popularity, which is binary:

1 → The song is repeatedly played within a month.

0 → The song is not repeatedly played.

Features

Predicts if a song will be popular based on its features.

Uses machine learning with a trained model.

Flask REST API for making predictions.

Scales and encodes input data before prediction.
