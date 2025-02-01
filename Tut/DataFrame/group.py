import pandas as pd

data = {
    'movieId': [1, 1, 1, 2, 2],
    'tag': ['funny', 'animated', 'family', 'action', 'thriller']
}

df = pd.DataFrame(data)

print(df)
print('')

result = df.groupby('movieId').agg({'tag': lambda x: ' '.join(x)}).reset_index()
print(result)

