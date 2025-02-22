"""Books."""


class Book:
    """Book class."""

    def __init__(self, title: str, author: str, pages: int, sales: int, genres: list[str], publication_year: int):
        """
        Initialize a Book object.

        :param title: The title of the book.
        :param author: The author of the book.
        :param pages: The amount of pages in the book.
        :param sales: The amount of times the book has been sold.
        :param genres: The genres of the book.
        :param publication_year: The year the book was published.
        """
        self.title = title
        self.author = author
        self.pages = pages
        self.sales = sales
        self.genres = genres
        self.year = publication_year

    def __eq__(self, other) -> bool:
        """Return True if the Book objects are equal."""
        return type(other) is self.__class__ and \
            self.title == other.title and \
            self.author == other.author and \
            self.pages == other.pages and \
            self.sales == other.sales and \
            self.genres == other.genres and \
            self.year == other.year

    def __hash__(self) -> int:
        """Allow a Book object to be used as a key in a dictionary. Don't change this method."""
        return hash((self.title, self.author, self.pages, self.sales, tuple(self.genres), self.year))

    def __repr__(self) -> str:
        """Return a string representation of the Book object."""
        return f'"{self.title}" by {self.author}'


def author_book_count(library: list[Book], author: str) -> int:
    """
    Find the number of books written by the given author.

    :param library: The list of books to search through.
    :param author: The given author.
    :return: The amount of books written by the author.
    """
    return sum(1 for book in library if book.author == author)


def author_page_count(library: list[Book], author: str) -> int:
    """
    Find the total number of pages written by the given author.

    :param library: The list of books to search through.
    :param author: The given author.
    :return: The total number of pages written by the author.
    """
    return sum(book.pages for book in library if book.author == author)


def most_popular_book(library: list[Book]) -> Book:
    """
    Find the book with the most sales.

    :param library: The list of books.
    :return: The Book object with the most sales.
    """
    return max(library, key=lambda book: book.sales)  # это наверху смотри, где репр


def most_popular_author(library: list[Book]) -> str:
    """
    Find the author with the most sales.

    If two or more authors have the same amount of sales, it doesn't matter which one is returned.

    :param library: The list of books.
    :return: The author with the most sales.
    """
    result = {}
    for book in library:
        if book.author not in result:
            result[book.author] = book.sales
        else:
            result[book.author] += book.sales
    return max(result, key=result.get)
    # result = {'a': 10, 'b': 20, 'c': 15}
    # max_key = max(result, key=result.get)  # max_key будет равно 'b'


def average_author_book_length(library: list[Book], author: str) -> float:
    """
    Find the average length of a book (amount of pages), that is written by the given author.

    :param library: The list of books.
    :param author: The given author.
    :return: The average length of the author's books.
    """
    books = {}
    for book in library:
        if book.author == author:
            books[book] = book.pages
    return sum(books.values()) / len(books.keys())


def find_best_selling_genre(library: list[Book]) -> str:
    """
    Find the genre, that has the most sales. If two or more genres have the same amount of sales, return either one.

    :param library: The list of books.
    :return: The genre with the most total sales.
    """
    result = {}
    for book in library:
        for genre in book.genres:
            if genre not in result:
                result[genre] = book.sales
            else:
                result[genre] += book.sales
    return max(result, key=result.get)  # values никак


def find_books_by_genre_and_year(library: list[Book], genre: str, year: int) -> list[Book]:
    """
    Find all books in the given list, that match the given year and genre.

    For the genre, you should check if the given genre is contained in the list of genres of the book.
    The result should be sorted by sales (descending) and if two or more books have the same sales,
    then sort them by title (alphabetically).

    :param library: The list of books to search from.
    :param genre: The genre to search for.
    :param year: The year to search for.
    :return: A list of books, that match the given genre and year, sorted by sales (descending) and title (alphabetically).
    """
    return sorted(filter(lambda book: genre in book.genres and year == book.year, library), key=lambda book: (-book.sales, book.title))  # Negate sales for descending order


def most_popular_author_per_century(library: list[Book]) -> dict[int, str]:
    """
    Find the author with the most sales for each century.

    If two or more authors have the same amount of sales, it doesn't matter which one is returned in the dictionary.

    :param library: The list of books.
    :return: A dictionary, where the keys are the centuries and the values are the authors with the most sales in that
    century.
    """
    sales = {}

    for book in library:
        century = (book.year // 100) + 1 if book.year % 100 != 0 else (book.year // 100)

        if century not in sales:
            sales[century] = {}

        if book.author not in sales[century]:
            sales[century][book.author] = 0

        sales[century][book.author] += book.sales

    result = {}
    for century, authors in sales.items():
        most_popular = max(authors, key=authors.get)
        result[century] = most_popular

    return dict(sorted(result.items(), key=lambda x: x[0]))


if __name__ == '__main__':
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 218, 100_000, ["Classic", "Fiction"], 1925)
    book2 = Book("Tender Is the Night", "F. Scott Fitzgerald", 320, 90_000, ["Classic", "Fiction"], 1934)
    book3 = Book("The Beautiful and Damned", "F. Scott Fitzgerald", 348, 120_000, ["Classic", "Fiction"], 1922)
    book4 = Book("To Kill a Mockingbird", "Harper Lee", 324, 80_000, ["Fiction"], 1960)
    book5 = Book("Go Set a Watchman", "Harper Lee", 278, 70_000, ["Fiction"], 2015)
    book6 = Book("In Cold Blood", "Harper Lee", 368, 110_000, ["True Crime"], 1966)
    book7 = Book("1984", "George Orwell", 328, 200_000, ["Dystopian", "Fiction"], 1949)
    book8 = Book("Animal Farm", "George Orwell", 144, 70_000, ["Satire", "Fiction"], 1945)
    book9 = Book("Nineteen Eighty-Four", "George Orwell", 328, 95_000, ["Dystopian", "Fiction"], 1949)
    book10 = Book("Pride and Prejudice", "Jane Austen", 432, 85_000, ["Classic", "Romance"], 1813)

    book_list: list[Book] = [book1, book2, book3, book4, book5, book6, book7, book8, book9, book10]

    print(author_book_count(book_list, "Harper Lee"))  # 3
    print(author_page_count(book_list, "Harper Lee"))  # 970
    print(author_book_count(book_list, "Willy Wonka"))  # 0
    print(author_page_count(book_list, "Walter White"))  # 0
    print()

    print(most_popular_book(book_list))  # "1984" by George Orwell
    print(most_popular_author(book_list))  # George Orwell
    print(average_author_book_length(book_list, "Harper Lee"))  # 323.3333333333333
    print()

    print(find_best_selling_genre(book_list))  # Fiction
    print(find_books_by_genre_and_year(book_list, "Fiction",
                                       1949))  # ["1984" by George Orwell, "Nineteen Eighty-Four" by George Orwell]
    print(most_popular_author_per_century(book_list))  # {19: 'Jane Austen', 20: 'George Orwell', 21: 'Harper Lee'}
    print()
