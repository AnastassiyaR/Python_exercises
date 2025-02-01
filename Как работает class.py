class Job:
    def __init__(self, title, salary):
        self.title = title
        self.salary = salary


class Person:
    def __init__(self, name, job, money=):
        self.name = name
        self.job = None
        self.money = 0

    def assign_job(self, job):
        self.job = job

    def work(self):
        if self.job:
            self.money += self.job.salary

..........................................................

class Person:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def buy_item(self, item):
        if self.money >= item.price:
            self.money -= item.price


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

..........................................................

class Post:
    def __init__(self, content, author):
        self.content = content  # Содержимое поста
        self.author = author  # Автор поста
        self.likes = 0  # Изначально 0 лайков

    def like(self):
        self.likes += 1  # Увеличиваем количество лайков на 1


class User:
    def __init__(self, name):
        self.name = name  # Имя пользователя
        self.posts = []  # Список постов пользователя

    def create_post(self, content):
        new_post = Post(content, self.name)  # создает новый объект класса Post или просто заменяешь значения
        self.posts.append(new_post)  # это список объектов типа Post
        return new_post  # [Post(content='Hello, this is my first post!', author='Alice', likes=1)]

    def like_post(self, post):
        post.like()

.....................................................................................

class Author:
    def __init__(self, name):
        self.name = name

author1 = Author("John Smith")
author2 = Author("John Smith")

# Сравнение объектов Author
print(author1 == author2)  # False, так как это разные объекты

# Сравнение имен авторов
print(author1.name == author2.name)  # True, так как имена одинаковые

.....................................................................................

class Author:
    def __init__(self, name):
        self.name = name

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []  # Järjend raamatutest

    def add_book(self, book):
        self.books.append(book)  # Lisa uus raamat järjendisse
!!! Но он добавляет self.books += [book1], то есть [Book(...)]. Если был бы просто текст, то надо было бы создавать
как в class Post().

    def books_by_author(self, author):
        return [book for book in self.books if book.author.name == author.name]

book.author.name
Каждый бук это Book(title, author). Мы выбираем autor, но в примере не пишут название, а вставляют переменную
Author(name). Поэтому book.author.name

.............................................................

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.rented = False

    def rent(self):
        if not self.rented:
            self.rented = True
            return "Vehicle rented"
        else:
            return "Cannot rent vehicle"


class RentalAgency:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    car1 = Vehicle("Toyota", "Corolla")
    rental_agency = RentalAgency()
    rental_agency.add_vehicle(car1)


    def rent_vehicle(self, make, model):
        for car in self.vehicles:
            if car.make == make and car.model == model:
                return car.rent()
            else:
                return "Vehicle not found"

    def return_vehicle(self, make, model):
        for car in self.vehicles:
            if make == car.make and model == car.model and car.rent():
                return "Vehicle returned"
            else:
                "Vehicle not found"

.............................................................