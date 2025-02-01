import pandas as pd

data = {
    'title': ['Movie A (2020)', 'Movie B (2019)', 'Movie C (2021)', 'Movie D (2022)']
}

movie_data = pd.DataFrame(data)
print(movie_data)
print()
extracted_years = movie_data['title'].str.extract(r'(\d{4})') == '2020'
print(extracted_years)
print()
print(extracted_years[0])

"""
      0
0  True
1  False
2  False
3  False
................................
0    2020
1    2019
2    2021
3    2022
Name: 0, dtype: object
"""
