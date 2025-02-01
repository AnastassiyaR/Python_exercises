import pandas as pd


movies_data = {
    'movieId': [1, 2, 3],
    'title': ['Фильм A', 'Фильм B', 'Фильм C']
}
movies = pd.DataFrame(movies_data)


ratings_data = {
    'movieId': [1, 1, 2],
    'rating': [5, 4, 3]
}
ratings = pd.DataFrame(ratings_data)


tags_data = {
    'movieId': [1, 1, 2],
    'tag': ['комедия', 'приключения', 'драма']
}
tags = pd.DataFrame(tags_data)


# Объединяем данные о фильмах и оценках
aggregate_movie_dataframe = movies.merge(ratings, on='movieId', how='left')
print(tags)
print('')

print('step 1')
print(aggregate_movie_dataframe)
print('')

# Объединяем с тегами
aggregate_movie_dataframe = aggregate_movie_dataframe.merge(tags, on='movieId', how='left')

print('step 2')
print(aggregate_movie_dataframe)
print('')
# Заполняем пустые значения в столбце 'tag'
nan_placeholder = 'Нет тегов'
aggregate_movie_dataframe['tag'] = aggregate_movie_dataframe['tag'].fillna(nan_placeholder)

# Печатаем итоговый датафрейм
print(aggregate_movie_dataframe)