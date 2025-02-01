"""Exam 3 (11.01.2025)."""

def delete_fragmemnt(message: str, char: str):
    """
    Convert the function name from kebab case to camel case.

    * Kebab case is a way of naming methods with "-" between words.
    * Camel case is a way of naming methods with the first letter being lowercase and other words being uppercase.
    * Your job is to convert a method name in kebab case to camel case.
    * If the input is an empty string or consists of only spaces return "".

    kebab_to_camel("this-is-function-name") => "thisIsFunctionName"
    kebab_to_camel("hello-hello-world") => "helloHelloWorld"

    :param kebab_str: Method name in kebab case to convert into camel case.
    :return: Method name that has been converted to camel case.
    """
    print(message, char)

def reverse_words_in_text(text: str):
    """reverse text"""
    result = ''
    text = text.split(' ')
    for i in text[::-1]:
        result += i + ' '

    return result.strip()

def number_palindrome(text: str):
    """reverse text"""
    return text

def reorganize_temperatures(city_dict: dict[str, tuple[str, float]]) -> dict[str, tuple[float, dict[str, float]]]:
    """reverse text"""
    return city_dict

def count_the_dumplings(day):
    """reverse text"""
    return day

def  star_pyramid(str):
    """reverse text"""
    return str


class Car:
    def __init__(self, make: str, model: str, year: int):
        """Initialize a car"""
        self.make = make
        self.model = model
        self.year = year

    def __repr__(self) -> str:
        """Return a string representation of the Car object."""
        return f'{self.year} {self.make} {self.make}'

    def __eq__(self, other):
        """Check if two cars are equal."""
        return type(other) is self.__class__ and \
            self.make == other.make and \
            self.model == other.model and \
            self.year == other.year

    def __hash__(self) -> int:
        """Allow a Car object to be used as a key in a dictionary. Don't change this method."""
        return hash((self.make, self.model, self.year))

class Garage:
    def __init__(self):
        """Initialize a car"""
        self.cars = []

    def add_car(self):
        if car not in garage.cars:
            garage.cars.append(car)

    def remove_car(self):
        if car in garage.cars:
            garage.cars.remove(car)

    def get_cars(self):
        return self.cars

    def find_cars_by_make(cars: list[Car], make: str) -> list[Car]:
        """Find all cars that have the given make."""
        result = []
        for i in self.cars:
            if i.make.lower() == make.lower():
                result.append(i)

        return result

    def find_cars_by_year(cars: list[Car], make: str) -> list[Car]:
        """Find all cars that have the given make."""
        result = []
        for i in self.cars:
            if i.year == year:
                result.append(i)

        return result

    def sort_cars_by_year(self) -> list:
        """
        Return a list of all cars in the garage, sorted by year."""
        return sorted(self.cars, key=lambda car: car.year)


if __name__ == "__main__":
    print("kebab_to_camel:")
    print(reverse_words_in_text("this-is-function-name"))