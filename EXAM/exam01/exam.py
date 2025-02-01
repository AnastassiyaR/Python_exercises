"""Exam 1 (07.01.2025)"""


def find_substring_index(sentence: str, substring: str) -> int:
    """
    Check the index of where the substring appears at first in a given sentence string.

    * If the substring does not appear at all return -1
    * If the substring appears in the given string, return the index of where it starts at
    * Must be case-insensitive!

    find_substring_index("Hello World!", "Hello") => 0
    find_substring_index("Hello World!", "Hello!") => -1
    find_substring_index("Hello World!", "WoRLD") => 6
    find_substring_index("Hello World!", "lo") => 3

    :param sentence: Sentence to look the substring from.
    :param substring: Substring to look for in the sentence.
    :return: Index where the substring was found in the sentence.
    """
    return sentence.lower().find(substring.lower())


def mark_double_symbols(text: str) -> str:
    """
    Mark double symbols in a string.

    If there are two consecutive symbols which are the same, then mark it by replacing the second one with "2".
    For example: "aabbc" => "a2b2c"
    After the pair, counting restarts. So "aaa" => "a2a", "aaaa" => "a2a2", "aaaaa" => "a2a2a".

    :param text: Input text to be checked.
    :return: Result where the double symbols are "marked".
    """
    letters = []
    result = ''
    for i in text:
        if not i in result:
            result += str(i)
        elif i in result and not i in letters:
            letters.append(i)
            i = 2
            result += str(i)
        elif i in letters and i in result:
            letters.remove(i)
            result += str(i)
    return result


def battleships(battleship_map: list[list[str]]) -> list[tuple[str, int]]:
    """
    Find the coordinates of ships from the given map.

    * Ships are marked with "X"-s, empty strings are not considered ships.
    * The letters of the coordinates must be capitalized!
    * The tuples in your answer must be correctly ordered.
    * Maps can vary in size and might not always be squares.
    * The rows can go up to 26 (latin alphabet letters) but there is no limit for columns.

    battleships([["", ""], ["X", ""], ["", ""], ["X", "X"]]) => [(B, 1), (D, 1), (D, 2)]
    battleships([["", "X", ""], ["X", "", ""], ["X", "", ""]]) => [(A, 2), (B, 1), (C, 1)]

    The previous example more visualized:
    [     1    2    3
       A ["", "X", ""],
       B ["X", "", ""],
       C ["X", "", ""]
    ]

    :param battleship_map: Map of battleships where "X" marks a ship and empty string marks water.
    :return: List containing of tuples with the ships' coordinates from the map.
    """
    result = []
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for number, tabel in enumerate(battleship_map):
        for num, i in enumerate(tabel):
            if i == "X":
                letter_x = letters[number]
                result.append((letter_x, num + 1))

    return result


def json_fruit(fruit_list: list) -> dict:
    """
    Process fruit data into a compressed format suitable for JSON representation.

    This function processes a list of fruit dictionaries where each fruit has several properties:
    - 'fruit': The name of the fruit (e.g., 'apple', 'orange', 'pear').
    - 'weight': The weight of the fruit.
    - 'cultivar': The cultivar or variety of the fruit (e.g., 'gala' for an apple).
    - 'origin': The country of origin for the fruit.

    The function will return a dictionary where:
    - The keys are the fruit names (e.g., 'apple', 'orange').
    - Each fruit maps to a dictionary with three properties:
        - 'countries': A list of unique countries where the fruit is grown.
        - 'cultivars': A list of unique cultivars for that fruit.
        - 'total_weight': The total weight of that fruit across all entries.

    Note:
    -----
    - Weights of fruits can be None or negative, and such entries should be ignored.
    - The lists of countries and cultivars in the result may appear in any order.

    :param fruit_list: List of dictionaries containing fruit information.
    :return: Processed dictionary with fruits, their countries, cultivars, and total weight.
    """
    result = {}
    for fruit in fruit_list:
        fruit_name = fruit.get('fruit')
        weight = fruit.get('weight')
        cultivar = fruit.get('cultivar')
        origin = fruit.get('origin')

        if weight is None or weight < 0:
            continue

        if fruit_name not in result:
            result[fruit_name] = {
                'countries': set(),
                'cultivars': set(),
                'total_weight': 0.0
            }

        result[fruit_name]['countries'].add(origin)
        result[fruit_name]['cultivars'].add(cultivar)
        result[fruit_name]['total_weight'] += weight

    for fruit_name in result:
        result[fruit_name]['countries'] = list(result[fruit_name]['countries'])
        result[fruit_name]['cultivars'] = list(result[fruit_name]['cultivars'])
        result[fruit_name]['total_weight'] = round(result[fruit_name]['total_weight'], 2)

    return result


def file_system(path: str, name: str = "", lvl: int = 0) -> tuple[int, str]:
    """
    Find the file name and in which level of subdirectories the file is located in.

    Given a path from root '/', find how many folders do you have to traverse to get to a file in the path.
    Every path starts with a root directory '/' which is not counted in the number of subdirectories.
    Here we assume that every filename has an extension and the name part and the extension part are
    separated by a dot: '.'. Every character can be a part of the filename except '.' and '/'.

    if the given path is an empty string or no filename is found, return an empty tuple.

    Examples:
        file_system("") -> ()
        file_system("/") -> ()
        file_system("/file.ext") -> (0, 'file')
        file_system("/dir1/dir2/file2.pdf") -> (2, 'file2')
        file_system("/dir1/dir2/oth3r-C#@rs_allowed.pdf") -> (2, 'oth3r-C#@rs_allowed')

    Return a tuple of the no. of subfolders to the file and the filename.

    :param path: string with file path
    :param name: file name
    :param lvl: subdirectory level from root
    :return: tuple(lvl, name)
    """
    pass





def compress_dict(nested_dict: dict) -> dict:
    """
    Compress nested dictionary.

    Nesting needs to be represented with dots. When value is dictionary then new_key == original_key.it's_value's_key.
    The data type of the final value is not always `int`.

    {'a': {'b': {'c': {'d': {'e': 1}}}}} -> {'a.b.c.d.e': 1}
    {'a': 1, 'b': {'c': 2}} -> {'a':1, 'b.c': 2}
    {'a': {'b': 1, 'c': 2}} -> {'a.b': 1, 'a.c': 2}
    {'a': True, 'b': {'c': {}}} -> {'a': True, 'b.c': {}}
    {} -> {}

    :param nested_dict: Dictionary that might have dictionaries as values.
    :return: Compressed dictionary.
    """
    result = {}

    for key, value in nested_dict.items():
        if isinstance(value, dict):
            nested_result = compress_dict(value)
            for nested_key, nested_value in nested_result.items():
                result[f"{key}.{nested_key}"] = nested_value
        else:
            result[key] = value

    return result


class Video:
    """Class Video."""

    def __init__(self, title: str, author: str, duration: int):
        """
        Initialize Video.

        :param title: title of the video, should be in title case
        :param author: author of the video
        :param duration: duration of the video
        """
        self.title = title.title()
        self.author = author
        self.duration = duration


    def __repr__(self) -> str:
        """
        Represent Video.

        Video should be represented in the following format:
        [MINUTES:SECONDS] VIDEO AUTHOR - VIDEO TITLE

        Example:
        '[48:44] Taltech Coding - Regulaaravaldis'

        :return: String representation of the Video instance
        """
        hour = self.duration // 60
        minutes = self.duration % 60
        return f"[{hour}:{minutes}] {self.author} - {self.title}"


class VideoPlayer:
    """Class VideoPlayer."""

    def __init__(self):
        """Initialize VideoPlayer."""
        self.videos = []

    def add_video(self, video: Video) -> None:
        """
        Add video to the playlist.

        If video is already in playlist, then don't add it

        :param video: video to add to the playlist
        """
        if video not in self.videos:
            self.videos.append(video)

    def remove_video(self, video: Video) -> None:
        """
        Remove video from the playlist.

        :param video: video to remove from the playlist
        """
        if video in self.videos:
            self.videos.remove(video)

    def get_duration_of_queue(self) -> int:
        """Get the duration of all the videos in the playlist."""
        result = 0
        for i in self.videos:
            result += i.duration
        return result

    def get_videos_by_author(self, author: str) -> list[Video]:
        """Get all the videos of a specific author. Getting videos by author should be case-insensitive."""
        result = []
        for i in self.videos:
            if i.author.lower() == author.lower():
                result.append(i)
        return result

    def sort_videos_alphabetically(self) -> list[Video]:
        """Return an alphabetically sorted list of all videos by title. If the titles match, sort by author."""
        return sorted(self.videos, key=lambda x: (x.title, x.author))

    def sort_videos_by_duration(self) -> list[Video]:
        """Return a list of videos sorted by duration from longest to shortest."""
        return sorted(self.videos, key=lambda x: -x.duration)

    def get_shortest_video(self) -> Video:
        """Get the shortest video from the playlist."""
        return min(self.videos, key=lambda x: x.duration)

    def get_videos(self) -> list[Video]:
        """Get all the videos from the playlist."""
        return self.videos


categories = frozenset({"Electronics", "Food", "Toys"})


class Product:
    """A class representing a product with name, price, and category.

    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
        category (str): The category of the product.

    """

    def __init__(self, name: str, price: float, category: str) -> None:
        """Initialize a new Product instance.

        Args:
            name: The name of the product.
            price: The price of the product.
            category: The category of the product.

        Raises:
            ValueError: If the price is negative, or the category isn't in the predefined categories.

        """
        if category not in categories or price < 0:
            raise ValueError

        self.name = name
        self.price = price
        self.category = category
        self.sold = False
        self.shop = False

    def __repr__(self) -> str:
        """Represent the product as a string.

        The price is rounded to two digits after the period and always with two digits after the period.

        Returns:
            The formatted string that represents the product.
            For example:

            Product(0.00)

        """
        return f"{self.name}({self.price:.2f})"



class Customer:
    """Represents a customer with a name, age, products, and money.

    Attributes:
        name (str): The name of the customer.
        age (int): The age of the customer.
        products (set[Products]): The products that the customer has.
        money (float): The amount of money the customer has.

    """

    def __init__(self, name: str, age: int) -> None:
        """Initialize a new Customer instance.

        A Customer is initialized with an empty set of products, and a zero balance.

        Args:
            name: The name of the customer.
            age: The age of the customer.

        Raises:
            ValueError: If age is negative.

        """
        if age < 0:
            raise ValueError

        self.name = name
        self.age = age
        self.products = set()
        self.money = 0

        self.spend = 0


    def add_product(self, product: Product) -> None:
        """Add a product to the customer's set of owned products.

        Args:
            product: The product to be added.

        Raises:
            ValueError: If the product is already in some customer's product set.

        """
        if product.sold:
            raise ValueError
        self.products.add(product)

    def add_money(self, amount: float) -> None:
        """Add money to the customer's balance.

        Args:
            amount: The amount of money to be added.

        Raises:
            ValueError: If the amount is negative.

        """
        if amount < 0:
            raise ValueError
        self.money += amount

    def subtract_money(self, amount: float) -> None:
        """Subtract money from the customer's balance.

        Args:
            amount: The amount of money to be subtracted.

        Raises:
            ValueError: If the amount is negative, or the amount is higher than the customer's money amount.

        """
        if amount < 0 or amount > self.money:
            raise ValueError
        self.money -= amount


class Shop:
    """Represents a shop that manages products and customer transactions.

    Attributes:
        name (str): The name of the shop.
        products (set[Product]): The products that the shop has.
        finished_orders (set[Order]): The orders that the shop has completed.

    """

    def __init__(self, name: str) -> None:
        """Initialize a new Shop instance.

        A Shop is initialized with an empty set of products and an empty set of finished orders.

        Args:
            name: The name of the shop.

        """
        self.name = name
        self.products = set()
        self.customers = set()

    def add_product(self, product: Product) -> None:
        """Add a product to the shop's inventory.

        Args:
            product: The product to be added.

        Raises:
            ValueError: If the product already belongs to a shop or a customer.

        """
        if product in self.products or any(product in i.products for i in self.customers):
            raise ValueError
        self.products.add(product)

    def remove_product(self, product: Product) -> None:
        """Remove a product from the shop's inventory.

        Args:
            product: The product to be removed.

        Raises:
            ValueError: If the specified product isn't in the shop's inventory.

        """
        if product not in self.products:
            raise ValueError
        self.products.discard(product)

    def sell_product(self, product: Product, customer: Customer) -> None:
        """Sell a product to a customer, updating their balances, and the shop's inventory.

        Args:
            product: The product to be sold.
            customer: The customer buying the product.

        Raises:
            ValueError: If the product isn't in the shop's inventory, or the customer doesn't have enough money.

        """
        if product not in self.products or product.price > customer.money:
            raise ValueError
        self.products.discard(product)
        self.customers.add(customer)
        customer.spend += product.price
        customer.money -= product.price
        product.sold = True

    def stock_total_cost(self) -> float:
        """Calculate the total cost of all products in the shop's inventory.

        The cost is rounded to two digits after the period.

        Returns:
            The total cost.

        """
        result = 0
        for i in self.products:
            result += i.price
        return round(result, 2)

    def cheapest_products_sorted(self, amount: int | None = None, category: str | None = None) -> list[Product]:
        """Retrieve the least expensive products from the shop's inventory, optionally filtered by a category.

        The returned list is sorted by product names alphabetically descending.
        Sorting by name is performed after selecting the number of products in the collection.

        Args:
            amount: The number of the least expensive products is to retrieve, default is all.
            category: The category by which to filter products, default is all.

        Returns:
            The list of least expensive products.

        Raises:
            ValueError: If the amount is negative, or the category is invalid.

        """
        if amount and amount < 0 or category and category not in categories:
            raise ValueError
        result = []
        if not self.products:
            return result
        min_price = min(self.products, key=lambda p: p.price)
        for i in self.products:
            if (category is None or i.category == category) and i.price == min_price:
                result.append(i)
        sort_items = sorted(result, key=lambda x: -x.name)

        if amount:
            sort_items = sort_items[:amount + 1]

        return sort_items


    def top_customers(self, amount: int) -> list[Customer]:
        """Retrieve the top customers based on their total spending, number of products bought, and age.

        The returned list is sorted by the following criteria:

        1. Total spending, highest to lowest.
        2. Number of products bought, lowest to highest.
        3. Customer age, oldest to youngest.

        Only purchases made via Order are considered.

        Args:
            amount: The number of top customers to retrieve.

        Returns:
            The list of top customers.

        Raises:
            ValueError: If amount is negative.

        """
        if amount < 0:
            raise ValueError
        return sorted(self.customers, key=lambda x: (-x.spend, len(x.products), x.age))[:amount + 1]


class Order:
    """Represents an order made by a customer at a shop.

    Attributes:
        shop (Shop): The shop that the order is made in.
        customer (Customer): The customer that made this order.
        products (set[Product]): Products in this order.

    """

    def __init__(self, shop: Shop, customer: Customer) -> None:
        """Initialize a new Order instance.

        An Order is initialized with an empty set of products.

        Args:
            shop: The shop where the order is placed.
            customer: The customer who placed the order.

        """
        self.shop = shop
        self.customer = customer
        self.price = 0
        self.products = set()


    def add_product(self, product: Product) -> None:
        """Add a product to the order.

        Args:
            product: The product to be added to the order.

        Raises:
            ValueError: If the product isn't in the shop or is already in the same order.

        """
        if product not in self.shop.products or product in self.products:
            raise ValueError

        self.products.add(product)
        self.price += product.price

    def total_price(self) -> float:
        """Calculate the total price of the products in the order.

        Returns:
            The total price of the products in the order.

        """
        return self.price

    def confirm_order(self) -> None:
        """Confirm the order by selling products to the customer.

        Raises:
            RuntimeError: If the customer doesn't have enough money,
            or someone already bought some product in the order.

        """
        if self.customer.money < self.price:
            raise RuntimeError
        return True

    def remove_conflicting_products(self) -> None:
        """Remove products from the order that are already bought by some customer."""
        raise NotImplementedError


if __name__ == "__main__":
    print("find_substring_index:")
    print(find_substring_index("Hello World!", "Hello"))  # => 0
    print(find_substring_index("Hello World!", "Hello!"))  # => -1
    print(find_substring_index("Hello World!", "WoRLD"))  # => 6
    print(find_substring_index("Hello World!", "lo"))  # => 3
    print()

    print("mark_double_symbols:")
    print(mark_double_symbols("aabbcc"))  # => "a2b2c2"
    print(mark_double_symbols("AAbB!!!"))  # => "A2bB!2!"
    print()

    print("battleships:")
    print(battleships([["", ""], ["X", ""], ["", ""], ["X", "X"]]))  # [(B, 1), (D, 1), (D, 2)]
    print(battleships([["", "X", ""], ["X", "", ""], ["X", "", ""]]))  # [(A, 2), (B, 1), (C, 1)]
    print()

    print("json_fruit:")
    print(json_fruit([{'fruit': 'apple', 'weight': 0.21, 'cultivar': 'gala', 'origin': 'USA'}]))
    # Output should be:
    # {
    #     'apple': {
    #         'countries': ['USA'],
    #         'cultivars': ['gala'],
    #         'total_weight': 0.21
    #     }
    # }
    print()

    print("file_system:")
    print(file_system(""))  # -> ()
    print(file_system("/"))  # -> ()
    print(file_system("/file.ext"))  # -> (0, 'file')
    print(file_system("/dir1/dir2/file2.pdf"))  # -> (2, 'file2')
    print(file_system("/dir1/dir2/oth3r-C#@rs_allowed.pdf"))  # -> (2, 'oth3r-C#@rs_allowed')
    print()

    print("compressed_dict:")
    print(compress_dict({'a': {'b': {'c': {'d': {'e': 1}}}}}))  # -> {'a.b.c.d.e': 1}
    print(compress_dict({'a': 1, 'b': {'c': 2}}))  # -> {'a':1, 'b.c': 2}
    print(compress_dict({'a': {'b': 1, 'c': 2}}))  # -> {'a.b': 1, 'a.c': 2}
    print(compress_dict({'a': True, 'b': {'c': {}}}))  # -> {'a': True, 'b.c': {}}
    print(compress_dict({}))  # -> {}
    print()

    print("playlist:")
    playlist = VideoPlayer()
    video_1 = Video("Regulaaravaldis", "Taltech Coding", 2924)
    playlist.add_video(video_1)

    print(video_1)  # -> '[48:44] Taltech Coding - Regulaaravaldis'
    print(playlist.get_videos())  # [[48:44] Taltech Coding - Regulaaravaldis]

    video_2 = Video("how to hack py exam", "tatoim", 1337)
    playlist.add_video(video_2)
    print(playlist.get_duration_of_queue())  # -> 4261
    print(playlist.get_videos_by_author("taltech coding"))  # [[48:44] Taltech Coding - Regulaaravaldis]
    print(
        playlist.sort_videos_alphabetically())  # [[22:17] tatoim - how to hack py exam, [48:44] Taltech Coding - Regulaaravaldis]
    print(
        playlist.sort_videos_by_duration())  # [[48:44] Taltech Coding - Regulaaravaldis, [22:17] tatoim - how to hack py exam]
    print(playlist.get_shortest_video())  # -> [22:17] tatoim - how to hack py exam
    playlist.remove_video(video_1)
    print(playlist.get_videos())  # [[22:17] tatoim - how to hack py exam]
    print()

    print(f"\n{'| Complex OOP: Shop |'.center(79, '=')}")
    print(f"{'| Product |'.center(49, '-')}")
    product11 = Product("Laptop", 450.0, "Electronics")
    print(product11)  # Laptop(450.00)
    product2 = Product("Water", 0.217, "Food")
    print(product2)  # Water(0.22)
    product3 = Product("Phone", 300.0, "Electronics")

    print(f"\n{'| Shop |'.center(49, '-')}")
    shop = Shop("E-Pood")
    shop.add_product(product11)
    shop.add_product(product3)
    print(shop.products)  # {Phone(300.00), Laptop(450.00)}
    print(shop.stock_total_cost())  # 750.0
    shop.add_product(product2)
    print(shop.products)  # {Water(0.22), Phone(300.00), Laptop(450.00)}
    print(shop.stock_total_cost())  # 750.22

    print(f"\n{'| Shop.get_cheapest_products_sorted |'.center(49, '-')}")
    print(shop.cheapest_products_sorted())  # [Water(0.22), Phone(300.00), Laptop(450.00)]
    print(shop.cheapest_products_sorted(2))  # [Water(0.22), Phone(300.00)]
    print(shop.cheapest_products_sorted(1, "Electronics"))  # [Phone(300.00)]
    print(shop.cheapest_products_sorted(None, "Electronics"))  # [Phone(300.00), Laptop(450.00)]
    print(shop.cheapest_products_sorted(2, "Food"))  # [Water(0.22)]
    print(shop.cheapest_products_sorted(2, "Toys"))  # []

    print(f"\n{'| Customer |'.center(49, '-')}")
    customer1 = Customer("John Doe", 30)
    print(customer1.products)  # {}
    print(customer1.money)  # 0.0
    customer1.add_money(1000.0)
    print(customer1.money)  # 1000.0

    print(f"\n{'| Order.total_price |'.center(49, '-')}")
    order1 = Order(shop, customer1)
    print(order1.total_price())  # 0.0
    order1.add_product(product11)
    order1.add_product(product3)
    print(order1.products)  # {Phone(300.00), Laptop(450.00)}
    print(order1.total_price())  # 750.0

    print(f"\n{'| Order.confirm_order |'.center(49, '-')}")
    customer2 = Customer("Aron", 25)
    customer2.add_money(1000.0)
    order2 = Order(shop, customer2)
    order2.add_product(product11)
    order2.add_product(product2)
    order2.add_product(product3)
    order1.confirm_order()
    print(customer1.money)  # 250.0
    print(shop.stock_total_cost())  # 0.22

    print(f"\n{'| Order.remove_conflicting_products |'.center(49, '-')}")
    order2.remove_conflicting_products()
    print(order2.products)  # {Water(0.22)}
    order2.confirm_order()

    print(f"\n{'| Shop.get_top_customers |'.center(49, '-')}")
    print(shop.top_customers(3))  # [John Doe, Aron]
    product4 = Product("Expensive laptop", 800.0, "Electronics")
    shop.add_product(product4)
    customer3 = Customer("Mikk", 30)
    customer3.add_money(1000.0)
    order3 = Order(shop, customer3)
    order3.add_product(product4)
    order3.confirm_order()
    print(shop.top_customers(3))  # [Mikk, John Doe, Aron]