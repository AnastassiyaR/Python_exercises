import pandas as pd

data = {
    'title': ['Movie A', 'Movie B', 'Movie C', 'Movie D'],
    'rating': [5.0, 7.5, 6.0, 8.2]
}

movie_data = pd.DataFrame(data)

rating = 6.0

boolean_series = movie_data['rating'] > rating
print(boolean_series)
print()

filtered_movies = movie_data[boolean_series]
print(filtered_movies)