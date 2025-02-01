import pandas as pd

data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

df = pd.DataFrame(data)

# Печать всего датафрейма
print(df)
print('')
# Печать первых 2 строк
print(df.head(2))
print('')
# Печать последних 2 строк
print(df.tail(1))
print('')
# Получение информации о датафрейме
df.info()
print('')
new_df = df.drop(labels=['B'], axis=1)
print(new_df)