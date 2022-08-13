import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import spotipy
import os

spotify_data = pd.read_csv('./spotifydata/data.csv')
genre_data = pd.read_csv('./spotifydata/data_by_genres.csv')
data_by_year = pd.read_csv('./spotifydata/data_by_year.csv')

sound_features = ['acousticness', 'danceability', 'speechiness']
fig = px.line(data_by_year, x='year', y=sound_features)
fig.show()