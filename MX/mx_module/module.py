"""What should we watch, Honey?..."""
import pandas as pd


class MovieData:
    """
    Class MovieData.

    Here we keep the initial data and the cleaned-up aggregate dataframe.
    """

    def __init__(self):
        """
        Class initialization.

        Here we declare variables for storing initial data and a variable for storing
        an aggregate of processed initial data.
        """
        self.movies = None or pd.DataFrame
        self.ratings = None or pd.DataFrame
        self.tags = None or pd.DataFrame
        self.aggregate_movie_dataframe = None or pd.DataFrame

    def load_data(self, movies_filename: str, ratings_filename: str, tags_filename: str) -> None:
        """
        Load Data from files into dataframes.

        Raise the built-in ValueError exception if either movies_filename, ratings_filename or
        tags_filename is None.

        :param movies_filename: file path for movies.csv file.
        :param ratings_filename: file path for ratings.csv file.
        :param tags_filename: filepath for tags.csv file.
        :return: None or raise ValueError
        """
        if movies_filename is None or ratings_filename is None or tags_filename is None:
            raise ValueError

        self.movies = pd.read_csv(movies_filename)
        self.ratings = pd.read_csv(ratings_filename)
        self.tags = pd.read_csv(tags_filename)

        # pd.read_csv(movies_filename): Эта функция из библиотеки pandas загружает данные из CSV файла,
        # путь к которому передан в переменной movies_filename.

    def remove_cols(self, df: pd.DataFrame, columns: list) -> pd.DataFrame:
        """
        Drop columns from dataframe.

        :param df: dataframe to be changed.
        :param columns: list of column names to be removed
        :return: dataframe without those columns
        """
        return df.drop(labels=columns, axis=1)

    """
    df.drop(...)
    df: Это входной параметр метода, который представляет собой объект pandas.DataFrame. Он содержит данные,
    из которых мы хотим удалить столбцы.
    .drop(...): Это метод pandas, который используется для удаления указанных строк или столбцов из датафрейма.

    2. labels=columns
    labels: Это параметр метода drop, который принимает список меток (имен) строк или столбцов, которые нужно удалить.
    columns: Это входной параметр метода remove_cols, который представляет собой список имен столбцов,
    которые мы хотим удалить из датафрейма df.

    3. axis=1
    axis: Этот параметр указывает, по какому измерению нужно выполнять операцию удаления.
    axis=0 означает, что мы хотим удалить строки (по индексу).
    axis=1 означает, что мы хотим удалить столбцы (по именам столбцов).
    В данном случае, поскольку мы хотим удалить столбцы, мы указываем axis=1.
    """

    def merge_col_string_on_key(self, df: pd.DataFrame, key: str, col: str) -> pd.DataFrame:
        """
        Merge columns.

        :param df: dataframe to be merged.
        :param key: column that needs to contain only unique values
        :param col: column that needs to contain joined values separated by ' '
        :return: dataframe with reduced number of rows
        """
        return df.groupby(key).agg({col: lambda x: ' '.join(x)}).reset_index()

    """
    1. df.groupby(key)
    df: Это входной параметр метода, который представляет собой объект pandas.DataFrame.
    .groupby(key): Этот метод группирует строки датафрейма по уникальным значениям в столбце,
    указанном в переменной key. Например, если key равен 'movieId',
    то все строки с одинаковым movieId будут сгруппированы вместе.

    2. .agg({col: lambda x: ' '.join(x)})
    .agg(...): Этот метод применяется к сгруппированным данным и позволяет выполнять агрегирующие операции.
    {col: lambda x: ' '.join(x)}: Здесь мы указываем,
    что для столбца col (например, tag) мы хотим объединить все значения в одну строку, разделенную пробелами.
    lambda x: ' '.join(x): Это анонимная функция, которая принимает серию значений x и объединяет их в одну строку,
    разделяя пробелами. Например, если у нас есть теги ['funny', 'animated', 'family'],
    то результатом будет строка 'funny animated family'.

    3. .reset_index()
    .reset_index(): Этот метод сбрасывает индекс датафрейма, создавая новый индекс для результирующего датафрейма.
    Это полезно, чтобы вернуть датафрейм в стандартный формат, где индексы начинаются с 0.
    """

    def create_aggregate_movie_dataframe(self, nan_placeholder: str = '') -> None:
        """
        Create an aggregate dataframe from frames self.movies, self.ratings and self.tags.

        No columns with name 'userId' or 'timestamp' allowed. Use function remove_cols.
        Columns should be in order:
        'movieId', 'title', 'genres', 'rating', 'tag'.
        Several lines in the tags.csv file with the same movieId
        should be joined together under the tag column. Use function merge_col_string_on_key.

        :param nan_placeholder: Value to replace all nan-valued elements in column 'tag'.
        :return: None
        """
        self.ratings = self.remove_cols(self.ratings, ['userId', 'timestamp'])
        self.tags = self.merge_col_string_on_key(self.tags, 'movieId', 'tag')

        self.aggregate_movie_dataframe = self.movies.merge(self.ratings, on='movieId', how='left')
        self.aggregate_movie_dataframe = self.aggregate_movie_dataframe.merge(self.tags, on='movieId', how='left')
        self.aggregate_movie_dataframe['tag'] = self.aggregate_movie_dataframe['tag'].fillna(nan_placeholder)

    """
    self.movies: Это датафрейм, который содержит информацию о фильмах.
    .merge(...): Этот метод объединяет два датафрейма.

    on='movieId': Мы объединяем данные по столбцу movieId, который должен присутствовать в обоих датафреймах.

    how='left': Это означает, что мы хотим сохранить все строки из self.movies и
    добавить соответствующие строки из self.ratings. Если для какого-то фильма нет оценок,
    в результирующем датафрейме будут NaN (пустые значения).

    Теперь мы добавляем теги (self.tags) к уже объединенным данным о фильмах и оценках, снова используя movieId как ключ.
    Опять же, если у фильма нет тегов, в соответствующих местах будет NaN.

    Мы заменяем все пустые значения в столбце tag на значение, указанное в nan_placeholder (например, 'Нет тегов').
    """

    def get_movies_dataframe(self) -> pd.DataFrame:
        """
        Return movies dataframe.

        :return: pandas DataFrame
        """
        return self.movies

    def get_ratings_dataframe(self) -> pd.DataFrame:
        """
        Return ratings dataframe.

        :return: pandas DataFrame
        """
        return self.ratings

    def get_tags_dataframe(self) -> pd.DataFrame:
        """
        Return tags dataframe.

        :return: pandas DataFrame
        """
        return self.tags

    def get_aggregate_movie_dataframe(self) -> pd.DataFrame:
        """
        Return aggregate_movie_dataframe variable created with function create_aggregate_movie_dataframe.

        :return: pandas DataFrame
        """
        return self.aggregate_movie_dataframe


class MovieFilter:
    """
    Class MovieFilter.

    Here we keep the aggregate dataframe from MovieData class and operate on that data.
    """

    def __init__(self):
        """
        Class initialization.

        Here we only need to store the aggregate dataframe from MovieData class.
        """
        self.movie_data = pd.DataFrame()
        # Запомни это pd!!!

    def set_movie_data(self, movie_data: pd.DataFrame) -> None:
        """
        Set the value of self.movie_data to be given argument movie_data.

        :param movie_data: pandas DataFrame object
        :return: None
        """
        self.movie_data = movie_data

    def filter_movies_by_rating_value(self, rating: float, comp: str) -> pd.DataFrame:
        """
        Return pandas DataFrame of self.movie_data filtered according to rating and comp string value.

        Raise the built-in ValueError exception if rating is None or < 0.
        Raise the built-in ValueError exception if comp is not 'greater_than', 'equals' or 'less_than'.

        :param rating: value for comparison operation to compare to
        :param comp: string representation of the comparison operation
        :return: pandas DataFrame object of the filtration result
        """
        if rating is None or rating < 0:
            raise ValueError
        if comp not in ['greater_than', 'equals', 'less_than']:
            raise ValueError

        if comp == 'greater_than':
            return self.movie_data[self.movie_data['rating'] > rating]
        elif comp == 'equals':
            return self.movie_data[self.movie_data['rating'] == rating]
        elif comp == 'less_than':
            return self.movie_data[self.movie_data['rating'] < rating]

    def filter_movies_by_genre(self, genre: str) -> pd.DataFrame:
        """
        Return a pandas DataFrame of self.movie_data filtered by parameter genre.

        Only rows where the given genre is in column 'genres' should be in the result.
        Operation should be case-insensitive.

        Raise the built-in ValueError exception if genre is an empty string or None.

        :param genre: string value to filter by
        :return: pandas DataFrame object of the filtration result
        """
        if genre is None or genre.strip() == "":
            raise ValueError("Genre must be a non-empty string")

        # Фильтрация по жанру
        return self.movie_data[self.movie_data['genres'].str.contains(genre, case=False)]

    """
    self.movie_data['genres']: Здесь мы обращаемся к столбцу genres в DataFrame.

    Метод str.contains(genre, case=False) выполняет следующее:

    Проверяет, содержится ли подстрока genre в каждой строке столбца genres:
    Это значит, что он ищет, есть ли указанный жанр (например, "Action") в жанрах фильмов.

    Параметр case=False: Указывает, что поиск не должен учитывать регистр.
    То есть "Action", "action" и "ACTION" будут считаться одинаковыми.

    Пример
    Если у вас есть столбец genres с такими значениями:

    "Action, Comedy"
    "Drama"
    "action, Thriller"
    "Horror"
    И вы ищете genre = "action", то str.contains("action", case=False) вернет True для первых и третьих строк,
    потому что "Action" и "action" присутствуют в этих строках, независимо от регистра.
    """

    def filter_movies_by_tag(self, tag: str) -> pd.DataFrame:
        """
        Return a pandas DataFrame of self.movie_data filtered by parameter tag.

        Only rows where the given tag is in column 'tag' should be left in the result.
        Operation should be case-insensitive.

        Raise the built-in ValueError exception if tag is an empty string or None.

        :param tag: string value to filter by
        :return: pandas DataFrame object of the filtration result
        """
        if tag is None or tag == '':
            raise ValueError("Tag cannot be empty or None")
        return self.movie_data[self.movie_data['tag'].str.contains(tag, case=False)]

    def filter_movies_by_year(self, year: int) -> pd.DataFrame:
        """
        Return a pandas DataFrame of self.movie_data filtered by year of release.

        Only rows where the year of release matches given parameter year should be left in the result.

        Raise the built-in ValueError exception if year is None or < 0.

        :param year: integer value of the year to filter by
        :return: pandas DataFrame object of the filtration result
        """
        if year is None or year < 0:
            raise ValueError("Year must be a non-negative integer")

        return self.movie_data[self.movie_data['title'].str.extract(r'(\d{4})')[0] == str(year)]

    def get_decent_movies(self) -> pd.DataFrame:
        """
        Return all movies with a rating of at least 3.0.

        :return: pandas DataFrame object of the search result
        """
        return self.movie_data[self.movie_data['rating'] >= 3.0]

    def get_decent_comedy_movies(self) -> pd.DataFrame:
        """
        Return all movies with a rating of at least 3.0 and where genre is 'Comedy'.

        :return: pandas DataFrame object of the search result
        """
        comedy_movies = self.filter_movies_by_genre('Comedy')
        return comedy_movies[comedy_movies['rating'] >= 3.0]

    def get_decent_children_movies(self) -> pd.DataFrame:
        """
        Return all movies with a rating of at least 3.0 and where genre is 'Children'.

        :return: pandas DataFrame object of the search result
        """
        children_movies = self.filter_movies_by_genre('Children')
        return children_movies[children_movies['rating'] >= 3.0]


if __name__ == '__main__':
    # this pd.option_context menu is for better display purposes
    # in terminal when using print. Keep these settings the same
    # unless you wish to display more than 10 rows
    with pd.option_context('display.max_rows', 10,
                           'display.max_columns', 5,
                           'display.width', 200):
        my_movie_data = MovieData()

        # give correct path names here. These names are only good if you
        # installed the 3 data files in 'EX/ex15_movie_data/ml-latest-small/'
        my_movie_data.load_data("movies.csv", "ratings.csv", "tags.csv")
        print(my_movie_data.get_movies_dataframe())  # ->
        #       movieId                    title                                       genres
        # 0           1         Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy
        # 1           2           Jumanji (1995)                   Adventure|Children|Fantasy
        # 2           3  Grumpier Old Men (1995)                               Comedy|Romance
        # 3           4 Waiting to Exhale (1995)                         Comedy|Drama|Romance
        # ...
        # [9742 rows x 3 columns]  <- if your numbers match the numbers shown here it's a good
        #                             chance your function is getting the correct results.

        print(my_movie_data.get_ratings_dataframe())  # ->
        #       userId      movieId     rating      timestamp
        # 0          1            1        4.0      964982703
        # 1          1            3        4.0      964981247
        # 2          1            6        4.0      964982224
        # 3          1           47        5.0      964983815
        # ...
        # [100836 rows x 4 columns]

        print(my_movie_data.get_tags_dataframe())  # ->
        #       userId      movieId             tag     timestamp
        # 0          2        60756           funny    1445714994
        # 1          2        60756 Highly quotable    1445714996
        # 2          2        60756    will ferrell    1445714992
        # 3          2        89774    Boxing story    1445715207
        # ...
        # [3683 rows x 4 columns]

        my_movie_data.create_aggregate_movie_dataframe('--empty--')
        print(my_movie_data.get_aggregate_movie_dataframe())  # ->
        #         movieId                                      title                                       genres  rating              tag
        # 0             1                           Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy     4.0  pixar pixar fun
        # 1             1                           Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy     4.0  pixar pixar fun
        # 2             1                           Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy     4.5  pixar pixar fun
        # 3             1                           Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy     2.5  pixar pixar fun
        # 4             1                           Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy     4.5  pixar pixar fun
        # ...
        # 100849   193581  Black Butler: Book of the Atlantic (2017)              Action|Animation|Comedy|Fantasy     4.0         --empty--
        # 100850   193583               No Game No Life: Zero (2017)                     Animation|Comedy|Fantasy     3.5         --empty--
        # 100851   193585                               Flint (2017)                                        Drama     3.5         --empty--
        # 100852   193587        Bungo Stray Dogs: Dead Apple (2018)                             Action|Animation     3.5         --empty--
        # 100853   193609        Andrew Dice Clay: Dice Rules (1991)                                       Comedy     4.0         --empty--
        # [100854 rows x 5 columns]
        # last rows in the aggregate dataframe will have the tag field set to '--empty--' since here
        # it is the nan_placeholder value given to the function.

        my_movie_filter = MovieFilter()
        my_movie_filter.set_movie_data(my_movie_data.get_aggregate_movie_dataframe())
        print(my_movie_filter.filter_movies_by_rating_value(2.1, 'less_than'))  # ->
        #   movieId             title                                       genres  rating               tag
        # 26      1  Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy     0.5   pixar pixar fun
        # 43      1  Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy     2.0   pixar pixar fun
        # 52      1  Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy     2.0   pixar pixar fun
        # 69      1  Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy     2.0   pixar pixar fun
        # ...
        # [13523 rows x 5 columns]

        print(my_movie_filter.filter_movies_by_year(1988))  # ->
        #        movieId                    title                                           genres  rating        tag
        # 17962      709  Oliver & Company (1988)      Adventure|Animation|Children|Comedy|Musical     5.0  --empty--
        # 17963      709  Oliver & Company (1988)      Adventure|Animation|Children|Comedy|Musical     2.0  --empty--
        # 17964      709  Oliver & Company (1988)      Adventure|Animation|Children|Comedy|Musical     3.0  --empty--
        # 17964      709  Oliver & Company (1988)      Adventure|Animation|Children|Comedy|Musical     3.5  --empty--
        # ...
        # [1551 rows x 5 columns]

        print(my_movie_filter.get_decent_movies())
        #   movieId              title                                       genres  rating               tag
        # 0       1   Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy     4.0   pixar pixar fun
        # 1       1   Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy     4.0   pixar pixar fun
        # 2       1   Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy     4.5   pixar pixar fun
        # 4       1   Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy     4.5   pixar pixar fun
        # 5       1   Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy     3.5   pixar pixar fun
        # [81763 rows x 5 columns]

        print(my_movie_filter.get_decent_comedy_movies())
        #   movieId              title                                       genres  rating               tag
        # 0       1   Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy     4.0   pixar pixar fun
        # 1       1   Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy     4.0   pixar pixar fun
        # 2       1   Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy     4.5   pixar pixar fun
        # 4       1   Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy     4.5   pixar pixar fun
        # 5       1   Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy     3.5   pixar pixar fun
        # [30274 rows x 5 columns]

        print(my_movie_filter.get_decent_children_movies())
        #   movieId               title                                       genres  rating                      tag
        # 0       1    Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy     4.0          pixar pixar fun
        # 1       1    Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy     4.0          pixar pixar fun
        # 2       1    Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy     4.5          pixar pixar fun
        # 4       1    Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy     4.5          pixar pixar fun
        # 5       1    Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy     3.5          pixar pixar fun
        # ...
        # [7326 rows x 5 columns]
